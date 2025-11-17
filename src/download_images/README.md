# Download Images Module

A refactored, SOLID-compliant module for downloading historical character images from Wikimedia Commons.

## Architecture

This module follows SOLID principles for maintainable, testable, and extensible code:

### Module Structure

```
src/download_images/
├── __init__.py                # Module exports
├── config.py                  # Configuration constants (SRP)
├── models.py                  # Data structures (SRP)
├── text_parser.py             # Text extraction utilities (SRP)
├── query_builder.py           # Search query generation (SRP, OCP)
├── image_scorer.py            # Image quality evaluation (SRP)
├── wikimedia_api.py           # API client (SRP, ISP)
├── file_manager.py            # File operations (SRP)
├── downloader.py              # Main orchestration (DIP)
├── preview.py                 # Image preview utility (SRP)
├── main.py                    # CLI entry point (SRP)
├── check_category_status.py   # Progress monitoring utility (SRP)
└── README.md                  # This file
```

## SOLID Principles Applied

### Single Responsibility Principle (SRP)
Each module has one clear responsibility:
- `config.py`: Configuration management
- `models.py`: Data structure definitions
- `text_parser.py`: Text parsing and extraction
- `query_builder.py`: Query generation
- `image_scorer.py`: Image quality evaluation
- `wikimedia_api.py`: API interactions
- `file_manager.py`: File I/O operations
- `preview.py`: Display functionality

### Open/Closed Principle (OCP)
- `query_builder.py` uses strategy pattern - easy to add new query strategies without modifying existing code
- New image scoring criteria can be added without changing existing scorers

### Liskov Substitution Principle (LSP)
- All strategy classes (`QueryStrategy` subclasses) can be substituted for each other
- Components can be swapped with compatible implementations

### Interface Segregation Principle (ISP)
- `WikimediaAPIClient` provides focused, minimal interface for API operations
- Each component exposes only methods relevant to its clients

### Dependency Inversion Principle (DIP)
- `CharacterImageDownloader` depends on abstractions (injected dependencies)
- Components can be mocked/replaced for testing
- Configuration is injected, not hard-coded

## Usage

### Download Images

```bash
# Download by category and batch (first 5 characters)
python3 -m src.download_images.web_main I 5 0

# Download specific category (next 5 characters)
python3 -m src.download_images.web_main R 5 5

# Download all characters in a category
python3 -m src.download_images.web_main S 10 0  # Scientists
python3 -m src.download_images.web_main A 5 0   # Artists

# Download specific characters by ID (comma-separated)
python3 -m src.download_images.web_main --ids 172,250,266,269,272,276

# Download specific characters by ID (space-separated)
python3 -m src.download_images.web_main --ids 172 250 266 269 272 276
```

### Check Download Progress

Check which categories have complete/incomplete image downloads:

```bash
python3 -m src.download_images.check_category_status
```

This script:
- Fetches all characters from the database grouped by category
- Checks which characters have images in `sourced_images/wikimedia/by_character_id/`
- Reports completion statistics per category
- Lists missing characters for incomplete categories
- Suggests next download commands

Example output:
```
Category                      Total    Complete   Missing    Progress
--------------------------------------------------------------------------------
✓ R - Royalty                 26       26         0          ██████████ 100.0%
○ I - Inventor                25       19         6          ███████░░░  76.0%
```

### Preview Downloaded Images

```bash
python3 -m src.download_images.preview
```

## Key Components

### QueryBuilder
Generates intelligent search queries using character data:
- Combines name, biography, dates for better accuracy
- Handles different character types (people vs. buildings)
- Uses strategy pattern for extensibility

### ImageScorer
Evaluates image quality based on:
- Aspect ratio (target: √2 for A4 portrait)
- Resolution (minimum: 2480px height)
- Weighted scoring system

### WikimediaAPIClient
Handles all Wikimedia Commons API interactions:
- Search with rate limiting
- Image metadata retrieval
- Automatic result scoring

### FileManager
Manages all file operations:
- Standardized filename generation
- Streaming downloads
- Metadata persistence

### CharacterImageDownloader
Orchestrates the complete download process:
- Dependency injection for flexibility
- Batch processing support
- Progress reporting

## Configuration

Edit `config.py` to customize:

```python
class ImageRequirements:
    MIN_HEIGHT = 2480              # Minimum image height
    TARGET_ASPECT_RATIO = √2       # Target aspect ratio

class DownloadConfig:
    MAX_ALTERNATIVES = 2           # Alt images per character
    OUTPUT_DIR = "sourced_images/wikimedia/by_character_id"
```

## Testing

The module is designed for testability with dependency injection:

```python
from src.download_images import CharacterImageDownloader
from src.download_images.query_builder import QueryBuilder

# Create components
query_builder = QueryBuilder()
downloader = CharacterImageDownloader(query_builder=query_builder)

# Use with test data
characters = [test_character]
downloader.download_batch(characters)
```

## Migration Notes

This module replaces:
- `download_images_improved.py` → `src/download_images/main.py`
- `preview_downloads.py` → `src/download_images/preview.py`

The refactored code maintains all original functionality while improving:
- Code organization and maintainability
- Testability through dependency injection
- Extensibility through SOLID principles
- Clarity through single-purpose modules

## Future Enhancements

Easy to add:
- New query strategies for different character types
- Alternative image sources beyond Wikimedia
- Custom scoring algorithms
- Parallel downloading
- Image processing pipeline
