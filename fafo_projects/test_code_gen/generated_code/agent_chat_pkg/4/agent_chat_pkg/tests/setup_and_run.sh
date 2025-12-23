#!/bin/bash
# Setup and run tests

echo "Setting up test environment..."
pip install -r requirements.txt

echo "Running tests..."
python -m pytest test.py -v
