#!/bin/bash
# Setup and run tests

set -e

echo "Setting up test environment..."

# Install the package in development mode
pip install -e ..

# Install test dependencies
pip install -r requirements.txt

echo "Running tests..."
python -m pytest test.py -v --cov=file_processing --cov-report=term-missing

echo "Tests completed!"
