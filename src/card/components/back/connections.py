"""
Connections table component for card back.
"""
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from typing import List
from src.types.supabase_types import DenormalizedConnection
from src.card.config import CARD_WIDTH, get_category_color


def draw_connections_table(c: canvas.Canvas, connections: List[DenormalizedConnection],
                          x: float, table_y: float) -> float:
    """
    Draw the connections table (excluding category T towns).

    The table displays up to 25 connections with columns for:
    - Value (score)
    - Category code (colored)
    - Character name
    - Why_short description

    Args:
        c: ReportLab canvas
        connections: List of connection data (should NOT include category T)
        x: X position of card bottom-left corner
        table_y: Y position where table should start (top of table)

    Returns:
        Y position of bottom of table (for positioning other elements)
    """
    if not connections:
        return table_y

    table_data = []
    for conn in connections[:25]:  # Can fit 25 rows with minimal row height (2.5mm)
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
    row_height = 2.5 * mm
    row_heights = [row_height] * len(table_data)
    table = Table(table_data, colWidths=[4 * mm, 2.7 * mm, 17.5 * mm, 44.8 * mm], rowHeights=row_heights)

    # Style the table - horizontal lines only, no vertical lines, no outer padding
    table_style = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 5),  # Default 5pt font
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically center all text

        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 6),  # Blank space above text to correct alignment
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
    for i, conn in enumerate(connections[:25]):
        cat_color = get_category_color(conn.category_code)
        table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
        table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

    # Set font size for name column (5pt to fit 'ALBERTUS MAGNUS')
    table_style.add('FONTSIZE', (2, 0), (2, -1), 5)

    # Set font size for why_short column (4pt to fit 47 characters)
    table_style.add('FONTSIZE', (3, 0), (3, -1), 5)

    table.setStyle(table_style)

    # Draw table edge to edge (no margin)
    table.wrapOn(c, CARD_WIDTH, 1000)  # Large height for wrapping
    bottom_y = table_y - len(table_data) * row_height
    table.drawOn(c, x, bottom_y)

    return bottom_y
