#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Set PYTHONPATH to include the project root
export PYTHONPATH="$(cd .. && pwd):${PYTHONPATH}"

# Run the tests
python3 test.py
python3 test_blind.py
