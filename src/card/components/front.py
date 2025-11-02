"""
Card front rendering component.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from src.types.supabase_types import Character
from src.card.config import CARD_WIDTH, CARD_HEIGHT, get_category_color
from src.card.image_handler import download_image_from_supabase
from src.card.components.banner import draw_banner


def draw_card_front_image(c: canvas.Canvas, character: Character, x: float, y: float, supabase_client):
    """
    Draw the portrait image on the card front.

    The image is centered on the card and scaled to fit while preserving
    its aspect ratio. The image fits within the card boundaries.

    Args:
        c: ReportLab canvas
        character: Character data (contains image_link)
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
        supabase_client: Supabase client for downloading images
    """
    if not character.image_link or not supabase_client:
        return

    img = download_image_from_supabase(supabase_client, character.image_link)
    if not img:
        return

    try:
        # Get original image dimensions
        img_obj = img._image  # Access the PIL Image object
        orig_width, orig_height = img_obj.size
        orig_aspect = orig_width / orig_height

        # Fit image within card while preserving aspect ratio
        card_aspect = CARD_WIDTH / CARD_HEIGHT

        # Calculate dimensions to fit within card (contain, not cover)
        if orig_aspect > card_aspect:
            # Image is wider - constrain by width
            final_width = CARD_WIDTH
            final_height = CARD_WIDTH / orig_aspect
        else:
            # Image is taller - constrain by height
            final_height = CARD_HEIGHT
            final_width = CARD_HEIGHT * orig_aspect

        # Center the image on the card
        img_x = x + (CARD_WIDTH - final_width) / 2
        img_y = y + (CARD_HEIGHT - final_height) / 2

        c.drawImage(
            img,
            img_x,
            img_y,
            width=final_width,
            height=final_height,
            preserveAspectRatio=True,
            mask='auto'
        )
    except Exception as e:
        print(f"Failed to draw image for {character.name}: {e}")


def draw_card_front_content(c: canvas.Canvas, character: Character, x: float, y: float,
                           category_color: HexColor, supabase_client=None):
    """
    Draw the complete card front: background, image, and banner.

    Args:
        c: ReportLab canvas
        character: Character data
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
        category_color: Color for the banner
        supabase_client: Supabase client for downloading images (optional)
    """
    # Draw card background
    c.setFillColor(HexColor('#cccccc'))
    c.rect(x, y, CARD_WIDTH, CARD_HEIGHT, fill=1)

    # Draw portrait image
    if supabase_client:
        draw_card_front_image(c, character, x, y, supabase_client)

    # Draw banner with name
    draw_banner(c, character.name, x, y, category_color)
