"""
Check completion status of character categories.

This script checks which categories have incomplete image downloads by:
1. Fetching all characters from Supabase grouped by category
2. Checking which characters have images in by_character_id/
3. Reporting completion statistics per category

Usage: python -m src.download_images.check_category_status
"""
import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.models import Character, CATEGORIES
from src.supabase_client import get_supabase_client


def get_all_characters():
    """Fetch all characters from Supabase."""
    client = get_supabase_client()
    response = client.table('character').select('*').execute()

    characters = [Character.from_dict(row) for row in response.data]
    return characters


def get_downloaded_character_ids():
    """Get set of character IDs that have downloaded images."""
    by_character_dir = Path('sourced_images/wikimedia/by_character_id')

    if not by_character_dir.exists():
        return set()

    downloaded_ids = set()

    # Look for image files in format: {id}_{category}_{name}_1.jpg
    for image_file in by_character_dir.glob('*.jpg'):
        try:
            # Extract character ID from filename (first part before underscore)
            char_id = int(image_file.stem.split('_')[0])
            downloaded_ids.add(char_id)
        except (ValueError, IndexError):
            # Skip files that don't match expected format
            continue

    return downloaded_ids


def analyze_category_status():
    """Analyze and display completion status for all categories."""
    print("="*80)
    print("CHARACTER CATEGORY COMPLETION STATUS")
    print("="*80)
    print()

    # Fetch data
    print("Fetching characters from Supabase...")
    characters = get_all_characters()
    downloaded_ids = get_downloaded_character_ids()

    # Group characters by category
    by_category = defaultdict(list)
    for char in characters:
        by_category[char.type].append(char)

    # Sort categories by the order defined in CATEGORIES
    category_order = {code: idx for idx, (code, _) in enumerate(CATEGORIES)}
    sorted_categories = sorted(by_category.keys(), key=lambda x: category_order.get(x, 999))

    # Category name lookup
    category_names = dict(CATEGORIES)

    # Display results
    incomplete_categories = []

    print(f"{'Category':<29} {'Total':<8} {'Complete':<10} {'Missing':<10} {'Progress':<12}")
    print("-"*80)

    for cat_code in sorted_categories:
        cat_chars = by_category[cat_code]
        cat_name = category_names.get(cat_code, 'Unknown')

        total = len(cat_chars)
        complete_chars = [c for c in cat_chars if c.id in downloaded_ids]
        complete_count = len(complete_chars)
        missing_count = total - complete_count

        if total > 0:
            progress_pct = (complete_count / total) * 100
            progress_bar = '█' * int(progress_pct / 10) + '░' * (10 - int(progress_pct / 10))
        else:
            progress_pct = 0
            progress_bar = '░' * 10

        status_icon = '✓' if missing_count == 0 else '○'

        print(f"{status_icon} {cat_code} - {cat_name:<23} {total:<8} {complete_count:<10} {missing_count:<10} {progress_bar} {progress_pct:>5.1f}%")

        if missing_count > 0:
            incomplete_categories.append({
                'code': cat_code,
                'name': cat_name,
                'total': total,
                'complete': complete_count,
                'missing': missing_count,
                'characters': cat_chars,
                'missing_chars': [c for c in cat_chars if c.id not in downloaded_ids]
            })

    print("-"*80)
    print(f"Total characters: {len(characters)}")
    print(f"Downloaded: {len(downloaded_ids)}")
    print(f"Missing: {len(characters) - len(downloaded_ids)}")
    print()

    # Show incomplete categories in detail
    if incomplete_categories:
        print("="*80)
        print("INCOMPLETE CATEGORIES")
        print("="*80)
        print()

        for cat_info in incomplete_categories:
            print(f"{cat_info['code']} - {cat_info['name']}")
            print(f"  Progress: {cat_info['complete']}/{cat_info['total']} ({cat_info['missing']} missing)")
            print(f"  Missing characters (first 10):")

            for idx, char in enumerate(cat_info['missing_chars'][:10], 1):
                print(f"    {idx}. ID {char.id}: {char.name} ({char.first_names or 'N/A'})")

            if cat_info['missing'] > 10:
                print(f"    ... and {cat_info['missing'] - 10} more")

            print()
    else:
        print("🎉 All categories complete!")

    return incomplete_categories


def main():
    """Main entry point."""
    try:
        incomplete_categories = analyze_category_status()

        if incomplete_categories:
            print("="*80)
            print("NEXT STEPS")
            print("="*80)
            print()
            print("To download images for a category, use:")
            print("  python -m src.download_images.web_main [CATEGORY] [BATCH_SIZE] [START_IDX]")
            print()
            print("Example:")
            for cat_info in incomplete_categories[:3]:  # Show first 3
                print(f"  python -m src.download_images.web_main {cat_info['code']} 5 0")
            print()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
