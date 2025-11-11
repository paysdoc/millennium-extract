"""
Interactive image selection CLI.
Usage: python -m src.download_images.interactive_main [CATEGORY]
"""
import sys
from pathlib import Path
from typing import List, Optional

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.interactive_selector import InteractiveImageSelector
from src.download_images.models import Character
from src.supabase_client import get_supabase_client


class InteractiveCLI:
    """CLI for interactive image selection."""

    def __init__(self):
        self.selector = InteractiveImageSelector(permissive_threshold=40)
        self.supabase = None
        self.skipped_characters = []
        self.selected_characters = []

    def connect_to_supabase(self):
        """Initialize Supabase connection."""
        print("Connecting to Supabase...")
        try:
            self.supabase = get_supabase_client()
            print("✅ Connected\n")
        except Exception as e:
            print(f"❌ Failed to connect: {e}")
            sys.exit(1)

    def get_characters(self, category_filter: Optional[str] = None) -> List[Character]:
        """
        Fetch characters from Supabase.

        Args:
            category_filter: Optional category to filter by (e.g., 'R' for Royalty)

        Returns:
            List of Character objects
        """
        try:
            query = self.supabase.table('character').select('*')

            if category_filter:
                query = query.eq('type', category_filter)
                print(f"Filtering for category: {category_filter}")

            # Order by category then name for consistent ordering
            query = query.order('type').order('name')

            response = query.execute()

            characters = [Character.from_dict(row) for row in response.data]
            print(f"Characters to process: {len(characters)}\n")

            return characters

        except Exception as e:
            print(f"❌ Failed to fetch characters: {e}")
            sys.exit(1)

    def print_header(self):
        """Print initial header."""
        print("=" * 80)
        print("Interactive Image Selection")
        print("=" * 80)
        print("\nWorkflow:")
        print("  1. Download 15 candidates per character")
        print("  2. Filter using permissive similarity check (threshold: 40)")
        print("  3. Show you top 3 candidates")
        print("  4. You select one, or ask for next 3, or skip")
        print("  5. Continue to next character")
        print("\nControls:")
        print("  1-3: Select that image")
        print("  n: Show next 3 candidates")
        print("  s: Skip this character")
        print("  q: Quit")
        print("=" * 80)
        print()

    def print_summary(self):
        """Print final summary."""
        print("\n" + "=" * 80)
        print("SESSION SUMMARY")
        print("=" * 80)
        print(f"\n✅ Selected: {len(self.selected_characters)}")
        print(f"⏭️  Skipped: {len(self.skipped_characters)}")

        if self.skipped_characters:
            print("\nSkipped characters:")
            for char in self.skipped_characters:
                print(f"  - {char.name} ({char.type})")

        print("\n" + "=" * 80)

    def run(self, category_filter: Optional[str] = None):
        """
        Run interactive selection session.

        Args:
            category_filter: Optional category filter
        """
        self.print_header()
        self.connect_to_supabase()

        # Get characters to process
        characters = self.get_characters(category_filter)

        if not characters:
            print("No characters found!")
            return

        # Process each character
        for idx, character in enumerate(characters, 1):
            print(f"\n{'#'*80}")
            print(f"Character {idx}/{len(characters)}")
            print(f"{'#'*80}")

            success = self.selector.process_character(character)

            if success:
                self.selected_characters.append(character)
            else:
                self.skipped_characters.append(character)

        # Print summary
        self.print_summary()


def main():
    """Main entry point."""
    # Parse arguments
    category_filter = None
    if len(sys.argv) > 1:
        category_filter = sys.argv[1].upper()

    # Run interactive CLI
    cli = InteractiveCLI()
    try:
        cli.run(category_filter)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        cli.print_summary()
        sys.exit(0)


if __name__ == "__main__":
    main()
