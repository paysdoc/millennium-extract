"""
Main card rendering functions - public API for drawing cards.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from src.types.supabase_types import CardData
from src.card.config import (
    CARD_HEIGHT, HEADER_HEIGHT,
    get_category_color
)
from src.card.components.front import draw_card_front_content
from src.card.components.banner import draw_banner
from src.card.components.back.header import draw_back_header
from src.card.components.back.connections import draw_connections_table
from src.card.components.back.towns import draw_towns_grid


def draw_card_front(c: canvas.Canvas, card_data: CardData, x: float, y: float, supabase_client=None):
    """
    Draw the front of a character card.

    Args:
        c: ReportLab canvas
        card_data: Card data to render
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        supabase_client: Supabase client for downloading images (optional)
    """
    character = card_data.character
    category_color = get_category_color(character.type)

    draw_card_front_content(c, character, x, y, category_color, supabase_client)


def draw_card_back(c: canvas.Canvas, card_data: CardData, x: float, y: float, card_number: int, supabase_client=None):
    """
    Draw the back of a character card with details and connections.

    Args:
        c: ReportLab canvas
        card_data: Card data to render
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        card_number: Card number to display
        supabase_client: Supabase client (not used for back, kept for consistency)
    """
    character = card_data.character
    category_color = get_category_color(character.type)

    # Draw header section (name, dates, biography, category box)
    draw_back_header(c, character, x, y, category_color)

    # Separate category T (Territory/Towns) from other connections
    regular_connections = []
    town_connections = []

    if card_data.connections:
        for conn in card_data.connections:
            if conn.category_code == 'T':
                town_connections.append(conn)
            else:
                # Special exception for SYLVESTER II: filter out joker connections
                if character.name == "SYLVESTER II":
                    # Skip connections with the joker phrase in 'why' field
                    # Matches: "Pope Sylvester is a joker..." or "Sylvester II is joker..."
                    if conn.why and "joker" in conn.why.lower() and ("sylv" in conn.why.lower() or "pope" in conn.why.lower()):
                        continue
                regular_connections.append(conn)

    # Draw regular connections table (excluding category T)
    connections_y = y + CARD_HEIGHT - HEADER_HEIGHT - 2 * mm
    if regular_connections:
        draw_connections_table(c, regular_connections, x, connections_y)

    # Draw town connections grid above banner
    if town_connections:
        draw_towns_grid(c, town_connections, x, y)

    # Draw banner with name at bottom
    draw_banner(c, character.name, x, y, category_color)
