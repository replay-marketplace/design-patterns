#!/bin/bash
# Setup and run tests

set -e

echo "Installing test dependencies..."
pip install -r requirements.txt

echo "Installing json_processing package..."
pip install -e ..

echo "Running tests..."
python -m pytest test.py -v
