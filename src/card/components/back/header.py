"""
Header section for card back (name, dates, biography, category box).
"""
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from src.types.supabase_types import Character
from src.card.config import (
    CARD_WIDTH, CARD_HEIGHT, HEADER_HEIGHT, MARGIN,
    get_category_name
)
from src.card.utils import draw_wrapped_text, draw_text_with_outline


def draw_back_header(c: canvas.Canvas, character: Character, x: float, y: float, category_color: HexColor):
    """
    Draw the header section on the card back.

    Includes:
    - Colored background (category color at 75% opacity)
    - Character name (bold, top)
    - Dates and category (below name)
    - Biography (truncated to 2 lines with ellipsis)
    - Category box (top right, same height as header)

    Args:
        c: ReportLab canvas
        character: Character data
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
        category_color: Color for the category box and header background
    """
    category_name = get_category_name(character.type)
    category_box_width = 14
    card_num_box_height = HEADER_HEIGHT

    # Draw header section with category color at 75% opacity (actually 50% in implementation)
    c.setFillColorRGB(
        category_color.red,
        category_color.green,
        category_color.blue,
        alpha=0.5
    )
    c.rect(x, y + CARD_HEIGHT - HEADER_HEIGHT, CARD_WIDTH, HEADER_HEIGHT, fill=1, stroke=0)

    # Calculate max text width excluding category box
    max_header_text_width = CARD_WIDTH - (2 * MARGIN) - category_box_width

    # Draw character name at top of header
    c.setFillColor(colors.black)
    full_name = f"{character.name or ''} {character.first_names or ''}".strip().upper()
    name_y = y + CARD_HEIGHT - MARGIN - 3
    draw_wrapped_text(
        c, full_name,
        x + MARGIN,
        name_y,
        max_header_text_width,
        "Helvetica-Bold", 9,
        line_height=10,
        max_lines=1
    )

    # Draw dates | category directly under name (constrained width)
    c.setFont("Helvetica", 6)
    category_display = category_name[:20]  # Truncate if too long
    dates = f"{character.birth_date or ''}-{character.death_date or ''}"
    dates_category_text = f"{dates} | {category_display}"
    dates_category_y = name_y - 10  # Directly under name

    # Truncate dates/category if too long
    while c.stringWidth(dates_category_text, "Helvetica", 6) > max_header_text_width and len(category_display) > 5:
        category_display = category_display[:-1]
        dates_category_text = f"{dates} | {category_display}"

    c.drawString(x + MARGIN, dates_category_y, dates_category_text)

    # Draw biography under dates with small margin (constrained width)
    if character.biography:
        bio_text = character.biography.replace('\n', ' ').strip()
        bio_y = dates_category_y - 8  # Small margin below dates
        draw_wrapped_text(
            c, bio_text,
            x + MARGIN,
            bio_y,
            max_header_text_width,
            "Helvetica", 6,
            line_height=6.5,
            max_lines=2,
            truncate_with_ellipsis=True
        )

    # Draw category box (top right)
    c.setFillColor(category_color)
    c.rect(
        x + CARD_WIDTH - category_box_width,
        y + CARD_HEIGHT - card_num_box_height,
        category_box_width,
        card_num_box_height,
        fill=1,
        stroke=0
    )

    # Draw category code centered in box
    c.setFont("Helvetica-Bold", 14)
    card_id = f"{character.type or 'X'}"
    card_id_width = c.stringWidth(card_id, "Helvetica-Bold", 14)

    # Center horizontally and vertically in box
    card_id_x = x + CARD_WIDTH - category_box_width + (category_box_width - card_id_width) / 2
    card_id_y = y + CARD_HEIGHT - card_num_box_height / 2 - 5

    # Draw with outline
    draw_text_with_outline(c, card_id, card_id_x, card_id_y, "Helvetica-Bold", 14)
