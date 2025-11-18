# Millennium Card Producer

A CLI application to generate printable PDF cards for Millennium game characters with data from Supabase.

## Features

- **Data Integration**: Fetches character and connection data from Supabase
- **Smart Denormalization**: Replaces character IDs with names in connections
- **PDF Generation**: Creates printable cards with front and back layouts
- **Category Color Coding**: Each character category has its own color scheme
- **Multiple Print Modes**: Generate all cards or preview a single card
- **Image Caching**: Downloads character portraits once and caches them locally for faster subsequent generations

## Card Layout

Cards are designed based on the `Sample_layout.jpeg` specifications:

### Front
- Portrait image
- Character name in colored banner
- Category-based color scheme

### Back
- Character name and dates
- Category and biography
- Connections table with color-coded categories
- Card ID in top right corner

## Category Colors

- **R** (Royalty): Red
- **S** (Statesman): Orange
- **P** (Philosopher): Yellow
- **M** (Mathematical Scientist): Green
- **N** (Natural Scientist): Turquoise
- **A** (Artist): Blue
- **B** (Builders and Engineers): Indigo
- **C** (Composer): Violet
- **D** (Dramatist): Pink
- **T** (Towns and cities): Brown

## Setup

### Prerequisites

- Python 3.8 or higher
- Supabase account with character and connection tables

### Installation

1. Clone the repository
2. Create a `.env` file with your Supabase credentials:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```
3. Run the setup script:
   ```bash
   ./setup.sh
   ```

### Manual Setup

If you prefer manual setup:

```bash
# Create virtual environment
python3 -m venv millennium_virtual_environment

# Activate environment
source millennium_virtual_environment/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Activate the virtual environment first:

```bash
source millennium_virtual_environment/bin/activate
```

### Generate All Cards

Generate PDF with all character cards:

```bash
python src/main.py generate-all
```

Options:
- `-o, --output`: Specify output file path (default: `millennium_cards.pdf`)
- `--fronts-only`: Generate only card fronts (no backs)

Example:
```bash
python src/main.py generate-all -o my_cards.pdf
python src/main.py generate-all --fronts-only
```

### Generate Single Card Preview

Preview a single character card (front and back side by side):

```bash
python src/main.py generate-single <character_name>
```

The command accepts character names (case-insensitive) and provides helpful suggestions for partial matches.

Examples:
```bash
# Generate card for Washington
python src/main.py generate-single WASHINGTON -o washington.pdf

# Case-insensitive search
python src/main.py generate-single newton -o newton.pdf

# Partial match shows suggestions
python src/main.py generate-single "da"
# Output: Did you mean: ADAM, DAGUERRE, DALI, DALTON, DANTE?
```

### List All Characters

View all characters in the database:

```bash
python src/main.py list-characters
```

The list command supports sorting by multiple columns:

Options:
- `-s, --sort-by`: Primary sort field (choices: id, name, category, birth_date, death_date, connections)
- `-s2, --sort-by-2`: Secondary sort field (optional)
- `-r, --reverse`: Reverse sort order (descending)

Examples:
```bash
# Sort by category, then by name
python src/main.py list-characters -s category -s2 name

# Sort by number of connections (highest first)
python src/main.py list-characters -s connections -r

# Sort by birth date
python src/main.py list-characters -s birth_date

# Sort by name only
python src/main.py list-characters -s name
```

## Project Structure

```
.
├── src/
│   ├── main.py              # CLI interface
│   ├── cards.py             # PDF generation
│   ├── card.py              # Card layout definitions
│   ├── supabase_client.py   # Supabase integration
│   └── types/
│       └── supabase_types.py # Data models
├── requirements.txt          # Python dependencies
├── setup.sh                  # Setup script
├── Sample_layout.jpeg        # Card design reference
└── README.md                 # This file
```

## Database Schema

### Character Table

