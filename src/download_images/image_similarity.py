"""
Image similarity comparison to validate downloaded images.
Single Responsibility: Compare images and reject those that are too different.
"""
from pathlib import Path
from typing import Optional, Tuple
from PIL import Image
import imagehash


class ImageSimilarityChecker:
    """
    Check if downloaded images are similar enough to existing cache images.
    Uses perceptual hashing to detect if images are completely different.
    """

    def __init__(self, similarity_threshold: int = 20):
        """
        Initialize similarity checker.

        Args:
            similarity_threshold: Maximum hash difference allowed (0-64).
                                Lower = more similar required.
                                20 is a good balance - allows variations but rejects totally different images.
        """
        self.similarity_threshold = similarity_threshold

    def calculate_hash(self, image_path: Path) -> Optional[imagehash.ImageHash]:
        """
        Calculate perceptual hash of an image.

        Args:
            image_path: Path to image file

        Returns:
            ImageHash object or None if error
        """
        try:
            with Image.open(image_path) as img:
                # Convert to RGB if needed
                if img.mode not in ('RGB', 'L'):
                    img = img.convert('RGB')

                # Use average hash - good for detecting completely different images
                return imagehash.average_hash(img)

        except Exception as e:
            print(f"    ⚠️  Could not hash image: {e}")
            return None

    def are_similar(self, image1_path: Path, image2_path: Path) -> Tuple[bool, Optional[int]]:
        """
        Check if two images are similar.

        Args:
            image1_path: Path to first image
            image2_path: Path to second image

        Returns:
            Tuple of (is_similar: bool, difference: int or None)
        """
        hash1 = self.calculate_hash(image1_path)
        hash2 = self.calculate_hash(image2_path)

        if hash1 is None or hash2 is None:
            # Can't compare, assume similar (don't reject)
            return True, None

        difference = hash1 - hash2

        is_similar = difference <= self.similarity_threshold

        return is_similar, difference

    def find_existing_image(self, character_name: str, character_id: int,
                           category: str, cache_dir: Path) -> Optional[Path]:
        """
        Find existing image for a character in cache.

        Args:
            character_name: Character name (e.g., "BARBAROSSA", "CATHERINE II")
            character_id: Character ID (integer)
            category: Character category (R, S, etc.)
            cache_dir: Path to image_cache directory

        Returns:
            Path to existing image or None
        """
        if not cache_dir.exists():
            return None

        # Strategy 1: Look for name-based cache files (e.g., "Barbarossa.jpg", "Catherine II.jpg")
        # Try exact name match
        name_variations = [
            character_name,  # "BARBAROSSA"
            character_name.title(),  # "Barbarossa"
            character_name.replace('_', ' '),  # Handle underscores
            character_name.replace('_', ' ').title(),  # "Catherine Ii" -> "Catherine II"
        ]

        for name_var in name_variations:
            # Look for common image extensions
            for ext in ['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG']:
                image_path = cache_dir / f"{name_var}.{ext}"
                if image_path.exists():
                    return image_path

        # Strategy 2: Look for ID-based cached images (new format)
        pattern = f"{character_id}_{category}_*"
        matches = list(cache_dir.glob(pattern))
        if matches:
            return matches[0]

        # Strategy 3: Check cropped cache
        cropped_cache = cache_dir / "cropped"
        if cropped_cache.exists():
            matches = list(cropped_cache.glob(pattern))
            if matches:
                return matches[0]

        return None

    def validate_download(self, downloaded_image: Path,
                         character_name: str, character_id: int,
                         category: str,
                         cache_dir: Path = Path("image_cache")) -> Tuple[bool, str]:
        """
        Validate a downloaded image against existing cache.

        Args:
            downloaded_image: Path to newly downloaded image
            character_name: Character name (e.g., "BARBAROSSA")
            character_id: Character ID (integer)
            category: Character category
            cache_dir: Path to image cache directory

        Returns:
            Tuple of (is_valid: bool, reason: str)
        """
        # Find existing image
        existing_image = self.find_existing_image(character_name, character_id, category, cache_dir)

        if existing_image is None:
            # No existing image to compare against - accept download
            return True, "No reference image to compare"

        # Compare similarity
        is_similar, difference = self.are_similar(downloaded_image, existing_image)

        if is_similar:
            return True, f"Similar to {existing_image.name} (diff: {difference})"
        else:
            return False, f"Too different from {existing_image.name} (diff: {difference}, threshold: {self.similarity_threshold})"


class ImageValidator:
    """High-level interface for image validation."""

    def __init__(self, similarity_threshold: int = 20):
        """Initialize validator."""
        self.checker = ImageSimilarityChecker(similarity_threshold)

    def should_keep_image(self, downloaded_image: Path,
                         character_name: str, character_id: int,
                         category: str) -> Tuple[bool, str]:
        """
        Determine if a downloaded image should be kept.

        Args:
            downloaded_image: Path to downloaded image
            character_name: Character name (e.g., "BARBAROSSA")
            character_id: Character ID (integer)
            category: Character category

        Returns:
            Tuple of (should_keep: bool, reason: str)
        """
        return self.checker.validate_download(downloaded_image, character_name, character_id, category)
