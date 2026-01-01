#!/bin/bash

# Make python env, install requirements, set PYTHONPATH in venv activation

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Create virtual environment
python3 -m venv "$SCRIPT_DIR/venv"

# Activate virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install requirements if file exists and is not empty
if [ -s "$SCRIPT_DIR/requirements.txt" ]; then
    pip install -r "$SCRIPT_DIR/requirements.txt"
fi

# Add PYTHONPATH to venv activation script
echo "" >> "$SCRIPT_DIR/venv/bin/activate"
echo "# Set PYTHONPATH for project" >> "$SCRIPT_DIR/venv/bin/activate"
echo "export PYTHONPATH=\"$PROJECT_DIR:\$PYTHONPATH\"" >> "$SCRIPT_DIR/venv/bin/activate"

# Create replay directory for test results
mkdir -p "$PROJECT_DIR/replay"

echo "Setup complete. Activate the virtual environment with:"
echo "source $SCRIPT_DIR/venv/bin/activate"
