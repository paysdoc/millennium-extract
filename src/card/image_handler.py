"""
Image downloading and caching for card generation.
"""
import os
import io
import json
from PIL import Image
from reportlab.lib.utils import ImageReader
from typing import Optional


def download_image_from_supabase(supabase_client, image_path: Optional[str]) -> Optional[ImageReader]:
    """
    Download image from Supabase storage bucket with local caching.

    Args:
        supabase_client: Supabase client instance
        image_path: Path from image_link column (e.g., 'data/images/washington.jpg' or 'Newton.jpg')

    Returns:
        ImageReader object or None if download fails

    Note:
        - The function extracts the filename from the path, ignoring any directory structure
        - Images are cached in 'image_cache/' directory at project root
        - Cached images are used on subsequent calls to avoid re-downloading
    """
    if not image_path:
        return None

    try:
        # Extract just the filename, ignoring any directory path
        # Examples: 'data/images/washington.jpg' -> 'washington.jpg'
        #           'Newton.jpg' -> 'Newton.jpg'
        filename = os.path.basename(image_path.strip())

        if not filename:
            return None

        # Setup cache directory at project root
        cache_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'image_cache')
        os.makedirs(cache_dir, exist_ok=True)

        cache_path = os.path.join(cache_dir, filename)

        # Download and check metadata for orientation
        metadata = None
        metadata_filename = os.path.splitext(filename)[0] + '.json'

        try:
            bucket = supabase_client.storage.from_('character_images')
            metadata_data = bucket.download(metadata_filename)
            metadata = json.loads(metadata_data.decode('utf-8'))
        except Exception as e:
            print(f"Could not download metadata for {filename}: {e}")

        # Check if image exists in cache
        if os.path.exists(cache_path):
            # Load from cache
            img = Image.open(cache_path)

            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Apply rotation if metadata indicates landscape orientation
            if metadata and metadata.get('orientation') == 'landscape':
                img = img.rotate(-90, expand=True)

            return ImageReader(img)

        # Image not in cache - download from Supabase
        bucket = supabase_client.storage.from_('character_images')
        image_data = bucket.download(filename)

        # Convert bytes to PIL Image
        img = Image.open(io.BytesIO(image_data))

        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Apply rotation if metadata indicates landscape orientation
        if metadata and metadata.get('orientation') == 'landscape':
            img = img.rotate(-90, expand=True)

        # Save to cache for future use
        img.save(cache_path)
        print(f"Cached image: {filename}")

        return ImageReader(img)

    except Exception as e:
        print(f"Failed to download image '{image_path}' (filename: '{filename}'): {e}")
        return None
