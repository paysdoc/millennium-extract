"""
Data models for Supabase tables.
"""
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Character:
    """Character data model matching Supabase character table."""
    id: int
    name: Optional[str] = None
    first_names: Optional[str] = None
    birth_date: Optional[str] = None
    death_date: Optional[str] = None
    biography: Optional[str] = None
    type: Optional[str] = None  # Category code (R, S, P, M, N, A, B, C, D, T)
    link: Optional[str] = None
    image_link: Optional[str] = None


@dataclass
class Connection:
    """Connection data model matching Supabase connection table."""
    id: int
    char1_id: Optional[int] = None
    char2_id: Optional[int] = None
    value: Optional[int] = None
    why: Optional[str] = None


@dataclass
class DenormalizedConnection:
    """Connection with character names instead of IDs."""
    character_name: str
    category_code: str
    value: int
    why: str


@dataclass
class CardData:
    """Complete card data ready for rendering."""
    character: Character
    connections: List[DenormalizedConnection]
