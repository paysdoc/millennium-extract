"""
Card layout definitions for Millennium card game.
Based on Sample_layout.jpeg specifications.
"""
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from typing import Optional
import io
import os
from PIL import Image
from src.types.supabase_types import CardData, DenormalizedConnection


# Card dimensions (1:√2 aspect ratio, like A4 paper)
# Width : Height = 1 : √2 ≈ 1 : 1.414
CARD_WIDTH = 69 * mm
CARD_HEIGHT = 97.58 * mm  # 69 * √2 ≈ 97.58mm

# Layout spacing
MARGIN = 3 * mm
IMAGE_HEIGHT = 71 * mm  # Portrait image height (adjusted for taller card)
BANNER_HEIGHT = 8 * mm
HEADER_HEIGHT = 14 * mm  # Header section on back
BIO_HEIGHT = 18 * mm  # Biography section height
TABLE_START_Y = 40 * mm  # Where connections table starts

# Category color mapping
CATEGORY_COLORS = {
    'R': HexColor('#DC143C'),  # Royalty - red
    'S': HexColor('#FF8C00'),  # Statesman - orange
    'P': HexColor('#FFD700'),  # Philosopher - yellow
    'M': HexColor('#228B22'),  # Mathematical Scientist - green
    'N': HexColor('#40E0D0'),  # Natural Scientist - turquoise
    'A': HexColor('#4169E1'),  # Artist - blue
    'B': HexColor('#4B0082'),  # Builders and Engineers - indigo
    'C': HexColor('#8B00FF'),  # Composer - violet
    'D': HexColor('#FF69B4'),  # Dramatist - pink
    'T': HexColor('#8B4513'),  # Towns and cities - brown
}

# Category full names
CATEGORY_NAMES = {
    'R': 'ROYALTY',
    'S': 'STATESMAN',
    'P': 'PHILOSOPHER',
    'M': 'MATHEMATICAL SCIENTIST',
    'N': 'NATURAL SCIENTIST',
    'A': 'ARTIST',
    'B': 'BUILDERS AND ENGINEERS',
    'C': 'COMPOSER',
    'D': 'DRAMATIST',
    'T': 'TOWNS AND CITIES',
}


def get_category_color(category_code: Optional[str]) -> HexColor:
    """Get color for a category code, default to gray if unknown."""
    if not category_code:
        return colors.grey
    return CATEGORY_COLORS.get(category_code, colors.grey)


def get_category_name(category_code: Optional[str]) -> str:
    """Get full name for a category code."""
    if not category_code:
        return "UNKNOWN"
    return CATEGORY_NAMES.get(category_code, "UNKNOWN")


def wrap_text(c: canvas.Canvas, text: str, max_width: float, font_name: str, font_size: int) -> list:
    """
    Wrap text to fit within a maximum width.

    Args:
        c: ReportLab canvas
        text: Text to wrap
        max_width: Maximum width in points
        font_name: Font name
        font_size: Font size

    Returns:
        List of text lines that fit within max_width
    """
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        width = c.stringWidth(test_line, font_name, font_size)

        if width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                # Single word is too long, add it anyway
                lines.append(word)

    if current_line:
        lines.append(' '.join(current_line))

    return lines


def draw_wrapped_text(c: canvas.Canvas, text: str, x: float, y: float, max_width: float,
                     font_name: str, font_size: int, line_height: float, max_lines: Optional[int] = None):
    """
    Draw text with word wrapping.

    Args:
        c: ReportLab canvas
        text: Text to draw
        x: X position
        y: Y position (top of text block)
        max_width: Maximum width for text
        font_name: Font name
        font_size: Font size
        line_height: Space between lines
        max_lines: Maximum number of lines to draw (optional)

    Returns:
        Final y position after drawing text
    """
    c.setFont(font_name, font_size)
    lines = wrap_text(c, text, max_width, font_name, font_size)

    if max_lines:
        lines = lines[:max_lines]

    current_y = y
    for line in lines:
        c.drawString(x, current_y, line)
        current_y -= line_height

    return current_y


