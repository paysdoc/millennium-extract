"""
Configuration constants for image downloading.
Single Responsibility: Centralize all configuration values.
"""
import math


class WikimediaConfig:
    """Configuration for Wikimedia API interactions."""
    API_URL = "https://commons.wikimedia.org/w/api.php"
    HEADERS = {
        'User-Agent': 'MillenniumCardGame/1.0 (Educational card game project; contact via GitHub)'
    }
    API_DELAY_SECONDS = 1.0
    SEARCH_DELAY_SECONDS = 0.2
    REQUEST_TIMEOUT_SECONDS = 30
    DOWNLOAD_TIMEOUT_SECONDS = 60
    SEARCH_LIMIT = 15


class ImageRequirements:
    """Requirements for image quality and dimensions."""
    TARGET_ASPECT_RATIO = 1.298  # Effective card aspect ratio (excluding banner)
    MIN_HEIGHT = 1000
    ACCEPTABLE_RATIO_MIN = 1
    ACCEPTABLE_RATIO_MAX = 2
    OPTIMAL_HEIGHT = 3508  # For resolution scoring

    # Scoring weights
    RATIO_WEIGHT = 0.7
    RESOLUTION_WEIGHT = 0.3


class DownloadConfig:
    """Configuration for download behavior."""
    MAX_ALTERNATIVES = 2  # Number of alternative images to download per character
    OUTPUT_DIR = "sourced_images/wikimedia/by_character_id"
    CHUNK_SIZE = 8192  # For streaming downloads

    # Query limits
    MAX_QUERIES_PER_CHARACTER = 10
    STOP_AFTER_CANDIDATES = 9  # (max_alternatives + 1) * 3
