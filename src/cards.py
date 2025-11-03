"""
PDF generation for Millennium cards.
Creates printable sheets with multiple cards per page.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from typing import List, Optional
from src.types.supabase_types import CardData
from src.card import draw_card_front, draw_card_back, CARD_WIDTH, CARD_HEIGHT
from src.config import BLEED, CROP_MARK_LENGTH


# A4 page dimensions
PAGE_WIDTH, PAGE_HEIGHT = A4

# Base card dimensions (original size)
BASE_CARD_WIDTH = CARD_WIDTH
BASE_CARD_HEIGHT = CARD_HEIGHT

# Layout configuration - 3x3 cards per page
CARDS_PER_ROW = 3
CARDS_PER_COL = 3
CARDS_PER_PAGE = CARDS_PER_ROW * CARDS_PER_COL


def calculate_layout(card_width: float):
    """Calculate card layout based on desired card width."""
    # Calculate scale factor
    scale = card_width / BASE_CARD_WIDTH
    scaled_height = BASE_CARD_HEIGHT * scale

    # Calculate spacing
    horizontal_margin = (PAGE_WIDTH - (CARDS_PER_ROW * card_width)) / (CARDS_PER_ROW + 1)
    vertical_margin = (PAGE_HEIGHT - (CARDS_PER_COL * scaled_height)) / (CARDS_PER_COL + 1)

    return scale, scaled_height, horizontal_margin, vertical_margin


def draw_crop_marks_and_bleed(c: canvas.Canvas, x: float, y: float, card_width: float, card_height: float, scale: float = 1.0):
    """
    Draw crop marks and bleed area around a card for professional printing.

    Args:
        c: ReportLab canvas
        x: X position of card bottom-left corner (without bleed)
        y: Y position of card bottom-left corner (without bleed)
        card_width: Card width (without bleed)
        card_height: Card height (without bleed)
        scale: Scale factor applied to the card
    """
    # Scale bleed and crop mark dimensions
    scaled_bleed = BLEED * scale
    scaled_crop_length = CROP_MARK_LENGTH * scale

    # Draw bleed area (light gray rectangle)
    c.saveState()
    c.setFillColor(colors.Color(0.95, 0.95, 0.95))  # Very light gray
    c.setStrokeColor(colors.Color(0.8, 0.8, 0.8))  # Light gray border
    c.setLineWidth(0.25)
    c.rect(
        x - scaled_bleed,
        y - scaled_bleed,
        card_width + 2 * scaled_bleed,
        card_height + 2 * scaled_bleed,
        fill=1,
        stroke=1
    )
    c.restoreState()

    # Draw crop marks (black lines at corners, extending into bleed area)
    c.saveState()
    c.setStrokeColor(colors.black)
    c.setLineWidth(0.5)

    # Corner positions (at card edge - the actual trim line)
    corners = [
        (x, y),  # Bottom-left
        (x + card_width, y),  # Bottom-right
        (x, y + card_height),  # Top-left
        (x + card_width, y + card_height),  # Top-right
    ]

    for corner_x, corner_y in corners:
        # Determine which corner this is
        is_left = corner_x == x
        is_bottom = corner_y == y

        # Horizontal crop mark - extends from trim line outward into bleed
        if is_left:
            # Extend to the left from trim line
            c.line(
                corner_x,  # Start at trim line
                corner_y,
                corner_x - scaled_crop_length,  # Extend into bleed area
                corner_y
            )
        else:
            # Extend to the right from trim line
            c.line(
                corner_x,  # Start at trim line
                corner_y,
                corner_x + scaled_crop_length,  # Extend into bleed area
                corner_y
            )

        # Vertical crop mark - extends from trim line outward into bleed
        if is_bottom:
            # Extend downward from trim line
            c.line(
                corner_x,
                corner_y,  # Start at trim line
                corner_x,
                corner_y - scaled_crop_length  # Extend into bleed area
            )
        else:
            # Extend upward from trim line
            c.line(
                corner_x,
                corner_y,  # Start at trim line
                corner_x,
                corner_y + scaled_crop_length  # Extend into bleed area
            )

    c.restoreState()


def generate_cards_pdf(card_data_list: List[CardData], output_path: str, fronts_only: bool = False, separate_pages: bool = True, card_width: Optional[float] = None, crop_marks: bool = False, supabase_client=None):
    """
    Generate PDF with all character cards.
    Each card is completed (front and back) before moving to the next card.
    Each card appears on its own page(s).

    Args:
        card_data_list: List of card data to render
        output_path: Path to save the PDF file
        fronts_only: If True, only render card fronts; if False, render fronts and backs
        separate_pages: If True, render front and back on separate pages (default); if False, render side by side
        card_width: Desired card width in mm (default: None = use original 69mm)
        crop_marks: If True, add crop marks and bleed area for professional printing
        supabase_client: Supabase client for downloading images (optional)
    """
    total_cards = len(card_data_list)

    # Calculate scaling based on desired width
    if card_width is None:
        card_width = BASE_CARD_WIDTH
    scale, scaled_height, _, _ = calculate_layout(card_width)

    # Calculate page size based on card dimensions and crop marks
    if crop_marks:
        # Add bleed area to page dimensions
        scaled_bleed = BLEED * scale
        if separate_pages:
            # Single card per page with bleed
            page_width = card_width + 2 * scaled_bleed
            page_height = scaled_height + 2 * scaled_bleed
        else:
            # Two cards side by side with bleed
            page_width = 2 * card_width + 4 * scaled_bleed
            page_height = scaled_height + 2 * scaled_bleed
    else:
        # No bleed, page matches card size exactly
        if separate_pages:
            page_width = card_width
            page_height = scaled_height
        else:
            # Two cards side by side
            page_width = 2 * card_width
            page_height = scaled_height

    c = canvas.Canvas(output_path, pagesize=(page_width, page_height))

    print(f"Generating PDF with {total_cards} cards...")
    print(f"Card size: {card_width / mm:.1f}mm × {scaled_height / mm:.1f}mm (scale: {scale:.2f}x)")
    print(f"Page size: {page_width / mm:.1f}mm × {page_height / mm:.1f}mm")
    print("Rendering cards (one card per page)...")

    # Generate cards one at a time
    for i, card_data in enumerate(card_data_list):
        card_number = i + 1

        if separate_pages:
            # Front on its own page
            if crop_marks:
                # Position card in center of bleed area
                scaled_bleed = BLEED * scale
                x_front = scaled_bleed
                y_front = scaled_bleed
                draw_crop_marks_and_bleed(c, x_front, y_front, card_width, scaled_height, scale)
            else:
                # No bleed, card fills page
                x_front = 0
                y_front = 0

            draw_card_front(c, card_data, x_front, y_front, scale, supabase_client)
            c.showPage()

            # Back on its own page
            if not fronts_only:
                if crop_marks:
                    scaled_bleed = BLEED * scale
                    x_back = scaled_bleed
                    y_back = scaled_bleed
                    draw_crop_marks_and_bleed(c, x_back, y_back, card_width, scaled_height, scale)
                else:
                    x_back = 0
                    y_back = 0

                draw_card_back(c, card_data, x_back, y_back, card_number, scale, supabase_client)
                c.showPage()
        else:
            # Front and back side by side on same page
            if crop_marks:
                scaled_bleed = BLEED * scale
                # Front on left with bleed
                x_front = scaled_bleed
                y_front = scaled_bleed
                draw_crop_marks_and_bleed(c, x_front, y_front, card_width, scaled_height, scale)
            else:
                x_front = 0
                y_front = 0

            draw_card_front(c, card_data, x_front, y_front, scale, supabase_client)

            # Back on right side
            if not fronts_only:
                if crop_marks:
                    scaled_bleed = BLEED * scale
                    x_back = card_width + 3 * scaled_bleed  # Skip front card + 2 bleeds between
                    y_back = scaled_bleed
                    draw_crop_marks_and_bleed(c, x_back, y_back, card_width, scaled_height, scale)
                else:
                    x_back = card_width
                    y_back = 0

                draw_card_back(c, card_data, x_back, y_back, card_number, scale, supabase_client)

            c.showPage()

    c.save()
    print(f"PDF saved to {output_path}")


def generate_single_card_pdf(card_data: CardData, output_path: str, card_number: int = 1, separate_pages: bool = True, card_width: Optional[float] = None, crop_marks: bool = False, supabase_client=None):
    """
    Generate PDF with a single card.

    Args:
        card_data: Card data to render
        output_path: Path to save the PDF file
        card_number: Card number to display
        separate_pages: If True, show front and back on separate pages (default); if False, show side by side
        card_width: Desired card width in mm (default: None = use original 69mm)
        crop_marks: If True, add crop marks and bleed area for professional printing
        supabase_client: Supabase client for downloading images (optional)
    """
    # Calculate scaling based on desired width
    if card_width is None:
        card_width = BASE_CARD_WIDTH
    scale, scaled_height, _, _ = calculate_layout(card_width)

    # Calculate page size based on card dimensions and crop marks
    if crop_marks:
        # Add bleed area to page dimensions
        scaled_bleed = BLEED * scale
        if separate_pages:
            # Single card per page with bleed
            page_width = card_width + 2 * scaled_bleed
            page_height = scaled_height + 2 * scaled_bleed
        else:
            # Two cards side by side with bleed
            page_width = 2 * card_width + 4 * scaled_bleed
            page_height = scaled_height + 2 * scaled_bleed
    else:
        # No bleed, page matches card size exactly
        if separate_pages:
            page_width = card_width
            page_height = scaled_height
        else:
            # Two cards side by side
            page_width = 2 * card_width
            page_height = scaled_height

    c = canvas.Canvas(output_path, pagesize=(page_width, page_height))

    if separate_pages:
        # Draw front on page 1
        if crop_marks:
            scaled_bleed = BLEED * scale
            x_front = scaled_bleed
            y_front = scaled_bleed
            draw_crop_marks_and_bleed(c, x_front, y_front, card_width, scaled_height, scale)
        else:
            x_front = 0
            y_front = 0

        draw_card_front(c, card_data, x_front, y_front, scale, supabase_client)
        c.showPage()

        # Draw back on page 2
        if crop_marks:
            scaled_bleed = BLEED * scale
            x_back = scaled_bleed
            y_back = scaled_bleed
            draw_crop_marks_and_bleed(c, x_back, y_back, card_width, scaled_height, scale)
        else:
            x_back = 0
            y_back = 0

        draw_card_back(c, card_data, x_back, y_back, card_number, scale, supabase_client)
    else:
        # Draw front on left side
        if crop_marks:
            scaled_bleed = BLEED * scale
            x_front = scaled_bleed
            y_front = scaled_bleed
            draw_crop_marks_and_bleed(c, x_front, y_front, card_width, scaled_height, scale)
        else:
            x_front = 0
            y_front = 0

        draw_card_front(c, card_data, x_front, y_front, scale, supabase_client)

        # Draw back on right side
        if crop_marks:
            scaled_bleed = BLEED * scale
            x_back = card_width + 3 * scaled_bleed
            y_back = scaled_bleed
            draw_crop_marks_and_bleed(c, x_back, y_back, card_width, scaled_height, scale)
        else:
            x_back = card_width
            y_back = 0

        draw_card_back(c, card_data, x_back, y_back, card_number, scale, supabase_client)

    c.save()
    print(f"Single card PDF saved to {output_path}")
    print(f"Card size: {card_width / mm:.1f}mm × {scaled_height / mm:.1f}mm (scale: {scale:.2f}x)")
    print(f"Page size: {page_width / mm:.1f}mm × {page_height / mm:.1f}mm")
