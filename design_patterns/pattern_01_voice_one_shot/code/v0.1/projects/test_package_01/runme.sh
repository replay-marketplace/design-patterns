#!/bin/bash

# Script to set up virtual environment, install package_01, and run the program

set -e  # Exit on error

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Find the repository root by looking for the python_packages directory
# Start from the script directory and walk up until we find it
REPO_ROOT="$SCRIPT_DIR"
while [ "$REPO_ROOT" != "/" ] && [ ! -d "$REPO_ROOT/python_packages" ]; do
    REPO_ROOT="$(dirname "$REPO_ROOT")"
done

if [ ! -d "$REPO_ROOT/python_packages" ]; then
    echo "Error: Could not find repository root (python_packages directory)" >&2
    exit 1
fi

PACKAGE_01_PATH="$REPO_ROOT/python_packages/package_01"

if [ ! -d "$PACKAGE_01_PATH" ]; then
    echo "Error: Could not find package_01 at $PACKAGE_01_PATH" >&2
    exit 1
fi

echo "Setting up virtual environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing package_01 in editable mode..."
echo "Package path: $PACKAGE_01_PATH"
pip install -e "$PACKAGE_01_PATH"

echo ""
echo "Running main.py..."
echo "=================="
python main.py

