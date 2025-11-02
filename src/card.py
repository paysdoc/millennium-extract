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
HEADER_HEIGHT = 14 * mm  # Header section on back (includes biography, dates, category)
BIO_HEIGHT = 18 * mm  # Biography section height
TABLE_START_Y = 40 * mm  # Where connections table starts

# Category color mapping
CATEGORY_COLORS = {
    'R': HexColor('#DC143C'),  # Royalty - red
    'S': HexColor('#FF8C00'),  # Statesman - orange
    'P': HexColor('#FFD700'),  # Philosopher - yellow
    'I': HexColor("#88FF00"),  # Innovator - lime green
    'M': HexColor('#228B22'),  # Mathematical Scientist - green
    'N': HexColor("#40E0B5"),  # Natural Scientist - turquoise
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
                     font_name: str, font_size: int, line_height: float, max_lines: Optional[int] = None,
                     truncate_with_ellipsis: bool = False):
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
        truncate_with_ellipsis: If True, add '...' to last line if text is truncated

    Returns:
        Final y position after drawing text
    """
    c.setFont(font_name, font_size)
    lines = wrap_text(c, text, max_width, font_name, font_size)

    was_truncated = False
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        was_truncated = True

    current_y = y
    for i, line in enumerate(lines):
        # Add ellipsis to last line if truncated
        if truncate_with_ellipsis and was_truncated and i == len(lines) - 1:
            # Try to fit ellipsis, remove words if needed
            ellipsis = "..."
            test_line = line + ellipsis
            while c.stringWidth(test_line, font_name, font_size) > max_width and line:
                # Remove last word
                words = line.split()
                if len(words) > 1:
                    words = words[:-1]
                    line = ' '.join(words)
                else:
                    line = line[:-1]  # Remove last character
                test_line = line + ellipsis
            line = test_line

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

    # Draw card background
    c.setFillColor(HexColor('#cccccc'))
    c.rect(x, y, CARD_WIDTH, CARD_HEIGHT, fill=1)

    # Draw portrait image - fits within card boundaries, centered and preserving aspect ratio
    if character.image_link and supabase_client:
        img = download_image_from_supabase(supabase_client, character.image_link)
        if img:
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

    # Draw colored banner floating over image, 4pt above bottom
    banner_y = y + 4  # 4pt above card bottom
    c.setFillColor(category_color)
    c.rect(x, banner_y, CARD_WIDTH, BANNER_HEIGHT, fill=1, stroke=0)

    # Draw name on floating banner (with wrapping if needed)
    name = (character.name or "UNKNOWN").upper()
    max_name_width = CARD_WIDTH - (2 * MARGIN)

    # Try to fit name in one line
    font_size = 12
    name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # If name wraps to multiple lines, reduce font size
    if len(name_lines) > 1:
        font_size = 10
        name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # Draw name with black outline for better readability on light backgrounds
    c.setFont("Helvetica-Bold", font_size)
    text_y_offset = banner_y + BANNER_HEIGHT / 2 - (len(name_lines) * font_size) / 2 + 2
    for line in name_lines[:2]:  # Max 2 lines
        text_width = c.stringWidth(line, "Helvetica-Bold", font_size)
        text_x = x + (CARD_WIDTH - text_width) / 2
        # Draw black outline first (slightly thicker)
        c.setStrokeColor(colors.black)
        c.setLineWidth(1.5)
        c.setFillColor(colors.black)
        for dx, dy in [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]:
            c.drawString(text_x + dx, text_y_offset + dy, line)
        # Draw white text on top
        c.setFillColor(colors.white)
        c.drawString(text_x, text_y_offset, line)
        text_y_offset -= font_size + 1


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

    # Draw header section with category color at 75% opacity
    c.setFillColorRGB(
        category_color.red,
        category_color.green,
        category_color.blue,
        alpha=0.5
    )
    c.rect(x, y + CARD_HEIGHT - HEADER_HEIGHT, CARD_WIDTH, HEADER_HEIGHT, fill=1, stroke=0)

    # Draw card type in colored box (top right) - same height as header
    category_box_width = 14 * mm
    card_num_box_height = HEADER_HEIGHT  # Match header height

    # Calculate max text width excluding category box
    max_header_text_width = CARD_WIDTH - (2 * MARGIN) - category_box_width

    # Draw character name at top of header
    c.setFillColor(colors.black)
    full_name = f"{character.name or ''} {character.first_names or ''}".strip().upper()
    name_y = y + CARD_HEIGHT - MARGIN - 3
    draw_wrapped_text(
        c, full_name,
        x + MARGIN,
        name_y,
        max_header_text_width,
        "Helvetica-Bold", 9,
        line_height=10,
        max_lines=1
    )

    # Draw dates | category directly under name (constrained width)
    c.setFont("Helvetica", 6)
    category_display = category_name[:20]  # Truncate if too long
    dates = f"{character.birth_date or ''}-{character.death_date or ''}"
    dates_category_text = f"{dates} | {category_display}"
    dates_category_y = name_y - 10  # Directly under name

    # Truncate dates/category if too long
    while c.stringWidth(dates_category_text, "Helvetica", 6) > max_header_text_width and len(category_display) > 5:
        category_display = category_display[:-1]
        dates_category_text = f"{dates} | {category_display}"

    c.drawString(x + MARGIN, dates_category_y, dates_category_text)

    # Draw biography under dates with small margin (constrained width)
    if character.biography:
        bio_text = character.biography.replace('\n', ' ').strip()
        bio_y = dates_category_y - 8  # Small margin below dates
        draw_wrapped_text(
            c, bio_text,
            x + MARGIN,
            bio_y,
            max_header_text_width,  # Same width constraint as name
            "Helvetica", 6,
            line_height=6.5,
            max_lines=2,
            truncate_with_ellipsis=True
        )
    c.setFillColor(category_color)
    c.rect(
        x + CARD_WIDTH - category_box_width,
        y + CARD_HEIGHT - card_num_box_height,
        category_box_width,
        card_num_box_height,
        fill=1,
        stroke=0
    )
    # Draw category code centered in box
    c.setFont("Helvetica-Bold", 14)
    card_id = f"{character.type or 'X'}"
    card_id_width = c.stringWidth(card_id, "Helvetica-Bold", 14)
    # Center horizontally and vertically in box
    card_id_x = x + CARD_WIDTH - category_box_width + (category_box_width - card_id_width) / 2
    card_id_y = y + CARD_HEIGHT - card_num_box_height / 2 - 5  # Center vertically
    # Draw black outline
    c.setFillColor(colors.black)
    for dx, dy in [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]:
        c.drawString(card_id_x + dx, card_id_y + dy, card_id)
    # Draw white text on top
    c.setFillColor(colors.white)
    c.drawString(card_id_x, card_id_y, card_id)

    # Draw connections table header (edge to edge) - directly under header
    connections_y = y + CARD_HEIGHT - HEADER_HEIGHT - 2 * mm

    # Draw connections table
    if card_data.connections:
        table_data = []
        for conn in card_data.connections[:25]:  # Can fit 25 rows with minimal row height (2.5mm)
            # Use why_short without truncation, allow text wrapping in table
            why_text = conn.why_short or ""

            table_data.append([
                str(conn.value),
                conn.category_code,
                conn.character_name or "",
                why_text
            ])

        # Full card width - edge to edge (total: 69mm)
        # Optimized: 4mm + 2.7mm + 17.5mm + 44.8mm = 69mm
        # Fits 'ALBERTUS MAGNUS' at 5pt and 47 chars at 4pt on single line
        # Set explicit row heights: 5pt font + 2pt padding = 7pt ≈ 3mm per row
        row_height = 2.5 * mm
        row_heights = [row_height] * len(table_data)
        table = Table(table_data, colWidths=[4 * mm, 2.7 * mm, 17.5 * mm, 44.8 * mm], rowHeights=row_heights)

        # Style the table - horizontal lines only, no vertical lines, no outer padding
        table_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 5),  # Default 6pt font
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (1, 0), (1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically center all text

            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 6),  # No blank space above text
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),  # No blank space below text
            # Reduce category column padding to 1pt
            ('LEFTPADDING', (1, 0), (1, -1), 1),
            ('RIGHTPADDING', (1, 0), (1, -1), 1),
            # Add more padding between name and why_short columns
            ('RIGHTPADDING', (2, 0), (2, -1), 4),  # Name column right padding
            ('LEFTPADDING', (3, 0), (3, -1), 4),   # Why_short column left padding
            ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable word wrapping
        ])

        # Add category colors to the category column
        for i, conn in enumerate(card_data.connections[:25]):
            cat_color = get_category_color(conn.category_code)
            table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
            table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

        # Set font size for name column (5pt to fit 'ALBERTUS MAGNUS')
        table_style.add('FONTSIZE', (2, 0), (2, -1), 5)

        # Set font size for why_short column (4pt to fit 47 characters)
        table_style.add('FONTSIZE', (3, 0), (3, -1), 4)

        table.setStyle(table_style)

        # Draw table edge to edge (no margin) - 2.5mm row height (no blank space)
        table.wrapOn(c, CARD_WIDTH, CARD_HEIGHT)
        table.drawOn(c, x, connections_y - len(table_data) * row_height)

    # Draw colored banner floating over image, 4pt above bottom
    banner_y = y + 4  # 4pt above card bottom
    c.setFillColor(category_color)
    c.rect(x, banner_y, CARD_WIDTH, BANNER_HEIGHT, fill=1, stroke=0)

    # Draw name on banner (with wrapping if needed)
    name = (character.name or "UNKNOWN").upper()
    max_name_width = CARD_WIDTH - (2 * MARGIN)

    # Try to fit name in one line
    font_size = 12
    name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # If name wraps to multiple lines, reduce font size
    if len(name_lines) > 1:
        font_size = 10
        name_lines = wrap_text(c, name, max_name_width, "Helvetica-Bold", font_size)

    # Draw name with black outline for better readability on light backgrounds
    c.setFont("Helvetica-Bold", font_size)
    y_offset = banner_y + BANNER_HEIGHT / 2 - (len(name_lines) * font_size) / 2 + 2
    for line in name_lines[:2]:  # Max 2 lines
        text_width = c.stringWidth(line, "Helvetica-Bold", font_size)
        text_x = x + (CARD_WIDTH - text_width) / 2
        # Draw black outline first
        c.setFillColor(colors.black)
        for dx, dy in [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]:
            c.drawString(text_x + dx, y_offset + dy, line)
        # Draw white text on top
        c.setFillColor(colors.white)
        c.drawString(text_x, y_offset, line)
        y_offset -= font_size + 1
