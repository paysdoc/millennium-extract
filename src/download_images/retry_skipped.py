"""
Retry skipped characters with custom creative search queries.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.simple_review import SimpleReviewGenerator
from src.download_images.models import Character
from src.download_images.custom_searches import get_custom_queries
from src.supabase_client import get_supabase_client


def main():
    """Process skipped characters with custom searches."""
    # List of skipped character names
    skipped_names = [
        "WILLIAM I",
        "FREDERICK II",
        "ISABELLA",
        "LOUIS IX",
        "NICHOLAS I",
        "PHILIP AUGUST",
        "STUPOR MUNDI",
    ]

    print("="*80)
    print("Retry Skipped Characters with Creative Searches")
    print("="*80)
    print(f"\nProcessing {len(skipped_names)} skipped characters...")
    print()

    # Connect to Supabase
    print("Connecting to Supabase...")
    client = get_supabase_client()

    # Fetch the skipped characters
    characters = []
    for name in skipped_names:
        response = client.table('character').select('*').eq('name', name).execute()
        if response.data and len(response.data) > 0:
            characters.append(Character.from_dict(response.data[0]))
        else:
            print(f"⚠️  Character not found: {name}")

    print(f"Found {len(characters)} characters\n")

    # Override query builder to use custom queries
    generator = SimpleReviewGenerator()

    # Monkey patch the query builder to use custom queries
    original_build = generator.selector.downloader.query_builder.build_queries

    def custom_build_queries(character):
        """Use custom queries if available, otherwise fall back to original."""
        custom_queries = get_custom_queries(character.name)
        if custom_queries:
            print(f"  Using {len(custom_queries)} custom creative queries")
            return custom_queries
        else:
            return original_build(character)

    generator.selector.downloader.query_builder.build_queries = custom_build_queries

    # Process all skipped characters
    generator.process_batch(characters, batch_size=len(characters), start_idx=0)


if __name__ == "__main__":
    main()
