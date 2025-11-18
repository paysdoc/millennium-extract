"""
Wikimedia Commons API client.
Single Responsibility: Handle all API interactions with Wikimedia.
Interface Segregation: Clear, focused interface for API operations.
"""
import time
import requests
from typing import List, Optional
from .models import ImageInfo
from .config import WikimediaConfig
from .image_scorer import ImageScorer


class WikimediaAPIClient:
    """
    Client for interacting with Wikimedia Commons API.
    Handles searching and fetching image information.
    """

    def __init__(self, config: WikimediaConfig = None, scorer: ImageScorer = None, category: str = None):
        """
        Initialize API client.

        Args:
            config: Wikimedia configuration (uses default if None)
            scorer: Image scorer for evaluating results (uses default if None)
            category: Character category code for category-specific scoring
        """
        self.config = config or WikimediaConfig()
        self.category = category
        self.scorer = scorer or ImageScorer(category=category)

    def get_image_info(self, title: str, log_rejections: bool = False) -> Optional[ImageInfo]:
        """
        Get detailed information about a specific image.

        Args:
            title: Wikimedia image title (e.g., "File:Portrait.jpg")
            log_rejections: If True, print rejection reasons

        Returns:
            ImageInfo object if image is valid, None otherwise
        """
        try:
            params = {
                'action': 'query',
                'format': 'json',
                'titles': title,
                'prop': 'imageinfo',
                'iiprop': 'url|size|mime',
            }

            response = requests.get(
                self.config.API_URL,
                params=params,
                headers=self.config.HEADERS,
                timeout=self.config.REQUEST_TIMEOUT_SECONDS
            )
            response.raise_for_status()
            data = response.json()

            pages = data.get('query', {}).get('pages', {})
            for page_id, page_data in pages.items():
                if 'imageinfo' in page_data and len(page_data['imageinfo']) > 0:
                    info = page_data['imageinfo'][0]

                    width = info.get('width', 0)
                    height = info.get('height', 0)
                    url = info.get('url', '')
                    mime = info.get('mime', '')

                    # Filter for supported image formats (JPEG and PNG)
                    if mime not in ['image/jpeg', 'image/png']:
                        if log_rejections:
                            print(f"        ❌ {title[:50]}... - Unsupported format: {mime}")
                            print(f"           URL: {url[:80]}...")
                        return None

                    # Use scorer to validate and create ImageInfo
                    image_info = self.scorer.create_image_info(url, title, width, height)

                    if image_info is None and log_rejections:
                        # Get validation details for logging
                        validation_errors = self.scorer.is_valid_image(width, height)
                        if validation_errors:
                            print(f"        ❌ {title[:50]}... - {', '.join(validation_errors)}")
                            print(f"           Size: {width}x{height}, URL: {url[:60]}...")

                    return image_info

            if log_rejections:
                print(f"        ❌ {title[:50]}... - No image info available")
            return None

        except Exception as e:
            if log_rejections:
                print(f"        ❌ {title[:50]}... - Error: {str(e)[:50]}")
            return None

    def search_images(self, query: str, limit: int = None, verbose: bool = False) -> List[ImageInfo]:
        """
        Search Wikimedia Commons for images.

        Args:
            query: Search query string
            limit: Maximum number of results to fetch
            verbose: If True, log detailed statistics

        Returns:
            List of ImageInfo objects, sorted by score (best first)
        """
        if limit is None:
            limit = self.config.SEARCH_LIMIT

        try:
            params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': query,
                'srnamespace': '6',  # File namespace
                'srlimit': limit,
            }

            response = requests.get(
                self.config.API_URL,
                params=params,
                headers=self.config.HEADERS,
                timeout=self.config.REQUEST_TIMEOUT_SECONDS
            )
            response.raise_for_status()
            data = response.json()

            if 'query' not in data or 'search' not in data['query']:
                if verbose:
                    print(f"      📊 Query: '{query[:60]}...'")
                    print(f"         Found: 0 images, Accepted: 0")
                return []

            search_results = data['query']['search']
            found_count = len(search_results)
            accepted_count = 0
            rejected_count = 0

            if verbose:
                print(f"      📊 Query: '{query[:60]}...'")
                print(f"         Found: {found_count} images from API")

            results = []
            for search_result in search_results:
                title = search_result['title']
                image_info = self.get_image_info(title, log_rejections=verbose)
                if image_info:
                    results.append(image_info)
                    accepted_count += 1
                    if verbose:
                        print(f"        ✅ {title[:50]}... - Accepted (score: {image_info.score:.3f})")
                        print(f"           Size: {image_info.width}x{image_info.height}, Ratio: {image_info.aspect_ratio:.3f}")
                else:
                    rejected_count += 1
                time.sleep(self.config.SEARCH_DELAY_SECONDS)

            if verbose:
                print(f"         Accepted: {accepted_count}, Rejected: {rejected_count}")

            # Sort by score (best first)
            results.sort(key=lambda x: x.score, reverse=True)
            return results

        except Exception as e:
            if verbose:
                print(f"      ❌ Query failed: {str(e)[:60]}")
            return []

    def search_with_queries(self, queries: List[str], max_results: int = None, verbose: bool = False) -> List[ImageInfo]:
        """
        Search using multiple queries and aggregate results.

        Args:
            queries: List of search query strings
            max_results: Stop searching after finding this many candidates
            verbose: If True, log detailed statistics for each query

        Returns:
            List of unique ImageInfo objects, sorted by score
        """
        all_results = []
        seen_urls = set()

        if verbose:
            print(f"\n    🔍 Searching with {len(queries)} queries (max results: {max_results or 'unlimited'})")

        for idx, query in enumerate(queries, 1):
            if verbose:
                print(f"\n    Query {idx}/{len(queries)}:")

            results = self.search_images(query, verbose=verbose)

            # Track unique vs duplicate results
            unique_count = 0
            duplicate_count = 0

            # Add unique results
            for result in results:
                if result.url not in seen_urls:
                    seen_urls.add(result.url)
                    all_results.append(result)
                    unique_count += 1
                else:
                    duplicate_count += 1

            if verbose and results:
                print(f"         New unique: {unique_count}, Duplicates: {duplicate_count}")
                print(f"         Total candidates so far: {len(all_results)}")

            # Add delay between queries
            time.sleep(self.config.API_DELAY_SECONDS)

            # Stop if we have enough candidates
            if max_results and len(all_results) >= max_results:
                if verbose:
                    print(f"\n    ✋ Stopping: reached max_results ({max_results})")
                break

        # Re-sort all results by score
        all_results.sort(key=lambda x: x.score, reverse=True)

        if verbose:
            print(f"\n    📊 Final summary:")
            print(f"       Queries executed: {min(idx, len(queries))}/{len(queries)}")
            print(f"       Total unique candidates: {len(all_results)}")
            if all_results:
                print(f"       Best score: {all_results[0].score:.3f}")
                print(f"       Worst score: {all_results[-1].score:.3f}")

        return all_results
