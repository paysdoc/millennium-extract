#!/usr/bin/env python3
"""
Test script to verify image caching functionality.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import os
import time
from src.supabase_client import get_supabase_client, fetch_all_card_data
from src.cards import generate_single_card_pdf


def main():
    print("=" * 70)
    print("Image Cache Verification Test")
    print("=" * 70)
    print()

    # Check cache directory
    cache_dir = os.path.join(os.path.dirname(__file__), 'image_cache')

    print(f"Cache directory: {cache_dir}")

    if os.path.exists(cache_dir):
        cached_files = os.listdir(cache_dir)
        print(f"Cached images: {len(cached_files)}")
        if cached_files:
            print("Sample cached files:")
            for f in cached_files[:5]:
                file_path = os.path.join(cache_dir, f)
                size_kb = os.path.getsize(file_path) / 1024
                print(f"  - {f} ({size_kb:.1f} KB)")
    else:
        print("Cache directory does not exist yet")

    print()
    print("-" * 70)
    print()

    # Test cache performance
    client = get_supabase_client()
    card_data_list = fetch_all_card_data(client)

    # Find a character with an image
    test_char = None
    for data in card_data_list:
        if data.character.image_link and data.character.name == "WASHINGTON":
            test_char = data
            break

    if not test_char:
        print("No test character found with image")
        return

    print(f"Testing with: {test_char.character.name}")
    print()

    # First generation (should download and cache)
    print("First generation (downloading and caching)...")
    start = time.time()
    generate_single_card_pdf(test_char, "test_cache_1.pdf", 1, supabase_client=client)
    first_time = time.time() - start
    print(f"  Time: {first_time:.3f}s")
    print()

    # Second generation (should use cache)
    print("Second generation (using cache)...")
    start = time.time()
    generate_single_card_pdf(test_char, "test_cache_2.pdf", 1, supabase_client=client)
    second_time = time.time() - start
    print(f"  Time: {second_time:.3f}s")
    print()

    # Performance comparison
    print("-" * 70)
    print()
    if second_time < first_time:
        speedup = (first_time - second_time) / first_time * 100
        print(f"✓ Cache is working! Second generation was {speedup:.1f}% faster")
    else:
        print("⚠ Cache may not be working as expected")

    print()

    # Cache statistics
    if os.path.exists(cache_dir):
        cached_files = os.listdir(cache_dir)
        total_size = sum(os.path.getsize(os.path.join(cache_dir, f)) for f in cached_files)

        print("=" * 70)
        print("Cache Statistics")
        print("=" * 70)
        print(f"  Cached images: {len(cached_files)}")
        print(f"  Total cache size: {total_size / 1024:.1f} KB ({total_size / (1024*1024):.2f} MB)")
        print()

    # Cleanup test files
    for f in ["test_cache_1.pdf", "test_cache_2.pdf"]:
        if os.path.exists(f):
            os.remove(f)


if __name__ == "__main__":
    main()
