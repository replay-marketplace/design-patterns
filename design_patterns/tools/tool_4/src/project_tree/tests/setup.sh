#!/bin/bash
# Make python env, install requirements, set PYTHONPATH in venv activation

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements if they exist
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Add PYTHONPATH to venv activation script
VENV_ACTIVATE="venv/bin/activate"
PARENT_DIR="$(cd .. && pwd)"

# Check if PYTHONPATH is already set in activate script
if ! grep -q "export PYTHONPATH.*project_tree" "$VENV_ACTIVATE"; then
    echo "" >> "$VENV_ACTIVATE"
    echo "# Set PYTHONPATH for project_tree module" >> "$VENV_ACTIVATE"
    echo "export PYTHONPATH=\"\${PYTHONPATH}:$PARENT_DIR\"" >> "$VENV_ACTIVATE"
fi

echo "Setup complete! Activate the virtual environment with: source venv/bin/activate"


