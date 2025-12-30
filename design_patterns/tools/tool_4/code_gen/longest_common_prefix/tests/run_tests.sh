#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

cd "$(dirname "$0")"
source venv/bin/activate
python3 test.py
python3 test_blind.py
