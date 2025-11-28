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
    depends on the image's aspect ratio (height/width):
    - Images with aspect ratio > 1.298: aligned to top of card
    - Images with aspect ratio <= 1.298: centered between card top and banner top

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
        # Effective card aspect ratio (excluding banner) = 1.298
        TARGET_ASPECT = 1.298

        # Calculate image aspect ratio (height/width)
        img_aspect = orig_height / orig_width

        # Calculate the available space above the banner
        banner_top_y = y + BANNER_HEIGHT  # Banner is at y (bottom), with BANNER_HEIGHT
        available_height = CARD_HEIGHT - BANNER_HEIGHT  # Space from banner top to card top

        if img_aspect > TARGET_ASPECT:
            # Image is too portrait (taller/narrower than target) - align to top of card
            img_y = y + CARD_HEIGHT - final_height
        else:
            # Image is landscape or matches target - center between card top and banner top
            img_y = banner_top_y + (available_height - final_height) / 2

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
                           category_color: HexColor, supabase_client=None, corner_radius: float = None, bleed: float = 0):
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
        bleed: Bleed distance to extend colors beyond card edge (default: 0)
    """
    if corner_radius is None:
        corner_radius = CORNER_RADIUS

    # Step 1: Draw background extending into bleed area FIRST (before anything else)
    c.saveState()
    c.setFillColor(HexColor('#cccccc'))
    c.setLineWidth(0)

    if bleed > 0:
        # Draw background extending into bleed on all sides
        c.rect(x - bleed, y - bleed, CARD_WIDTH + 2 * bleed, CARD_HEIGHT + 2 * bleed, fill=1, stroke=0)
    else:
        # No bleed, just draw card background
        draw_rounded_rect(c, x, y, CARD_WIDTH, CARD_HEIGHT, corner_radius, fill=1, stroke=0)
    c.restoreState()

    # Step 2: Draw banner background extending into bleed (BEFORE clipping)
    if bleed > 0:
        # Only draw the banner background before clipping, not the text
        c.setFillColor(category_color)
        c.rect(x - bleed, y - bleed, CARD_WIDTH + 2 * bleed, BANNER_HEIGHT + bleed, fill=1, stroke=0)

    # Step 3: Set up clipping for the card area (don't redraw background to avoid edge line)
    c.saveState()

    # Only draw rounded background if there's no bleed (to avoid creating edge line)
    if bleed == 0:
        c.setFillColor(HexColor('#cccccc'))
        draw_rounded_rect(c, x, y, CARD_WIDTH, CARD_HEIGHT, corner_radius, fill=1, stroke=0)

    # Set clipping path to rounded rectangle so image respects the rounded corners
    clip_to_rounded_rect(c, x, y, CARD_WIDTH, CARD_HEIGHT, corner_radius)

    # Draw portrait image
    if supabase_client:
        draw_card_front_image(c, character, x, y, supabase_client)

    # Step 4: Draw banner (background if no bleed, always text) AFTER image so it appears on top
    draw_banner(c, character.name, x, y, category_color, 0)

    # Restore state to remove clipping
    c.restoreState()
