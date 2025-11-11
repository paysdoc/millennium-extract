"""
Final retry for ABBOT HUGH with expanded "Abbot of Cluny" searches.
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
    """Retry ABBOT HUGH with expanded creative searches."""

    print("=" * 80)
    print("Final Retry: ABBOT HUGH with 'Abbot of Cluny' searches")
    print("=" * 80)
    print()

    # Connect to Supabase
    print("Connecting to Supabase...")
    client = get_supabase_client()

    # Fetch ABBOT HUGH
    query = client.table('character').select('*').eq('type', 'S').eq('name', 'ABBOT HUGH')
    response = query.execute()

    if not response.data:
        print("❌ ABBOT HUGH not found in database")
        return

    character = Character.from_dict(response.data[0])
    print(f"Found: {character.name}")
    print(f"  First names: {character.first_names}")
    print()

    # Create generator
    generator = SimpleReviewGenerator()

    # Monkey patch the query builder to use custom queries
    original_build = generator.selector.downloader.query_builder.build_queries

    def custom_build_queries(char):
        """Build queries with custom searches for ABBOT HUGH."""
        custom_queries = get_custom_queries(char.name)
        if custom_queries:
            print(f"  Using {len(custom_queries)} creative search queries")
            print("  Including: 'Abbot of Cluny', 'Abbé de Cluny', 'Hugh Grand Abbot Cluny'")
            return custom_queries
        else:
            print(f"  Using standard queries")
            return original_build(char)

    generator.selector.downloader.query_builder.build_queries = custom_build_queries

    # Process just ABBOT HUGH
    generator.process_batch([character], batch_size=1)

    print("\n" + "=" * 80)
    print("✅ Final retry complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
