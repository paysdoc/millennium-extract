#!/usr/bin/env python3
"""
Simple test to verify all imports work correctly.
Run this after setup to ensure everything is configured properly.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

print("Testing imports...")

try:
    print("  ✓ Importing click...", end=" ")
    import click
    print("OK")

    print("  ✓ Importing dotenv...", end=" ")
    from dotenv import load_dotenv
    print("OK")

    print("  ✓ Importing supabase...", end=" ")
    from supabase import create_client
    print("OK")

    print("  ✓ Importing reportlab...", end=" ")
    from reportlab.pdfgen import canvas
    print("OK")

    print("  ✓ Importing PIL...", end=" ")
    from PIL import Image
    print("OK")

    print("  ✓ Importing requests...", end=" ")
    import requests
    print("OK")

    print("\n  ✓ Importing src.types.supabase_types...", end=" ")
    from src.types.supabase_types import Character, Connection, CardData
    print("OK")

    print("  ✓ Importing src.supabase_client...", end=" ")
    from src.supabase_client import get_supabase_client
    print("OK")

    print("  ✓ Importing src.card...", end=" ")
    from src.card import draw_card_front, draw_card_back
    print("OK")

    print("  ✓ Importing src.cards...", end=" ")
    from src.cards import generate_cards_pdf
    print("OK")

    print("\n✓ All imports successful!")
    print("\nYou can now run:")
    print("  python src/main.py --help")

except ImportError as e:
    print(f"\n✗ Import failed: {e}")
    print("\nMake sure you:")
    print("  1. Activated the virtual environment: source millennium_virtual_environment/bin/activate")
    print("  2. Installed dependencies: pip install -r requirements.txt")
    sys.exit(1)
