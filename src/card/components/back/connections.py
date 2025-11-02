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

    For <=26 connections:
    - 4 columns: Value, Category, Name, Why_short
    - Single column layout with detailed descriptions

    For >26 connections:
    - 3 columns: Value, Category, Name (no why_short)
    - 2-column layout ordered top to bottom
    - More compact to fit more connections

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

    num_connections = len(connections)

    # Choose layout based on number of connections
    if num_connections <= 26:
        return _draw_detailed_table(c, connections, x, table_y)
    else:
        return _draw_compact_two_column_table(c, connections, x, table_y)


def _draw_detailed_table(c: canvas.Canvas, connections: List[DenormalizedConnection],
                        x: float, table_y: float) -> float:
    """
    Draw detailed single-column table with why_short (for <=26 connections).
    """
    table_data = []
    for conn in connections[:26]:
        why_text = conn.why_short or ""
        table_data.append([
            str(conn.value),
            conn.category_code,
            conn.character_name or "",
            why_text
        ])

    # Full card width - edge to edge (total: 69mm)
    # Optimized: 4mm + 2.7mm + 17.5mm + 44.8mm = 69mm
    row_height = 2.5 * mm
    row_heights = [row_height] * len(table_data)
    table = Table(table_data, colWidths=[4 * mm, 2.7 * mm, 17.5 * mm, 44.8 * mm], rowHeights=row_heights)

    # Style the table
    table_style = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 5),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 6),  # Padding to ensure correct vertical alignment
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Reduce category column padding to 1pt
        ('LEFTPADDING', (1, 0), (1, -1), 1),
        ('RIGHTPADDING', (1, 0), (1, -1), 1),
        # Add padding between name and why_short columns
        ('RIGHTPADDING', (2, 0), (2, -1), 4),
        ('LEFTPADDING', (3, 0), (3, -1), 4),
        ('WORDWRAP', (0, 0), (-1, -1), True),
    ])

    # Add category colors
    for i, conn in enumerate(connections[:26]):
        cat_color = get_category_color(conn.category_code)
        table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
        table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

    # Set font sizes and styles
    table_style.add('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold')  # Score column - bold
    table_style.add('FONTSIZE', (2, 0), (2, -1), 5)  # Name column
    table_style.add('FONTSIZE', (3, 0), (3, -1), 4)  # Why_short column

    table.setStyle(table_style)

    # Draw table
    table.wrapOn(c, CARD_WIDTH, 1000)
    bottom_y = table_y - len(table_data) * row_height
    table.drawOn(c, x, bottom_y)

    return bottom_y


def _draw_compact_two_column_table(c: canvas.Canvas, connections: List[DenormalizedConnection],
                                   x: float, table_y: float) -> float:
    """
    Draw compact 2-column table without why_short (for >26 connections).
    Ordered top to bottom, then left to right.
    """
    # Split connections into two columns, ordered top-to-bottom
    num_per_column = (len(connections) + 1) // 2  # Round up for left column
    left_connections = connections[:num_per_column]
    right_connections = connections[num_per_column:]

    # Build table data - each row has left and right connection
    table_data = []
    for i in range(num_per_column):
        left_conn = left_connections[i]
        left_row = [
            str(left_conn.value),
            left_conn.category_code,
            left_conn.character_name or ""
        ]

        # Right side (may be empty for last row if odd number of connections)
        if i < len(right_connections):
            right_conn = right_connections[i]
            right_row = [
                str(right_conn.value),
                right_conn.category_code,
                right_conn.character_name or ""
            ]
        else:
            right_row = ["", "", ""]

        table_data.append(left_row + right_row)

    # Column widths: value(3mm) + cat(2.7mm) + name(27.8mm) = 33.5mm per column
    # Total: 33.5mm * 2 = 67mm, leaving 2mm margin
    col_widths = [3 * mm, 2.7 * mm, 27.8 * mm, 3 * mm, 2.7 * mm, 27.8 * mm]

    # Smaller row height for compact layout
    row_height = 2 * mm
    row_heights = [row_height] * len(table_data)
    table = Table(table_data, colWidths=col_widths, rowHeights=row_heights)

    # Style the table
    table_style = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 4),  # Smaller font for compact layout
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),  # Left value column
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),  # Left category column
        ('ALIGN', (3, 0), (3, -1), 'CENTER'),  # Right value column
        ('ALIGN', (4, 0), (4, -1), 'CENTER'),  # Right category column
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 1),
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),
        ('TOPPADDING', (0, 0), (-1, -1), 7),  # Padding to ensure correct vertical alignment (compact view)
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Extra tight padding for category columns
        ('LEFTPADDING', (1, 0), (1, -1), 0.5),
        ('RIGHTPADDING', (1, 0), (1, -1), 0.5),
        ('LEFTPADDING', (4, 0), (4, -1), 0.5),
        ('RIGHTPADDING', (4, 0), (4, -1), 0.5),
    ])

    # Add category colors for both columns
    for i in range(len(table_data)):
        # Left column
        if i < len(left_connections):
            left_conn = left_connections[i]
            cat_color = get_category_color(left_conn.category_code)
            table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
            table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

        # Right column
        if i < len(right_connections):
            right_conn = right_connections[i]
            cat_color = get_category_color(right_conn.category_code)
            table_style.add('BACKGROUND', (4, i), (4, i), cat_color)
            table_style.add('TEXTCOLOR', (4, i), (4, i), colors.white)

    # Make score columns bold
    table_style.add('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold')  # Left score column
    table_style.add('FONTNAME', (3, 0), (3, -1), 'Helvetica-Bold')  # Right score column

    table.setStyle(table_style)

    # Draw table
    table.wrapOn(c, CARD_WIDTH, 1000)
    bottom_y = table_y - len(table_data) * row_height
    table.drawOn(c, x, bottom_y)

    return bottom_y
