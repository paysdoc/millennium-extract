"""
Data models for Supabase tables.
"""
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Character:
    """Character data model matching Supabase character table."""
    id: int  # Integer ID (primary key)
    name: Optional[str] = None
    first_names: Optional[str] = None
    birth_date: Optional[str] = None
    death_date: Optional[str] = None
    biography: Optional[str] = None
    type: Optional[str] = None  # Category code (R, S, P, M, N, A, B, C, D, T)
    link: Optional[str] = None
    image_link: Optional[str] = None
    joker_type: Optional[str] = None  # Joker category (or "*" for wildcard)
    joker_type_value: Optional[int] = None  # Joker connection value
    joker_type_why: Optional[str] = None  # Joker connection why
    joker_type_why_short: Optional[str] = None  # Joker connection why_short


@dataclass
class Connection:
    """Connection data model matching Supabase connection table."""
    id: int  # Integer ID (primary key)
    char1_id: Optional[int] = None  # Character 1 ID (integer)
    char2_id: Optional[int] = None  # Character 2 ID (integer)
    value: Optional[int] = None
    why: Optional[str] = None
    why_short: Optional[str] = None  # Short version of connection description
    active: Optional[bool] = None  # Whether the connection is active


@dataclass
class DenormalizedConnection:
    """Connection with character names instead of IDs."""
    character_name: str
    category_code: str
    value: int
    why: str
    why_short: Optional[str] = None  # Short version of connection description


@dataclass
class CardData:
    """Complete card data ready for rendering."""
    character: Character
    connections: List[DenormalizedConnection]
