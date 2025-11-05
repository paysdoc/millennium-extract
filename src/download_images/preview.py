"""
Preview downloaded images and their metadata.
Single Responsibility: Display downloaded image information.
"""
import json
from pathlib import Path
from typing import Dict, List
from .config import DownloadConfig


class MetadataLoader:
    """Load and parse metadata files."""

    @staticmethod
    def load_metadata(json_file: Path) -> dict:
        """
        Load metadata from JSON file.

        Args:
            json_file: Path to JSON metadata file

        Returns:
            Metadata dictionary
        """
        with open(json_file) as f:
            return json.load(f)

    @staticmethod
    def group_by_character(json_files: List[Path]) -> Dict[str, List[dict]]:
        """
        Group metadata by character name.

        Args:
            json_files: List of JSON file paths

        Returns:
            Dictionary mapping character names to their image metadata
        """
        characters = {}

        for json_file in json_files:
            metadata = MetadataLoader.load_metadata(json_file)
            char_name = metadata.get('character_name', 'Unknown')

            if char_name not in characters:
                characters[char_name] = []
            characters[char_name].append(metadata)

        return characters


class PreviewPrinter:
    """Format and print preview information."""

    @staticmethod
    def print_header():
        """Print preview header."""
        print("\n" + "=" * 80)
        print("DOWNLOADED IMAGES PREVIEW")
        print("=" * 80 + "\n")

    @staticmethod
    def print_character_info(metadata: dict):
        """
        Print character information from metadata.

        Args:
            metadata: First image metadata for character
        """
        if metadata.get('first_names'):
            print(f"  First names: {metadata['first_names']}")

        if metadata.get('biography'):
            bio = metadata['biography']
            bio_display = bio[:100] + "..." if len(bio) > 100 else bio
            print(f"  Biography: {bio_display}")

        if metadata.get('birth_date') or metadata.get('death_date'):
            dates = f"{metadata.get('birth_date', '?')} - {metadata.get('death_date', '?')}"
            print(f"  Dates: {dates}")

        print()

    @staticmethod
    def print_image_info(metadata: dict):
        """
        Print information about a single image.

        Args:
            metadata: Image metadata
        """
        rank = metadata.get('rank', 0)
        label = "PRIMARY" if rank == 1 else f"ALT {rank-1}"

        title = metadata.get('wikimedia_title', 'Unknown')[:80]
        width = metadata.get('width', 0)
        height = metadata.get('height', 0)
        ratio = metadata.get('aspect_ratio', 0)
        score = metadata.get('score', 0)

        print(f"  [{label}]")
        print(f"    Title: {title}")
        print(f"    Size: {width}x{height}, Ratio: {ratio:.3f}, Score: {score:.3f}")
        print()

    @staticmethod
    def print_character(char_name: str, images: List[dict]):
        """
        Print all information for a character.

        Args:
            char_name: Character name
            images: List of image metadata
        """
        print(f"\n{char_name}")
        print("-" * 80)

        # Show character info from first image
        if images:
            PreviewPrinter.print_character_info(images[0])

        # Show all images
        for img in images:
            PreviewPrinter.print_image_info(img)

    @staticmethod
    def print_summary(char_count: int, image_count: int, output_dir: Path):
        """
        Print summary statistics.

        Args:
            char_count: Number of characters
            image_count: Total number of images
            output_dir: Directory where images are stored
        """
        print("=" * 80)
        print(f"Total characters: {char_count}")
        print(f"Total images: {image_count}")
        print("\nTo view images:")
        print(f"  cd {output_dir}")
        print(f"  open *.jpg")
        print("=" * 80 + "\n")


class ImagePreview:
    """Main preview coordinator."""

    def __init__(self, output_dir: Path = None):
        """
        Initialize preview.

        Args:
            output_dir: Directory to search for images (uses default if None)
        """
        if output_dir is None:
            output_dir = Path(DownloadConfig.OUTPUT_DIR)
        self.output_dir = output_dir
        self.loader = MetadataLoader()
        self.printer = PreviewPrinter()

    def run(self):
        """Run the preview display."""
        self.printer.print_header()

        # Find all JSON metadata files
        json_files = sorted(self.output_dir.glob("*.json"))

        if not json_files:
            print("No images downloaded yet.")
            return

        # Group by character
        characters = self.loader.group_by_character(json_files)

        # Display each character
        for char_name, images in characters.items():
            self.printer.print_character(char_name, images)

        # Print summary
        self.printer.print_summary(len(characters), len(json_files), self.output_dir)


def main():
    """Main entry point for preview script."""
    preview = ImagePreview()
    preview.run()


if __name__ == '__main__':
    main()
