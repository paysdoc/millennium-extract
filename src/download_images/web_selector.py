"""
Web-based interactive image selection.
Creates HTML pages for reviewing candidates in a browser.
"""
import json
import shutil
from pathlib import Path
from typing import List, Tuple
from datetime import datetime

from .interactive_selector import InteractiveImageSelector
from .models import Character


class WebSelector:
    """
    Web-based image selector - generates HTML for browser-based review.
    """

    def __init__(self):
        self.selector = InteractiveImageSelector(permissive_threshold=40)
        self.review_dir = Path("sourced_images/review")
        self.review_dir.mkdir(parents=True, exist_ok=True)

        # State tracking
        self.current_character_idx = 0
        self.characters = []
        self.state_file = self.review_dir / "state.json"
        self.selections_file = self.review_dir / "selections.json"

    def load_state(self):
        """Load saved state."""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                state = json.load(f)
                self.current_character_idx = state.get('current_idx', 0)
                return True
        return False

    def save_state(self):
        """Save current state."""
        state = {
            'current_idx': self.current_character_idx,
            'timestamp': datetime.now().isoformat()
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def save_selection(self, character: Character, selected_idx: int):
        """Save user selection."""
        selections = {}
        if self.selections_file.exists():
            with open(self.selections_file, 'r') as f:
                selections = json.load(f)

        # JSON keys must be strings, so convert ID to string for dictionary key
        selections[str(character.id)] = {
            'name': character.name,
            'type': character.type,
            'selected_idx': selected_idx,
            'timestamp': datetime.now().isoformat()
        }

        with open(self.selections_file, 'w') as f:
            json.dump(selections, f, indent=2)

    def generate_review_page(
        self,
        character: Character,
        candidates: List[tuple],
        filtered: List[tuple]
    ) -> Path:
        """
        Generate HTML review page for a character.

        Args:
            character: Character object
            candidates: All downloaded candidates
            filtered: Filtered candidates to show

        Returns:
            Path to generated HTML file
        """
        html_file = self.review_dir / f"{character.id}_review.html"

        # Copy images to review directory
        review_images = []
        for idx, (image_info, filepath) in enumerate(filtered):
            new_filename = f"{character.id}_{idx}.jpg"
            new_path = self.review_dir / new_filename
            shutil.copy2(filepath, new_path)
            review_images.append((idx, image_info, new_filename))

        # Generate HTML
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Select Image for {character.name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            margin: 0 0 10px 0;
            color: #333;
        }}
        .character-info {{
            color: #666;
            line-height: 1.6;
        }}
        .progress {{
            background: #e0e0e0;
            height: 30px;
            border-radius: 15px;
            margin: 20px 0;
            overflow: hidden;
        }}
        .progress-bar {{
            background: linear-gradient(90deg, #4CAF50, #45a049);
            height: 100%;
            line-height: 30px;
            color: white;
            text-align: center;
            font-weight: bold;
        }}
        .candidates {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .candidate {{
            background: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .candidate:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        .candidate img {{
            width: 100%;
            height: auto;
            border-radius: 4px;
            display: block;
            margin-bottom: 10px;
        }}
        .candidate-info {{
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
        }}
        .candidate-title {{
            font-size: 12px;
            color: #888;
            margin-bottom: 10px;
            word-wrap: break-word;
        }}
        .button {{
            display: inline-block;
            padding: 12px 24px;
            margin: 5px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
            transition: background 0.2s;
        }}
        .select-button {{
            background: #4CAF50;
            color: white;
            width: 100%;
        }}
        .select-button:hover {{
            background: #45a049;
        }}
        .action-buttons {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .skip-button {{
            background: #f44336;
            color: white;
        }}
        .skip-button:hover {{
            background: #da190b;
        }}
        .stats {{
            background: #2196F3;
            color: white;
            padding: 10px 20px;
            border-radius: 4px;
            display: inline-block;
            margin: 10px 5px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>[{character.type}] {character.name}</h1>
        <div class="character-info">
            {"<strong>First names:</strong> " + character.first_names + "<br>" if character.first_names else ""}
            {"<strong>Dates:</strong> " + (character.birth_date or "?") + " - " + (character.death_date or "?") + "<br>" if character.birth_date or character.death_date else ""}
            {"<strong>Biography:</strong> " + character.biography[:200] + "..." if character.biography and len(character.biography) > 200 else character.biography or ""}
        </div>
        <div class="progress">
            <div class="progress-bar" style="width: {(self.current_character_idx / len(self.characters) * 100):.1f}%">
                Character {self.current_character_idx + 1} / {len(self.characters)}
            </div>
        </div>
        <div>
            <span class="stats">📦 Downloaded: {len(candidates)}</span>
            <span class="stats">✅ Filtered: {len(filtered)}</span>
        </div>
    </div>

    <h2>Select the Best Image</h2>
    <div class="candidates">
"""

        for idx, image_info, filename in review_images:
            html += f"""
        <div class="candidate">
            <img src="{filename}" alt="Candidate {idx + 1}">
            <div class="candidate-info">
                <strong>Size:</strong> {image_info.width}×{image_info.height}px<br>
                <strong>Aspect Ratio:</strong> {image_info.aspect_ratio:.3f}<br>
                <strong>Quality Score:</strong> {image_info.score:.3f}
            </div>
            <div class="candidate-title">
                {image_info.title[:100]}...
            </div>
            <a href="select.html?char={character.id}&idx={idx}" class="button select-button">
                ✅ Select This Image
            </a>
        </div>
"""

        html += f"""
    </div>

    <div class="action-buttons">
        <h3>Don't like any of these?</h3>
        <a href="skip.html?char={character.id}" class="button skip-button">
            ⏭️ Skip This Character
        </a>
    </div>

    <script>
        // Handle selection
        const urlParams = new URLSearchParams(window.location.search);
        if (window.location.pathname.includes('select.html')) {{
            const charId = urlParams.get('char');
            const idx = urlParams.get('idx');
            if (charId && idx) {{
                alert('Image ' + (parseInt(idx) + 1) + ' selected! Saving...');
                // In a real implementation, this would POST to a server
                window.location.href = 'next.html?selected=' + idx;
            }}
        }}
        if (window.location.pathname.includes('skip.html')) {{
            const charId = urlParams.get('char');
            if (charId) {{
                alert('Character skipped');
                window.location.href = 'next.html?skipped=true';
            }}
        }}
    </script>
</body>
</html>
"""

        with open(html_file, 'w') as f:
            f.write(html)

        return html_file

    def process_character_for_review(self, character: Character) -> bool:
        """
        Process one character and generate review page.

        Args:
            character: Character to process

        Returns:
            True if successful
        """
        print(f"\nProcessing {character.name}...")

        # Download candidates
        candidates = self.selector.download_candidates(character, max_candidates=15)
        if not candidates:
            print(f"  ⚠️  No candidates found - skipping")
            return False

        # Filter
        filtered = self.selector.filter_by_similarity(character, candidates)
        if not filtered:
            print(f"  ⚠️  All candidates rejected - showing all anyway")
            filtered = candidates

        # Generate HTML
        html_file = self.generate_review_page(character, candidates, filtered)
        print(f"  ✅ Review page created: {html_file}")

        return True

    def generate_batch(self, characters: List[Character], batch_size: int = 5):
        """
        Generate review pages for a batch of characters.

        Args:
            characters: List of characters
            batch_size: Number of characters to process in this batch
        """
        self.characters = characters

        # Load state if exists
        self.load_state()

        end_idx = min(self.current_character_idx + batch_size, len(characters))

        print(f"\n{'='*80}")
        print(f"Generating review pages for characters {self.current_character_idx + 1}-{end_idx}")
        print(f"{'='*80}\n")

        for idx in range(self.current_character_idx, end_idx):
            character = characters[idx]
            self.process_character_for_review(character)
            self.current_character_idx = idx + 1
            self.save_state()

        # Generate index page
        self.generate_index_page()

        print(f"\n{'='*80}")
        print(f"✅ Review pages generated!")
        print(f"{'='*80}")
        print(f"\nOpen this file in your browser:")
        print(f"  {self.review_dir.absolute() / 'index.html'}")
        print(f"\nThen review each character and select the best image.")
        print(f"{'='*80}\n")

    def generate_index_page(self):
        """Generate index page with links to all character reviews."""
        index_file = self.review_dir / "index.html"

        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Image Selection Review</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 {
            color: #333;
        }
        .character-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 15px;
        }
        .character-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .character-card a {
            color: #2196F3;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }
        .character-card a:hover {
            text-decoration: underline;
        }
        .character-info {
            color: #666;
            font-size: 14px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Character Image Selection</h1>
    <p>Click on each character to review and select their image.</p>
    <div class="character-list">
"""

        for idx in range(self.current_character_idx):
            if idx < len(self.characters):
                character = self.characters[idx]
                review_file = f"{character.id}_review.html"
                html += f"""
        <div class="character-card">
            <a href="{review_file}">{character.name}</a>
            <div class="character-info">
                Category: {character.type}<br>
                {character.birth_date or "?"} - {character.death_date or "?"}
            </div>
        </div>
"""

        html += """
    </div>
</body>
</html>
"""

        with open(index_file, 'w') as f:
            f.write(html)
