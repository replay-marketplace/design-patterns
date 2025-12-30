#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

cd "$(dirname "$0")"
source venv/bin/activate
python test.py
python test_blind.py
