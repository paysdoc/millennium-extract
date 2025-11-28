#!/usr/bin/env python3
"""
Generate an empty PDF card with proper Millennium card dimensions and format.
This creates a blank card template with rounded corners and optional grid/guides.
"""
import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent))

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from src.config import CARD_WIDTH, CARD_HEIGHT, CORNER_RADIUS, BLEED, CROP_MARK_LENGTH
from src.card.utils import draw_rounded_rect
import click


def draw_crop_marks(c: canvas.Canvas, x: float, y: float, width: float, height: float,
                    bleed: float, mark_length: float):
    """
    Draw crop marks at the corners of the card.

    Args:
        c: ReportLab canvas
        x: X position of card (including bleed)
        y: Y position of card (including bleed)
        width: Card width (excluding bleed)
        height: Card height (excluding bleed)
        bleed: Bleed distance
        mark_length: Length of crop marks
    """
    c.setStrokeColor(colors.black)
    c.setLineWidth(0.25)

    # Actual card corners (without bleed)
    left = x + bleed
    right = x + bleed + width
    bottom = y + bleed
    top = y + bleed + height

    # Bottom-left corner
    c.line(left - bleed, bottom, left - bleed + mark_length, bottom)  # Horizontal
    c.line(left, bottom - bleed, left, bottom - bleed + mark_length)  # Vertical

    # Bottom-right corner
    c.line(right + bleed, bottom, right + bleed - mark_length, bottom)  # Horizontal
    c.line(right, bottom - bleed, right, bottom - bleed + mark_length)  # Vertical

    # Top-left corner
    c.line(left - bleed, top, left - bleed + mark_length, top)  # Horizontal
    c.line(left, top + bleed, left, top + bleed - mark_length)  # Vertical

    # Top-right corner
    c.line(right + bleed, top, right + bleed - mark_length, top)  # Horizontal
    c.line(right, top + bleed, right, top + bleed - mark_length)  # Vertical


def draw_guide_lines(c: canvas.Canvas, x: float, y: float, grid_spacing: float = 10 * mm):
    """
    Draw optional guide grid lines.

    Args:
        c: ReportLab canvas
        x: X position of card
        y: Y position of card
        grid_spacing: Spacing between grid lines
    """
    c.setStrokeColor(colors.Color(0.8, 0.8, 1.0, alpha=0.3))  # Light blue, semi-transparent
    c.setLineWidth(0.25)

    # Vertical lines
    current_x = x
    while current_x <= x + CARD_WIDTH:
        c.line(current_x, y, current_x, y + CARD_HEIGHT)
        current_x += grid_spacing

    # Horizontal lines
    current_y = y
    while current_y <= y + CARD_HEIGHT:
        c.line(x, current_y, x + CARD_WIDTH, current_y)
        current_y += grid_spacing


def create_empty_card(output_path: str, with_crop_marks: bool = False,
                     with_guides: bool = False, corner_radius: float = CORNER_RADIUS,
                     background_color=colors.white):
    """
    Create an empty PDF card with proper dimensions.

    Args:
        output_path: Path to save the PDF
        with_crop_marks: Whether to include crop marks for printing
        with_guides: Whether to include guide grid lines
        corner_radius: Corner radius in mm (default: 5mm)
        background_color: Background color for the card
    """
    # Calculate page size (card + bleed if crop marks are enabled)
    if with_crop_marks:
        page_width = CARD_WIDTH + 2 * BLEED + 2 * CROP_MARK_LENGTH
        page_height = CARD_HEIGHT + 2 * BLEED + 2 * CROP_MARK_LENGTH
        card_x = CROP_MARK_LENGTH
        card_y = CROP_MARK_LENGTH
    else:
        page_width = CARD_WIDTH
        page_height = CARD_HEIGHT
        card_x = 0
        card_y = 0

    # Create canvas
    c = canvas.Canvas(output_path, pagesize=(page_width, page_height))

    # Draw crop marks if requested
    if with_crop_marks:
        draw_crop_marks(c, card_x, card_y, CARD_WIDTH, CARD_HEIGHT, BLEED, CROP_MARK_LENGTH)

    # Draw card background with rounded corners
    c.setFillColor(background_color)
    c.setStrokeColor(colors.grey)
    c.setLineWidth(0.5)

    draw_rounded_rect(
        c,
        card_x + (BLEED if with_crop_marks else 0),
        card_y + (BLEED if with_crop_marks else 0),
        CARD_WIDTH,
        CARD_HEIGHT,
        corner_radius,
        fill=1,
        stroke=1
    )

    # Draw guide lines if requested
    if with_guides:
        draw_guide_lines(
            c,
            card_x + (BLEED if with_crop_marks else 0),
            card_y + (BLEED if with_crop_marks else 0)
        )

    # Add dimension annotations
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.grey)

    # Card dimensions text
    dim_text = f"{CARD_WIDTH/mm:.1f}mm × {CARD_HEIGHT/mm:.1f}mm"
    text_x = card_x + (BLEED if with_crop_marks else 0) + CARD_WIDTH / 2
    text_y = card_y + (BLEED if with_crop_marks else 0) + CARD_HEIGHT / 2

    # Draw dimension text in center
    c.drawCentredString(text_x, text_y, dim_text)
    c.drawCentredString(text_x, text_y - 10, f"Corner radius: {corner_radius/mm:.1f}mm")

    # Save PDF
    c.save()
    print(f"Empty card created: {output_path}")
    print(f"  Dimensions: {CARD_WIDTH/mm:.1f}mm × {CARD_HEIGHT/mm:.1f}mm")
    print(f"  Corner radius: {corner_radius/mm:.1f}mm")
    if with_crop_marks:
        print(f"  With crop marks (bleed: {BLEED/mm:.1f}mm)")
    if with_guides:
        print("  With guide grid lines")


@click.command()
@click.option(
    '--output',
    '-o',
    default='empty_card.pdf',
    help='Output PDF file path'
)
@click.option(
    '--crop-marks',
    is_flag=True,
    help='Include crop marks for professional printing'
)
@click.option(
    '--guides',
    is_flag=True,
    help='Include guide grid lines (10mm spacing)'
)
@click.option(
    '--corner-radius',
    '-r',
    type=float,
    default=5.0,
    help='Corner radius in mm (default: 5mm)'
)
@click.option(
    '--color',
    '-c',
    default='white',
    help='Background color (white, lightgray, lightblue, etc.)'
)
def main(output, crop_marks, guides, corner_radius, color):
    """Generate an empty PDF card with Millennium card dimensions."""

    # Parse color
    color_map = {
        'white': colors.white,
        'lightgray': colors.lightgrey,
        'lightblue': colors.lightblue,
        'lightyellow': colors.lightyellow,
        'lightgreen': colors.lightgreen,
    }
    bg_color = color_map.get(color.lower(), colors.white)

    create_empty_card(
        output_path=output,
        with_crop_marks=crop_marks,
        with_guides=guides,
        corner_radius=corner_radius * mm,
        background_color=bg_color
    )


if __name__ == '__main__':
    main()
