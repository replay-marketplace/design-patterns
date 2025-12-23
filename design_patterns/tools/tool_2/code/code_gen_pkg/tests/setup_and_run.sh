#!/bin/bash

# Setup and run tests for code_gen package

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
echo "Installing code_gen package..."
CODE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
pip install -q -e ..

echo "Installing other packages..."
pip install -q -e $CODE_DIR/agent_chat_pkg
pip install -q -e $CODE_DIR/file_processing_pkg
pip install -q -e $CODE_DIR/json_processing_pkg
pip install -q -e $CODE_DIR/analysis_pkg
pip install -q -e $CODE_DIR/string_processing_pkg

# Run tests
echo "Running tests..."
python test.py

echo "Done!"

