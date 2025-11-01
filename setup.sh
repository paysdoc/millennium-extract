#!/bin/bash
# Setup script for Millennium Card Producer

set -e  # Exit on error

echo "Setting up Millennium Card Producer..."

# Check if virtual environment already exists
if [ -d "millennium_virtual_environment" ]; then
    echo "Virtual environment already exists. Remove it first if you want to recreate it."
    echo "Run: rm -r millennium_virtual_environment"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Using Python $PYTHON_VERSION"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv millennium_virtual_environment

# Activate and install dependencies
echo "Installing dependencies..."
source millennium_virtual_environment/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt

echo ""
echo "Testing imports..."
python test_imports.py

echo ""
echo "✓ Setup complete!"
echo ""
echo "To activate the environment, run:"
echo "  source millennium_virtual_environment/bin/activate"
echo ""
echo "Then you can run the CLI:"
echo "  python src/main.py --help"
echo ""
echo "Quick commands:"
echo "  python src/main.py list-characters"
echo "  python src/main.py generate-all"
