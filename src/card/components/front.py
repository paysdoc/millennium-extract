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


def draw_card_front_image(c: canvas.Canvas, character: Character, x: float, y: float, supabase_client, bleed: float = 0):
    """
    Draw the portrait image on the card front.

    The image is scaled to fit while preserving its aspect ratio. Vertical alignment
    depends on the image's aspect ratio (height/width):
    - Images with aspect ratio > 1.298: aligned to top of card
    - Images with aspect ratio <= 1.298: centered between card top and banner top

    When bleed > 0, the image is slightly enlarged to overlap into the bleed area
    (approximately 0.3-0.5mm) to prevent white gaps at edges after trimming.

    Args:
        c: ReportLab canvas
        character: Character data (contains image_link)
        x: X position of card bottom-left corner
        y: Y position of card bottom-left corner
        supabase_client: Supabase client for downloading images
        bleed: Bleed distance (when > 0, image slightly overlaps into bleed area)
    """
    if not character.image_link or not supabase_client:
        return

    img = download_image_from_supabase(supabase_client, character.image_link)
    if not img:
        return

    try:
        from reportlab.lib.units import mm

        # Get original image dimensions
        img_obj = img._image  # Access the PIL Image object
        orig_width, orig_height = img_obj.size
        orig_aspect = orig_width / orig_height

        # Fit image within card while preserving aspect ratio
        card_aspect = CARD_WIDTH / CARD_HEIGHT

        # Small overlap into bleed area (0.4mm on each side that has bleed)
        image_overlap = 1 * mm if bleed > 0 else 0

        # Calculate dimensions to fit within card (contain, not cover)
        # Add overlap to width/height to extend slightly into bleed
        if orig_aspect > card_aspect:
            # Image is wider - constrain by width, add overlap on left and right
            final_width = CARD_WIDTH + (2 * image_overlap)
            final_height = final_width / orig_aspect
        else:
            # Image is taller - constrain by height, add overlap on top (and bottom if not banner)
            final_height = CARD_HEIGHT + image_overlap  # Only top overlap (bottom has banner)
            final_width = final_height * orig_aspect

        # Horizontal centering (shift left by overlap amount to maintain visual center)
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
            # Shift up by overlap to extend into top bleed
            img_y = y + CARD_HEIGHT - final_height + image_overlap
        else:
            # Image is landscape or matches target - center between card top and banner top
            # Center position remains the same (overlap is symmetric)
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

    # Drawing order differs based on whether we have bleed or not
    if bleed > 0:
        # WITH BLEED: Draw elements in order: grey bg → image → banner
        # No clipping needed since we want elements to extend into bleed

        # Step 1: Draw grey background extending into bleed
        c.saveState()
        c.setFillColor(HexColor('#cccccc'))
        c.rect(x - bleed, y - bleed, CARD_WIDTH + 2 * bleed, CARD_HEIGHT + 2 * bleed, fill=1, stroke=0)
        c.restoreState()

        # Step 2: Draw portrait image (with slight overlap into bleed)
        if supabase_client:
            draw_card_front_image(c, character, x, y, supabase_client, bleed)

        # Step 3: Draw banner on top of image (extends into bleed)
        draw_banner(c, character.name, x, y, category_color, bleed)
    else:
        # WITHOUT BLEED: Use clipping for rounded corners

        # Step 1: Draw grey background with rounded corners
        c.saveState()
        c.setFillColor(HexColor('#cccccc'))
        draw_rounded_rect(c, x, y, CARD_WIDTH, CARD_HEIGHT, corner_radius, fill=1, stroke=0)
        c.restoreState()

        # Step 2: Set up clipping for rounded corners
        c.saveState()
        clip_to_rounded_rect(c, x, y, CARD_WIDTH, CARD_HEIGHT, corner_radius)

        # Step 3: Draw portrait image inside clipping
        if supabase_client:
            draw_card_front_image(c, character, x, y, supabase_client, bleed)

        # Step 4: Draw banner inside clipping
        draw_banner(c, character.name, x, y, category_color, 0)

        # Restore clipping
        c.restoreState()
