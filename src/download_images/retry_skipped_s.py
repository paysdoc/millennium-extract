"""
Retry script for skipped Category S characters with creative search strategies.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.simple_review import SimpleReviewGenerator
from src.download_images.custom_searches import get_custom_queries
from src.download_images.models import Character
from src.supabase_client import get_supabase_client


def main():
    """Retry the 4 skipped Category S characters with creative searches."""

    # Characters that were skipped in initial batches
    skipped_names = [
        "ABBOT HUGH",
        "BECKET",
        "BONIFACE VIII",
        "GREGORY VII",
    ]

    print("=" * 80)
    print("Retrying Skipped Category S Characters with Creative Searches")
    print("=" * 80)
    print(f"\nProcessing {len(skipped_names)} skipped characters:")
    for name in skipped_names:
        print(f"  - {name}")
    print()

    # Connect to Supabase
    print("Connecting to Supabase...")
    client = get_supabase_client()

    # Fetch Category S characters
    query = client.table('character').select('*').eq('type', 'S').order('name')
    response = query.execute()
    all_characters = [Character.from_dict(row) for row in response.data]

    # Filter to skipped ones
    skipped_chars = [c for c in all_characters if c.name in skipped_names]

    print(f"Found {len(skipped_chars)} characters to retry\n")

    # Create generator
    generator = SimpleReviewGenerator()

    # Monkey patch the query builder to use custom queries
    original_build = generator.selector.downloader.query_builder.build_queries

    def custom_build_queries(character):
        """Build queries with custom searches for difficult characters."""
        custom_queries = get_custom_queries(character.name)
        if custom_queries:
            print(f"  Using {len(custom_queries)} creative search queries")
            return custom_queries
        else:
            print(f"  Using standard queries")
            return original_build(character)

    generator.selector.downloader.query_builder.build_queries = custom_build_queries

    # Process all skipped characters at once
    generator.process_batch(skipped_chars, batch_size=len(skipped_chars))

    print("\n" + "=" * 80)
    print("✅ Retry complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
