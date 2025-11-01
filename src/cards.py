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

# Layout configuration - 3x3 cards per page
CARDS_PER_ROW = 3
CARDS_PER_COL = 3
CARDS_PER_PAGE = CARDS_PER_ROW * CARDS_PER_COL

# Calculate spacing
HORIZONTAL_MARGIN = (PAGE_WIDTH - (CARDS_PER_ROW * CARD_WIDTH)) / (CARDS_PER_ROW + 1)
VERTICAL_MARGIN = (PAGE_HEIGHT - (CARDS_PER_COL * CARD_HEIGHT)) / (CARDS_PER_COL + 1)


def generate_cards_pdf(card_data_list: List[CardData], output_path: str, fronts_only: bool = False, supabase_client=None):
    """
    Generate PDF with all character cards.

    Args:
        card_data_list: List of card data to render
        output_path: Path to save the PDF file
        fronts_only: If True, only render card fronts; if False, render fronts and backs
        supabase_client: Supabase client for downloading images (optional)
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    total_cards = len(card_data_list)
    print(f"Generating PDF with {total_cards} cards...")

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
            x = HORIZONTAL_MARGIN + col * (CARD_WIDTH + HORIZONTAL_MARGIN)
            y = PAGE_HEIGHT - VERTICAL_MARGIN - (row + 1) * CARD_HEIGHT - row * VERTICAL_MARGIN

            draw_card_front(c, card_data_list[i], x, y, supabase_client)

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
                x = HORIZONTAL_MARGIN + col * (CARD_WIDTH + HORIZONTAL_MARGIN)
                y = PAGE_HEIGHT - VERTICAL_MARGIN - (row + 1) * CARD_HEIGHT - row * VERTICAL_MARGIN

                # Use the card's position in the deck as the card number
                card_number = i + 1
                draw_card_back(c, card_data_list[i], x, y, card_number, supabase_client)

            c.showPage()

    c.save()
    print(f"PDF saved to {output_path}")


def generate_single_card_pdf(card_data: CardData, output_path: str, card_number: int = 1, supabase_client=None):
    """
    Generate PDF with a single card (front and back side by side).

    Args:
        card_data: Card data to render
        output_path: Path to save the PDF file
        card_number: Card number to display
        supabase_client: Supabase client for downloading images (optional)
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    # Draw front on left side
    x_front = (PAGE_WIDTH / 2 - CARD_WIDTH) / 2
    y_front = (PAGE_HEIGHT - CARD_HEIGHT) / 2
    draw_card_front(c, card_data, x_front, y_front, supabase_client)

    # Draw back on right side
    x_back = PAGE_WIDTH / 2 + (PAGE_WIDTH / 2 - CARD_WIDTH) / 2
    y_back = (PAGE_HEIGHT - CARD_HEIGHT) / 2
    draw_card_back(c, card_data, x_back, y_back, card_number, supabase_client)

    c.save()
    print(f"Single card PDF saved to {output_path}")
