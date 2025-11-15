# Millennium Extract - Batch Image Download Process Documentation

## Overview
This document describes the complete workflow for downloading, reviewing, and selecting historical portrait images for Millennium characters in batches.

---

## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Key Scripts and Their Roles](#key-scripts-and-their-roles)
3. [File Storage Structure](#file-storage-structure)
4. [Complete Workflow](#complete-workflow)
5. [User Selection Process](#user-selection-process)
6. [Troubleshooting and Recovery](#troubleshooting-and-recovery)

---

## Architecture Overview

The system uses a multi-stage pipeline:
1. **Download Phase**: Fetch candidate images from Wikimedia Commons
2. **Review Phase**: Generate HTML pages for browser-based selection
3. **Selection Phase**: User chooses best images via web interface
4. **Storage Phase**: Save selected images to final directory

---

## Key Scripts and Their Roles

### Main Download Scripts

#### 1. `src/download_images/web_main.py`
**Purpose**: Main batch download orchestrator

**Usage**:
```bash
python3 -m src.download_images.web_main [CATEGORY] [BATCH_SIZE] [START_IDX]
```

**Examples**:
```bash
# Download first 5 characters from Inventors category
python3 -m src.download_images.web_main I 5 0

# Download next 5 characters (characters 6-10)
python3 -m src.download_images.web_main I 5 5

# Download batch 3 of Mathematicians (characters 11-15)
python3 -m src.download_images.web_main M 5 10
```

**What it does**:
1. Connects to Supabase database
2. Fetches characters filtered by category
3. Generates search queries for each character (10 variations)
4. Downloads 10-15 candidate images per character from Wikimedia Commons
5. Copies downloaded images to review directory
6. Generates HTML review pages
7. Starts HTTP server for browser review
8. Records port information for cleanup

**Output**:
- Review pages in `sourced_images/review/[CATEGORY]_batch[N]/`
- HTTP server URL (e.g., `http://localhost:8004/I_batch1/index.html`)

---

#### 2. Custom Search Scripts (e.g., `retry_i_batch1.py`)
**Purpose**: Retry downloads with expanded custom search queries

**When to use**: When default queries return poor results or no images

**Process**:
1. Define custom queries in `src/download_images/custom_searches.py`
2. Create retry script (or use existing template)
3. Run with expanded query set (20-30 queries per character)

**Custom Query Examples**:
```python
"AGRICOLA": [
    "Georgius Agricola mineralogist portrait",
    "Georg Bauer Agricola portrait",
    "Georgius Agricola De Re Metallica portrait",
    # ... 20 more targeted queries
]
```

---

### Supporting Scripts

#### 3. `src/download_images/save_selections.py`
**Purpose**: Save user-selected images to final directory

**Usage**:
```bash
python3 -m src.download_images.save_selections "CHARACTER1: 3
CHARACTER2: 5"
```

**Manual Alternative** (more reliable):
```python
import shutil
from pathlib import Path

# Copy from review directory
source = Path('sourced_images/review/I_batch1/16_3.jpg')
dest = Path('sourced_images/wikimedia/by_character_id/16_I_ARKWRIGHT_1.jpg')
shutil.copy2(source, dest)
```

---

#### 4. `src/download_images/cleanup_servers.py`
**Purpose**: Stop all running HTTP servers

**Usage**:
```bash
python3 -m src.download_images.cleanup_servers
```

**Port Management**:
- Ports tracked in `sourced_images/review/.ports.json`
- Automatically finds available ports (8000-8020)
- Prevents port conflicts between batches

---

#### 5. `src/download_images/port_manager.py`
**Purpose**: Manage HTTP server ports across multiple batches

**Functions**:
- `find_available_port()`: Finds next free port
- `register_port()`: Records port assignment
- `cleanup_port()`: Releases port after server stops

---

#### 6. `src/download_images/generate_missing_metadata.py`
**Purpose**: Create JSON metadata files for images and clean up orphaned JSON files

**Usage**:
```bash
# Dry run (preview what would be created/removed)
python3 -m src.download_images.generate_missing_metadata --dry-run

# Generate metadata and cleanup
python3 -m src.download_images.generate_missing_metadata
```

**What it does**:
1. Scans `by_character_id/` for images without corresponding `.json` files
2. Parses character info from filename (ID, category, name)
3. Fetches character details from Supabase
4. Reads image dimensions using PIL/Pillow
5. Calculates quality scores using `ImageScorer`
6. Creates comprehensive metadata JSON files
7. **Removes orphaned JSON files** (JSON files without corresponding images)

**Generated Metadata**:
```json
{
  "character_name": "ARKWRIGHT",
  "character_id": 16,
  "category": "I",
  "first_names": "Sir Richard",
  "biography": "English inventor & industrialist,",
  "birth_date": "1732",
  "death_date": "1792 (60yrs)",
  "width": 3306,
  "height": 4096,
  "aspect_ratio": 1.239,
  "quality_score": 0.896,
  "ratio_score": 0.851,
  "resolution_score": 1.0,
  "meets_strict_requirements": true,
  "source": "metadata_generation",
  "download_timestamp": "2025-11-11T23:11:16.276877",
  "rank": 1
}
```

**When to use**:
- After manually copying images
- After batch imports from external sources
- To regenerate metadata with updated scoring logic
- To ensure all images have complete metadata
- To clean up orphaned JSON files after deleting images
- As part of regular maintenance to keep directory clean

---

## File Storage Structure

```
sourced_images/
├── reference_images/          # Original reference images from database
│   └── AGRICOLA.jpg
│
├── temp_candidates/           # TEMPORARY download staging area
│   ├── 11_I_AGRICOLA_temp1.jpg      # Gets cleared after each character
│   ├── 11_I_AGRICOLA_temp2.jpg      # NOT persistent
│   └── ...
│
├── review/                    # TEMPORARY review interface files
│   ├── .ports.json                   # Port tracking for HTTP servers
│   ├── state.json                    # Session state (optional)
│   │
│   ├── I_batch1/                     # Batch-specific directory
│   │   ├── index.html                # Main navigation page
│   │   ├── 11_review.html            # Character review page
│   │   ├── 11_1.jpg                  # Candidate image #1
│   │   ├── 11_2.jpg                  # Candidate image #2
│   │   ├── 11_3.jpg                  # etc.
│   │   ├── 16_review.html
│   │   ├── 16_1.jpg
│   │   └── ...
│   │
│   ├── I_batch1_expanded/            # Expanded search results
│   │   └── [same structure]
│   │
│   └── M_batch1/                     # Another category batch
│       └── [same structure]
│
└── wikimedia/
    └── by_character_id/       # FINAL selected images (persistent)
        ├── 16_I_ARKWRIGHT_1.jpg      # Selected image
        ├── 16_I_ARKWRIGHT_1.json     # Metadata
        ├── 20_I_BABBAGE_1.jpg
        ├── 20_I_BABBAGE_1.json
        └── ...
```

### Storage Lifecycle

#### Temporary Files (Cleared Regularly)
- **`temp_candidates/`**: Cleared after each character is processed
- **`review/[BATCH]/`**: Can be deleted after selections are saved
  - Keep until category is complete for reference
  - Regenerate anytime by re-running download

#### Persistent Files (Keep Forever)
- **`reference_images/`**: Original images from database
- **`by_character_id/`**: Final selected images
  - Format: `{id}_{category}_{name}_1.jpg`
  - One image per character (rank 1)
  - Accompanied by `.json` metadata

---

## Complete Workflow

### Phase 1: Initial Setup

```bash
# Activate virtual environment
source millennium_virtual_environment/bin/activate

# Check category status
python3 -c "
from src.supabase_client import get_supabase_client
client = get_supabase_client()
response = client.table('character').select('type').execute()
# ... check completion status
"
```

---

### Phase 2: Batch Download

```bash
# Download batch 1 (characters 1-5) for Inventors
python3 -m src.download_images.web_main I 5 0
```

**What happens**:
1. Script connects to Supabase
2. Fetches 5 characters from category I (Inventors)
3. Generates batch ID: `I_batch1`
4. Creates directory: `sourced_images/review/I_batch1/`

**For each character**:
1. Builds 10 search query variations:
   - `{first_names} {name} {year} portrait`
   - `{first_names} {name} portrait`
   - `{first_names} {name} {category} portrait`
   - etc.

2. Searches Wikimedia Commons API
3. Downloads up to 15 candidate images to `temp_candidates/`
4. Copies all candidates to `review/I_batch1/`
   - Renames: `{char_id}_1.jpg`, `{char_id}_2.jpg`, etc.
5. Generates `{char_id}_review.html`
6. Clears `temp_candidates/`

**After all characters**:
8. Generates `index.html` with navigation
9. Finds available port (8000-8020)
10. Starts HTTP server: `python3 -m http.server {port}`
11. Registers port in `.ports.json`
12. Opens browser to review URL

**Output**:
```
================================================================================
🌐 HTTP Server Started
================================================================================
Port: 8004
PID: 72972

📂 Open in browser:
  http://localhost:8004/I_batch1/index.html
================================================================================
```

---

### Phase 3: User Review

**Browser Interface**:
- Navigate to `http://localhost:{port}/{batch_id}/index.html`
- See list of all characters in batch
- Click character name to see candidates

**Review Page Features**:
1. **Header**: Character info (name, dates, biography)
2. **Progress Bar**: Shows current character position
3. **Gallery**: Grid of candidate images
   - Large, zoomable images
   - Image metadata (dimensions, source)
   - Clickable for full size
4. **Selection**: Click image number to select
   - Browser localStorage saves selection
   - Green highlight marks selected image
   - Persists across page reloads

**Navigation**:
- "Next Character" button → moves to next review page
- "Previous Character" → goes back
- Index link → returns to main list

---

### Phase 4: Recording Selections

After reviewing all images, record your selections:

```bash
# Note which images you selected
# Format: CHARACTER_NAME: image_number
ARKWRIGHT: 3
BABBAGE: 3
```

**Manual Selection Save** (Recommended):
```python
import shutil
from pathlib import Path
import json
from datetime import datetime

selections = {
    'ARKWRIGHT': {'id': 16, 'image_num': 3, 'type': 'I'},
    'BABBAGE': {'id': 20, 'image_num': 3, 'type': 'I'}
}

review_dir = Path('sourced_images/review/I_batch1')
output_dir = Path('sourced_images/wikimedia/by_character_id')

for name, info in selections.items():
    source = review_dir / f"{info['id']}_{info['image_num']}.jpg"
    dest = output_dir / f"{info['id']}_{info['type']}_{name}_1.jpg"

    shutil.copy2(source, dest)

    # Save metadata
    metadata = {
        'character_name': name,
        'character_id': info['id'],
        'category': info['type'],
        'source': 'manual_selection',
        'selected_option': info['image_num'],
        'download_timestamp': datetime.now().isoformat(),
        'rank': 1
    }

    with open(dest.with_suffix('.json'), 'w') as f:
        json.dump(metadata, f, indent=2)
```

**Verification**:
```bash
# Check files were created
ls -lh sourced_images/wikimedia/by_character_id/*ARKWRIGHT*
ls -lh sourced_images/wikimedia/by_character_id/*BABBAGE*
```

---

### Phase 5: Expanded Searches (If Needed)

**When to use**: Images are unusable, wrong person, or no results

**Step 1**: Add custom queries to `custom_searches.py`:
```python
"ALHAZEN": [
    "Ibn al-Haytham portrait",
    "Alhazen Book of Optics portrait",
    "Ibn Haytham Islamic Golden Age portrait",
    # ... 20-30 targeted queries
]
```

**Step 2**: Create retry script:
```python
# retry_i_batch1.py
from src.download_images.custom_searches import get_custom_queries

# Monkey patch to use custom queries
def custom_build_queries(char):
    custom = get_custom_queries(char.name)
    if custom:
        return custom
    return original_build(char)

generator.selector.downloader.query_builder.build_queries = custom_build_queries
```

**Step 3**: Run expanded search:
```bash
python3 retry_i_batch1.py
```

**Result**: New review pages in `I_batch1_expanded/`

---

### Phase 6: Next Batch

```bash
# Continue with next 5 characters
python3 -m src.download_images.web_main I 5 5  # batch 2 (chars 6-10)
python3 -m src.download_images.web_main I 5 10 # batch 3 (chars 11-15)
python3 -m src.download_images.web_main I 5 15 # batch 4 (chars 16-20)
python3 -m src.download_images.web_main I 5 20 # batch 5 (chars 21-25)
```

---

## User Selection Process

### Browser Interface Details

The HTML review pages use:
- **LocalStorage**: Saves selections in browser
  - Key: `selection_{batch_id}_{char_id}`
  - Value: Selected image number
  - Persists until cleared or different batch

- **Visual Feedback**:
  - Selected card: Green border + pulsing number
  - Hover: Card lifts up with shadow
  - Click anywhere on card: Toggles selection

- **Keyboard Shortcuts** (potential addition):
  - Number keys: Select image
  - Arrow keys: Navigate images
  - Enter: Confirm and move to next

### Selection States

```javascript
// LocalStorage structure
{
  "selection_I_batch1_11": "3",    // AGRICOLA chose image 3
  "selection_I_batch1_16": "1",    // ARKWRIGHT chose image 1
  "selection_I_batch1_20": "5",    // BABBAGE chose image 5
}
```

### Extracting Selections

**From Browser Console**:
```javascript
// Get all selections for current batch
Object.keys(localStorage)
  .filter(k => k.startsWith('selection_I_batch1'))
  .map(k => ({
    key: k,
    char_id: k.split('_')[3],
    selection: localStorage[k]
  }));
```

**Current Limitation**: No automatic export
- User must manually note selections
- Future: Add export button to download JSON

---

## Troubleshooting and Recovery

### Issue: No images found

**Causes**:
1. Character too obscure
2. Name variations not captured
3. No portrait exists

**Solutions**:
1. Check Wikipedia for alternative names
2. Add custom queries to `custom_searches.py`
3. Try different language searches (German, French, Italian)
4. Look for specific artworks (paintings, engravings)

**Example Fix**:
```python
# For AGRICOLA (Roman general instead of mineralogist)
"AGRICOLA": [
    "Georgius Agricola mineralogist",  # Not "Gnaeus Julius Agricola"
    "Georg Bauer Agricola",            # German name
    "De Re Metallica author portrait", # Known work
]
```

---


### Issue: Wrong person downloaded

**Examples**:
- AGRICOLA → Roman general (not mineralogist)
- BACON, ROGER → Francis Bacon (not Roger Bacon)

**Solution**: Add disambiguating terms
```python
"BACON, ROGER": [
    "Roger Bacon medieval",           # Not Francis
    "Roger Bacon 13th century",       # Time period
    "Roger Bacon Franciscan friar",   # Profession
]
```

---

### Issue: Server port in use

**Error**: `Address already in use`

**Solution**:
```bash
# List running servers
python3 -m src.download_images.cleanup_servers

# Or manually
lsof -ti:8004 | xargs kill
```

---

### Issue: Lost selections

**Recovery**:
```javascript
// In browser console
console.log(localStorage);  // View all saved selections

// Export to clipboard
copy(JSON.stringify(localStorage, null, 2));
```

---

### Issue: Need to re-download batch

**Safe to delete**:
```bash
rm -rf sourced_images/review/I_batch1/
rm -rf sourced_images/temp_candidates/
```

**Re-run**:
```bash
python3 -m src.download_images.web_main I 5 0
```

---

## Best Practices

### 1. Batch Size
- **5 characters**: Good for starting out
- **10 characters**: Faster, but more to review at once
- **1 character**: For difficult cases with custom searches

### 2. Review Workflow
1. Quick pass: Mark obvious good/bad images
2. Second pass: Compare finalists side-by-side
3. Record selections immediately (don't trust memory)

### 3. Port Management
- Note the port number when server starts
- Use cleanup script between sessions
- Check `.ports.json` if confused

### 4. File Organization
- Keep review directories until category complete
- Back up `by_character_id/` regularly
- Delete `temp_candidates/` if disk space low

### 5. Custom Searches
- Research character on Wikipedia first
- Look for: Alternative names, titles, famous works
- Try different languages (especially German, French, Italian)
- Include time period in queries (e.g., "16th century")

---

## Completion Tracking

### Check Status
```python
from pathlib import Path

category = "I"
char_ids = [11, 16, 20, 23, ...]  # All IDs for category

complete = []
for char_id in char_ids:
    files = list(Path('sourced_images/wikimedia/by_character_id').glob(f'{char_id}_*.jpg'))
    if files:
        complete.append(char_id)

print(f"Complete: {len(complete)}/{len(char_ids)}")
```

### Progress Report
```bash
# Count files by category
ls sourced_images/wikimedia/by_character_id/ | grep "^[0-9]*_I_" | wc -l
```

---

## Future Improvements

### Planned Features
1. **Auto-export selections**: Button to download JSON
2. **Bulk save**: Process all selections at once
3. **Comparison view**: Side-by-side image comparison
4. **Undo/redo**: Revert selection changes
5. **Notes field**: Add comments about images
6. **Quality indicators**: Flag low-resolution images

### Technical Debt
1. Port manager needs better error handling
2. Temp file cleanup sometimes fails
3. Selection save script unreliable (use manual approach)
4. No progress tracking between sessions

---

## Summary

**Key Scripts**:
- `web_main.py`: Main batch downloader
- `custom_searches.py`: Expanded query definitions
- `save_selections.py`: Save final choices (or use manual Python)
- `cleanup_servers.py`: Stop HTTP servers

**Key Directories**:
- `temp_candidates/`: Temporary downloads (auto-cleared)
- `review/{batch}/`: HTML interface (temporary)
- `by_character_id/`: Final selections (persistent)

**Workflow**:
1. Run `web_main.py` with category and batch size
2. Review images in browser at `localhost:{port}/{batch}/index.html`
3. Click images to select
4. Note selections and save manually with Python script
5. Repeat for next batch

**Recovery**:
- Re-run downloads anytime (non-destructive)
- Selections saved in browser localStorage
- Custom searches for difficult characters
- Manual save process most reliable

---

*Last Updated: 2025-11-11*
