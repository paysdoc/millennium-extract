"""
Town connections grid component for card back.
"""
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from typing import List
from src.types.supabase_types import DenormalizedConnection
from src.config import CARD_WIDTH, BANNER_HEIGHT, get_category_color


def draw_towns_grid(c: canvas.Canvas, town_connections: List[DenormalizedConnection],
                   x: float, y: float):
    """
    Draw the town connections grid above the banner.

    Towns are displayed in a compact grid format with 3 towns per row.
    Each town shows "value: name" (e.g., "5: CAMBRIDGE") in white text
    on a colored background (category T color).

    Args:
        c: ReportLab canvas
        town_connections: List of category T connections
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
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

    # Draw background with category T color (includes padding)
    c.setFillColor(get_category_color('T'))
    c.rect(x, town_bottom_y, CARD_WIDTH, town_bg_height, fill=1, stroke=0)

    # Draw towns with white text on colored background
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 5)

    col_width = CARD_WIDTH / 3
    # Start text after top padding
    town_text_start_y = town_grid_y - town_padding_top

    for i, town in enumerate(town_connections):
        col = i % 3  # 0, 1, or 2
        row = i // 3

        town_x = x + (col * col_width) + 2
        town_y = town_text_start_y - (row * town_row_height) - 4  # 4pt from top of row

        town_display = f"{town.value}: {town.character_name}"
        c.drawString(town_x, town_y, town_display)
