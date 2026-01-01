#!/bin/bash
# Make python env, install requirements, set PYTHONPATH in venv activation

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Setting up test environment in $SCRIPT_DIR"

# Create virtual environment
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$SCRIPT_DIR/venv"
fi

# Activate virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install requirements
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r "$SCRIPT_DIR/requirements.txt"
fi

# Add PYTHONPATH to venv activation script
ACTIVATE_SCRIPT="$SCRIPT_DIR/venv/bin/activate"
if ! grep -q "PYTHONPATH.*$PROJECT_DIR/src" "$ACTIVATE_SCRIPT"; then
    echo "" >> "$ACTIVATE_SCRIPT"
    echo "# Added by setup.sh - set PYTHONPATH for project" >> "$ACTIVATE_SCRIPT"
    echo "export PYTHONPATH=\"$PROJECT_DIR/src:\$PYTHONPATH\"" >> "$ACTIVATE_SCRIPT"
    echo "PYTHONPATH configured in venv activation script"
fi

# Create replay directory for test results
mkdir -p "$PROJECT_DIR/replay"

echo ""
echo "Setup complete!"
echo "To activate the environment, run:"
echo "  source $SCRIPT_DIR/venv/bin/activate"
echo ""
echo "To run tests, run:"
echo "  bash $SCRIPT_DIR/run_tests.sh"
