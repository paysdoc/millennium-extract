"""
Image downloading and caching for card generation.
All images are converted to CMYK color mode for professional printing.
Color enhancement is applied to compensate for CMYK's smaller gamut.
"""
import os
import io
import json
from PIL import Image, ImageEnhance
from reportlab.lib.utils import ImageReader
from typing import Optional


def enhance_for_cmyk(img: Image.Image) -> Image.Image:
    """
    Enhance image brightness and saturation before CMYK conversion.

    CMYK has a smaller color gamut than RGB, which can make images appear
    duller. This function pre-enhances the image to compensate for the loss.

    Args:
        img: PIL Image in RGB mode

    Returns:
        Enhanced PIL Image in RGB mode
    """
    # Enhance brightness (1.0 = original, >1.0 = brighter)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1)  # not brighter

    # Enhance color saturation (1.0 = original, >1.0 = more saturated)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.15)  # 15% more saturated

    # Enhance contrast slightly (1.0 = original, >1.0 = more contrast)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.05)  # 5% more contrast

    return img


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
        if not os.path.exists(cache_path):
            # Image not in cache - download from Supabase
            bucket = supabase_client.storage.from_('character_images')
            image_data = bucket.download(filename)

            # Convert bytes to PIL Image
            img = Image.open(io.BytesIO(image_data))

            # Convert to RGB first if needed (for enhancement)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Enhance image before CMYK conversion to compensate for gamut loss
            img = enhance_for_cmyk(img)

            # Convert to CMYK for printing
            img = img.convert('CMYK')

            # Save the enhanced CMYK image to cache (before rotation)
            img.save(cache_path)
            print(f"Cached enhanced CMYK image: {filename}")

        # Load the image from cache
        img = Image.open(cache_path)

        # Ensure it's in CMYK mode (apply enhancement if converting from RGB)
        if img.mode != 'CMYK':
            # If we need to convert, apply enhancement first
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = enhance_for_cmyk(img)
            img = img.convert('CMYK')

        # Apply rotation if metadata indicates landscape orientation
        # This mutation is applied AFTER caching, so the original is preserved
        if metadata and metadata.get('orientation') == 'landscape':
            img = img.rotate(-90, expand=True)

        return ImageReader(img)

    except Exception as e:
        print(f"Failed to download image '{image_path}' (filename: '{filename}'): {e}")
        return None
