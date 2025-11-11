"""
Check which characters have selections and which are missing.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.supabase_client import get_supabase_client
from src.download_images.models import Character

def main():
    # Connect to Supabase
    client = get_supabase_client()

    # Categories to check
    categories = ['R', 'S', 'P', 'M', 'N']

    for category in categories:
        print(f"\n{'='*80}")
        print(f"CATEGORY {category}")
        print(f"{'='*80}")

        # Fetch all characters in this category with raw data
        response = client.table('character').select('*').eq('type', category).order('name').execute()

        if not response.data:
            print(f"No characters found in category {category}")
            continue

        # Separate into selected and missing
        selected = []
        missing = []

        for row in response.data:
            name = row.get('name', 'UNKNOWN')
            # Check various possible field names for selection
            has_selection = (
                row.get('wikimedia_selected_id') or
                row.get('selected_image_id') or
                row.get('selected_wikimedia_id') or
                row.get('image_id')
            )

            if has_selection:
                selected.append(name)
            else:
                missing.append(name)

        # Print selected
        if selected:
            print(f"\n✅ SELECTED ({len(selected)}/{len(response.data)}):")
            for name in selected:
                print(f"   {name}")

        # Print missing
        if missing:
            print(f"\n❌ MISSING ({len(missing)}/{len(response.data)}):")
            for name in missing:
                print(f"   {name}")

        # Summary
        print(f"\nProgress: {len(selected)}/{len(response.data)} ({100*len(selected)//len(response.data) if response.data else 0}%)")

    print(f"\n{'='*80}\n")

if __name__ == "__main__":
    main()
