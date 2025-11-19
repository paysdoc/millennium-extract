"""
Check completion status of character categories.

This script checks which categories have incomplete image downloads by:
1. Fetching all characters from Supabase grouped by category
2. Checking which characters have images in by_character_id/
3. Reporting completion statistics per category
4. Displaying image dimensions, aspect ratios, and orientations for existing images

Orientation classification:
- Portrait: height > width (and aspect ratio not between 0.9-1.1)
- Landscape: width > height (and aspect ratio not between 0.9-1.1)
- Square: aspect ratio between 0.9 and 1.1

Usage: python -m src.download_images.check_category_status
"""
import sys
from pathlib import Path
from collections import defaultdict
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.models import Character, CATEGORIES
from src.supabase_client import get_supabase_client


def get_all_characters():
    """Fetch all characters from Supabase."""
    client = get_supabase_client()
    response = client.table('character').select('*').execute()

    characters = [Character.from_dict(row) for row in response.data]
    return characters


def get_downloaded_character_images():
    """Get dictionary mapping character IDs to their image files with metadata."""
    by_character_dir = Path('sourced_images/wikimedia/by_character_id')

    if not by_character_dir.exists():
        return {}

    downloaded_images = defaultdict(list)

    # Look for image files in format: {id}_{category}_{name}.jpg
    for image_file in by_character_dir.glob('*.jpg'):
        try:
            # Extract character ID from filename (first part before underscore)
            filename_stem = image_file.stem
            parts = filename_stem.split('_')
            if parts and parts[0].isdigit():
                char_id = int(parts[0])

                # Get image dimensions
                try:
                    with Image.open(image_file) as img:
                        width, height = img.size
                        aspect_ratio = width / height if height > 0 else 0

                        downloaded_images[char_id].append({
                            'file': image_file,
                            'width': width,
                            'height': height,
                            'aspect_ratio': aspect_ratio,
                            'filename': image_file.name
                        })
                except Exception as e:
                    print(f"Warning: Could not read image {image_file}: {e}", file=sys.stderr)

        except (ValueError, IndexError):
            # Skip files that don't match expected format
            continue

    return downloaded_images


def get_downloaded_character_ids(downloaded_images):
    """Get set of character IDs from downloaded images dict."""
    return set(downloaded_images.keys())


def print_category_image_report(category_code, category_name, characters, downloaded_images):
    """Print detailed image report for a category."""
    import math

    print("="*80)
    print(f"IMAGE REPORT: {category_code} - {category_name}")
    print("="*80)
    print()

    # Get characters with images in this category
    chars_with_images = [c for c in characters if c.id in downloaded_images]

    if not chars_with_images:
        print("No images found for this category.")
        print()
        return

    # Sort by character ID
    chars_with_images.sort(key=lambda c: c.id)

    # Target ratio: 1/1.298 ≈ 0.7704 (effective card aspect ratio excluding banner)
    effective_ratio = 1.0 / 1.298

    for char in chars_with_images:
        images = downloaded_images[char.id]

        for idx, img_info in enumerate(images, 1):
            width = img_info['width']
            height = img_info['height']
            raw_aspect = img_info['aspect_ratio']

            # Calculate aspect ratio (height/width)
            aspect_ratio_hw = height / width if width > 0 else 0.0

            # Determine orientation (square if aspect ratio between 0.9 and 1.1)
            if 0.9 <= aspect_ratio_hw <= 1.1:
                normalized_ratio = "~1:1"
                orientation = "square"
            elif width < height:
                normalized_ratio = f"1:{height/width:.3f}"
                orientation = "portrait"
            else:
                normalized_ratio = f"{width/height:.3f}:1"
                orientation = "landscape"

            # Calculate deviation from effective card aspect ratio
            # For portrait: ratio should be close to effective_ratio (0.7704)
            # For landscape: ratio should be close to 1/effective_ratio (1.298)
            if raw_aspect < 1:
                # Portrait: compare to 1/1.298
                deviation_pct = abs((raw_aspect - effective_ratio) / effective_ratio) * 100
            else:
                # Landscape: compare to 1.298
                deviation_pct = abs((raw_aspect - (1/effective_ratio)) / (1/effective_ratio)) * 100

            # Print everything on one line
            img_suffix = f" #{idx}" if len(images) > 1 else ""
            print(f"  ID {char.id}: {char.name}{img_suffix} | {width}x{height}px | {normalized_ratio} ({orientation}) | Card dev: {deviation_pct:.1f}%")

    # Summary statistics
    total_images = sum(len(downloaded_images[c.id]) for c in chars_with_images)
    all_deviations = []

    for c in chars_with_images:
        for img in downloaded_images[c.id]:
            raw_aspect = img['aspect_ratio']
            if raw_aspect < 1:
                dev = abs((raw_aspect - effective_ratio) / effective_ratio) * 100
            else:
                dev = abs((raw_aspect - (1/effective_ratio)) / (1/effective_ratio)) * 100
            all_deviations.append(dev)

    if all_deviations:
        avg_deviation = sum(all_deviations) / len(all_deviations)
        min_deviation = min(all_deviations)
        max_deviation = max(all_deviations)

        print(f"Summary: {len(chars_with_images)} characters, {total_images} total images")
        print(f"A-series deviation: {min_deviation:.1f}% to {max_deviation:.1f}% (avg: {avg_deviation:.1f}%)")
        print()
    print()


def analyze_category_status():
    """Analyze and display completion status for all categories."""
    print("="*80)
    print("CHARACTER CATEGORY COMPLETION STATUS")
    print("="*80)
    print()

    # Fetch data
    print("Fetching characters from Supabase...")
    characters = get_all_characters()
    downloaded_images = get_downloaded_character_images()
    downloaded_ids = get_downloaded_character_ids(downloaded_images)

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

            cat_ids = [char.id for char in cat_info['missing_chars']]
            print(f"    IDs: {','.join(map(str, cat_ids[:10]))}")
            for idx, char in enumerate(cat_info['missing_chars'][:10], 1):
                print(f"    {idx}. ID {char.id}: {char.name} ({char.first_names or 'N/A'})")

            if cat_info['missing'] > 10:
                print(f"    ... and {cat_info['missing'] - 10} more")

            print()
    else:
        print("🎉 All categories complete!")

    # Print detailed image reports per category
    print()
    print()
    for cat_code in sorted_categories:
        cat_chars = by_category[cat_code]
        cat_name = category_names.get(cat_code, 'Unknown')
        print_category_image_report(cat_code, cat_name, cat_chars, downloaded_images)

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
