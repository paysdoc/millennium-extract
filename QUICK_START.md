# Quick Start Guide

## 1. Setup (One Time)

```bash
# Make setup script executable (if not already)
chmod +x setup.sh

# Run setup
./setup.sh
```

This will:
- Create a Python virtual environment
- Install all required dependencies

## 2. Activate Environment

**Every time you want to use the application**, activate the environment:

```bash
source millennium_virtual_environment/bin/activate
```

## 3. Generate Cards

### All Cards

```bash
python src/main.py generate-all
```

Output: `millennium_cards.pdf`

### Custom Output

```bash
python src/main.py generate-all -o my_cards.pdf
```

### Fronts Only

```bash
python src/main.py generate-all --fronts-only
```

## 4. List Characters

```bash
# List all characters
python src/main.py list-characters

# Sort by category, then name
python src/main.py list-characters -s category -s2 name

# Sort by connections (highest first)
python src/main.py list-characters -s connections -r
```

## 5. Preview Single Card

```bash
# List all characters first to find ID
python src/main.py list-characters

# Generate preview for character ID 5
python src/main.py generate-single 5
```

## Common Commands

```bash
# View all available commands
python src/main.py --help

# View command-specific help
python src/main.py list-characters --help
python src/main.py generate-all --help
```

## Troubleshooting

### "Module not found" Error

Make sure you activated the virtual environment:
```bash
source millennium_virtual_environment/bin/activate
```

You can also test if all imports work:
```bash
python test_imports.py
```

### Supabase Connection Error

Check your `.env` file:
```bash
cat .env
```

Should contain:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-key-here
```

### Need to Reinstall

```bash
rm -rf millennium_virtual_environment
./setup.sh
```

## That's It!

You're ready to generate your Millennium cards.
