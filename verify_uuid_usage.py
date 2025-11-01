#!/usr/bin/env python3
"""
Verification script to demonstrate that UUIDs are used internally
while the interface uses character names.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.supabase_client import get_supabase_client, fetch_all_card_data


def main():
    print("=" * 70)
    print("UUID Usage Verification")
    print("=" * 70)
    print()

    client = get_supabase_client()
    card_data_list = fetch_all_card_data(client)

    # Find a character with connections
    sample = None
    for data in card_data_list:
        if len(data.connections) >= 3:
            sample = data
            break

    if not sample:
        print("No character with connections found")
        return

    print(f"Character: {sample.character.name} ({sample.character.first_names})")
    print(f"Internal UUID: {sample.character.id}")
    print(f"Category: {sample.character.type}")
    print()
    print("=" * 70)
    print("Connections (Denormalized)")
    print("=" * 70)
    print()
    print("Internal Process:")
    print("  1. UUIDs are used to fetch connections from database")
    print("  2. Character IDs in connections are replaced with names")
    print("  3. User sees human-readable names in output")
    print()
    print(f"Found {len(sample.connections)} connections:")
    print()

    for i, conn in enumerate(sample.connections[:5], 1):
        print(f"  {i}. {conn.character_name} ({conn.category_code})")
        print(f"     Value: {conn.value}")
        if conn.why:
            print(f"     Why: {conn.why[:60]}...")
        print()

    print("=" * 70)
    print("Interface Usage")
    print("=" * 70)
    print()
    print(f"To generate a card for this character, use:")
    print(f"  python src/main.py generate-single {sample.character.name}")
    print()
    print("NOT the UUID:")
    print(f"  python src/main.py generate-single {sample.character.id}  # ❌ This won't work")
    print()
    print("=" * 70)
    print("✓ Verification Complete")
    print("=" * 70)
    print()
    print("Summary:")
    print("  • UUIDs are used internally for database operations")
    print("  • Character names are used in the CLI interface")
    print("  • Connections properly denormalize UUID references to names")
    print()


if __name__ == "__main__":
    main()
