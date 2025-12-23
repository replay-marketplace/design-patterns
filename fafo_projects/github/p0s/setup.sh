#!/bin/bash

# Setup script for GitHub P0 Issues Analyzer
# This script activates the virtual environment, installs dependencies, and runs the code

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if GITHUB_TOKEN is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo ""
    echo "⚠️  WARNING: GITHUB_TOKEN environment variable is not set."
    echo "   The script will prompt you to set it."
    echo ""
    echo "   To set it, run:"
    echo "   export GITHUB_TOKEN=your_token_here"
    echo ""
    echo "   Or set it in this script before running."
    echo ""
fi

# Run the analyzer
echo ""
echo "Running GitHub P0 Issues Analyzer..."
echo "======================================"
python analyze_p0_issues.py


