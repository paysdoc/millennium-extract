#!/usr/bin/env python3
"""
Upload images from bigger_images folder to Supabase storage bucket.
Overwrites existing images.
"""
import os
from pathlib import Path
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


def upload_images():
    """Upload all images from bigger_images to Supabase images bucket."""
    # Get Supabase client with admin privileges
    client = get_admin_supabase_client()
    bucket = client.storage.from_('character_images')

    # Find all JPG images in bigger_images folder
    image_dir = Path(__file__).parent / 'bigger_images'
    image_files = list(image_dir.glob('*.jpg')) + list(image_dir.glob('*.JPG'))

    print(f"Found {len(image_files)} images to upload")
    print("=" * 70)

    success_count = 0
    error_count = 0

    for image_path in sorted(image_files):
        filename = image_path.name

        # Skip .DS_Store and other hidden files
        if filename.startswith('.'):
            continue

        try:
            # Read image file
            with open(image_path, 'rb') as f:
                file_data = f.read()

            # Upload to Supabase (upsert=True overwrites existing files)
            result = bucket.upload(
                path=filename,
                file=file_data,
                file_options={"content-type": "image/jpeg", "upsert": "true"}
            )

            print(f"✓ Uploaded: {filename} ({len(file_data) // 1024} KB)")
            success_count += 1

        except Exception as e:
            print(f"✗ Failed: {filename} - {str(e)}")
            error_count += 1

    print("=" * 70)
    print(f"Upload complete: {success_count} successful, {error_count} failed")

    if error_count == 0:
        print("✓ All images uploaded successfully!")


if __name__ == "__main__":
    upload_images()
