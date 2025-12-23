#!/bin/bash
# Setup and run tests

# Install the package in editable mode
cd "$(dirname "$0")/.." || exit
pip install -e .

# Run tests
cd tests || exit
python -m pytest test_hello.py -v

