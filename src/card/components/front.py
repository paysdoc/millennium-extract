"""
Card front rendering component.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from src.types.supabase_types import Character
from src.config import CARD_WIDTH, CARD_HEIGHT, BANNER_HEIGHT, CORNER_RADIUS, get_category_color
from src.card.image_handler import download_image_from_supabase
from src.card.components.banner import draw_banner
from src.card.utils import draw_rounded_rect, clip_to_rounded_rect


def draw_card_front_image(c: canvas.Canvas, character: Character, x: float, y: float, supabase_client):
    """
    Draw the portrait image on the card front.

    The image is scaled to fit while preserving its aspect ratio. Vertical alignment
    depends on the image's aspect ratio:
    - Images wider than 1×√2 (≈0.707): aligned to top of card
    - Square images (±10% of 1:1): centered between card top and banner top
    - Other images: centered on the card

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

        # Horizontal centering (always centered horizontally)
        img_x = x + (CARD_WIDTH - final_width) / 2

        # Vertical positioning based on aspect ratio
        # 1×√2 aspect ratio ≈ 0.707
        sqrt2_aspect = 1 / 1.414  # Approximately 0.707

        # Calculate the available space above the banner
        banner_top_y = y + 4 + BANNER_HEIGHT  # Banner is at y+4, with BANNER_HEIGHT
        available_height = CARD_HEIGHT - (4 + BANNER_HEIGHT)  # Space from banner top to card top

        if orig_aspect > sqrt2_aspect:
            # Image is wider than 1×√2 - align to top of card
            img_y = y + CARD_HEIGHT - final_height

            # But if the image height is less than the available space above the banner,
            # center it between the top of the card and the top of the banner
            if final_height < available_height:
                img_y = banner_top_y + (available_height - final_height) / 2
        elif abs(orig_aspect - 1.0) < 0.1:  # Square (within 10% of 1:1)
            # Square orientation - center between top of card and top of banner
            img_y = banner_top_y + (available_height - final_height) / 2
        else:
            # Default: center on the card
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
                           category_color: HexColor, supabase_client=None, corner_radius: float = None):
    """
    Draw the complete card front: background, image, and banner.

    Args:
        c: ReportLab canvas
        character: Character data
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
        category_color: Color for the banner
        supabase_client: Supabase client for downloading images (optional)
        corner_radius: Corner radius for rounded edges (default: CORNER_RADIUS from config)
    """
    if corner_radius is None:
        corner_radius = CORNER_RADIUS

    # Draw card background with rounded corners
    c.setFillColor(HexColor('#cccccc'))
    c.setStrokeColor(HexColor('#cccccc'))  # Match stroke to fill to hide border
    c.setLineWidth(0)  # Remove border
    draw_rounded_rect(c, x, y, CARD_WIDTH, CARD_HEIGHT, corner_radius, fill=1, stroke=0)

    # Set clipping path to rounded rectangle so image and banner respect the rounded corners
    c.saveState()
    clip_to_rounded_rect(c, x, y, CARD_WIDTH, CARD_HEIGHT, corner_radius)

    # Draw portrait image
    if supabase_client:
        draw_card_front_image(c, character, x, y, supabase_client)

    # Draw banner with name
    draw_banner(c, character.name, x, y, category_color)

    # Restore state to remove clipping
    c.restoreState()
