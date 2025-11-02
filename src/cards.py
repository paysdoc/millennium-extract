"""
PDF generation for Millennium cards.
Creates printable sheets with multiple cards per page.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from typing import List, Optional
from src.types.supabase_types import CardData
from src.card import draw_card_front, draw_card_back, CARD_WIDTH, CARD_HEIGHT


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


def generate_cards_pdf(card_data_list: List[CardData], output_path: str, fronts_only: bool = False, separate_pages: bool = True, card_width: Optional[float] = None, supabase_client=None):
    """
    Generate PDF with all character cards.

    Args:
        card_data_list: List of card data to render
        output_path: Path to save the PDF file
        fronts_only: If True, only render card fronts; if False, render fronts and backs
        separate_pages: If True, render fronts and backs on separate pages (default); if False, render side by side
        card_width: Desired card width in mm (default: None = use original 69mm)
        supabase_client: Supabase client for downloading images (optional)
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    total_cards = len(card_data_list)

    # Calculate scaling based on desired width
    if card_width is None:
        card_width = BASE_CARD_WIDTH
    scale, scaled_height, horizontal_margin, vertical_margin = calculate_layout(card_width)

    print(f"Generating PDF with {total_cards} cards...")
    print(f"Card size: {card_width / mm:.1f}mm × {scaled_height / mm:.1f}mm (scale: {scale:.2f}x)")

    # Generate front pages
    print("Rendering card fronts...")
    for page_num in range((total_cards + CARDS_PER_PAGE - 1) // CARDS_PER_PAGE):
        start_idx = page_num * CARDS_PER_PAGE
        end_idx = min(start_idx + CARDS_PER_PAGE, total_cards)

        for i in range(start_idx, end_idx):
            card_idx = i - start_idx
            row = card_idx // CARDS_PER_ROW
            col = card_idx % CARDS_PER_ROW

            # Calculate position (bottom-left corner)
            x = horizontal_margin + col * (card_width + horizontal_margin)
            y = PAGE_HEIGHT - vertical_margin - (row + 1) * scaled_height - row * vertical_margin

            draw_card_front(c, card_data_list[i], x, y, scale, supabase_client)

        c.showPage()

    if not fronts_only:
        # Generate back pages
        print("Rendering card backs...")
        for page_num in range((total_cards + CARDS_PER_PAGE - 1) // CARDS_PER_PAGE):
            start_idx = page_num * CARDS_PER_PAGE
            end_idx = min(start_idx + CARDS_PER_PAGE, total_cards)

            for i in range(start_idx, end_idx):
                card_idx = i - start_idx
                row = card_idx // CARDS_PER_ROW
                # Mirror column position for back-to-back printing
                col = (CARDS_PER_ROW - 1) - (card_idx % CARDS_PER_ROW)

                # Calculate position (bottom-left corner)
                x = horizontal_margin + col * (card_width + horizontal_margin)
                y = PAGE_HEIGHT - vertical_margin - (row + 1) * scaled_height - row * vertical_margin

                # Use the card's position in the deck as the card number
                card_number = i + 1
                draw_card_back(c, card_data_list[i], x, y, card_number, scale, supabase_client)

            c.showPage()

    c.save()
    print(f"PDF saved to {output_path}")


def generate_single_card_pdf(card_data: CardData, output_path: str, card_number: int = 1, separate_pages: bool = True, card_width: Optional[float] = None, supabase_client=None):
    """
    Generate PDF with a single card.

    Args:
        card_data: Card data to render
        output_path: Path to save the PDF file
        card_number: Card number to display
        separate_pages: If True, show front and back on separate pages (default); if False, show side by side
        card_width: Desired card width in mm (default: None = use original 69mm)
        supabase_client: Supabase client for downloading images (optional)
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    # Calculate scaling based on desired width
    if card_width is None:
        card_width = BASE_CARD_WIDTH
    scale, scaled_height, _, _ = calculate_layout(card_width)

    if separate_pages:
        # Draw front on page 1 (centered)
        x_front = (PAGE_WIDTH - card_width) / 2
        y_front = (PAGE_HEIGHT - scaled_height) / 2
        draw_card_front(c, card_data, x_front, y_front, scale, supabase_client)
        c.showPage()

        # Draw back on page 2 (centered)
        x_back = (PAGE_WIDTH - card_width) / 2
        y_back = (PAGE_HEIGHT - scaled_height) / 2
        draw_card_back(c, card_data, x_back, y_back, card_number, scale, supabase_client)
    else:
        # Draw front on left side
        x_front = (PAGE_WIDTH / 2 - card_width) / 2
        y_front = (PAGE_HEIGHT - scaled_height) / 2
        draw_card_front(c, card_data, x_front, y_front, scale, supabase_client)

        # Draw back on right side
        x_back = PAGE_WIDTH / 2 + (PAGE_WIDTH / 2 - card_width) / 2
        y_back = (PAGE_HEIGHT - scaled_height) / 2
        draw_card_back(c, card_data, x_back, y_back, card_number, scale, supabase_client)

    c.save()
    print(f"Single card PDF saved to {output_path}")
    print(f"Card size: {card_width / mm:.1f}mm × {scaled_height / mm:.1f}mm (scale: {scale:.2f}x)")
