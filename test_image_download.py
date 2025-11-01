#!/usr/bin/env python3
"""
Test script to verify Supabase image downloads work correctly.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.supabase_client import get_supabase_client, fetch_all_card_data
from src.card import download_image_from_supabase
import os


def main():
    print("=" * 70)
    print("Supabase Image Download Test")
    print("=" * 70)
    print()

    client = get_supabase_client()
    card_data_list = fetch_all_card_data(client)

    # Test different image path formats
    test_cases = [
        ("WASHINGTON", " data/images/washington.jpg"),
        ("NEWTON", " data/images/Newton.jpg"),
        ("ABELARD", " data/images/abelard.jpg"),
        ("ABBOT HUGH", " data/images/abbot hugh.jpg"),
    ]

    print("Testing image downloads from Supabase storage...")
    print()

    success_count = 0
    fail_count = 0

    for name, expected_path in test_cases:
        # Find the character
        char_data = None
        for data in card_data_list:
            if data.character.name == name:
                char_data = data
                break

        if not char_data:
            print(f"❌ {name}: Character not found in database")
            fail_count += 1
            continue

        image_path = char_data.character.image_link
        print(f"Testing: {name}")
        print(f"  Database path: {image_path}")

        # Extract filename
        filename = os.path.basename(image_path.strip()) if image_path else None
        print(f"  Extracted filename: {filename}")

        # Try to download
        img = download_image_from_supabase(client, image_path)

        if img:
            print(f"  ✓ Successfully downloaded image")
            success_count += 1
        else:
            print(f"  ❌ Failed to download image")
            fail_count += 1

        print()

    print("=" * 70)
    print(f"Results: {success_count} successful, {fail_count} failed")
    print("=" * 70)
    print()

    if fail_count == 0:
        print("✓ All image downloads successful!")
        print()
        print("Key improvements:")
        print("  • Images are downloaded from Supabase storage bucket")
        print("  • Path prefixes (data/images/) are automatically stripped")
        print("  • Filenames with spaces are handled correctly")
        print("  • Case-sensitive filenames work (e.g., Newton.jpg)")
    else:
        print(f"⚠ {fail_count} image(s) failed to download")

    print()


if __name__ == "__main__":
    main()