def download_image_from_supabase(supabase_client, image_path: Optional[str]) -> Optional[ImageReader]:
    """
    Download image from Supabase storage bucket with local caching.

    Args:
        supabase_client: Supabase client instance
        image_path: Path from image_link column (e.g., 'data/images/washington.jpg' or 'Newton.jpg')

    Returns:
        ImageReader object or None if download fails

    Note:
        - The function extracts the filename from the path, ignoring any directory structure
        - Images are cached in 'image_cache/' directory at project root
        - Cached images are used on subsequent calls to avoid re-downloading
    """
    if not image_path:
        return None

    try:
        # Extract just the filename, ignoring any directory path
        # Examples: 'data/images/washington.jpg' -> 'washington.jpg'
        #           'Newton.jpg' -> 'Newton.jpg'
        filename = os.path.basename(image_path.strip())

        if not filename:
            return None

        # Setup cache directory at project root
        cache_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'image_cache')
        os.makedirs(cache_dir, exist_ok=True)

        cache_path = os.path.join(cache_dir, filename)

        # Check if image exists in cache
        if os.path.exists(cache_path):
            # Load from cache
            img = Image.open(cache_path)

            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')

            return ImageReader(img)

        # Image not in cache - download from Supabase
        bucket = supabase_client.storage.from_('images')
        image_data = bucket.download(filename)

        # Convert bytes to PIL Image
        img = Image.open(io.BytesIO(image_data))

        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save to cache for future use
        img.save(cache_path)
        print(f"Cached image: {filename}")

        return ImageReader(img)

    except Exception as e:
        print(f"Failed to download image '{image_path}' (filename: '{filename}'): {e}")
        return None


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

    # Draw card border
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(x, y, CARD_WIDTH, CARD_HEIGHT)

    # Draw portrait image - centered and maximized while preserving aspect ratio
    if character.image_link and supabase_client:
        img = download_image_from_supabase(supabase_client, character.image_link)
        if img:
            try:
                # Get original image dimensions
                img_obj = img._image  # Access the PIL Image object
                orig_width, orig_height = img_obj.size
                orig_aspect = orig_width / orig_height

                # Available space on card (above banner, below top)
                available_width = CARD_WIDTH
                available_height = CARD_HEIGHT - BANNER_HEIGHT
                available_aspect = available_width / available_height

                # Calculate dimensions that fit within available space while preserving aspect ratio
                if orig_aspect > available_aspect:
                    # Image is wider - constrain by width
                    final_width = available_width
                    final_height = available_width / orig_aspect
                else:
                    # Image is taller - constrain by height
                    final_height = available_height
                    final_width = available_height * orig_aspect

                # Center the image in available space
                img_x = x + (available_width - final_width) / 2
                img_y = y + BANNER_HEIGHT + (available_height - final_height) / 2

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

    # Draw colored banner at bottom with name
    c.setFillColor(category_color)
    c.rect(x, y, CARD_WIDTH, BANNER_HEIGHT, fill=1, stroke=0)

    # Draw name on banner (with wrapping if needed)
    c.setFillColor(colors.white)
    name = (character.name or "UNKNOWN").upper()
    max_name_width = CARD_WIDTH - (2 * MARGIN)

    # Try to fit name in one line
    font_size = 12
    name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # If name wraps to multiple lines, reduce font size
    if len(name_lines) > 1:
        font_size = 10
        name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # Draw name (centered)
    c.setFont("Helvetica-Bold", font_size)
    y_offset = y + BANNER_HEIGHT / 2 - (len(name_lines) * font_size) / 2 + 2
    for line in name_lines[:2]:  # Max 2 lines
        text_width = c.stringWidth(line, "Helvetica-Bold", font_size)
        c.drawString(
            x + (CARD_WIDTH - text_width) / 2,
            y_offset,
            line
        )
        y_offset -= font_size + 1


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
    category_name = get_category_name(character.type)

    # Draw card border
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(x, y, CARD_WIDTH, CARD_HEIGHT)

    # Draw header section with beige background
    header_color = HexColor('#F5DEB3')
    c.setFillColor(header_color)
    c.rect(x, y + CARD_HEIGHT - HEADER_HEIGHT, CARD_WIDTH, HEADER_HEIGHT, fill=1, stroke=0)

    # Draw character name (wrapped if necessary)
    c.setFillColor(colors.black)
    full_name = f"{character.name or ''} {character.first_names or ''}".strip().upper()
    max_header_width = CARD_WIDTH - (2 * MARGIN) - 16 * mm  # Account for card number box
    draw_wrapped_text(
        c, full_name,
        x + MARGIN,
        y + CARD_HEIGHT - MARGIN - 4,
        max_header_width,
        "Helvetica-Bold", 9,
        line_height=10,
        max_lines=1
    )

    # Draw dates and category
    c.setFont("Helvetica", 7)
    dates = f"{character.birth_date or ''}-{character.death_date or ''}"
    c.drawString(x + MARGIN, y + CARD_HEIGHT - HEADER_HEIGHT + MARGIN + 2, dates)

    # Category name (smaller font to fit)
    category_display = category_name[:20]  # Truncate if too long
    c.setFont("Helvetica", 6)
    c.drawString(x + MARGIN, y + CARD_HEIGHT - HEADER_HEIGHT + MARGIN - 4, category_display)

    # Draw card number in colored box (top right)
    card_num_box_width = 15 * mm
    card_num_box_height = 10 * mm
    c.setFillColor(category_color)
    c.rect(
        x + CARD_WIDTH - card_num_box_width,
        y + CARD_HEIGHT - card_num_box_height,
        card_num_box_width,
        card_num_box_height,
        fill=1,
        stroke=0
    )
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 14)
    card_id = f"{character.type or 'X'}{card_number}"
    c.drawString(
        x + CARD_WIDTH - card_num_box_width + 3,
        y + CARD_HEIGHT - card_num_box_height + 2,
        card_id
    )

    # Draw biography section with text wrapping
    bio_y = y + CARD_HEIGHT - HEADER_HEIGHT - MARGIN - 5
    c.setFillColor(colors.black)

    if character.biography:
        bio_text = character.biography.replace('\n', ' ').strip()
        # Wrap biography text to fit within card width
        max_bio_width = CARD_WIDTH - (2 * MARGIN)
        draw_wrapped_text(
            c, bio_text,
            x + MARGIN,
            bio_y,
            max_bio_width,
            "Helvetica", 6,
            line_height=7,
            max_lines=3  # Limit to 3 lines to leave space for connections
        )

    # Draw connections table header (edge to edge)
    connections_y = y + CARD_HEIGHT - HEADER_HEIGHT - 26 * mm
    c.setFillColor(category_color)
    c.rect(x, connections_y, CARD_WIDTH, 5 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(x + 2, connections_y + 2, "CONNECTIONS:")

    # Draw connections table
    if card_data.connections:
        table_data = []
        for conn in card_data.connections[:8]:  # Limit to 8 connections to fit smaller card
            # Use why_short without truncation, allow text wrapping in table
            why_text = conn.why_short or ""

            table_data.append([
                str(conn.value),
                conn.category_code,
                conn.character_name or "",
                why_text
            ])

        # Full card width - edge to edge (total: 69mm)
        table = Table(table_data, colWidths=[6 * mm, 6 * mm, 20 * mm, 37 * mm])

        # Style the table - horizontal lines only, no vertical lines, no outer padding
        table_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 6),  # 6pt font size
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (1, 0), (1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Top align for wrapped text
            # Horizontal lines only (between rows)
            ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable word wrapping
        ])

        # Add category colors to the category column
        for i, conn in enumerate(card_data.connections[:8]):
            cat_color = get_category_color(conn.category_code)
            table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
            table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

        table.setStyle(table_style)

        # Draw table edge to edge (no margin)
        table.wrapOn(c, CARD_WIDTH, CARD_HEIGHT)
        table.drawOn(c, x, connections_y - len(table_data) * 5 * mm)

    # Draw colored banner at bottom with name
    c.setFillColor(category_color)
    c.rect(x, y, CARD_WIDTH, BANNER_HEIGHT, fill=1, stroke=0)

    # Draw name on banner (with wrapping if needed)
    c.setFillColor(colors.white)
    name = (character.name or "UNKNOWN").upper()
    max_name_width = CARD_WIDTH - (2 * MARGIN)

    # Try to fit name in one line
    font_size = 12
    name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # If name wraps to multiple lines, reduce font size
    if len(name_lines) > 1:
        font_size = 10
        name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # Draw name (centered)
    c.setFont("Helvetica-Bold", font_size)
    y_offset = y + BANNER_HEIGHT / 2 - (len(name_lines) * font_size) / 2 + 2
    for line in name_lines[:2]:  # Max 2 lines
        text_width = c.stringWidth(line, "Helvetica-Bold", font_size)
        c.drawString(
            x + (CARD_WIDTH - text_width) / 2,
            y_offset,
            line
        )
        y_offset -= font_size + 1
