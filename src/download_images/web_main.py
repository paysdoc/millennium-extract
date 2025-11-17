"""
Web-based selection CLI.

Usage:
  # By category and batch
  python -m src.download_images.web_main [CATEGORY] [BATCH_SIZE] [START_IDX]

  # By character IDs
  python -m src.download_images.web_main --ids ID1,ID2,ID3,...
  python -m src.download_images.web_main --ids ID1 ID2 ID3 ...

Examples:
  python -m src.download_images.web_main I 5 0
  python -m src.download_images.web_main --ids 172,250,266,269,272,276
  python -m src.download_images.web_main --ids 172 250 266
"""
import sys
import os
import signal
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.simple_review import SimpleReviewGenerator
from src.download_images.models import Character
from src.download_images.port_manager import PortManager
from src.supabase_client import get_supabase_client


def start_http_server(port: int, directory: Path) -> int:
    """
    Start an HTTP server on the given port.

    Args:
        port: Port number
        directory: Directory to serve

    Returns:
        Process ID of the server
    """
    # Start server in background
    process = subprocess.Popen(
        [sys.executable, '-m', 'http.server', str(port)],
        cwd=str(directory),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return process.pid


def parse_character_ids(args):
    """
    Parse character IDs from command line arguments.

    Supports:
      --ids 1,2,3
      --ids 1 2 3

    Args:
        args: Command line arguments

    Returns:
        List of character IDs or None if not using --ids
    """
    if len(args) < 2 or args[1] != '--ids':
        return None

    if len(args) < 3:
        print("Error: --ids requires at least one character ID")
        sys.exit(1)

    char_ids = []

    # Check if using comma-separated format
    if ',' in args[2]:
        # Format: --ids 1,2,3
        char_ids = [int(id.strip()) for id in args[2].split(',')]
    else:
        # Format: --ids 1 2 3
        for arg in args[2:]:
            try:
                char_ids.append(int(arg))
            except ValueError:
                print(f"Error: Invalid character ID: {arg}")
                sys.exit(1)

    return char_ids


def main():
    """Main entry point."""
    # Check if using --ids mode
    char_ids = parse_character_ids(sys.argv)

    if char_ids is not None:
        # Character ID mode
        category_filter = None
        batch_size = len(char_ids)
        start_idx = 0

        print("="*80)
        print("Web-Based Image Selection - By Character IDs")
        print("="*80)
        print(f"Character IDs: {', '.join(map(str, char_ids))}")
        print(f"Total characters: {len(char_ids)}")
        print("="*80)

        # Connect to Supabase
        print("\nConnecting to Supabase...")
        client = get_supabase_client()

        # Fetch characters by ID
        response = client.table('character').select('*').in_('id', char_ids).execute()
        characters = [Character.from_dict(row) for row in response.data]

        # Sort by ID to match the order given
        id_to_char = {char.id: char for char in characters}
        characters = [id_to_char[cid] for cid in char_ids if cid in id_to_char]

        # Report any missing IDs
        found_ids = {char.id for char in characters}
        missing_ids = set(char_ids) - found_ids
        if missing_ids:
            print(f"\n⚠️  Warning: Could not find characters with IDs: {', '.join(map(str, sorted(missing_ids)))}")

        print(f"Found {len(characters)} characters:")
        for char in characters:
            print(f"  - ID {char.id}: {char.name} ({char.type})")

        # Generate batch ID based on IDs
        batch_id = f"ids_{'_'.join(map(str, sorted(char_ids)[:3]))}"
        if len(char_ids) > 3:
            batch_id += f"_plus{len(char_ids)-3}"

    else:
        # Category mode (original behavior)
        category_filter = sys.argv[1].upper() if len(sys.argv) > 1 else None
        batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        start_idx = int(sys.argv[3]) if len(sys.argv) > 3 else 0

        print("="*80)
        print("Web-Based Image Selection")
        print("="*80)
        if category_filter:
            print(f"Category: {category_filter}")
        print(f"Batch size: {batch_size} characters")
        if start_idx > 0:
            print(f"Starting from: #{start_idx + 1}")
        print("="*80)

        # Connect to Supabase
        print("\nConnecting to Supabase...")
        client = get_supabase_client()

        # Fetch characters
        query = client.table('character').select('*')
        if category_filter:
            query = query.eq('type', category_filter)
        query = query.order('type').order('name')

        response = query.execute()
        characters = [Character.from_dict(row) for row in response.data]

        print(f"Total characters: {len(characters)}")

        # Generate review pages with batch-specific ID to isolate localStorage
        batch_num = (start_idx // batch_size) + 1
        batch_id = f"{category_filter or 'ALL'}_batch{batch_num}"

    print(f"Batch ID: {batch_id}")

    generator = SimpleReviewGenerator(batch_id=batch_id)
    generator.process_batch(characters, batch_size, start_idx)

    # Find available port and start HTTP server
    port_manager = PortManager()
    port = port_manager.find_available_port()

    if port is None:
        print("\n⚠️  WARNING: No available ports (8000-8020)")
        print("Review pages generated but HTTP server not started")
        print(f"You can manually start a server:")
        print(f"  cd {generator.review_dir.absolute()}")
        print(f"  python3 -m http.server 8000")
        return

    # Start HTTP server - serve from the root review directory
    review_dir_root = Path("sourced_images/review")
    try:
        pid = start_http_server(port, review_dir_root)

        # Register port
        if char_ids is not None:
            batch_info = f"Character IDs: {', '.join(map(str, char_ids[:5]))}"
            if len(char_ids) > 5:
                batch_info += f" +{len(char_ids)-5} more"
        else:
            batch_info = f"Batch {start_idx//batch_size + 1} (chars {start_idx+1}-{start_idx+batch_size})"
        port_manager.register_port(port, category_filter or "IDs", batch_info, pid)

        print(f"\n{'='*80}")
        print(f"🌐 HTTP Server Started")
        print(f"{'='*80}")
        print(f"Port: {port}")
        print(f"PID: {pid}")
        print(f"\n📂 Open in browser:")
        print(f"  http://localhost:{port}/{batch_id}/index.html")
        print(f"\n{'='*80}")
        print(f"ℹ️  The server will keep running in the background")
        print(f"   To stop it later, use:")
        print(f"   python3 -m src.download_images.cleanup_servers")
        print(f"{'='*80}\n")

    except Exception as e:
        print(f"\n⚠️  Failed to start HTTP server: {e}")
        print(f"You can manually start a server:")
        print(f"  cd {review_dir_root.absolute()}")
        print(f"  python3 -m http.server {port}")


if __name__ == "__main__":
    main()
