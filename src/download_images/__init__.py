"""
Download Images Module
Provides tools for downloading and managing character images from Wikimedia Commons.
"""

# Core components
from .downloader import CharacterImageDownloader, DownloadSummaryPrinter
from .wikimedia_api import WikimediaAPIClient
from .query_builder import QueryBuilder
from .file_manager import FileManager
from .image_scorer import ImageScorer

# Models
from .models import ImageInfo, SearchResult, DownloadMetadata

# Configuration
from .config import WikimediaConfig, ImageRequirements, DownloadConfig

# Utilities
from .text_parser import YearExtractor, NameParser, BiographyParser

__all__ = [
    # Main components
    'CharacterImageDownloader',
    'DownloadSummaryPrinter',
    'WikimediaAPIClient',
    'QueryBuilder',
    'FileManager',
    'ImageScorer',

    # Models
    'ImageInfo',
    'SearchResult',
    'DownloadMetadata',

    # Configuration
    'WikimediaConfig',
    'ImageRequirements',
    'DownloadConfig',

    # Utilities
    'YearExtractor',
    'NameParser',
    'BiographyParser',
]
