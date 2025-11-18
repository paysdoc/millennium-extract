"""
Image quality evaluation and scoring.
Single Responsibility: Score and rank images based on quality criteria.
"""
from .models import ImageInfo
from .config import ImageRequirements


class ImageScorer:
    """
    Evaluates and scores images based on aspect ratio and resolution.
    """

    def __init__(self, config: ImageRequirements = None, category: str = None):
        """
        Initialize scorer with configuration.

        Args:
            config: Image requirements configuration (uses default if None)
            category: Character category code (e.g., 'T', 'P', 'R')
        """
        self.config = config or ImageRequirements()
        self.category = category

    def calculate_ratio_score(self, aspect_ratio: float) -> float:
        """
        Calculate score based on how close the aspect ratio is to target.
        For category T, allows both portrait (√2) and landscape (1/√2) ratios.

        Args:
            aspect_ratio: Height/width ratio

        Returns:
            Score between 0 and 1
        """
        target_ratio = self.config.TARGET_ASPECT_RATIO

        # For category T, check both portrait and landscape ratios
        if self.category == 'T':
            portrait_diff = abs(aspect_ratio - target_ratio)
            landscape_diff = abs(aspect_ratio - (1 / target_ratio))
            # Use the better (smaller) difference
            min_diff = min(portrait_diff, landscape_diff)
            return 1 / (1 + min_diff)

        return 1 / (1 + abs(aspect_ratio - target_ratio))

    def calculate_resolution_score(self, height: int) -> float:
        """
        Calculate score based on image resolution.

        Args:
            height: Image height in pixels

        Returns:
            Score between 0 and 1 (capped at 1.0)
        """
        return min(height / self.config.OPTIMAL_HEIGHT, 1.0)

    def calculate_total_score(self, aspect_ratio: float, height: int) -> float:
        """
        Calculate weighted total score for an image.

        Args:
            aspect_ratio: Height/width ratio
            height: Image height in pixels

        Returns:
            Weighted total score
        """
        ratio_score = self.calculate_ratio_score(aspect_ratio)
        resolution_score = self.calculate_resolution_score(height)

        total = (ratio_score * self.config.RATIO_WEIGHT +
                 resolution_score * self.config.RESOLUTION_WEIGHT)

        return total

    def is_valid_image(self, width: int, height: int) -> list[str]:
        """
        Check if image meets minimum requirements.
        For category T, allows both portrait and landscape orientations.

        Args:
            width: Image width in pixels
            height: Image height in pixels

        Returns:
            List of validation failure reasons. Empty list means valid.
        """
        reasons = []

        # Check minimum dimensions
        if width == 0 or height == 0:
            reasons.append("zero dimensions")
            return reasons  # No point checking further

        if height < self.config.MIN_HEIGHT:
            reasons.append(f"height {height}px < minimum {self.config.MIN_HEIGHT}px")

        # Check orientation
        aspect_ratio = height / width

        # Category T allows both portrait and landscape
        # All other categories require portrait orientation
        if aspect_ratio < 1.0 and self.category != 'T':
            reasons.append(f"landscape orientation (ratio={aspect_ratio:.3f})")

        return reasons

    def score_image(self, width: int, height: int) -> tuple[bool, float, float]:
        """
        Evaluate an image and return validity and scores.

        Args:
            width: Image width in pixels
            height: Image height in pixels

        Returns:
            Tuple of (is_valid, aspect_ratio, score)
        """
        validation_errors = self.is_valid_image(width, height)
        if validation_errors:  # Empty list means valid
            return False, 0.0, 0.0

        aspect_ratio = height / width
        score = self.calculate_total_score(aspect_ratio, height)

        return True, aspect_ratio, score

    def create_image_info(self, url: str, title: str, width: int, height: int) -> ImageInfo | None:
        """
        Create ImageInfo object if image is valid.

        Args:
            url: Image URL
            title: Image title
            width: Image width
            height: Image height

        Returns:
            ImageInfo object if valid, None otherwise
        """
        is_valid, aspect_ratio, score = self.score_image(width, height)

        if not is_valid:
            return None

        return ImageInfo(
            url=url,
            title=title,
            width=width,
            height=height,
            aspect_ratio=aspect_ratio,
            score=score
        )
