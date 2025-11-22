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
from src.config import CARD_WIDTH, CARD_HEIGHT, HEADER_HEIGHT, BANNER_HEIGHT, get_category_color


def draw_connections_table(c: canvas.Canvas, connections: List[DenormalizedConnection],
                          x: float, table_y: float, num_towns: int = 0) -> float:
    """
    Draw the connections table (excluding category T towns).

    The layout adapts based on:
    1. Number of connections
    2. Available space (which varies based on number of town connections)

    Three possible layouts:
    - Single-column detailed: Value, Category, Name, Why_short (for few connections)
    - Two-column compact: Value, Category, Name (no why_short)
    - Three-column compact: Value, Category, Name (no why_short, maximum density)

    Args:
        c: ReportLab canvas
        connections: List of connection data (should NOT include category T)
        x: X position of card bottom-left corner
        table_y: Y position where table should start (top of table)
        num_towns: Number of town connections (affects available space)

    Returns:
        Y position of bottom of table (for positioning other elements)
    """
    if not connections:
        return table_y

    num_connections = len(connections)

    # Calculate available space for connections
    # Town grid height calculation (from towns.py)
    town_height = 0
    if num_towns > 0:
        num_town_rows = (num_towns + 2) // 3  # 3 towns per row
        town_row_height = 6  # points
        town_padding = 4  # 2pt top + 2pt bottom
        town_bg_height = num_town_rows * town_row_height + town_padding
        town_margin = 2 * mm
        town_height = (town_bg_height / 72 * 25.4) * mm  # Convert points to mm

    # Available height for connections table
    available_height = CARD_HEIGHT - HEADER_HEIGHT - BANNER_HEIGHT - (2 * mm) - town_height
    row_height = 2 * mm
    max_rows = int(available_height / row_height)

    # Choose layout based on connections count and available space
    # Calculate rows needed for each layout type
    rows_needed_single = num_connections
    rows_needed_two_col = (num_connections + 1) // 2
    rows_needed_three_col = (num_connections + 2) // 3

    # Use detailed single-column if it fits (includes why_short descriptions)
    if rows_needed_single <= max_rows:
        return _draw_detailed_table(c, connections, x, table_y)
    # Use two-column compact if it fits
    elif rows_needed_two_col <= max_rows:
        return _draw_compact_two_column_table(c, connections, x, table_y)
    # Otherwise use three-column compact (most dense)
    else:
        return _draw_compact_three_column_table(c, connections, x, table_y)


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
    Includes vertical white stripe separator between columns.
    """
    # Split connections into two columns, ordered top-to-bottom
    num_per_column = (len(connections) + 1) // 2  # Round up for left column
    left_connections = connections[:num_per_column]
    right_connections = connections[num_per_column:]

    # Build table data - each row has left and right connection with separator
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

        # Add white separator column between left and right
        table_data.append(left_row + [""] + right_row)

    # Column widths: value(3mm) + cat(2.7mm) + name(26.65mm) + separator(4mm) = 36.35mm left + 4mm sep + 28.65mm right
    # Total: 3mm + 2.7mm + 26.65mm + 4mm + 3mm + 2.7mm + 26.65mm = 69mm (full card width)
    col_widths = [3 * mm, 2.7 * mm, 26.65 * mm, 4 * mm, 3 * mm, 2.7 * mm, 26.65 * mm]

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
        ('ALIGN', (4, 0), (4, -1), 'CENTER'),  # Right value column (after separator)
        ('ALIGN', (5, 0), (5, -1), 'CENTER'),  # Right category column (after separator)
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 1),
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),
        ('TOPPADDING', (0, 0), (-1, -1), 7),  # Padding to ensure correct vertical alignment (compact view)
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Extra tight padding for category columns
        ('LEFTPADDING', (1, 0), (1, -1), 0.5),
        ('RIGHTPADDING', (1, 0), (1, -1), 0.5),
        ('LEFTPADDING', (5, 0), (5, -1), 0.5),
        ('RIGHTPADDING', (5, 0), (5, -1), 0.5),
        # White separator column (column 3) - no padding
        ('LEFTPADDING', (3, 0), (3, -1), 0),
        ('RIGHTPADDING', (3, 0), (3, -1), 0),
        ('BACKGROUND', (3, 0), (3, -1), colors.white),  # Always white
    ])

    # Add category colors for both columns
    for i in range(len(table_data)):
        # Left column
        if i < len(left_connections):
            left_conn = left_connections[i]
            cat_color = get_category_color(left_conn.category_code)
            table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
            table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

        # Right column (after separator at column 3)
        if i < len(right_connections):
            right_conn = right_connections[i]
            cat_color = get_category_color(right_conn.category_code)
            table_style.add('BACKGROUND', (5, i), (5, i), cat_color)
            table_style.add('TEXTCOLOR', (5, i), (5, i), colors.white)

    # Make score columns bold
    table_style.add('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold')  # Left score column
    table_style.add('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold')  # Right score column (after separator)

    table.setStyle(table_style)

    # Draw table
    table.wrapOn(c, CARD_WIDTH, 1000)
    bottom_y = table_y - len(table_data) * row_height
    table.drawOn(c, x, bottom_y)

    return bottom_y


def _draw_compact_three_column_table(c: canvas.Canvas, connections: List[DenormalizedConnection],
                                     x: float, table_y: float) -> float:
    """
    Draw compact 3-column table without why_short (for 73+ connections).
    Ordered top to bottom, then left to right.
    Maximum capacity: ~108 connections (36 rows × 3 columns).
    Includes vertical white stripe separators between columns.
    """
    # Split connections into three columns, ordered top-to-bottom
    num_per_column = (len(connections) + 2) // 3  # Round up for left column
    left_connections = connections[:num_per_column]
    middle_connections = connections[num_per_column:2*num_per_column]
    right_connections = connections[2*num_per_column:]

    # Build table data - each row has left, middle, and right connection with separators
    table_data = []
    for i in range(num_per_column):
        # Left column
        left_conn = left_connections[i]
        left_row = [
            str(left_conn.value),
            left_conn.category_code,
            left_conn.character_name or ""
        ]

        # Middle column (may be empty for last rows if not evenly divisible by 3)
        if i < len(middle_connections):
            middle_conn = middle_connections[i]
            middle_row = [
                str(middle_conn.value),
                middle_conn.category_code,
                middle_conn.character_name or ""
            ]
        else:
            middle_row = ["", "", ""]

        # Right column (may be empty for last rows if not evenly divisible by 3)
        if i < len(right_connections):
            right_conn = right_connections[i]
            right_row = [
                str(right_conn.value),
                right_conn.category_code,
                right_conn.character_name or ""
            ]
        else:
            right_row = ["", "", ""]

        # Add white separator columns between left/middle and middle/right
        table_data.append(left_row + [""] + middle_row + [""] + right_row)

    # Column widths: value(2.5mm) + cat(2.7mm) + name(16mm) + sep(2mm) = 21.2mm per section + 2mm separators
    # Total: (2.5 + 2.7 + 16) + 2 + (2.5 + 2.7 + 16) + 2 + (2.5 + 2.7 + 16) = 21.2 + 2 + 21.2 + 2 + 21.2 = 67.6mm
    # Adjusted: Add 1.4mm distributed to name columns (0.47mm each ~ 0.5mm each) = 69mm total
    col_widths = [2.5 * mm, 2.7 * mm, 16.3 * mm,  # Left column
                  2 * mm,                           # Separator 1
                  2.5 * mm, 2.7 * mm, 16.3 * mm,  # Middle column
                  2 * mm,                           # Separator 2
                  2.5 * mm, 2.7 * mm, 16.3 * mm]  # Right column

    # Smaller row height for compact layout
    row_height = 2 * mm
    row_heights = [row_height] * len(table_data)
    table = Table(table_data, colWidths=col_widths, rowHeights=row_heights)

    # Style the table
    table_style = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 4),  # Smaller font for compact layout
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        # Center align value and category columns
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),  # Left value column
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),  # Left category column
        ('ALIGN', (4, 0), (4, -1), 'CENTER'),  # Middle value column (after separator)
        ('ALIGN', (5, 0), (5, -1), 'CENTER'),  # Middle category column (after separator)
        ('ALIGN', (8, 0), (8, -1), 'CENTER'),  # Right value column (after separator)
        ('ALIGN', (9, 0), (9, -1), 'CENTER'),  # Right category column (after separator)
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, HexColor('#F0F0F0')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 1),
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),
        ('TOPPADDING', (0, 0), (-1, -1), 7),  # Padding to ensure correct vertical alignment (compact view)
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Extra tight padding for category columns
        ('LEFTPADDING', (1, 0), (1, -1), 0.5),
        ('RIGHTPADDING', (1, 0), (1, -1), 0.5),
        ('LEFTPADDING', (5, 0), (5, -1), 0.5),
        ('RIGHTPADDING', (5, 0), (5, -1), 0.5),
        ('LEFTPADDING', (9, 0), (9, -1), 0.5),
        ('RIGHTPADDING', (9, 0), (9, -1), 0.5),
        # White separator columns (columns 3 and 7) - no padding
        ('LEFTPADDING', (3, 0), (3, -1), 0),
        ('RIGHTPADDING', (3, 0), (3, -1), 0),
        ('BACKGROUND', (3, 0), (3, -1), colors.white),  # Separator 1 - always white
        ('LEFTPADDING', (7, 0), (7, -1), 0),
        ('RIGHTPADDING', (7, 0), (7, -1), 0),
        ('BACKGROUND', (7, 0), (7, -1), colors.white),  # Separator 2 - always white
    ])

    # Add category colors for all three columns
    for i in range(len(table_data)):
        # Left column
        if i < len(left_connections):
            left_conn = left_connections[i]
            cat_color = get_category_color(left_conn.category_code)
            table_style.add('BACKGROUND', (1, i), (1, i), cat_color)
            table_style.add('TEXTCOLOR', (1, i), (1, i), colors.white)

        # Middle column (after separator at column 3)
        if i < len(middle_connections):
            middle_conn = middle_connections[i]
            cat_color = get_category_color(middle_conn.category_code)
            table_style.add('BACKGROUND', (5, i), (5, i), cat_color)
            table_style.add('TEXTCOLOR', (5, i), (5, i), colors.white)

        # Right column (after separator at column 7)
        if i < len(right_connections):
            right_conn = right_connections[i]
            cat_color = get_category_color(right_conn.category_code)
            table_style.add('BACKGROUND', (9, i), (9, i), cat_color)
            table_style.add('TEXTCOLOR', (9, i), (9, i), colors.white)

    # Make score columns bold
    table_style.add('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold')  # Left score column
    table_style.add('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold')  # Middle score column (after separator)
    table_style.add('FONTNAME', (8, 0), (8, -1), 'Helvetica-Bold')  # Right score column (after separator)

    table.setStyle(table_style)

    # Draw table
    table.wrapOn(c, CARD_WIDTH, 1000)
    bottom_y = table_y - len(table_data) * row_height
    table.drawOn(c, x, bottom_y)

    return bottom_y
