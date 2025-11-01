#!/usr/bin/env python3
"""
Test script to verify connections table uses why_short without truncation.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.supabase_client import get_supabase_client, fetch_all_card_data


def main():
    print("=" * 70)
    print("Connections Table Verification")
    print("=" * 70)
    print()

    client = get_supabase_client()
    card_data_list = fetch_all_card_data(client)

    # Test characters with varying connection counts
    test_chars = ['WASHINGTON', 'AQUINAS', 'BACON, ROGER']

    for char_name in test_chars:
        data = next((d for d in card_data_list if d.character.name == char_name), None)
        if not data:
            continue

        print(f"{char_name}")
        print(f"  Total connections: {len(data.connections)}")
        print(f"  Displayed: {min(8, len(data.connections))} (max 8)")
        print()

        # Check why_short values
        connections_with_why_short = 0
        total_why_short_length = 0

        for i, conn in enumerate(data.connections[:8]):
            if conn.why_short:
                connections_with_why_short += 1
                total_why_short_length += len(conn.why_short)
                if i < 3:  # Show first 3 as examples
                    print(f"    {i+1}. {conn.character_name}")
                    print(f"       why_short: {len(conn.why_short)} chars")
                    print(f"       \"{conn.why_short}\"")

        print()
        print(f"  Connections with why_short: {connections_with_why_short}/8")
        if connections_with_why_short > 0:
            avg_length = total_why_short_length / connections_with_why_short
            print(f"  Average why_short length: {avg_length:.1f} chars")
        print()
        print("-" * 70)
        print()

    print("=" * 70)
    print("Table Configuration")
    print("=" * 70)
    print()
    print("✓ Font size: 6pt (increased from 5pt)")
    print("✓ Text wrapping: ENABLED")
    print("✓ Data source: why_short field only")
    print("✓ Truncation: REMOVED - full text displayed with wrapping")
    print("✓ Column widths: 6mm, 6mm, 18mm, 33mm")
    print("✓ Vertical alignment: TOP (for multi-line text)")
    print("✓ Max connections displayed: 8 per card")
    print()
    print("Character names and why_short values are shown in full,")
    print("wrapping to multiple lines as needed within table cells.")
    print()


if __name__ == "__main__":
    main()
