#!/bin/bash

# Setup and run tests for string_processing package

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Install the package in development mode
echo "Installing string_processing package..."
pip install -q -e ..

# Run tests
echo "Running tests..."
python test.py

echo "Done!"


