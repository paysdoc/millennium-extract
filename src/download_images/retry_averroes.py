"""
Retry image search for Averroes with expanded custom queries.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.simple_review import SimpleReviewGenerator
from src.download_images.custom_searches import get_custom_queries
from src.download_images.models import Character
from src.supabase_client import get_supabase_client


def main():
    """Re-search for Averroes with custom queries."""
    print("="*80)
    print("Searching for AVERROES with expanded Ibn Rushd queries")
    print("="*80)

    # Connect to Supabase
    print("\nConnecting to Supabase...")
    client = get_supabase_client()

    # Fetch Averroes
    response = client.table('character').select('*').eq('name', 'AVERROES').execute()

    if not response.data:
        print("Error: Averroes not found in database")
        sys.exit(1)

    character = Character.from_dict(response.data[0])
    print(f"Found character: {character.name}")
    print(f"  First names: {character.first_names}")

    # Generate review page
    generator = SimpleReviewGenerator()

    # Monkey patch the query builder to use custom queries
    original_build = generator.selector.downloader.query_builder.build_queries

    def custom_build_queries(char):
        """Build queries with custom searches for AVERROES."""
        custom_queries = get_custom_queries(char.name)
        if custom_queries:
            print(f"\n  Using {len(custom_queries)} custom search queries")
            print("  Including: 'Ibn Rushd portrait', 'Averroes philosopher', etc.")
            return custom_queries
        else:
            print(f"  Using standard queries")
            return original_build(char)

    generator.selector.downloader.query_builder.build_queries = custom_build_queries

    print(f"\nProcessing {character.name}...")

    # Download candidates with expanded queries
    candidates = generator.selector.download_candidates(character, max_candidates=15)

    if not candidates:
        print(f"  ⚠️  No candidates found")
        return

    # Filter
    filtered = generator.selector.filter_by_similarity(character, candidates)
    if not filtered:
        print(f"  ⚠️  All filtered out - using all candidates")
        filtered = candidates

    # Generate page
    html_file = generator.generate_character_page(
        character, candidates, filtered, 1, 1, [character]
    )
    print(f"  ✅ Page created: {html_file.name}")

    print(f"\n{'='*80}")
    print(f"✅ Review page ready!")
    print(f"{'='*80}")
    print(f"\n📂 Open: {html_file.absolute()}")
    print(f"\n{'='*80}\n")


if __name__ == "__main__":
    main()
