# Millennium Card Producer - Project Summary

## Overview

This project implements a complete CLI application for generating printable PDF cards for the Millennium board game. The application fetches character data from Supabase, processes connections between characters, and creates beautifully formatted cards ready for printing.

## What Was Built

### Core Components

1. **Data Models** ([src/types/supabase_types.py](src/types/supabase_types.py))
   - `Character`: Represents game characters with biographical data
   - `Connection`: Represents relationships between characters
   - `DenormalizedConnection`: Connection with resolved character names
   - `CardData`: Complete card data ready for rendering

2. **Supabase Integration** ([src/supabase_client.py](src/supabase_client.py))
   - `get_supabase_client()`: Creates authenticated Supabase client
   - `fetch_all_characters()`: Retrieves all characters from database
   - `fetch_connections_for_character()`: Gets connections for a character
   - `denormalize_connections()`: Replaces character IDs with names
   - `fetch_all_card_data()`: Fetches complete data for all cards

3. **Card Layout** ([src/card.py](src/card.py))
   - Category color mapping (R=red, S=orange, P=yellow, etc.)
   - `draw_card_front()`: Renders card front with portrait and name
   - `draw_card_back()`: Renders card back with details and connections table
   - Image downloading and processing
   - ReportLab-based rendering

4. **PDF Generation** ([src/cards.py](src/cards.py))
   - `generate_cards_pdf()`: Creates multi-page PDF with all cards
   - `generate_single_card_pdf()`: Creates preview PDF for one card
   - 3x3 card layout per A4 page
   - Optimized for double-sided printing

5. **CLI Interface** ([src/main.py](src/main.py))
   - `generate-all`: Generate PDF with all character cards
   - `generate-single <id>`: Preview a single character card
   - `list-characters`: View all characters in database
   - Click-based command interface with options

### Supporting Files

- **[requirements.txt](requirements.txt)**: Python dependencies
  - supabase==2.3.4
  - reportlab==4.0.7
  - Pillow==10.1.0
  - click==8.1.7
  - python-dotenv==1.0.0

- **[setup.sh](setup.sh)**: Automated setup script
- **[README.md](README.md)**: Complete documentation
- **[.env.sample](.env.sample)**: Environment variable template
- **[.gitignore](.gitignore)**: Updated with Python patterns

## Card Design Specifications

Based on [Sample_layout.jpeg](Sample_layout.jpeg):

### Front
- Full-height portrait image
- Colored banner at bottom with character name
- Category-specific background color

### Back
- Beige header with name, dates, and category
- Biography section with bullet points
- Colored "CONNECTIONS" header
- Table with connections (value, category, name, description)
- Card ID in colored box (top right)
- Colored banner at bottom with name

### Category Colors
| Code | Category | Color |
|------|----------|-------|
| R | Royalty | Red |
| S | Statesman | Orange |
| P | Philosopher | Yellow |
| M | Mathematical Scientist | Green |
| N | Natural Scientist | Turquoise |
| A | Artist | Blue |
| B | Builders and Engineers | Indigo |
| C | Composer | Violet |
| D | Dramatist | Pink |
| T | Towns and cities | Brown |

## Data Flow

1. **Fetch**: Application connects to Supabase and fetches all characters
2. **Process**: For each character:
   - Fetch all connections (where char1_id or char2_id matches)
   - Denormalize connections by replacing IDs with character names
   - Create `CardData` object
3. **Render**: For each card:
   - Download character portrait image
   - Draw front: portrait + name banner
   - Draw back: details + connections table + name banner
4. **Generate**: Create PDF with 3x3 cards per page, optimized for printing

## Usage Instructions

### First Time Setup

```bash
# Run setup script
./setup.sh

# Or manually:
python3 -m venv millennium_virtual_environment
source millennium_virtual_environment/bin/activate
pip install -r requirements.txt
```

### Generate All Cards

```bash
source millennium_virtual_environment/bin/activate
python src/main.py generate-all -o output.pdf
```

### Preview Single Card

```bash
python src/main.py generate-single 1 -o preview.pdf
```

### List Characters

```bash
python src/main.py list-characters
```

## Technical Decisions

1. **ReportLab for PDF**: Industry-standard library with excellent control over layout
2. **Click for CLI**: Modern, user-friendly CLI framework with great documentation
3. **Dataclasses**: Type-safe, clean data models
4. **Modular Architecture**: Separation of concerns (data, rendering, generation, interface)
5. **3x3 Layout**: Optimal use of A4 paper for card size (63mm × 88mm)
6. **Double-Sided Printing**: Back pages mirror column order for alignment

## Next Steps (Optional Enhancements)

1. **Image Optimization**: Cache downloaded images to avoid re-downloading
2. **Batch Processing**: Process cards in batches for large datasets
3. **Custom Layouts**: Allow users to customize card dimensions
4. **Export Formats**: Support additional formats (PNG, SVG)
5. **Validation**: Add data validation for missing/invalid fields
6. **Progress Bar**: Show progress during PDF generation
7. **Error Recovery**: Better handling of failed image downloads

## Files Created

```
src/
├── __init__.py
├── main.py                 (CLI interface - 125 lines)
├── cards.py                (PDF generation - 90 lines)
├── card.py                 (Card layouts - 280 lines)
├── supabase_client.py      (Data fetching - 130 lines)
└── types/
    ├── __init__.py
    └── supabase_types.py   (Data models - 40 lines)

requirements.txt            (6 dependencies)
setup.sh                    (Setup automation)
README.md                   (Complete documentation)
.env.sample                 (Environment template)
PROJECT_SUMMARY.md          (This file)
```

**Total Lines of Code**: ~665 lines of Python

## Ready to Use!

The project is complete and ready for immediate use. Simply:

1. Run `./setup.sh` to set up the environment
2. Ensure your `.env` file has valid Supabase credentials
3. Run `python src/main.py generate-all` to generate all cards

The output will be a print-ready PDF file with all character cards!
