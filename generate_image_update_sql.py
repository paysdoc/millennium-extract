#!/usr/bin/env python3
"""
Generate SQL script to update character image_link column
with sourced Wikimedia images.
"""

import os
from pathlib import Path

# Directory containing the images
IMAGE_DIR = Path("sourced_images/wikimedia/by_character_id")
# Prefix for the image links in the database
IMAGE_PREFIX = "data/character_images/"
# Output SQL file
OUTPUT_FILE = "update_character_images.sql"

def extract_character_id(filename):
    """Extract character ID from filename like '100_S_GORBACHEV.jpg'"""
    try:
        return int(filename.split('_')[0])
    except (IndexError, ValueError):
        return None

def generate_sql():
    """Generate SQL UPDATE statements for all sourced images"""

    # Find all JPG files in the directory
    jpg_files = sorted(IMAGE_DIR.glob("*.jpg"))

    print(f"Found {len(jpg_files)} JPG images in {IMAGE_DIR}")

    # Generate SQL statements
    sql_lines = [
        "-- Update character image_link column with Wikimedia sourced images",
        f"-- Generated on 2025-11-18",
        f"-- Prefix: {IMAGE_PREFIX}",
        "",
        "BEGIN;",
        "",
        "-- Update statements for each character with a sourced image",
        ""
    ]

    update_count = 0
    skipped = []

    for jpg_file in jpg_files:
        filename = jpg_file.name

        # Skip .DS_Store and other non-image files
        if filename.startswith('.'):
            continue

        character_id = extract_character_id(filename)

        if character_id is None:
            skipped.append(filename)
            continue

        # Generate UPDATE statement
        image_path = f"{IMAGE_PREFIX}{filename}"
        sql = f"UPDATE character SET image_link = '{image_path}' WHERE id = {character_id};"
        sql_lines.append(sql)
        update_count += 1

    sql_lines.append("")
    sql_lines.append("COMMIT;")
    sql_lines.append("")
    sql_lines.append(f"-- Total updates: {update_count}")

    if skipped:
        sql_lines.append(f"-- Skipped files (couldn't extract ID): {len(skipped)}")
        for filename in skipped:
            sql_lines.append(f"--   {filename}")

    # Write to file
    with open(OUTPUT_FILE, 'w') as f:
        f.write('\n'.join(sql_lines))

    print(f"\nGenerated SQL script: {OUTPUT_FILE}")
    print(f"Total UPDATE statements: {update_count}")
    if skipped:
        print(f"Skipped files: {len(skipped)}")
        for filename in skipped:
            print(f"  - {filename}")

if __name__ == "__main__":
    generate_sql()
