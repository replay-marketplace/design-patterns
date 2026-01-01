#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create virtual environment
python3 -m venv "$SCRIPT_DIR/venv"

# Activate virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r "$SCRIPT_DIR/requirements.txt"

# Set PYTHONPATH in venv activation script
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
echo "export PYTHONPATH=\"$PROJECT_ROOT:\$PYTHONPATH\"" >> "$SCRIPT_DIR/venv/bin/activate"

echo "Setup complete. Run 'bash run_tests.sh' to execute tests."
