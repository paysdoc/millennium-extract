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
import requests
from PIL import Image
from src.types.supabase_types import CardData, DenormalizedConnection


# Card dimensions (standard poker card size)
CARD_WIDTH = 63 * mm
CARD_HEIGHT = 88 * mm

# Layout spacing
MARGIN = 3 * mm
IMAGE_HEIGHT = 65 * mm
BANNER_HEIGHT = 8 * mm
HEADER_HEIGHT = 15 * mm
TABLE_START_Y = 35 * mm

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


def download_image(url: Optional[str]) -> Optional[ImageReader]:
    """Download image from URL and return as ImageReader."""
    if not url:
        return None

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        img = Image.open(io.BytesIO(response.content))
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
        return ImageReader(img)
    except Exception as e:
        print(f"Failed to download image from {url}: {e}")
        return None


def draw_card_front(c: canvas.Canvas, card_data: CardData, x: float, y: float):
    """
    Draw the front of a character card.

    Args:
        c: ReportLab canvas
        card_data: Card data to render
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
    """
    character = card_data.character
    category_color = get_category_color(character.type)

    # Draw card border
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(x, y, CARD_WIDTH, CARD_HEIGHT)

    # Draw portrait image
    if character.image_link:
        img = download_image(character.image_link)
        if img:
            # Calculate image dimensions to fit while maintaining aspect ratio
            img_y = y + BANNER_HEIGHT
            img_width = CARD_WIDTH - (2 * MARGIN)
            img_height = IMAGE_HEIGHT

            try:
                c.drawImage(
                    img,
                    x + MARGIN,
                    img_y,
                    width=img_width,
                    height=img_height,
                    preserveAspectRatio=True,
                    mask='auto'
                )
            except Exception as e:
                print(f"Failed to draw image for {character.name}: {e}")

    # Draw colored banner at bottom with name
    c.setFillColor(category_color)
    c.rect(x, y, CARD_WIDTH, BANNER_HEIGHT, fill=1, stroke=0)

    # Draw name on banner
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 14)
    name = (character.name or "UNKNOWN").upper()
    text_width = c.stringWidth(name, "Helvetica-Bold", 14)
    c.drawString(
        x + (CARD_WIDTH - text_width) / 2,
        y + BANNER_HEIGHT / 2 - 3,
        name
    )


def draw_card_back(c: canvas.Canvas, card_data: CardData, x: float, y: float, card_number: int):
    """
    Draw the back of a character card with details and connections.

    Args:
        c: ReportLab canvas
        card_data: Card data to render
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        card_number: Card number to display
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

    # Draw character name
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 11)
    full_name = f"{character.name or ''} {character.first_names or ''}".strip().upper()
    c.drawString(x + MARGIN, y + CARD_HEIGHT - MARGIN - 8, full_name)

    # Draw dates and category
    c.setFont("Helvetica", 8)
    dates = f"{character.birth_date or ''}-{character.death_date or ''}"
    c.drawString(x + MARGIN, y + CARD_HEIGHT - MARGIN - 15, dates)
    c.drawString(x + MARGIN, y + CARD_HEIGHT - HEADER_HEIGHT + MARGIN, category_name)

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

    # Draw biography section
    bio_y = y + CARD_HEIGHT - HEADER_HEIGHT - MARGIN - 5
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 7)

    # Split biography into bullet points
    if character.biography:
        bio_lines = character.biography.split('.')
        for line in bio_lines[:4]:  # Limit to 4 lines
            if line.strip():
                c.drawString(x + MARGIN, bio_y, f"-{line.strip()}")
                bio_y -= 8

    # Draw connections table header
    connections_y = y + CARD_HEIGHT - HEADER_HEIGHT - 35 * mm
    c.setFillColor(category_color)
    c.rect(x + MARGIN, connections_y, CARD_WIDTH - 2 * MARGIN, 5 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x + MARGIN + 2, connections_y + 2, "CONNECTIONS:")

    # Draw connections table
    if card_data.connections:
        table_data = []
        for conn in card_data.connections[:10]:  # Limit to 10 connections
            table_data.append([
                str(conn.value),
                conn.category_code,
                conn.character_name,
                conn.why
            ])

        table = Table(table_data, colWidths=[8 * mm, 8 * mm, 20 * mm, 21 * mm])

        # Style the table
        table_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 6),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (1, 0), (1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
        ])

        # Add category colors to the category column
        for i, conn in enumerate(card_data.connections[:10]):
            cat_color = get_category_color(conn.category_code)
            table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
            table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

        table.setStyle(table_style)

        # Draw table
        table.wrapOn(c, CARD_WIDTH - 2 * MARGIN, CARD_HEIGHT)
        table.drawOn(c, x + MARGIN, connections_y - len(table_data) * 5 * mm)

    # Draw colored banner at bottom with name
    c.setFillColor(category_color)
    c.rect(x, y, CARD_WIDTH, BANNER_HEIGHT, fill=1, stroke=0)

    # Draw name on banner
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 14)
    name = (character.name or "UNKNOWN").upper()
    text_width = c.stringWidth(name, "Helvetica-Bold", 14)
    c.drawString(
        x + (CARD_WIDTH - text_width) / 2,
        y + BANNER_HEIGHT / 2 - 3,
        name
    )
