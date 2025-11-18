#!/usr/bin/env python3
"""
Upload changed image and metadata files from sourced_images/wikimedia/by_character_id/
to Supabase storage bucket 'character_images'.

A file is considered "changed" if its local modification timestamp is newer than
the file in Supabase storage, or if the file doesn't exist in storage yet.

Usage:
    python upload_changed_wikimedia_images.py                    # Interactive mode with confirmation
    python upload_changed_wikimedia_images.py --yes              # Auto-confirm upload
    python upload_changed_wikimedia_images.py --dry-run          # Check only, don't upload
    python upload_changed_wikimedia_images.py --json-only        # Only upload JSON files
    python upload_changed_wikimedia_images.py --jpg-only         # Only upload JPG files
    python upload_changed_wikimedia_images.py --files "1_*.jpg"  # Upload specific files (glob pattern)
"""
import os
import sys
import argparse
import fnmatch
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()


def get_admin_supabase_client():
    """Create and return a Supabase client with service role key (admin access)."""
    url = os.getenv("SUPABASE_URL")
    service_key = os.getenv("SUPABASE_SERVICE_KEY")

    if not url or not service_key:
        raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in .env file")

    return create_client(url, service_key)


def get_remote_file_timestamp(bucket, filename: str) -> datetime | None:
    """
    Get the last modified timestamp of a file in Supabase storage.

    Args:
        bucket: Supabase storage bucket instance
        filename: Name of the file to check

    Returns:
        datetime object of last modification time, or None if file doesn't exist
    """
    try:
        # List files to get metadata
        files = bucket.list()

        for file_info in files:
            if file_info.get('name') == filename:
                # Parse the updated_at or created_at timestamp
                timestamp_str = file_info.get('updated_at') or file_info.get('created_at')
                if timestamp_str:
                    # Parse ISO format timestamp
                    return datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))

        return None  # File not found
    except Exception as e:
        print(f"Warning: Could not check remote timestamp for {filename}: {e}")
        return None


def get_local_file_timestamp(file_path: Path) -> datetime:
    """Get the modification timestamp of a local file."""
    return datetime.fromtimestamp(file_path.stat().st_mtime)


