"""
Special retry for William I with expanded creative searches.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.simple_review import SimpleReviewGenerator
from src.download_images.models import Character
from src.download_images.custom_searches import get_custom_queries
from src.supabase_client import get_supabase_client


def main():
    """Process William I with expanded creative searches."""
    print("="*80)
    print("William I - Expanded Creative Search")
    print("="*80)
    print("\nSearching with 20 creative queries including:")
    print("  - Bayeux tapestry specific scenes")
    print("  - Medieval seals and manuscripts")
    print("  - Battle of Hastings imagery")
    print("  - French language searches")
    print("  - Historical engravings")
    print()

    # Connect to Supabase
    print("Connecting to Supabase...")
    client = get_supabase_client()

    # Fetch William I
    response = client.table('character').select('*').eq('name', 'WILLIAM I').execute()
    if not response.data or len(response.data) == 0:
        print("❌ William I not found in database")
        return

    character = Character.from_dict(response.data[0])
    print(f"✅ Found: {character.name}\n")

    # Create generator
    generator = SimpleReviewGenerator()

    # Override query builder to use custom queries
    original_build = generator.selector.downloader.query_builder.build_queries

    def custom_build_queries(char):
        """Use custom queries."""
        custom_queries = get_custom_queries(char.name)
        if custom_queries:
            print(f"  Using {len(custom_queries)} expanded creative queries")
            return custom_queries
        else:
            return original_build(char)

    generator.selector.downloader.query_builder.build_queries = custom_build_queries

    # Process William I
    generator.process_batch([character], batch_size=1, start_idx=0)


if __name__ == "__main__":
    main()
