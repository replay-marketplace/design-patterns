#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Activate virtual environment if it exists
if [ -f "$SCRIPT_DIR/venv/bin/activate" ]; then
    source "$SCRIPT_DIR/venv/bin/activate"
fi

# Set PYTHONPATH to include src directory
export PYTHONPATH="$PROJECT_DIR/src:$PYTHONPATH"

# Run tests
echo "Running tests from $SCRIPT_DIR"
echo "PYTHONPATH: $PYTHONPATH"
echo ""

# Try pytest first, fall back to unittest
if command -v pytest &> /dev/null; then
    python -m pytest "$SCRIPT_DIR" -v
else
    python -m unittest discover -s "$SCRIPT_DIR" -p "test*.py" -v
fi

# Capture exit code
EXIT_CODE=$?

echo ""
echo "Tests completed with exit code: $EXIT_CODE"

exit $EXIT_CODE
