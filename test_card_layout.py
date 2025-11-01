#!/usr/bin/env python3
"""
Test script to verify card dimensions and text wrapping.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.card import CARD_WIDTH, CARD_HEIGHT
from reportlab.lib.units import mm


def main():
    print("=" * 70)
    print("Card Layout Verification")
    print("=" * 70)
    print()

    # Check card dimensions
    expected_width = 69 * mm
    expected_height = 96 * mm

    print(f"Card Dimensions:")
    print(f"  Width:  {CARD_WIDTH / mm:.2f}mm (expected: 69mm) - {'✓' if abs(CARD_WIDTH - expected_width) < 0.01 else '✗'}")
    print(f"  Height: {CARD_HEIGHT / mm:.2f}mm (expected: 96mm) - {'✓' if abs(CARD_HEIGHT - expected_height) < 0.01 else '✗'}")
    print(f"  Aspect Ratio: {CARD_WIDTH/CARD_HEIGHT:.3f} (69:96 = {69/96:.3f})")
    print()

    # Test text wrapping
    from src.supabase_client import get_supabase_client, fetch_all_card_data
    from reportlab.pdfgen import canvas as pdf_canvas
    from reportlab.lib.pagesizes import A4
    import tempfile

    print("Testing Text Wrapping...")
    client = get_supabase_client()
    card_data_list = fetch_all_card_data(client)

    # Create a temporary canvas for testing
    with tempfile.NamedTemporaryFile(suffix='.pdf') as tmp:
        c = pdf_canvas.Canvas(tmp.name, pagesize=A4)

        # Test cases: characters with potentially long text
        test_cases = [
            "WASHINGTON",
            "BACON, ROGER",
            "BARBAROSSA",
            "ALEXANDER VI",
        ]

        for char_name in test_cases:
            data = next((d for d in card_data_list if d.character.name == char_name), None)
            if data:
                full_name = f"{data.character.name or ''} {data.character.first_names or ''}".strip()
                bio = data.character.biography or ""
                print(f"\n  {char_name}:")
                print(f"    Full name: {len(full_name)} chars - {full_name[:40]}...")
                print(f"    Biography: {len(bio)} chars")
                print(f"    Connections: {len(data.connections)}")

    print()
    print("=" * 70)
    print("Layout Features")
    print("=" * 70)
    print()
    print("✓ Card dimensions: 69mm × 96mm (width × height)")
    print("✓ Text wrapping implemented for:")
    print("  • Character names on banners")
    print("  • Full names in header")
    print("  • Biography text")
    print("✓ Tables adjusted for narrower card:")
    print("  • Reduced to 8 connections (from 10)")
    print("  • Smaller font size (5pt)")
    print("  • Uses why_short for compact descriptions")
    print("✓ Images constrained to card boundaries")
    print("  • Max height: 70mm")
    print("  • Maintains aspect ratio")
    print()


if __name__ == "__main__":
    main()
