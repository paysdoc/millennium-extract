"""
Simple review page generator - creates one HTML page per character with visual selection.
"""
import json
import shutil
from pathlib import Path
from typing import List, Tuple

from .interactive_selector import InteractiveImageSelector
from .models import Character
from .file_manager import FileManager


class SimpleReviewGenerator:
    """Generate simple review pages where you can note your selection."""

    def __init__(self, batch_id: str = None):
        self.selector = InteractiveImageSelector(permissive_threshold=40)
        # Use batch_id to namespace localStorage and prevent leakage between batches
        self.batch_id = batch_id or "default"
        # CRITICAL: Use batch-specific directory to prevent file conflicts between parallel processes
        self.review_dir = Path("sourced_images/review") / self.batch_id
        self.review_dir.mkdir(parents=True, exist_ok=True)
        self.file_manager = FileManager()

    def generate_character_page(
        self,
        character: Character,
        candidates: List[tuple],
        filtered: List[tuple],
        char_index: int,
        total_chars: int,
        all_characters: List[Character]
    ) -> Path:
        """Generate review page for one character."""

        # Copy images to review directory
        review_images = []
        for idx, (image_info, filepath) in enumerate(filtered, 1):
            new_filename = f"{character.id}_{idx}.jpg"
            new_path = self.review_dir / new_filename
            shutil.copy2(filepath, new_path)
            review_images.append((idx, image_info, new_filename))

        html_file = self.review_dir / f"{character.id}_review.html"

        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Select Image for {character.name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1600px;
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
        .info {{
            color: #666;
            line-height: 1.8;
            margin: 15px 0;
        }}
        .stats {{
            background: #2196F3;
            color: white;
            padding: 10px 20px;
            border-radius: 4px;
            display: inline-block;
            margin: 10px 5px;
        }}
        .gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 25px;
            margin: 30px 0;
        }}
        .image-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        .image-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        .image-number {{
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            background: #e8f5e9;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 15px auto;
        }}
        .image-card img {{
            width: 100%;
            height: auto;
            border-radius: 4px;
            display: block;
            margin: 15px 0;
            cursor: pointer;
        }}
        .image-card.selected {{
            border: 4px solid #4CAF50;
            box-shadow: 0 0 20px rgba(76, 175, 80, 0.5);
        }}
        .image-card.selected .image-number {{
            background: #4CAF50;
            color: white;
            animation: pulse 1s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
        }}
        .image-info {{
            font-size: 14px;
            color: #666;
            line-height: 1.6;
            margin: 10px 0;
        }}
        .image-title {{
            font-size: 12px;
            color: #999;
            word-wrap: break-word;
            margin-top: 10px;
            font-style: italic;
        }}
        .selection-box {{
            background: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 8px;
            padding: 25px;
            margin: 30px 0;
            text-align: center;
        }}
        .selection-box h2 {{
            color: #856404;
            margin-top: 0;
        }}
        .selection-input {{
            font-size: 48px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            padding: 20px;
            border: 3px solid #4CAF50;
            border-radius: 8px;
            width: 150px;
            margin: 20px auto;
            display: block;
        }}
        .nav-buttons {{
            display: flex;
            justify-content: space-between;
            margin: 20px 0;
        }}
        .button {{
            padding: 15px 30px;
            font-size: 18px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: background 0.2s;
        }}
        .button-primary {{
            background: #4CAF50;
            color: white;
        }}
        .button-primary:hover {{
            background: #45a049;
        }}
        .button-secondary {{
            background: #2196F3;
            color: white;
        }}
        .button-secondary:hover {{
            background: #0b7dda;
        }}
        .button-skip {{
            background: #f44336;
            color: white;
        }}
        .button-skip:hover {{
            background: #da190b;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div style="background: #4CAF50; color: white; padding: 5px 15px; border-radius: 4px; display: inline-block; font-size: 12px; font-weight: bold; margin-bottom: 10px;">
            📦 {self.batch_id}
        </div>
        <h1>[{character.type}] {character.name}</h1>
        <div class="progress">
            <div class="progress-bar" style="width: {(char_index / total_chars * 100):.1f}%">
                Character {char_index} / {total_chars}
            </div>
        </div>
        <div class="info">
            {"<strong>First names:</strong> " + character.first_names + "<br>" if character.first_names else ""}
            {"<strong>Dates:</strong> " + (character.birth_date or "?") + " - " + (character.death_date or "?") + "<br>" if character.birth_date or character.death_date else ""}
            {"<strong>Bio:</strong> " + (character.biography[:300] + "..." if character.biography and len(character.biography) > 300 else character.biography or "")}
        </div>
        <div>
            <span class="stats">📦 Downloaded: {len(candidates)}</span>
            <span class="stats">✅ After filtering: {len(filtered)}</span>
        </div>
    </div>

    <h2 style="text-align: center; color: #333;">Review the Images Below</h2>
    <p style="text-align: center; color: #666; font-size: 18px;">Each image is numbered. Note which number you prefer.</p>

    <div class="gallery">
"""

        for idx, image_info, filename in review_images:
            html += f"""
        <div class="image-card">
            <div class="image-number">{idx}</div>
            <img src="{filename}" alt="Option {idx}" onclick="document.getElementById('selection').value={idx}">
            <div class="image-info">
                <strong>📐 Size:</strong> {image_info.width} × {image_info.height} px<br>
                <strong>📊 Aspect Ratio:</strong> {image_info.aspect_ratio:.3f}<br>
                <strong>⭐ Quality Score:</strong> {image_info.score:.3f}
            </div>
            <div class="image-title">
                {image_info.title[:120]}{"..." if len(image_info.title) > 120 else ""}
            </div>
        </div>
"""

        html += f"""
    </div>

    <div class="selection-box">
        <h2>📝 Your Selection</h2>
        <p style="font-size: 18px; color: #666;">
            Type the number of your selected image, or type 0 to skip this character:
        </p>
        <input type="number" id="selection" class="selection-input" min="0" max="{len(review_images)}"
               placeholder="?" autofocus>
        <p style="margin-top: 20px; color: #856404;">
            <strong>Note:</strong> Remember this number! You'll enter all selections after reviewing all characters.
        </p>
    </div>

    <div class="nav-buttons">
        <a href="index.html" class="button button-secondary">⬅️ Back to Index</a>
        <a href="{"submit.html" if char_index >= total_chars else str(all_characters[char_index].id) + "_review.html"}"
           class="button button-primary">
            {("✅ Done - Submit Selections" if char_index >= total_chars else f"Next: {all_characters[char_index].name} ➡️")}
        </a>
    </div>

    <script>
        const CHARACTER_ID = '{character.id}';
        const BATCH_ID = '{self.batch_id}';
        const STORAGE_KEY = BATCH_ID + '_selection_' + CHARACTER_ID;

        // Load saved selection on page load
        function loadSavedSelection() {{
            const saved = localStorage.getItem(STORAGE_KEY);
            if (saved !== null) {{
                const savedNum = parseInt(saved);
                document.getElementById('selection').value = savedNum;
                if (savedNum > 0) {{
                    // Highlight the selected image card
                    const cards = document.querySelectorAll('.image-card');
                    if (cards[savedNum - 1]) {{
                        cards[savedNum - 1].classList.add('selected');
                    }}
                }}
            }}
        }}

        // Save selection to localStorage
        function saveSelection(value) {{
            localStorage.setItem(STORAGE_KEY, value);
        }}

        // Allow clicking images to select
        document.querySelectorAll('.image-card img').forEach((img, index) => {{
            img.style.cursor = 'pointer';
            img.addEventListener('click', function() {{
                const selectedValue = index + 1;
                document.getElementById('selection').value = selectedValue;

                // Save to localStorage
                saveSelection(selectedValue);

                // Remove 'selected' class from all cards
                document.querySelectorAll('.image-card').forEach(card => {{
                    card.classList.remove('selected');
                }});

                // Add 'selected' class to clicked card
                this.parentElement.classList.add('selected');

                // Flash the selection box
                const box = document.querySelector('.selection-box');
                box.style.background = '#d4edda';
                box.style.borderColor = '#28a745';
                setTimeout(() => {{
                    box.style.background = '#fff3cd';
                    box.style.borderColor = '#ffc107';
                }}, 500);
            }});
        }});

        // Save selection when input changes
        document.getElementById('selection').addEventListener('change', function() {{
            saveSelection(this.value || '0');

            // Update visual selection
            const value = parseInt(this.value);
            document.querySelectorAll('.image-card').forEach(card => {{
                card.classList.remove('selected');
            }});
            if (value > 0) {{
                const cards = document.querySelectorAll('.image-card');
                if (cards[value - 1]) {{
                    cards[value - 1].classList.add('selected');
                }}
            }}
        }});

        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {{
            if (e.key >= '0' && e.key <= '9') {{
                document.getElementById('selection').value = e.key;
                saveSelection(e.key);

                // Update visual selection
                const value = parseInt(e.key);
                document.querySelectorAll('.image-card').forEach(card => {{
                    card.classList.remove('selected');
                }});
                if (value > 0 && value <= {len(review_images)}) {{
                    const cards = document.querySelectorAll('.image-card');
                    if (cards[value - 1]) {{
                        cards[value - 1].classList.add('selected');
                    }}
                }}
            }}
        }});

        // Load saved selection on page load
        loadSavedSelection();
    </script>
</body>
</html>
"""

        with open(html_file, 'w') as f:
            f.write(html)

        return html_file

    def generate_index(self, characters: List[Character], processed_count: int):
        """Generate index page."""
        index_file = self.review_dir / "index.html"

        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Image Selection Review - {processed_count} Characters</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            margin: 0 0 15px 0;
        }}
        .instructions {{
            background: #e3f2fd;
            border-left: 4px solid #2196F3;
            padding: 20px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .character-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
        }}
        .character-card {{
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        .character-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        .character-card h3 {{
            margin: 0 0 10px 0;
            color: #333;
        }}
        .character-card a {{
            color: #2196F3;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
        }}
        .character-card a:hover {{
            text-decoration: underline;
        }}
        .character-info {{
            color: #666;
            font-size: 14px;
            margin-top: 10px;
            line-height: 1.6;
        }}
        .character-number {{
            background: #4CAF50;
            color: white;
            border-radius: 50%;
            width: 35px;
            height: 35px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin-right: 10px;
        }}
        .character-card.has-selection {{
            border-left: 5px solid #4CAF50;
        }}
        .character-card.has-selection .character-number {{
            background: #4CAF50;
        }}
        .selection-status {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            margin-top: 8px;
        }}
        .selection-status.selected {{
            background: #d4edda;
            color: #155724;
        }}
        .selection-status.skipped {{
            background: #f8d7da;
            color: #721c24;
        }}
        .button-primary {{
            padding: 15px 30px;
            font-size: 18px;
            background: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            display: inline-block;
            transition: background 0.2s;
        }}
        .button-primary:hover {{
            background: #45a049;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎨 Image Selection Review</h1>
        <p style="font-size: 18px; color: #666; margin: 10px 0;">
            Review {processed_count} characters and select the best image for each.
        </p>
        <div style="background: #4CAF50; color: white; padding: 10px 20px; border-radius: 4px; display: inline-block; margin-top: 10px; font-weight: bold;">
            📦 Batch: {self.batch_id}
        </div>

        <div class="instructions">
            <h3 style="margin-top: 0;">📋 How to Use:</h3>
            <ol style="line-height: 1.8;">
                <li>Click on each character below to view their candidate images</li>
                <li>Review all the images and note which number you prefer (or 0 to skip)</li>
                <li>After reviewing all characters, you'll enter your selections</li>
                <li>The selected images will be automatically saved</li>
            </ol>
        </div>
    </div>

    <h2>Characters to Review</h2>
    <div class="character-grid">
"""

        for idx in range(processed_count):
            character = characters[idx]
            review_file = f"{character.id}_review.html"
            html += f"""
        <div class="character-card" data-char-id="{character.id}">
            <span class="character-number">{idx + 1}</span>
            <a href="{review_file}">{character.name}</a>
            <div class="character-info">
                <strong>Category:</strong> {character.type}<br>
                <strong>Dates:</strong> {character.birth_date or "?"} - {character.death_date or "?"}
            </div>
            <span class="selection-status" style="display: none;"></span>
        </div>
"""

        html += """
    </div>

    <div style="background: white; padding: 30px; margin-top: 30px; border-radius: 8px; text-align: center;">
        <h2>✅ Ready to Submit Your Selections?</h2>
        <p style="color: #666; font-size: 18px; margin: 20px 0;">
            After reviewing all characters, click the button below to submit your selections.
        </p>
        <a href="submit.html" class="button button-primary" style="padding: 15px 30px; font-size: 18px; background: #4CAF50; color: white; text-decoration: none; border: none; border-radius: 4px; display: inline-block; cursor: pointer;">
            Submit Selections
        </a>
    </div>

    <script>
        const BATCH_ID = '{self.batch_id}';

        // Check localStorage and update status indicators
        function updateStatusIndicators() {{
            document.querySelectorAll('.character-card').forEach(card => {{
                const charId = card.getAttribute('data-char-id');
                const statusSpan = card.querySelector('.selection-status');

                try {{
                    const storageKey = BATCH_ID + '_selection_' + charId;
                    const saved = localStorage.getItem(storageKey);
                    if (saved !== null) {{
                        const value = parseInt(saved);
                        card.classList.add('has-selection');
                        statusSpan.style.display = 'inline-block';

                        if (value === 0) {{
                            statusSpan.textContent = 'Skipped';
                            statusSpan.classList.add('skipped');
                        }} else {{
                            statusSpan.textContent = 'Selected: #' + value;
                            statusSpan.classList.add('selected');
                        }}
                    }}
                }} catch (e) {{
                    // localStorage may not work with file:// protocol
                    console.log('Could not access localStorage:', e);
                }}
            }});
        }}

        // Try to update status indicators on page load
        try {{
            updateStatusIndicators();
        }} catch (e) {{
            console.log('Status indicators disabled:', e);
        }}
    </script>
</body>
</html>
"""

        with open(index_file, 'w') as f:
            f.write(html)

    def process_batch(self, characters: List[Character], batch_size: int = 5, start_idx: int = 0):
        """Process a batch of characters."""
        print(f"\nGenerating review pages for {batch_size} characters starting from #{start_idx + 1}...")

        # Slice to the batch we want
        batch_characters = characters[start_idx:start_idx + batch_size]
        actual_count = len(batch_characters)

        for idx in range(actual_count):
            character = batch_characters[idx]
            print(f"\n[{idx + 1}/{actual_count}] {character.name}")

            # Download candidates
            candidates = self.selector.download_candidates(character, max_candidates=15)
            if not candidates:
                print(f"  ⚠️  No candidates - skipping")
                continue

            # Filter
            filtered = self.selector.filter_by_similarity(character, candidates)
            if not filtered:
                print(f"  ⚠️  All filtered out - using all candidates")
                filtered = candidates

            # Generate page
            html_file = self.generate_character_page(
                character, candidates, filtered, idx + 1, actual_count, batch_characters
            )
            print(f"  ✅ Page created: {html_file.name}")

        # Generate index
        self.generate_index(batch_characters, actual_count)

        # Generate submit page
        self.generate_submit_page(batch_characters)

        print(f"\n{'='*80}")
        print(f"✅ Review pages ready!")
        print(f"{'='*80}")
        print(f"\n📂 Open in browser: {self.review_dir.absolute() / 'index.html'}")
        print(f"\n{'='*80}\n")

    def generate_submit_page(self, characters: List[Character]):
        """Generate submission page for entering selections."""
        submit_file = self.review_dir / "submit.html"

        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Submit Your Selections</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .header h1 {{
            color: #4CAF50;
            margin: 0 0 15px 0;
        }}
        .instructions {{
            background: #e3f2fd;
            border-left: 4px solid #2196F3;
            padding: 20px;
            margin: 20px 0;
            border-radius: 4px;
            line-height: 1.8;
        }}
        .selection-form {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .character-input {{
            margin: 20px 0;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 4px;
            border-left: 4px solid #4CAF50;
        }}
        .character-input label {{
            display: block;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
            font-size: 18px;
        }}
        .character-input input {{
            width: 100px;
            padding: 12px;
            font-size: 24px;
            text-align: center;
            border: 2px solid #4CAF50;
            border-radius: 4px;
            font-weight: bold;
        }}
        .button {{
            padding: 15px 30px;
            font-size: 18px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin: 10px 5px;
        }}
        .button-primary {{
            background: #4CAF50;
            color: white;
        }}
        .button-primary:hover {{
            background: #45a049;
        }}
        textarea {{
            width: 100%;
            height: 200px;
            padding: 15px;
            font-family: monospace;
            font-size: 14px;
            border: 2px solid #ddd;
            border-radius: 4px;
            margin-top: 15px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div style="background: #4CAF50; color: white; padding: 5px 15px; border-radius: 4px; display: inline-block; font-size: 12px; font-weight: bold; margin-bottom: 10px;">
            📦 {self.batch_id}
        </div>
        <h1>✅ Submit Your Selections</h1>
        <p style="color: #666; font-size: 18px;">
            Enter the image numbers you selected for each character
        </p>
    </div>

    <div class="instructions">
        <h3 style="margin-top: 0;">📋 Instructions:</h3>
        <ol>
            <li>Enter the number of the image you selected for each character</li>
            <li>Enter <strong>0</strong> to skip a character (no selection)</li>
            <li>After entering all selections, copy the text from the box below</li>
            <li>Paste it to me in the chat, and I'll save your selections!</li>
        </ol>
    </div>

    <div class="selection-form">
        <h2>Your Selections</h2>
"""

        for idx, character in enumerate(characters, 1):
            html += f"""
        <div class="character-input">
            <label for="char{idx}">{idx}. {character.name} [{character.type}]</label>
            <input type="number" id="char{idx}" min="0" max="15" placeholder="?"
                   data-char-id="{character.id}" data-char-name="{character.name}"
                   oninput="updateOutput()" onchange="updateOutput()">
            <a href="{character.id}_review.html" style="margin-left: 15px; color: #2196F3;">Review images</a>
        </div>
"""

        html += f"""
        <h3 style="margin-top: 30px;">📋 Copy this text and send it to me:</h3>
        <textarea id="output" readonly placeholder="Enter your selections above, then copy this text..."></textarea>

        <div style="text-align: center; margin-top: 20px;">
            <button class="button button-primary" onclick="copyToClipboard()">
                📋 Copy to Clipboard
            </button>
        </div>
    </div>

    <script>
        const BATCH_ID = '{self.batch_id}';

        // Update the output textarea with current selections
        function updateOutput() {{
            const selections = [];
            const inputs = document.querySelectorAll('input[type="number"]');

            inputs.forEach(input => {{
                const value = input.value;
                const name = input.getAttribute('data-char-name');
                if (value && value !== '') {{
                    selections.push(name + ': ' + value);
                }}
            }});

            document.getElementById('output').value = selections.join('\\n');
        }}

        function copyToClipboard() {{
            const textarea = document.getElementById('output');
            textarea.select();
            document.execCommand('copy');
            alert('Copied to clipboard! Paste this in the chat.');
        }}

        // Load selections from localStorage
        function loadSelectionsFromStorage() {{
            const inputs = document.querySelectorAll('input[type="number"]');
            let loaded = 0;

            inputs.forEach(input => {{
                const charId = input.getAttribute('data-char-id');
                try {{
                    const storageKey = BATCH_ID + '_selection_' + charId;
                    const saved = localStorage.getItem(storageKey);
                    if (saved !== null && saved !== 'null' && saved !== '') {{
                        input.value = saved;
                        loaded++;
                        console.log('Loaded ' + charId + ': ' + saved);
                    }}
                }} catch (e) {{
                    console.log('Could not read localStorage for ' + charId, e);
                }}
            }});

            console.log('Loaded ' + loaded + ' selections from localStorage');
            if (loaded === 0) {{
                console.log('No selections found - localStorage may not work with file:// protocol');
                console.log('Please manually enter your selections');
            }}
            updateOutput();
        }}

        // Keyboard navigation - Enter moves to next field
        document.addEventListener('DOMContentLoaded', function() {{
            const inputs = document.querySelectorAll('input[type="number"]');
            inputs.forEach((input, index) => {{
                input.addEventListener('keydown', (e) => {{
                    if (e.key === 'Enter' && index < inputs.length - 1) {{
                        inputs[index + 1].focus();
                    }}
                }});
            }});

            // Try to load selections from localStorage
            loadSelectionsFromStorage();
        }});
    </script>
</body>
</html>
"""

        with open(submit_file, 'w') as f:
            f.write(html)
