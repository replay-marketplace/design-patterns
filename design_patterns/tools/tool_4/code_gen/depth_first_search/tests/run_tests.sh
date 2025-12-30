#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Set PYTHONPATH to include parent directory and run tests
PYTHONPATH="$(cd .. && pwd)" python3 test.py
PYTHONPATH="$(cd .. && pwd)" python3 test_blind.py
