#!/usr/bin/env python3
"""
Test script to verify card aspect ratio matches A4 (1:√2).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import math
from src.card import CARD_WIDTH, CARD_HEIGHT
from reportlab.lib.units import mm


def main():
    print("=" * 70)
    print("Card Aspect Ratio Verification (A4 Standard)")
    print("=" * 70)
    print()

    # Calculate dimensions in mm
    width_mm = CARD_WIDTH / mm
    height_mm = CARD_HEIGHT / mm

    print(f"Card Dimensions:")
    print(f"  Width:  {width_mm:.2f}mm")
    print(f"  Height: {height_mm:.2f}mm")
    print()

    # Calculate aspect ratios
    aspect_ratio = width_mm / height_mm
    sqrt_2 = math.sqrt(2)
    expected_ratio = 1 / sqrt_2

    print(f"Aspect Ratio Analysis:")
    print(f"  Width/Height:     {aspect_ratio:.8f}")
    print(f"  Expected (1/√2):  {expected_ratio:.8f}")
    print(f"  Difference:       {abs(aspect_ratio - expected_ratio):.8f}")
    print()

    # Show the inverse (height/width)
    height_width_ratio = height_mm / width_mm
    print(f"Height/Width Ratio:")
    print(f"  Actual:           {height_width_ratio:.8f}")
    print(f"  Expected (√2):    {sqrt_2:.8f}")
    print(f"  Difference:       {abs(height_width_ratio - sqrt_2):.8f}")
    print()

    # Verification
    tolerance = 0.001
    matches = abs(aspect_ratio - expected_ratio) < tolerance

    print("=" * 70)
    if matches:
        print("✓ PASSED: Card aspect ratio matches A4 standard (1:√2)")
    else:
        print("✗ FAILED: Card aspect ratio does not match A4 standard")
    print("=" * 70)
    print()

    # Additional context
    print("Reference Information:")
    print(f"  √2 ≈ {sqrt_2:.6f}")
    print(f"  A4 paper: 210mm × 297mm (ratio = {210/297:.6f})")
    print(f"  A5 paper: 148mm × 210mm (ratio = {148/210:.6f})")
    print(f"  A6 paper: 105mm × 148mm (ratio = {105/148:.6f})")
    print()
    print("All A-series paper sizes share the 1:√2 aspect ratio,")
    print("which allows them to scale proportionally when folded or cut.")
    print()

    # Show card proportions
    print(f"Card proportions relative to A-series:")
    a7_width = 74  # mm
    a7_height = 105  # mm
    print(f"  A7 paper: {a7_width}mm × {a7_height}mm")
    print(f"  This card: {width_mm:.1f}mm × {height_mm:.1f}mm")
    print(f"  Card is approximately {width_mm/a7_width:.1%} of A7 width")
    print()


if __name__ == "__main__":
    main()