def upload_changed_files(
    auto_confirm: bool = False,
    dry_run: bool = False,
    json_only: bool = False,
    jpg_only: bool = False,
    file_pattern: str = None
):
    """
    Upload all changed images and JSON metadata files from
    sourced_images/wikimedia/by_character_id/ to Supabase character_images bucket.

    Args:
        auto_confirm: If True, skip confirmation prompt and proceed with upload
        dry_run: If True, check which files need updating but don't upload
        json_only: If True, only upload JSON files
        jpg_only: If True, only upload JPG files
        file_pattern: Optional glob pattern to filter specific files (e.g., "1_*.jpg")
    """
    # Get Supabase client with admin privileges
    client = get_admin_supabase_client()
    bucket = client.storage.from_('character_images')

    # Find all image and JSON files in the directory
    source_dir = Path(__file__).parent / 'sourced_images' / 'wikimedia' / 'by_character_id'

    if not source_dir.exists():
        print(f"Error: Source directory not found: {source_dir}")
        sys.exit(1)

    # Get all .jpg and .json files
    jpg_files = list(source_dir.glob('*.jpg')) + list(source_dir.glob('*.JPG'))
    json_files = list(source_dir.glob('*.json'))

    # Apply file type filters
    if json_only:
        all_files = json_files
        print(f"Filter: JSON files only")
    elif jpg_only:
        all_files = jpg_files
        print(f"Filter: JPG files only")
    else:
        all_files = jpg_files + json_files

    # Apply file pattern filter
    if file_pattern:
        all_files = [f for f in all_files if fnmatch.fnmatch(f.name, file_pattern)]
        print(f"Filter: Files matching pattern '{file_pattern}'")

    # Filter out hidden files
    all_files = [f for f in all_files if not f.name.startswith('.')]

    print(f"Found {len(all_files)} files to check ({len(jpg_files)} JPG, {len(json_files)} JSON total)")
    print("Checking which files need updating...")
    print("=" * 80)

    files_to_upload = []

    for file_path in sorted(all_files):
        filename = file_path.name

        # Get local timestamp
        local_timestamp = get_local_file_timestamp(file_path)

        # Get remote timestamp
        remote_timestamp = get_remote_file_timestamp(bucket, filename)

        # Decide if we need to upload
        needs_upload = False
        reason = ""

        if remote_timestamp is None:
            needs_upload = True
            reason = "new file"
        elif local_timestamp.replace(tzinfo=None) > remote_timestamp.replace(tzinfo=None):
            needs_upload = True
            reason = f"changed (local: {local_timestamp.strftime('%Y-%m-%d %H:%M:%S')}, remote: {remote_timestamp.strftime('%Y-%m-%d %H:%M:%S')})"
        else:
            reason = "up to date"

        if needs_upload:
            files_to_upload.append((file_path, filename, reason))
        else:
            print(f"⊘ Skip: {filename} - {reason}")

    print("=" * 80)
    print(f"\n{len(files_to_upload)} files need uploading")

    if len(files_to_upload) == 0:
        print("✓ All files are up to date!")
        return

    # Show files to upload
    print(f"\nFiles to upload:")
    for file_path, filename, reason in files_to_upload:
        file_size_kb = file_path.stat().st_size // 1024
        print(f"  • {filename} ({file_size_kb} KB) - {reason}")

    # Dry run mode - exit here
    if dry_run:
        print(f"\n[DRY RUN] Would upload {len(files_to_upload)} files")
        return

    # Confirm upload (unless auto-confirmed)
    if not auto_confirm:
        try:
            response = input(f"\nProceed with uploading {len(files_to_upload)} files? [y/N]: ")
            if response.lower() != 'y':
                print("Upload cancelled")
                return
        except EOFError:
            print("\n[ERROR] Cannot read input in non-interactive mode. Use --yes to auto-confirm.")
            sys.exit(1)

    print("\n" + "=" * 80)
    print("Uploading files...")
    print("=" * 80)

    success_count = 0
    error_count = 0

    for file_path, filename, reason in files_to_upload:
        try:
            # Read file
            with open(file_path, 'rb') as f:
                file_data = f.read()

            # Determine content type
            if filename.endswith('.json'):
                content_type = "application/json"
            elif filename.endswith(('.jpg', '.JPG')):
                content_type = "image/jpeg"
            else:
                content_type = "application/octet-stream"

            # Upload to Supabase (upsert=True overwrites existing files)
            result = bucket.upload(
                path=filename,
                file=file_data,
                file_options={"content-type": content_type, "upsert": "true"}
            )

            file_size_kb = len(file_data) // 1024
            print(f"✓ Uploaded: {filename} ({file_size_kb} KB)")
            success_count += 1

        except Exception as e:
            print(f"✗ Failed: {filename} - {str(e)}")
            error_count += 1

    print("=" * 80)
    print(f"Upload complete: {success_count} successful, {error_count} failed")

    if error_count == 0:
        print("✓ All changed files uploaded successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Upload changed Wikimedia images and metadata to Supabase storage",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check what needs updating (dry run)
  python upload_changed_wikimedia_images.py --dry-run

  # Upload all changed files (interactive)
  python upload_changed_wikimedia_images.py

  # Upload all changed files (auto-confirm)
  python upload_changed_wikimedia_images.py --yes

  # Upload only JSON metadata files
  python upload_changed_wikimedia_images.py --json-only --yes

  # Upload only JPG image files
  python upload_changed_wikimedia_images.py --jpg-only --yes

  # Upload specific files by pattern
  python upload_changed_wikimedia_images.py --files "1_*.jpg" --yes
  python upload_changed_wikimedia_images.py --files "*EINSTEIN*" --yes
  python upload_changed_wikimedia_images.py --files "203_*.json" --yes
        """
    )
    parser.add_argument(
        "--yes", "-y",
        action="store_true",
        help="Auto-confirm upload without prompting"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check which files need updating without uploading"
    )
    parser.add_argument(
        "--json-only",
        action="store_true",
        help="Only upload JSON metadata files"
    )
    parser.add_argument(
        "--jpg-only",
        action="store_true",
        help="Only upload JPG image files"
    )
    parser.add_argument(
        "--files", "-f",
        type=str,
        metavar="PATTERN",
        help="Upload only files matching this glob pattern (e.g., '1_*.jpg', '*EINSTEIN*')"
    )

    args = parser.parse_args()

    # Validate conflicting options
    if args.json_only and args.jpg_only:
        parser.error("Cannot use --json-only and --jpg-only together")

    upload_changed_files(
        auto_confirm=args.yes,
        dry_run=args.dry_run,
        json_only=args.json_only,
        jpg_only=args.jpg_only,
        file_pattern=args.files
    )
