"""
Generate missing JSON metadata files and clean up orphaned JSON files.

This script:
1. Scans for image files (.jpg) without corresponding .json files
2. Extracts character information from filename and Supabase
3. Analyzes image dimensions using PIL/Pillow
4. Calculates quality scores using ImageScorer
5. Creates comprehensive metadata JSON files
6. Removes orphaned JSON files (JSON files without corresponding images)

Usage:
    python -m src.download_images.generate_missing_metadata [--dry-run]

    --dry-run: Preview actions without making changes
"""
import sys
import json
from pathlib import Path
from datetime import datetime
from PIL import Image

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.supabase_client import get_supabase_client
from src.download_images.models import Character
from src.download_images.image_scorer import ImageScorer


def parse_filename(filename: str) -> tuple[int, str, str] | None:
    """
    Parse character info from filename.

    Expected format: {id}_{category}_{name}_1.jpg or {id}_{category}_{name}.jpg

    Args:
        filename: Image filename (e.g., "16_I_ARKWRIGHT_1.jpg")

    Returns:
        Tuple of (character_id, category, name) or None if parsing fails
    """
    try:
        # Remove extension
        base = filename.replace('.jpg', '').replace('.jpeg', '').replace('.png', '')

        # Split into parts
        parts = base.split('_')

        if len(parts) < 3:
            return None

        char_id = int(parts[0])
        category = parts[1]

        # Name is everything between category and optional rank number
        # Handle case where last part is a rank number
        if parts[-1].isdigit():
            name = '_'.join(parts[2:-1])
        else:
            name = '_'.join(parts[2:])

        return char_id, category, name

    except (ValueError, IndexError):
        return None


def get_character_from_db(client, char_id: int) -> Character | None:
    """
    Fetch character data from Supabase.

    Args:
        client: Supabase client
        char_id: Character ID

    Returns:
        Character object or None if not found
    """
    try:
        response = client.table('character').select('*').eq('id', char_id).execute()

        if response.data and len(response.data) > 0:
            return Character.from_dict(response.data[0])

        return None

    except Exception as e:
        print(f"  ⚠️  Database error: {e}")
        return None


def get_image_dimensions(image_path: Path) -> tuple[int, int] | None:
    """
    Get image dimensions using PIL.

    Args:
        image_path: Path to image file

    Returns:
        Tuple of (width, height) or None if error
    """
    try:
        with Image.open(image_path) as img:
            return img.size  # Returns (width, height)

    except Exception as e:
        print(f"  ⚠️  Image read error: {e}")
        return None


def generate_metadata(
    image_path: Path,
    character: Character,
    width: int,
    height: int,
    scorer: ImageScorer
) -> dict:
    """
    Generate metadata dictionary for an image.

    Args:
        image_path: Path to image file
        character: Character object
        width: Image width
        height: Image height
        scorer: ImageScorer instance

    Returns:
        Metadata dictionary
    """
    # Calculate aspect ratio and scores regardless of validation
    # (scorer.score_image returns 0 for invalid images, so we calculate manually)
    aspect_ratio = height / width if width > 0 else 0.0

    # Calculate scores manually
    ratio_score = scorer.calculate_ratio_score(aspect_ratio) if aspect_ratio > 0 else 0.0
    resolution_score = scorer.calculate_resolution_score(height)
    quality_score = scorer.calculate_total_score(aspect_ratio, height) if aspect_ratio > 0 else 0.0

    # Check if meets strict validation requirements
    is_valid = scorer.is_valid_image(width, height)

    # Determine rank from filename
    filename = image_path.stem
    rank = 1
    if filename.endswith('_1') or filename.endswith('_2') or filename.endswith('_3'):
        try:
            rank = int(filename[-1])
        except ValueError:
            rank = 1

    # Build metadata
    metadata = {
        'character_name': character.name,
        'character_id': character.id,
        'category': character.type,
        'first_names': character.first_names,
        'biography': character.biography,
        'birth_date': character.birth_date,
        'death_date': character.death_date,
        'width': width,
        'height': height,
        'aspect_ratio': round(aspect_ratio, 3),
        'quality_score': round(quality_score, 3),
        'ratio_score': round(ratio_score, 3),
        'resolution_score': round(resolution_score, 3),
        'meets_strict_requirements': is_valid,
        'source': 'metadata_generation',
        'download_timestamp': datetime.now().isoformat(),
        'rank': rank,
    }

    return metadata


def find_images_without_metadata(directory: Path) -> list[Path]:
    """
    Find all image files without corresponding JSON files.

    Args:
        directory: Directory to scan

    Returns:
        List of image file paths without metadata
    """
    missing = []

    # Find all image files
    for ext in ['*.jpg', '*.jpeg', '*.png']:
        for image_path in directory.glob(ext):
            # Check if corresponding JSON exists
            json_path = image_path.with_suffix('.json')

            if not json_path.exists():
                missing.append(image_path)

    return missing


