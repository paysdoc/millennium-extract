"""
Banner component for card front and back.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from src.config import CARD_WIDTH, BANNER_HEIGHT, MARGIN
from src.card.utils import wrap_text, draw_text_with_outline


def draw_banner(c: canvas.Canvas, name: str, x: float, y: float, category_color: HexColor):
    """
    Draw a colored banner with character name (used on both front and back).

    The banner is positioned at the bottom of the card and includes
    text with an outline for better readability on light-colored backgrounds.

    Args:
        c: ReportLab canvas
        name: Character name to display (will be uppercased)
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
        category_color: Color for the banner background
    """
    # Draw colored banner at the very bottom of the card
    banner_y = y  # At card bottom
    c.setFillColor(category_color)
    c.rect(x, banner_y, CARD_WIDTH, BANNER_HEIGHT, fill=1, stroke=0)

    # Prepare name text
    name_upper = (name or "UNKNOWN").upper()
    max_name_width = CARD_WIDTH - (2 * MARGIN)

    # Try to fit name in one line
    font_size = 12
    name_lines = wrap_text(c, name_upper, max_name_width, "Helvetica-Bold", font_size)

    # If name wraps to multiple lines, reduce font size
    if len(name_lines) > 1:
        font_size = 10
        name_lines = wrap_text(c, name_upper, max_name_width, "Helvetica-Bold", font_size)

    # Draw name with black outline for better readability
    c.setFont("Helvetica-Bold", font_size)
    text_y_offset = banner_y + BANNER_HEIGHT / 2 - (len(name_lines) * font_size) / 2 + 2

    for line in name_lines[:2]:  # Max 2 lines
        text_width = c.stringWidth(line, "Helvetica-Bold", font_size)
        text_x = x + (CARD_WIDTH - text_width) / 2

        # Draw with outline
        draw_text_with_outline(c, line, text_x, text_y_offset, "Helvetica-Bold", font_size)

        text_y_offset -= font_size + 1