- `id`: UUID string (primary key)
- `name`: string (used for CLI identification)
- `first_names`: string
- `birth_date`: string
- `death_date`: string
- `biography`: string
- `type`: string (category code: R, S, P, M, N, A, B, C, D, T)
- `link`: string
- `image_link`: string

### Connection Table

- `id`: UUID string (primary key)
- `char1_id`: UUID string (foreign key to character)
- `char2_id`: UUID string (foreign key to character)
- `value`: integer (connection strength)
- `why`: string (connection description)
- `why_short`: string (short connection description)

**Note**: While UUIDs are used internally for data integrity, the CLI interface uses character names for user-friendly interaction.

## Image Management

### Image Cache

Character portrait images are automatically cached in the `image_cache/` directory at the project root. This significantly speeds up subsequent card generations.

#### View Cache Statistics

```bash
python manage_cache.py stats
```

This shows:
- Number of cached images
- File sizes
- Total cache size

#### Clear Cache

To remove all cached images (they will be re-downloaded on next use):

```bash
python manage_cache.py clear
```

**Note**: The cache directory is automatically created and excluded from git.

### Uploading Images to Supabase Storage

The project includes a script to upload changed images and metadata from `sourced_images/wikimedia/by_character_id/` to the Supabase `character_images` storage bucket. Files are only uploaded if they are newer than the version already in storage or don't exist yet.

#### Basic Usage

```bash
# Activate virtual environment first
source millennium_virtual_environment/bin/activate

# Check what needs updating (dry run - no upload)
python3 upload_changed_wikimedia_images.py --dry-run

# Upload all changed files (interactive - asks for confirmation)
python3 upload_changed_wikimedia_images.py

# Upload all changed files (auto-confirm - no prompt)
python3 upload_changed_wikimedia_images.py --yes
```

#### Upload Specific File Types

```bash
# Upload only JSON metadata files
python3 upload_changed_wikimedia_images.py --json-only --yes

# Upload only JPG image files
python3 upload_changed_wikimedia_images.py --jpg-only --yes
```

#### Upload Specific Files by Pattern

Use glob patterns to upload specific files:

```bash
# Upload all files for a specific character (by ID)
python3 upload_changed_wikimedia_images.py --files "76_M_EINSTEIN*" --yes

# Upload all files starting with "1_"
python3 upload_changed_wikimedia_images.py --files "1_*" --yes

# Upload all files containing "EINSTEIN"
python3 upload_changed_wikimedia_images.py --files "*EINSTEIN*" --yes

# Upload specific metadata file
python3 upload_changed_wikimedia_images.py --files "203_R_PHILIP_AUGUST.json" --yes
```

#### Command Options

- `--yes`, `-y`: Auto-confirm upload without prompting
- `--dry-run`: Check which files need updating without uploading
- `--json-only`: Only upload JSON metadata files
- `--jpg-only`: Only upload JPG image files
- `--files PATTERN`, `-f PATTERN`: Upload only files matching glob pattern

#### How It Works

The script compares local file modification timestamps with remote storage timestamps:
- Files newer than the remote version → uploaded
- Files that don't exist remotely → uploaded
- Files older than or same age as remote → skipped

**Note**: Requires `SUPABASE_SERVICE_KEY` in your `.env` file for admin access to storage.

## Development

The project follows a modular architecture:

1. **Data Layer** (`supabase_client.py`): Handles all database interactions
2. **Model Layer** (`supabase_types.py`): Defines data structures
3. **View Layer** (`card.py`): Renders card layouts with image caching
4. **Generation Layer** (`cards.py`): Creates PDF documents
5. **Interface Layer** (`main.py`): CLI commands

## Troubleshooting

### Import Errors

Make sure the virtual environment is activated:
```bash
source millennium_virtual_environment/bin/activate
```

### Supabase Connection Errors

Verify your `.env` file contains valid credentials:
```bash
cat .env
```

### Image Download Failures

Some character images may fail to download due to network issues or invalid URLs. The application will continue with a warning message.

## License

This project is for the Millennium card game.
