"""
Data models for image downloading.
Single Responsibility: Define data structures only.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class ImageInfo:
    """Information about a Wikimedia image."""
    url: str
    title: str
    width: int
    height: int
    aspect_ratio: float
    score: float

    def is_valid_portrait(self) -> bool:
        """Check if image is in portrait orientation."""
        return self.aspect_ratio >= 1.0


@dataclass
class SearchResult:
    """Result from a search query with metadata."""
    image_info: ImageInfo
    query: str
    rank: int


@dataclass
class DownloadMetadata:
    """Metadata to save alongside downloaded images."""
    character_name: str
    character_id: str
    category: str
    first_names: Optional[str]
    biography: Optional[str]
    birth_date: Optional[str]
    death_date: Optional[str]
    wikimedia_title: str
    wikimedia_url: str
    width: int
    height: int
    aspect_ratio: float
    score: float
    download_timestamp: str
    rank: int

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'character_name': self.character_name,
            'character_id': self.character_id,
            'category': self.category,
            'first_names': self.first_names,
            'biography': self.biography,
            'birth_date': self.birth_date,
            'death_date': self.death_date,
            'wikimedia_title': self.wikimedia_title,
            'wikimedia_url': self.wikimedia_url,
            'width': self.width,
            'height': self.height,
            'aspect_ratio': self.aspect_ratio,
            'score': self.score,
            'download_timestamp': self.download_timestamp,
            'rank': self.rank,
        }
