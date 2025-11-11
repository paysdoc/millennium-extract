#!/usr/bin/env python3
"""
Cleanup utility for temporary candidate images.
Removes all files from sourced_images/temp_candidates directory.
"""
import shutil
from pathlib import Path


def cleanup_temp_candidates(dry_run: bool = False) -> tuple[int, int]:
    """
    Remove all temporary candidate files.

    Args:
        dry_run: If True, just report what would be deleted without deleting

    Returns:
        Tuple of (files_deleted, bytes_freed)
    """
    temp_dir = Path("sourced_images/temp_candidates")

    if not temp_dir.exists():
        print(f"No temp directory found at: {temp_dir}")
        return 0, 0

    files = list(temp_dir.glob("*"))
    total_size = sum(f.stat().st_size for f in files if f.is_file())
    file_count = len([f for f in files if f.is_file()])

    print(f"\n{'='*80}")
    print(f"Temporary Candidates Cleanup")
    print(f"{'='*80}")
    print(f"Location: {temp_dir.absolute()}")
    print(f"Files: {file_count}")
    print(f"Total size: {total_size / (1024*1024):.2f} MB")

    if dry_run:
        print(f"\n🔍 DRY RUN - No files will be deleted")
        if file_count > 0:
            print(f"\nFiles that would be deleted:")
            for f in files[:10]:
                if f.is_file():
                    print(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")
            if file_count > 10:
                print(f"  ... and {file_count - 10} more")
        return 0, 0

    if file_count == 0:
        print(f"\n✅ No files to clean up")
        return 0, 0

    # Confirm deletion
    response = input(f"\n⚠️  Delete {file_count} files ({total_size / (1024*1024):.2f} MB)? [y/N]: ").strip().lower()

    if response != 'y':
        print("❌ Cancelled")
        return 0, 0

    # Delete files
    deleted = 0
    for f in files:
        if f.is_file():
            try:
                f.unlink()
                deleted += 1
            except Exception as e:
                print(f"⚠️  Could not delete {f.name}: {e}")

    print(f"\n✅ Deleted {deleted} files ({total_size / (1024*1024):.2f} MB freed)")
    print(f"{'='*80}\n")

    return deleted, total_size


def main():
    """Main entry point."""
    import sys

    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv

    cleanup_temp_candidates(dry_run=dry_run)

    if dry_run:
        print("\nTo actually delete files, run:")
        print("  python3 -m src.download_images.cleanup_temp")


if __name__ == "__main__":
    main()