def find_orphaned_json_files(directory: Path) -> list[Path]:
    """
    Find all JSON files without corresponding image files.

    Args:
        directory: Directory to scan

    Returns:
        List of JSON file paths without images
    """
    orphaned = []

    # Find all JSON files
    for json_path in directory.glob('*.json'):
        # Check if corresponding image exists
        has_image = False
        for ext in ['.jpg', '.jpeg', '.png']:
            image_path = json_path.with_suffix(ext)
            if image_path.exists():
                has_image = True
                break

        if not has_image:
            orphaned.append(json_path)

    return orphaned


def main():
    """Main entry point."""
    # Parse arguments
    dry_run = '--dry-run' in sys.argv

    print("=" * 80)
    print("Generate Missing Metadata for Images")
    print("=" * 80)

    if dry_run:
        print("🔍 DRY RUN MODE - No files will be created")

    print()

    # Initialize
    directory = Path('sourced_images/wikimedia/by_character_id')

    if not directory.exists():
        print(f"❌ Directory not found: {directory}")
        sys.exit(1)

    # Find images without metadata
    print("Scanning for images without metadata...")
    missing = find_images_without_metadata(directory)
    print(f"Found {len(missing)} image(s) without JSON metadata")

    # Find orphaned JSON files
    print("Scanning for orphaned JSON files...")
    orphaned = find_orphaned_json_files(directory)
    print(f"Found {len(orphaned)} orphaned JSON file(s)\n")

    if len(missing) == 0 and len(orphaned) == 0:
        print("✅ All images have metadata and no orphaned JSON files!")
        return

    success_count = 0
    error_count = 0

    # Process missing metadata
    if len(missing) > 0:
        # Connect to Supabase
        print("Connecting to Supabase...")
        try:
            client = get_supabase_client()
            print("✅ Connected\n")
        except Exception as e:
            print(f"❌ Failed to connect: {e}")
            sys.exit(1)

        # Initialize scorer
        scorer = ImageScorer()

        # Process each image
        print("=" * 80)
        print(f"Processing {len(missing)} image(s)...")
        print("=" * 80)
        print()

        for idx, image_path in enumerate(missing, 1):
            print(f"[{idx}/{len(missing)}] {image_path.name}")

            # Parse filename
            parsed = parse_filename(image_path.name)
            if not parsed:
                print(f"  ❌ Could not parse filename")
                error_count += 1
                continue

            char_id, category, name = parsed
            print(f"  Parsed: ID={char_id}, Category={category}, Name={name}")

            # Get character from database
            character = get_character_from_db(client, char_id)
            if not character:
                print(f"  ❌ Character not found in database")
                error_count += 1
                continue

            print(f"  Found character: {character.name} ({character.first_names})")

            # Get image dimensions
            dimensions = get_image_dimensions(image_path)
            if not dimensions:
                print(f"  ❌ Could not read image")
                error_count += 1
                continue

            width, height = dimensions
            print(f"  Dimensions: {width}x{height}")

            # Generate metadata
            metadata = generate_metadata(image_path, character, width, height, scorer)

            # Save to JSON
            json_path = image_path.with_suffix('.json')

            if dry_run:
                print(f"  🔍 Would create: {json_path.name}")
                print(f"     Aspect ratio: {metadata['aspect_ratio']}")
                print(f"     Quality score: {metadata['quality_score']}")
            else:
                try:
                    with open(json_path, 'w') as f:
                        json.dump(metadata, f, indent=2)
                    print(f"  ✅ Created: {json_path.name}")
                    success_count += 1
                except Exception as e:
                    print(f"  ❌ Failed to write JSON: {e}")
                    error_count += 1

            print()

    # Clean up orphaned JSON files
    if len(orphaned) > 0:
        print("=" * 80)
        print(f"Cleaning up {len(orphaned)} orphaned JSON file(s)...")
        print("=" * 80)
        print()

        removed_count = 0

        for idx, json_path in enumerate(orphaned, 1):
            print(f"[{idx}/{len(orphaned)}] {json_path.name}")

            if dry_run:
                print(f"  🔍 Would remove (no corresponding image)")
            else:
                try:
                    json_path.unlink()
                    print(f"  🗑️  Removed")
                    removed_count += 1
                except Exception as e:
                    print(f"  ❌ Failed to remove: {e}")

            print()

    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    if dry_run:
        print(f"\n🔍 DRY RUN MODE:")
        if len(missing) > 0:
            print(f"   Would create {len(missing)} metadata file(s)")
        if len(orphaned) > 0:
            print(f"   Would remove {len(orphaned)} orphaned JSON file(s)")
    else:
        if len(missing) > 0:
            print(f"\n📝 Metadata Generation:")
            print(f"   ✅ Success: {success_count}")
            print(f"   ❌ Errors: {error_count}")
            print(f"   📊 Total: {len(missing)}")

        if len(orphaned) > 0:
            print(f"\n🗑️  Orphaned Files Cleanup:")
            print(f"   ✅ Removed: {removed_count}")
            print(f"   📊 Total: {len(orphaned)}")

    print()


if __name__ == "__main__":
    main()
