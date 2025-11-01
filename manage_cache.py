#!/usr/bin/env python3
"""
Image cache management utility.
"""
import os
import sys
from pathlib import Path


def get_cache_dir():
    """Get the cache directory path."""
    return os.path.join(os.path.dirname(__file__), 'image_cache')


def show_cache_stats():
    """Display cache statistics."""
    cache_dir = get_cache_dir()

    if not os.path.exists(cache_dir):
        print("Cache directory does not exist")
        return

    files = os.listdir(cache_dir)
    if not files:
        print("Cache is empty")
        return

    total_size = 0
    print("=" * 70)
    print("Image Cache Statistics")
    print("=" * 70)
    print()
    print(f"Cache location: {cache_dir}")
    print(f"Cached images: {len(files)}")
    print()

    print("Cached files:")
    for f in sorted(files):
        file_path = os.path.join(cache_dir, f)
        size = os.path.getsize(file_path)
        total_size += size
        print(f"  {f:40s} {size/1024:7.1f} KB")

    print()
    print(f"Total cache size: {total_size/1024:.1f} KB ({total_size/(1024*1024):.2f} MB)")
    print()


def clear_cache():
    """Clear all cached images."""
    cache_dir = get_cache_dir()

    if not os.path.exists(cache_dir):
        print("Cache directory does not exist")
        return

    files = os.listdir(cache_dir)
    if not files:
        print("Cache is already empty")
        return

    print(f"Found {len(files)} cached images")
    response = input("Are you sure you want to delete all cached images? (y/N): ")

    if response.lower() != 'y':
        print("Cancelled")
        return

    for f in files:
        os.remove(os.path.join(cache_dir, f))

    print(f"✓ Deleted {len(files)} cached images")


def main():
    if len(sys.argv) < 2:
        print("Image Cache Management")
        print()
        print("Usage:")
        print("  python manage_cache.py stats   - Show cache statistics")
        print("  python manage_cache.py clear   - Clear all cached images")
        return

    command = sys.argv[1]

    if command == "stats":
        show_cache_stats()
    elif command == "clear":
        clear_cache()
    else:
        print(f"Unknown command: {command}")
        print("Use 'stats' or 'clear'")


if __name__ == "__main__":
    main()
