"""
Town connections grid component for card back.
"""
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from typing import List
from src.types.supabase_types import DenormalizedConnection
from src.config import CARD_WIDTH, BANNER_HEIGHT, get_category_color


def draw_towns_text(c: canvas.Canvas, town_connections: List[DenormalizedConnection],
                   x: float, y: float):
    """
    Draw only the text content of towns (not the background).
    Used when bleed > 0, as the background is drawn before clipping.

    Args:
        c: ReportLab canvas
        town_connections: List of category T connections
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
    """
    if not town_connections:
        return

    # Calculate grid dimensions (same as draw_towns_grid)
    num_town_rows = (len(town_connections) + 2) // 3
    town_row_height = 6
    town_padding_top = 2
    town_padding_bottom = 2
    town_bg_height = num_town_rows * town_row_height + town_padding_top + town_padding_bottom

    banner_top = y + BANNER_HEIGHT
    town_margin = 2 * mm
    town_bottom_y = banner_top + town_margin
    town_grid_y = town_bottom_y + town_bg_height

    # Draw towns with black text
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 5)

    col_width = CARD_WIDTH / 3
    town_text_start_y = town_grid_y - town_padding_top
    left_indent = 3.5

    for i, town in enumerate(town_connections):
        col = i % 3
        row = i // 3

        value_x = x + (col * col_width) + left_indent
        town_y = town_text_start_y - (row * town_row_height) - 4

        # Draw value number (bold)
        c.setFont("Helvetica-Bold", 5)
        c.drawString(value_x, town_y, str(town.value))

        # Draw town name (regular font)
        c.setFont("Helvetica", 5)
        value_width = c.stringWidth(str(town.value), "Helvetica-Bold", 5)
        name_x = value_x + value_width + 2
        town_display = town.character_name or ""
        c.drawString(name_x, town_y, town_display)


def draw_towns_grid(c: canvas.Canvas, town_connections: List[DenormalizedConnection],
                   x: float, y: float, bleed: float = 0):
    """
    Draw the town connections grid above the banner.

    Towns are displayed in a compact grid format with 3 towns per row.
    Each town shows "value name" (e.g., "5 CAMBRIDGE") in black text
    on a colored background (category T color).

    Args:
        c: ReportLab canvas
        town_connections: List of category T connections
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
        bleed: Bleed distance to extend background beyond card edge (default: 0)
    """
    if not town_connections:
        return

    # Calculate grid dimensions
    num_town_rows = (len(town_connections) + 2) // 3  # 3 towns per row, round up
    town_row_height = 6  # 6pt per row
    town_padding_top = 2  # 2pt padding at top
    town_padding_bottom = 2  # 2pt padding at bottom
    town_bg_height = num_town_rows * town_row_height + town_padding_top + town_padding_bottom

    # Position towns just above banner with 2mm margin
    banner_top = y + BANNER_HEIGHT  # Top of banner (banner is now at y, the bottom of the card)
    town_margin = 2 * mm  # Margin above banner
    town_bottom_y = banner_top + town_margin
    town_grid_y = town_bottom_y + town_bg_height  # Top of town grid

    # Draw background with category T color (includes padding), extending into bleed
    c.setFillColor(get_category_color('T'))
    if bleed > 0:
        # Extend into bleed on left and right
        c.rect(x - bleed, town_bottom_y, CARD_WIDTH + 2 * bleed, town_bg_height, fill=1, stroke=0)
    else:
        c.rect(x, town_bottom_y, CARD_WIDTH, town_bg_height, fill=1, stroke=0)

    # Draw towns with black text on colored background
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 5)

    col_width = CARD_WIDTH / 3
    # Start text after top padding
    town_text_start_y = town_grid_y - town_padding_top

    # Left indent for value number to align with connections table
    # Connections table has 3mm or 4mm value column, add 2pt left padding
    left_indent = 3.5  # points, aligns value numbers with regular connections

    for i, town in enumerate(town_connections):
        col = i % 3  # 0, 1, or 2
        row = i // 3

        # Value number position (with indent to align with connections table)
        value_x = x + (col * col_width) + left_indent
        town_y = town_text_start_y - (row * town_row_height) - 4  # 4pt from top of row

        # Draw value number (bold, to match connections table)
        c.setFont("Helvetica-Bold", 5)
        c.drawString(value_x, town_y, str(town.value))

        # Draw town name (regular font, space after value)
        c.setFont("Helvetica", 5)
        value_width = c.stringWidth(str(town.value), "Helvetica-Bold", 5)
        name_x = value_x + value_width + 2  # 2pt space after value
        town_display = town.character_name or ""
        c.drawString(name_x, town_y, town_display)
