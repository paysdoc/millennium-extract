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

    def __init__(self, config: WikimediaConfig = None, scorer: ImageScorer = None):
        """
        Initialize API client.

        Args:
            config: Wikimedia configuration (uses default if None)
            scorer: Image scorer for evaluating results (uses default if None)
        """
        self.config = config or WikimediaConfig()
        self.scorer = scorer or ImageScorer()

    def get_image_info(self, title: str) -> Optional[ImageInfo]:
        """
        Get detailed information about a specific image.

        Args:
            title: Wikimedia image title (e.g., "File:Portrait.jpg")

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
                        return None

                    # Use scorer to validate and create ImageInfo
                    return self.scorer.create_image_info(url, title, width, height)

            return None

        except Exception as e:
            # Silent failure - let caller handle missing results
            return None

    def search_images(self, query: str, limit: int = None) -> List[ImageInfo]:
        """
        Search Wikimedia Commons for images.

        Args:
            query: Search query string
            limit: Maximum number of results to fetch

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
                return []

            results = []
            for search_result in data['query']['search']:
                title = search_result['title']
                image_info = self.get_image_info(title)
                if image_info:
                    results.append(image_info)
                time.sleep(self.config.SEARCH_DELAY_SECONDS)

            # Sort by score (best first)
            results.sort(key=lambda x: x.score, reverse=True)
            return results

        except Exception as e:
            # Silent failure - let caller handle missing results
            return []

    def search_with_queries(self, queries: List[str], max_results: int = None) -> List[ImageInfo]:
        """
        Search using multiple queries and aggregate results.

        Args:
            queries: List of search query strings
            max_results: Stop searching after finding this many candidates

        Returns:
            List of unique ImageInfo objects, sorted by score
        """
        all_results = []
        seen_urls = set()

        for query in queries:
            results = self.search_images(query)

            # Add unique results
            for result in results:
                if result.url not in seen_urls:
                    seen_urls.add(result.url)
                    all_results.append(result)

            # Add delay between queries
            time.sleep(self.config.API_DELAY_SECONDS)

            # Stop if we have enough candidates
            if max_results and len(all_results) >= max_results:
                break

        # Re-sort all results by score
        all_results.sort(key=lambda x: x.score, reverse=True)
        return all_results
