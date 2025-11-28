"""
Main card rendering functions - public API for drawing cards.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from src.types.supabase_types import CardData
from src.config import (
    CARD_WIDTH, CARD_HEIGHT, HEADER_HEIGHT, CORNER_RADIUS,
    get_category_color
)
from src.card.components.front import draw_card_front_content
from src.card.components.banner import draw_banner
from src.card.components.back.header import draw_back_header
from src.card.components.back.connections import draw_connections_table
from src.card.components.back.towns import draw_towns_grid
from src.card.utils import draw_rounded_rect, clip_to_rounded_rect


def draw_card_front(c: canvas.Canvas, card_data: CardData, x: float, y: float, scale: float = 1.0, supabase_client=None, corner_radius: float = None, bleed: float = 0):
    """
    Draw the front of a character card.

    Args:
        c: ReportLab canvas
        card_data: Card data to render
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        scale: Scale factor for the card (default: 1.0 = original size 69mm)
        supabase_client: Supabase client for downloading images (optional)
        corner_radius: Corner radius for rounded edges (default: CORNER_RADIUS from config)
        bleed: Bleed distance to extend colors beyond card edge (default: 0)
    """
    if corner_radius is None:
        corner_radius = CORNER_RADIUS

    character = card_data.character
    category_color = get_category_color(character.type)

    # Save canvas state and apply scaling transformation
    c.saveState()
    c.translate(x, y)  # Move origin to card position
    c.scale(scale, scale)  # Apply uniform scaling

    # Draw at origin (0, 0) since we've translated
    draw_card_front_content(c, character, 0, 0, category_color, supabase_client, corner_radius, bleed)

    # Restore canvas state
    c.restoreState()


def draw_card_back(c: canvas.Canvas, card_data: CardData, x: float, y: float, card_number: int, scale: float = 1.0, supabase_client=None, corner_radius: float = None, bleed: float = 0):
    """
    Draw the back of a character card with details and connections.

    Args:
        c: ReportLab canvas
        card_data: Card data to render
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        card_number: Card number to display
        scale: Scale factor for the card (default: 1.0 = original size 69mm)
        supabase_client: Supabase client (not used for back, kept for consistency)
        corner_radius: Corner radius for rounded edges (default: CORNER_RADIUS from config)
        bleed: Bleed distance to extend colors beyond card edge (default: 0)
    """
    if corner_radius is None:
        corner_radius = CORNER_RADIUS

    character = card_data.character
    category_color = get_category_color(character.type)

    # Save canvas state and apply scaling transformation
    c.saveState()
    c.translate(x, y)  # Move origin to card position
    c.scale(scale, scale)  # Apply uniform scaling

    # Step 1: Draw white background extending into bleed (if bleed > 0)
    c.saveState()
    c.setFillColor(colors.white)
    if bleed > 0:
        # Extend white background into bleed on all sides
        c.rect(-bleed, -bleed, CARD_WIDTH + 2 * bleed, CARD_HEIGHT + 2 * bleed, fill=1, stroke=0)
    c.restoreState()

    # Step 2: Draw header and banner extending into bleed (BEFORE clipping)
    if bleed > 0:
        draw_back_header(c, character, 0, 0, category_color, bleed)
        draw_banner(c, character.name, 0, 0, category_color, bleed)

    # Step 3: Set up clipping for the card area
    c.saveState()

    # Only draw rounded background and header/banner if there's no bleed
    if bleed == 0:
        c.setFillColor(colors.white)
        c.setStrokeColor(colors.white)
        draw_rounded_rect(c, 0, 0, CARD_WIDTH, CARD_HEIGHT, corner_radius, fill=1, stroke=0)

    # Set clipping path to rounded rectangle so content respects the rounded corners
    clip_to_rounded_rect(c, 0, 0, CARD_WIDTH, CARD_HEIGHT, corner_radius)

    # Draw header section only if there's no bleed (to avoid double-drawing with transparency)
    if bleed == 0:
        draw_back_header(c, character, 0, 0, category_color, 0)

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
    connections_y = CARD_HEIGHT - HEADER_HEIGHT - 2 * mm
    if regular_connections:
        draw_connections_table(c, regular_connections, 0, connections_y, num_towns=len(town_connections))

    # Draw town connections grid above banner
    if town_connections:
        draw_towns_grid(c, town_connections, 0, 0)

    # Draw banner only if there's no bleed (to avoid double-drawing)
    if bleed == 0:
        draw_banner(c, character.name, 0, 0, category_color, 0)

    # Restore state to remove clipping
    c.restoreState()

    # Restore canvas state (from scale/translate)
    c.restoreState()
