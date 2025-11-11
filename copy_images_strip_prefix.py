#!/usr/bin/env python3
"""
Copy images from sourced_images/wikimedia/by_character_id to bigger_images.
Strip ID and category prefix from filenames.

Original format: <id>_<category>_<name>.jpg
New format: <name>.jpg

Ignores .json files.
"""
import re
import shutil
from pathlib import Path
from typing import Tuple, List


def parse_filename(filename: str) -> Tuple[str, str, str]:
    """
    Parse filename to extract ID, category, and name.

    Args:
        filename: Original filename (e.g., "1_S_WASHINGTON.jpg")

    Returns:
        Tuple of (id, category, name_with_extension)
        Returns (None, None, None) if format doesn't match
    """
    # Pattern: <digits>_<single_letter>_<rest>.jpg
    pattern = r'^(\d+)_([A-Z])_(.+)$'

    match = re.match(pattern, filename)
    if match:
        file_id = match.group(1)
        category = match.group(2)
        name_with_ext = match.group(3)
        return file_id, category, name_with_ext

    return None, None, None


def copy_images(source_dir: Path, dest_dir: Path, dry_run: bool = True) -> Tuple[int, int, List[str]]:
    """
    Copy images from source to destination, stripping ID and category prefix.

    Args:
        source_dir: Source directory containing images
        dest_dir: Destination directory
        dry_run: If True, only show what would be done

    Returns:
        Tuple of (copied_count, skipped_count, errors)
    """
    if not source_dir.exists():
        return 0, 0, [f"Source directory not found: {source_dir}"]

    # Create destination directory
    if not dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)

    copied_count = 0
    skipped_count = 0
    errors = []

    # Get all .jpg files
    jpg_files = sorted([f for f in source_dir.iterdir() if f.suffix.lower() == '.jpg'])

    print(f"\nProcessing {len(jpg_files)} JPG files from {source_dir}")
    print("=" * 70)

    for file_path in jpg_files:
        filename = file_path.name

        # Parse filename
        file_id, category, name_with_ext = parse_filename(filename)

        if file_id is None:
            error_msg = f"Could not parse filename: {filename}"
            errors.append(error_msg)
            print(f"  ⚠️  {error_msg}")
            skipped_count += 1
            continue

        # New filename is just the name part
        new_filename = name_with_ext
        dest_path = dest_dir / new_filename

        # Check if destination already exists
        if dest_path.exists() and not dry_run:
            error_msg = f"Destination already exists: {new_filename}"
            errors.append(error_msg)
            print(f"  ⚠️  {error_msg}")
            skipped_count += 1
            continue

        # Copy file
        if dry_run:
            print(f"  [DRY RUN] {filename} → {new_filename}")
        else:
            try:
                shutil.copy2(file_path, dest_path)
                print(f"  ✓ {filename} → {new_filename}")
            except Exception as e:
                error_msg = f"Failed to copy {filename}: {e}"
                errors.append(error_msg)
                print(f"  ❌ {error_msg}")
                skipped_count += 1
                continue

        copied_count += 1

    return copied_count, skipped_count, errors


def main():
    """Main execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Copy images and strip ID/category prefix from filenames'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Actually copy files (default is dry-run mode)'
    )

    args = parser.parse_args()
    dry_run = not args.execute

    if dry_run:
        print("=" * 70)
        print("DRY RUN MODE - No files will be copied")
        print("Use --execute flag to actually copy files")
        print("=" * 70)
    else:
        print("=" * 70)
        print("EXECUTION MODE - Files will be copied")
        print("=" * 70)

    # Define paths
    project_root = Path(__file__).parent
    source_dir = project_root / "sourced_images" / "wikimedia" / "by_character_id"
    dest_dir = project_root / "bigger_images"

    # Copy images
    copied, skipped, errors = copy_images(source_dir, dest_dir, dry_run)

    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Files copied: {copied}")
    print(f"Files skipped: {skipped}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(f"  • {error}")

    if dry_run and copied > 0:
        print("\n💡 Run with --execute flag to actually copy files")

    return 0 if len(errors) == 0 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
