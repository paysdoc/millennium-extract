#!/usr/bin/env python3
"""
Main entry point for Wikimedia Commons Image Downloader.
Single Responsibility: Handle CLI interface and coordinate execution.
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.supabase_client import get_supabase_client, fetch_all_card_data
from src.download_images.downloader import CharacterImageDownloader, DownloadSummaryPrinter
from src.download_images.config import DownloadConfig


class CommandLineInterface:
    """Handle command-line interface for the downloader."""

    @staticmethod
    def parse_arguments() -> tuple[str | None, bool, bool]:
        """
        Parse command-line arguments.

        Returns:
            Tuple of (category_filter, is_test_mode, auto_yes)
        """
        auto_yes = '--yes' in sys.argv or '-y' in sys.argv
        args = [arg for arg in sys.argv[1:] if arg not in ('--yes', '-y')]

        if len(args) > 0:
            category_filter = args[0].upper()
            return category_filter, False, auto_yes
        else:
            return None, True, auto_yes

    @staticmethod
    def print_usage():
        """Print usage information."""
        print("TEST MODE: Downloading first 5 characters only")
        print("Usage: python -m src.download_images.main [CATEGORY]")
        print("Example: python -m src.download_images.main R  # For all Royalty")
        print()

    @staticmethod
    def confirm_download(count: int) -> bool:
        """
        Ask user to confirm large downloads.

        Args:
            count: Number of characters to download

        Returns:
            True if user confirms, False otherwise
        """
        if count > 10:
            response = input(f"Download images for {count} characters? (y/n): ").strip().lower()
            return response == 'y'
        return True


class CharacterFilter:
    """Filter and select characters to download."""

    @staticmethod
    def filter_by_category(card_data_list, category: str):
        """
        Filter characters by category.

        Args:
            card_data_list: List of card data objects
            category: Category code to filter by

        Returns:
            List of filtered character objects
        """
        print(f"Filtering for category: {category}")
        return [cd.character for cd in card_data_list if cd.character.type == category]

    @staticmethod
    def get_test_subset(card_data_list, limit: int = 5):
        """
        Get test subset of characters.

        Args:
            card_data_list: List of card data objects
            limit: Number of characters to return

        Returns:
            List of character objects
        """
        return [cd.character for cd in card_data_list[:limit]]


class DownloadOrchestrator:
    """Orchestrate the overall download process."""

    def __init__(self):
        """Initialize orchestrator."""
        self.cli = CommandLineInterface()
        self.filter = CharacterFilter()
        self.downloader = CharacterImageDownloader()
        self.summary_printer = DownloadSummaryPrinter()

    def get_characters(self, client):
        """
        Get and filter characters based on CLI arguments.

        Args:
            client: Supabase client

        Returns:
            Tuple of (characters list, auto_yes boolean)
        """
        # Fetch all character data
        card_data_list = fetch_all_card_data(client)

        # Parse arguments
        category_filter, is_test_mode, auto_yes = self.cli.parse_arguments()

        if category_filter:
            characters = self.filter.filter_by_category(card_data_list, category_filter)
        elif is_test_mode:
            self.cli.print_usage()
            characters = self.filter.get_test_subset(card_data_list)
        else:
            characters = [cd.character for cd in card_data_list]

        return characters, auto_yes

    def run(self):
        """Main execution flow."""
        # Print header
        self.summary_printer.print_header()

        # Connect to database
        print("Connecting to Supabase...")
        client = get_supabase_client()

        # Get characters
        characters, auto_yes = self.get_characters(client)
        print(f"Characters to process: {len(characters)}\n")

        # Confirm if large batch (unless auto_yes)
        if not auto_yes and not self.cli.confirm_download(len(characters)):
            print("Cancelled.")
            return

        # Setup output directory
        output_dir = Path(DownloadConfig.OUTPUT_DIR)

        # Download
        success_count, total_count = self.downloader.download_batch(
            characters,
            output_dir
        )

        # Print summary
        self.summary_printer.print_summary(success_count, total_count, output_dir)


def main():
    """Main entry point."""
    orchestrator = DownloadOrchestrator()
    orchestrator.run()


if __name__ == '__main__':
    main()
