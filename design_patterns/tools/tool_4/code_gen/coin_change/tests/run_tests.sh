#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

cd "$(dirname "$0")"
mkdir -p ../replay
PYTHONPATH="$(cd .. && pwd)" python3 test.py
PYTHONPATH="$(cd .. && pwd)" python3 test_blind.py
