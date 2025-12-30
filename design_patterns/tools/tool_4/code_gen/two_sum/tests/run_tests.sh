#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

cd "$(dirname "$0")"
source venv/bin/activate
PYTHONPATH="$(dirname "$0")/.." python3 test.py
PYTHONPATH="$(dirname "$0")/.." python3 test_blind.py
