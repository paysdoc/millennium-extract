"""
Card configuration: dimensions, colors, and category mappings.
"""
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from typing import Optional


# Card dimensions (1:√2 aspect ratio, like A4 paper)
# Width : Height = 1 : √2 ≈ 1 : 1.414
CARD_WIDTH = 69 * mm
CARD_HEIGHT = 97.58 * mm  # 69 * √2 ≈ 97.58mm

# Layout spacing
MARGIN = 3 * mm
IMAGE_HEIGHT = 71 * mm  # Portrait image height (adjusted for taller card)
BANNER_HEIGHT = 8 * mm
HEADER_HEIGHT = 14 * mm  # Header section on back (includes biography, dates, category)

# Category color mapping
CATEGORY_COLORS = {
    'R': HexColor('#DC143C'),  # Royalty - red
    'S': HexColor('#FF8C00'),  # Statesman - orange
    'P': HexColor('#FFD700'),  # Philosopher - yellow
    'I': HexColor("#88FF00"),  # Innovator - lime green
    'M': HexColor('#228B22'),  # Mathematical Scientist - green
    'N': HexColor("#40E0B5"),  # Natural Scientist - turquoise
    'A': HexColor('#4169E1'),  # Artist - blue
    'B': HexColor('#4B0082'),  # Builders and Engineers - indigo
    'C': HexColor('#8B00FF'),  # Composer - violet
    'D': HexColor('#FF69B4'),  # Dramatist - pink
    'T': HexColor('#cccccc'),  # Towns and cities - gray
}

# Category full names
CATEGORY_NAMES = {
    'R': 'ROYALTY',
    'S': 'STATESMAN',
    'P': 'PHILOSOPHER',
    'I': 'INNOVATOR',
    'M': 'MATHEMATICAL SCIENTIST',
    'N': 'NATURAL SCIENTIST',
    'A': 'ARTIST',
    'B': 'BUILDERS AND ENGINEERS',
    'C': 'COMPOSER',
    'D': 'DRAMATIST',
    'T': 'TOWNS AND CITIES',
}

# Category sort order (for sorting cards and connections)
CATEGORY_ORDER = {
    'R': 0,   # Royalty
    'S': 1,   # Statesman
    'P': 2,   # Philosopher
    'I': 3,   # Innovator
    'M': 4,   # Mathematical Scientist
    'N': 5,   # Natural Scientist
    'A': 6,   # Artist
    'B': 7,   # Builders and Engineers
    'C': 8,   # Composer
    'D': 9,   # Dramatist
    'T': 10,  # Towns and Cities
}


def get_category_color(category_code: Optional[str]) -> HexColor:
    """Get color for a category code, default to gray if unknown."""
    if not category_code:
        return colors.grey
    return CATEGORY_COLORS.get(category_code, colors.grey)


def get_category_name(category_code: Optional[str]) -> str:
    """Get full name for a category code."""
    if not category_code:
        return "UNKNOWN"
    return CATEGORY_NAMES.get(category_code, "UNKNOWN")
