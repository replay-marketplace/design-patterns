#!/bin/bash
# Setup and run tests

echo "Installing test dependencies..."
pip install -r requirements.txt

echo "Running tests..."
python -m pytest test.py -v
