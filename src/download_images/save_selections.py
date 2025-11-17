"""
Save user-selected images to final directory.
"""
import sys
import argparse
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
    import json
    from datetime import datetime

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

    # Prioritize copying JSON from temp_candidates over generating new metadata
    metadata_path = final_path.with_suffix('.json')
    temp_candidates_dir = Path("sourced_images/temp_candidates")

    # Construct the temp_candidates filename pattern: {id}_{category}_{name}_temp{number}.json
    normalized_name = character.name.replace(' ', '_').replace('/', '_')
    temp_filename = f"{character.id}_{character.type}_{normalized_name}_temp{image_number}.json"
    source_metadata = temp_candidates_dir / temp_filename

    if source_metadata.exists():
        # Copy existing metadata from temp_candidates
        shutil.copy2(source_metadata, metadata_path)
        print(f"  📋 Copied metadata from temp_candidates")

        # Update rank and selection metadata in the copied file
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)

        metadata['rank'] = 1
        metadata['selected_option'] = image_number
        metadata['selection_timestamp'] = datetime.now().isoformat()

        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
    else:
        # Generate basic metadata as fallback
        print(f"  ⚠️  No metadata in temp_candidates, generating basic metadata")
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
    parser = argparse.ArgumentParser(
        description="Save selected images from review to final directory"
    )
    parser.add_argument(
        'selections',
        help='Selection text in format "CHARACTER: NUM\\nCHARACTER: NUM"'
    )
    parser.add_argument(
        '--batch',
        help='Batch directory name (e.g., M_batch1, M_batch2). If not specified, uses sourced_images/review',
        default=None
    )

    args = parser.parse_args()
    selection_text = args.selections

    print("="*80)
    print("Saving Selected Images")
    print("="*80)

    # Parse selections
    selections = parse_selections(selection_text)
    print(f"\nProcessing {len(selections)} selections...")

    # Determine review directory based on batch parameter
    if args.batch:
        review_dir = Path("sourced_images/review") / args.batch
        if not review_dir.exists():
            print(f"❌ Error: Batch directory not found: {review_dir}")
            sys.exit(1)
        print(f"📁 Using batch: {args.batch}")
    else:
        review_dir = Path("sourced_images/review")
        print(f"📁 Using default review directory")

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
