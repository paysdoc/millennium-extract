"""
Text rendering utilities for card generation.
"""
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from typing import Optional


def create_rounded_rect_path(c: canvas.Canvas, x: float, y: float, width: float, height: float, radius: float):
    """
    Create a rounded rectangle path (for drawing or clipping).

    Args:
        c: ReportLab canvas
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        width: Width of rectangle
        height: Height of rectangle
        radius: Corner radius

    Returns:
        Path object for the rounded rectangle
    """
    # Ensure radius doesn't exceed half of smallest dimension
    max_radius = min(width, height) / 2
    radius = min(radius, max_radius)

    p = c.beginPath()

    # Start from bottom-left, moving clockwise
    # Bottom-left corner
    p.moveTo(x + radius, y)

    # Bottom edge to bottom-right corner
    p.lineTo(x + width - radius, y)
    p.arcTo(x + width - 2*radius, y, x + width, y + 2*radius, startAng=270, extent=90)

    # Right edge to top-right corner
    p.lineTo(x + width, y + height - radius)
    p.arcTo(x + width - 2*radius, y + height - 2*radius, x + width, y + height, startAng=0, extent=90)

    # Top edge to top-left corner
    p.lineTo(x + radius, y + height)
    p.arcTo(x, y + height - 2*radius, x + 2*radius, y + height, startAng=90, extent=90)

    # Left edge to bottom-left corner
    p.lineTo(x, y + radius)
    p.arcTo(x, y, x + 2*radius, y + 2*radius, startAng=180, extent=90)

    p.close()
    return p


def draw_rounded_rect(c: canvas.Canvas, x: float, y: float, width: float, height: float,
                     radius: float, fill: int = 1, stroke: int = 0):
    """
    Draw a rectangle with rounded corners.

    Args:
        c: ReportLab canvas
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        width: Width of rectangle
        height: Height of rectangle
        radius: Corner radius
        fill: Whether to fill (1) or not (0)
        stroke: Whether to stroke (1) or not (0)
    """
    p = create_rounded_rect_path(c, x, y, width, height, radius)
    c.drawPath(p, fill=fill, stroke=stroke)


def clip_to_rounded_rect(c: canvas.Canvas, x: float, y: float, width: float, height: float, radius: float):
    """
    Set clipping path to a rounded rectangle.
    Call this before drawing content that should be clipped to rounded corners.
    Remember to call c.restoreState() after drawing the clipped content.

    Args:
        c: ReportLab canvas
        x: X position of bottom-left corner
        y: Y position of bottom-left corner
        width: Width of rectangle
        height: Height of rectangle
        radius: Corner radius
    """
    p = create_rounded_rect_path(c, x, y, width, height, radius)
    c.clipPath(p, stroke=0, fill=0)


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


def draw_text_with_outline(c: canvas.Canvas, text: str, x: float, y: float,
                          font_name: str, font_size: int,
                          text_color=colors.white, outline_color=colors.black,
                          outline_width: float = 0.5):
    """
    Draw text with an outline for better readability on light backgrounds.

    Args:
        c: ReportLab canvas
        text: Text to draw
        x: X position
        y: Y position
        font_name: Font name
        font_size: Font size
        text_color: Color of the text (default: white)
        outline_color: Color of the outline (default: black)
        outline_width: Width of the outline offset (default: 0.5)
    """
    c.setFont(font_name, font_size)

    # Draw outline by drawing text at slight offsets
    c.setFillColor(outline_color)
    for dx, dy in [(-outline_width, -outline_width), (-outline_width, outline_width),
                   (outline_width, -outline_width), (outline_width, outline_width)]:
        c.drawString(x + dx, y + dy, text)

    # Draw main text on top
    c.setFillColor(text_color)
    c.drawString(x, y, text)
