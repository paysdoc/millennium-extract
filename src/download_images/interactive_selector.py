"""
Interactive image selection workflow.
Download multiple candidates, filter by similarity, and allow human review.
"""
import sys
from pathlib import Path
from typing import List, Optional, Tuple
from PIL import Image

from .models import Character
from .downloader import CharacterImageDownloader
from .file_manager import FileManager
from .config import DownloadConfig


class InteractiveImageSelector:
    """
    Interactive workflow for selecting character images.

    Workflow:
    1. Download 15 candidates for a character
    2. Filter using permissive similarity check (if reference exists)
    3. Show top 3 to user for selection
    4. Save selected image or skip character
    5. Move to next character
    """

    def __init__(
        self,
        downloader: CharacterImageDownloader = None,
        permissive_threshold: int = 40  # Kept for backwards compatibility but unused
    ):
        """
        Initialize interactive selector.

        Args:
            downloader: Image downloader instance
            permissive_threshold: Deprecated parameter, kept for backwards compatibility
        """
        self.downloader = downloader or CharacterImageDownloader()
        self.temp_dir = Path("sourced_images/temp_candidates")
        self.output_dir = Path("sourced_images/wikimedia/by_character_id")
        self.file_manager = FileManager()

        # Create temp directory
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download_candidates(self, character: Character, max_candidates: int = 15) -> List[tuple]:
        """
        Download candidate images for a character.

        Args:
            character: Character object
            max_candidates: Maximum number of candidates to download

        Returns:
            List of (ImageInfo, filepath) tuples
        """
        print(f"\n{'='*80}")
        print(f"[{character.type}] {character.name}")
        print(f"{'='*80}")

        if character.first_names:
            print(f"  First names: {character.first_names}")
        if character.birth_date or character.death_date:
            dates = f"{character.birth_date or '?'} - {character.death_date or '?'}"
            print(f"  Dates: {dates}")

        # Build search queries
        queries = self.downloader.query_builder.build_queries(character)
        if not queries:
            print(f"  ❌ Could not generate search queries")
            return []

        print(f"\n  Search strategies: {len(queries)}")
        for i, q in enumerate(queries[:3], 1):
            print(f"    {i}. {q}")
        if len(queries) > 3:
            print(f"    ... and {len(queries) - 3} more")

        # Search for images
        results = self.downloader.search_for_images(queries)

        if not results:
            print(f"  ❌ No suitable images found")
            return []

        print(f"\n  Downloading {min(len(results), max_candidates)} candidates...")

        # Download candidates to temp directory
        candidates = []
        for idx, image_info in enumerate(results[:max_candidates], 1):
            # Generate temp filename
            filename = f"{character.id}_{character.type}_{character.name}_temp{idx}.jpg"
            filepath = self.temp_dir / filename

            # Download
            success, actual_extension = self.file_manager.download_image(image_info.url, filepath)
            if success:
                # Update filepath with actual extension if different
                if actual_extension and actual_extension != 'jpg':
                    actual_filename = f"{character.id}_{character.type}_{character.name}_temp{idx}.{actual_extension}"
                    filepath = self.temp_dir / actual_filename
                candidates.append((image_info, filepath))
                print(f"    [{idx}/{max_candidates}] ✅ Downloaded")
            else:
                print(f"    [{idx}/{max_candidates}] ❌ Failed")

        print(f"\n  📦 Downloaded {len(candidates)} candidates")
        return candidates

    def filter_by_similarity(
        self,
        character: Character,
        candidates: List[tuple]
    ) -> List[tuple]:
        """
        Return all candidates (filtering has been removed).

        Args:
            character: Character object
            candidates: List of (ImageInfo, filepath) tuples

        Returns:
            All candidates (unfiltered)
        """
        print(f"  ✅ Using all {len(candidates)} candidates (no filtering)")
        return candidates

    def display_image_terminal(self, filepath: Path, width: int = 80):
        """
        Display image info in terminal (text-based for now).

        Args:
            filepath: Path to image file
            width: Terminal width
        """
        try:
            with Image.open(filepath) as img:
                w, h = img.size
                ratio = h / w if w > 0 else 0
                print(f"      Size: {w}x{h}px")
                print(f"      Aspect ratio: {ratio:.3f}")
                print(f"      Path: {filepath.name}")
        except Exception as e:
            print(f"      ⚠️  Could not read image: {e}")

    def show_candidates(
        self,
        character: Character,
        candidates: List[tuple],
        start_idx: int = 0,
        batch_size: int = 3
    ) -> Tuple[Optional[int], bool]:
        """
        Show a batch of candidates and get user selection.

        Args:
            character: Character object
            candidates: List of (ImageInfo, filepath) tuples
            start_idx: Starting index in candidates list
            batch_size: Number to show at once

        Returns:
            Tuple of (selected_index or None, continue_flag)
            - (index, True): User selected image at index
            - (None, True): User wants to see next batch
            - (None, False): User wants to skip this character
        """
        end_idx = min(start_idx + batch_size, len(candidates))
        batch = candidates[start_idx:end_idx]

        if not batch:
            print(f"\n  ℹ️  No more candidates to show")
            return None, False

        print(f"\n{'='*80}")
        print(f"REVIEW: {character.name}")
        print(f"Showing candidates {start_idx + 1}-{end_idx} of {len(candidates)}")
        print(f"{'='*80}")

        for i, (image_info, filepath) in enumerate(batch, start=start_idx + 1):
            print(f"\n  Option {i}:")
            print(f"    Title: {image_info.title[:70]}")
            self.display_image_terminal(filepath)
            print(f"    Score: {image_info.score:.3f}")

        print(f"\n{'='*80}")
        print(f"Choose an option:")
        print(f"  1-{len(batch)}: Select this image")
        if end_idx < len(candidates):
            print(f"  n: Show next {min(batch_size, len(candidates) - end_idx)} candidates")
        print(f"  s: Skip this character")
        print(f"  q: Quit")
        print(f"{'='*80}")

        while True:
            try:
                choice = input("\nYour choice: ").strip().lower()

                if choice == 'q':
                    print("Exiting...")
                    sys.exit(0)

                if choice == 's':
                    return None, False

                if choice == 'n':
                    if end_idx < len(candidates):
                        return None, True
                    else:
                        print("No more candidates available. Choose 1-{}, 's', or 'q'".format(len(batch)))
                        continue

                # Try to parse as number
                try:
                    num = int(choice)
                    if 1 <= num <= len(batch):
                        return start_idx + num - 1, True
                    else:
                        print(f"Invalid option. Choose 1-{len(batch)}, 'n', 's', or 'q'")
                except ValueError:
                    print(f"Invalid input. Choose 1-{len(batch)}, 'n', 's', or 'q'")

            except EOFError:
                print("\nEOF received - skipping character")
                return None, False
            except KeyboardInterrupt:
                print("\nInterrupted - exiting")
                sys.exit(0)

    def save_selected_image(
        self,
        character: Character,
        image_info,
        temp_filepath: Path
    ) -> bool:
        """
        Save the selected image to final destination.

        Args:
            character: Character object
            image_info: ImageInfo object
            temp_filepath: Path to temporary downloaded file

        Returns:
            True if successful
        """
        # Generate final filename
        filename = self.file_manager.generate_filename(
            character.id,
            character.type,
            character.name,
            rank=1  # Always primary for selected image
        )

        final_path = self.output_dir / filename
        metadata_path = final_path.with_suffix('.json')

        # Copy temp file to final location
        try:
            import shutil
            shutil.copy2(temp_filepath, final_path)
            print(f"  ✅ Saved to: {filename}")

            # Save metadata
            metadata = self.file_manager.create_metadata(character, image_info, rank=1)
            self.file_manager.save_metadata(metadata, metadata_path)

            return True

        except Exception as e:
            print(f"  ❌ Failed to save: {e}")
            return False

    def cleanup_temp_files(self):
        """Remove all temporary candidate files."""
        try:
            for file in self.temp_dir.glob("*"):
                file.unlink()
            print(f"  🧹 Cleaned up temp files")
        except Exception as e:
            print(f"  ⚠️  Cleanup warning: {e}")

    def process_character(self, character: Character) -> bool:
        """
        Complete workflow for one character.

        Args:
            character: Character object

        Returns:
            True if image was selected and saved, False if skipped
        """
        # Step 1: Download candidates
        candidates = self.download_candidates(character, max_candidates=15)

        if not candidates:
            print(f"  ⚠️  Skipping - no candidates found")
            self.cleanup_temp_files()
            return False

        # Step 2: Filter by similarity (if reference exists)
        filtered = self.filter_by_similarity(character, candidates)

        if not filtered:
            print(f"  ⚠️  All candidates rejected by similarity filter")
            print(f"  ℹ️  Showing all {len(candidates)} candidates anyway...")
            filtered = candidates

        # Step 3: Interactive selection
        batch_size = 3
        start_idx = 0

        while start_idx < len(filtered):
            selected_idx, should_continue = self.show_candidates(
                character,
                filtered,
                start_idx,
                batch_size
            )

            if selected_idx is not None:
                # User selected an image
                image_info, filepath = filtered[selected_idx]
                print(f"\n  ✨ You selected option {selected_idx + 1}")

                # Step 4: Save selected image
                success = self.save_selected_image(character, image_info, filepath)
                self.cleanup_temp_files()
                return success

            if not should_continue:
                # User chose to skip
                print(f"\n  ⏭️  Skipping {character.name}")
                self.cleanup_temp_files()
                return False

            # User wants to see next batch
            start_idx += batch_size

        # Exhausted all candidates without selection
        print(f"\n  ⏭️  No selection made - skipping {character.name}")
        self.cleanup_temp_files()
        return False
