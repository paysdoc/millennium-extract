"""
Main downloader orchestration.
Dependency Inversion: Depends on abstractions, coordinates all components.
Open/Closed: Easy to extend with new components without modification.
"""
from pathlib import Path
from typing import List, Optional
from .models import ImageInfo
from .config import DownloadConfig, WikimediaConfig
from .query_builder import QueryBuilder
from .wikimedia_api import WikimediaAPIClient
from .file_manager import FileManager


class CharacterImageDownloader:
    """
    Orchestrates the download of images for characters.
    Uses dependency injection to remain flexible and testable.
    """

    def __init__(
        self,
        query_builder: Optional[QueryBuilder] = None,
        api_client: Optional[WikimediaAPIClient] = None,
        file_manager: Optional[FileManager] = None,
        config: Optional[DownloadConfig] = None
    ):
        """
        Initialize downloader with dependencies.

        Args:
            query_builder: Query builder for generating search queries
            api_client: Wikimedia API client for searching
            file_manager: File manager for saving files
            config: Download configuration
        """
        self.query_builder = query_builder or QueryBuilder()
        self.api_client = api_client or WikimediaAPIClient()
        self.file_manager = file_manager or FileManager()
        self.config = config or DownloadConfig()

    def print_character_header(self, character):
        """Print formatted header for character processing."""
        name = (character.name or "").strip()
        category = character.type or "?"

        print(f"\n{'='*80}")
        print(f"[{category}] {name}")
        print(f"{'='*80}")

        # Show character details
        if character.first_names:
            print(f"  First names: {character.first_names}")
        if character.birth_date or character.death_date:
            dates = f"{character.birth_date or '?'} - {character.death_date or '?'}"
            print(f"  Dates: {dates}")
        if character.biography:
            bio_short = (character.biography[:100] + "..."
                        if len(character.biography) > 100
                        else character.biography)
            print(f"  Bio: {bio_short}")

    def print_queries(self, queries: List[str]):
        """Print search queries being used."""
        print(f"\n  Search strategies: {len(queries)}")
        for i, q in enumerate(queries[:3], 1):
            print(f"    {i}. {q}")
        if len(queries) > 3:
            print(f"    ... and {len(queries) - 3} more")

    def search_for_images(self, queries: List[str]) -> List[ImageInfo]:
        """
        Search for images using multiple queries.

        Args:
            queries: List of search query strings

        Returns:
            List of ImageInfo objects found
        """
        all_results = self.api_client.search_with_queries(
            queries,
            max_results=self.config.STOP_AFTER_CANDIDATES
        )

        print(f"  ✅ Found {len(all_results)} total candidates")
        return all_results

    def download_images_for_character(
        self,
        character,
        output_dir: Path
    ) -> int:
        """
        Download images for a single character.

        Args:
            character: Character object with name, biography, etc.
            output_dir: Directory to save images

        Returns:
            Number of images successfully downloaded
        """
        name = (character.name or "").strip()

        # Print header
        self.print_character_header(character)

        # Build search queries
        queries = self.query_builder.build_queries(character)
        if not queries:
            print(f"  ❌ Could not generate search queries")
            return 0

        self.print_queries(queries)

        # Search for images
        results = self.search_for_images(queries)

        if not results:
            print(f"  ❌ No suitable images found")
            return 0

        # Download top images (primary + alternatives)
        max_downloads = self.config.MAX_ALTERNATIVES + 1
        downloaded_count = 0

        for idx, image_info in enumerate(results[:max_downloads], 1):
            label = "Primary" if idx == 1 else f"Alt {idx-1}"

            print(f"\n  {label}: {image_info.title[:60]}...")
            print(f"    Size: {image_info.width}x{image_info.height}, "
                  f"Ratio: {image_info.aspect_ratio:.3f}, "
                  f"Score: {image_info.score:.3f}")

            if self.file_manager.download_with_metadata(
                character,
                image_info,
                output_dir,
                idx
            ):
                downloaded_count += 1

        print(f"\n  📊 Downloaded {downloaded_count} image(s)")
        return downloaded_count

    def download_batch(
        self,
        characters: List,
        output_dir: Optional[Path] = None
    ) -> tuple[int, int]:
        """
        Download images for multiple characters.

        Args:
            characters: List of character objects
            output_dir: Output directory (uses default if None)

        Returns:
            Tuple of (success_count, total_count)
        """
        # Ensure output directory exists
        output_dir = self.file_manager.ensure_output_dir(output_dir)

        success_count = 0
        total_count = len(characters)

        for idx, character in enumerate(characters, 1):
            print(f"\n[{idx}/{total_count}]")
            downloaded = self.download_images_for_character(character, output_dir)
            if downloaded > 0:
                success_count += 1

        return success_count, total_count


class DownloadSummaryPrinter:
    """
    Utility for printing download summaries.
    Single Responsibility: Format and display summary information.
    """

    @staticmethod
    def print_header():
        """Print initial header."""
        print("=" * 80)
        print("Improved Wikimedia Commons Image Downloader")
        print("=" * 80)
        print("\nUsing: first_names, biography, birth_date, death_date for smart searches")
        print(f"Target Aspect Ratio: 1:{WikimediaAPIClient().scorer.config.TARGET_ASPECT_RATIO:.3f} (A4 portrait)")
        print(f"Minimum Resolution: {WikimediaAPIClient().scorer.config.MIN_HEIGHT}px height\n")

    @staticmethod
    def print_summary(success_count: int, total_count: int, output_dir: Path):
        """
        Print final download summary.

        Args:
            success_count: Number of successful downloads
            total_count: Total number attempted
            output_dir: Where images were saved
        """
        print(f"\n{'='*80}")
        print("DOWNLOAD SUMMARY")
        print(f"{'='*80}")
        print(f"\n✅ Successful: {success_count}/{total_count}")
        print(f"❌ Failed: {total_count - success_count}/{total_count}")
        print(f"\nImages saved to: {output_dir}")
        print(f"\nNext steps:")
        print(f"  1. Review images: python -m src.download_images.preview")
        print(f"  2. Open: sourced_images/image_preview.html")
        print(f"  3. Identify any incorrect images")
        print(f"  4. Download full category: python -m src.download_images.main R")
        print(f"{'='*80}\n")
