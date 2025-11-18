#!/usr/bin/env python3
"""
Scale images in sourced_images/wikimedia/by_character_id so that the longest side
is no larger than 1500px. Smaller images remain unchanged.
"""

import os
from pathlib import Path
from PIL import Image

def scale_image(image_path, max_dimension=1000):
    """
    Scale an image so its longest side is no larger than max_dimension.

    Args:
        image_path: Path to the image file
        max_dimension: Maximum size for the longest side (default: 1500)

    Returns:
        tuple: (was_scaled, original_size, new_size)
    """
    try:
        with Image.open(image_path) as img:
            original_size = img.size
            width, height = original_size

            # Check if scaling is needed
            if width <= max_dimension and height <= max_dimension:
                return (False, original_size, original_size)

            # Calculate new dimensions maintaining aspect ratio
            if width > height:
                new_width = max_dimension
                new_height = int((height / width) * max_dimension)
            else:
                new_height = max_dimension
                new_width = int((width / height) * max_dimension)

            new_size = (new_width, new_height)

            # Resize the image using high-quality resampling
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)

            # Convert RGBA to RGB if necessary (for JPEG compatibility)
            if resized_img.mode in ('RGBA', 'LA', 'P'):
                # Create a white background
                rgb_img = Image.new('RGB', resized_img.size, (255, 255, 255))
                # Paste the image on the white background
                if resized_img.mode == 'P':
                    resized_img = resized_img.convert('RGBA')
                rgb_img.paste(resized_img, mask=resized_img.split()[-1] if resized_img.mode in ('RGBA', 'LA') else None)
                resized_img = rgb_img

            # Save the resized image, preserving format and quality
            resized_img.save(image_path, quality=95, optimize=True)

            return (True, original_size, new_size)

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return (False, None, None)

def main():
    """Process all images in the wikimedia directory."""
    base_dir = Path("sourced_images/wikimedia/by_character_id")

    if not base_dir.exists():
        print(f"Directory not found: {base_dir}")
        return

    # Get all JPG files
    image_files = sorted(base_dir.glob("*.jpg"))

    if not image_files:
        print("No JPG files found in directory")
        return

    print(f"Found {len(image_files)} images to process")
    print(f"Maximum dimension: 1500px")
    print("-" * 60)

    scaled_count = 0
    unchanged_count = 0
    error_count = 0

    for image_path in image_files:
        was_scaled, original_size, new_size = scale_image(image_path)

        if was_scaled:
            scaled_count += 1
            print(f"✓ Scaled: {image_path.name}")
            print(f"  {original_size[0]}x{original_size[1]} → {new_size[0]}x{new_size[1]}")
        elif original_size is None:
            error_count += 1
        else:
            unchanged_count += 1
            if unchanged_count <= 5:  # Show first few unchanged files
                print(f"- Unchanged: {image_path.name} ({original_size[0]}x{original_size[1]})")

    print("-" * 60)
    print(f"Summary:")
    print(f"  Scaled: {scaled_count}")
    print(f"  Unchanged (already small enough): {unchanged_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total processed: {len(image_files)}")

if __name__ == "__main__":
    main()
