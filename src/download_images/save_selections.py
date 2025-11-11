"""
Save user-selected images to final directory.
"""
import sys
import shutil
from pathlib import Path

from .models import Character, ImageInfo
from .file_manager import FileManager
from src.supabase_client import get_supabase_client


def parse_selections(selection_text: str) -> dict:
    """Parse selections like 'BARBAROSSA: 5' into dict."""
    selections = {}
    for line in selection_text.strip().split('\n'):
        if ':' in line:
            name, num = line.split(':', 1)
            name = name.strip()
            num = int(num.strip())
            if num > 0:  # Skip 0 (means skip character)
                selections[name] = num
    return selections


def get_character_by_name(name: str) -> Character:
    """Fetch character from Supabase by name."""
    client = get_supabase_client()
    response = client.table('character').select('*').eq('name', name.upper()).execute()

    if not response.data or len(response.data) == 0:
        raise ValueError(f"Character not found: {name}")

    return Character.from_dict(response.data[0])


def save_selection(character: Character, image_number: int, review_dir: Path, output_dir: Path):
    """
    Save the selected image from review directory to final output.

    Args:
        character: Character object
        image_number: Selected image number (1-indexed)
        review_dir: Path to review directory
        output_dir: Path to output directory
    """
    file_manager = FileManager()

    # Find the selected image in review directory
    source_image = review_dir / f"{character.id}_{image_number}.jpg"

    if not source_image.exists():
        raise FileNotFoundError(f"Selected image not found: {source_image}")

    # Generate final filename
    final_filename = file_manager.generate_filename(
        character.id,
        character.type,
        character.name,
        rank=1  # Always primary for selected images
    )

    final_path = output_dir / final_filename

    # Copy image to final location
    shutil.copy2(source_image, final_path)

    # Create basic metadata (we don't have ImageInfo, so use placeholder)
    # The metadata will be updated with actual Wikimedia info if needed
    from datetime import datetime
    metadata_path = final_path.with_suffix('.json')

    import json
    basic_metadata = {
        'character_name': character.name,
        'character_id': character.id,
        'category': character.type,
        'first_names': character.first_names,
        'biography': character.biography,
        'birth_date': character.birth_date,
        'death_date': character.death_date,
        'source': 'manual_selection',
        'selected_option': image_number,
        'download_timestamp': datetime.now().isoformat(),
        'rank': 1
    }

    with open(metadata_path, 'w') as f:
        json.dump(basic_metadata, f, indent=2)

    return final_path


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python -m src.download_images.save_selections 'BARBAROSSA: 5\\nCATHERINE II: 3'")
        sys.exit(1)

    selection_text = sys.argv[1]

    print("="*80)
    print("Saving Selected Images")
    print("="*80)

    # Parse selections
    selections = parse_selections(selection_text)
    print(f"\nProcessing {len(selections)} selections...")

    review_dir = Path("sourced_images/review")
    output_dir = Path("sourced_images/wikimedia/by_character_id")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process each selection
    saved_count = 0
    for char_name, image_num in selections.items():
        print(f"\n[{char_name}] → Image #{image_num}")

        try:
            # Get character from database
            character = get_character_by_name(char_name)

            # Save selected image
            final_path = save_selection(character, image_num, review_dir, output_dir)

            print(f"  ✅ Saved: {final_path.name}")
            saved_count += 1

        except Exception as e:
            print(f"  ❌ Error: {e}")

    print(f"\n{'='*80}")
    print(f"✅ Saved {saved_count}/{len(selections)} images")
    print(f"{'='*80}")
    print(f"\nImages saved to: {output_dir.absolute()}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
