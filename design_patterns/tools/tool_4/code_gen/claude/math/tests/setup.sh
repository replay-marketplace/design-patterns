#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Add PYTHONPATH to venv activation script
echo "export PYTHONPATH=\$PYTHONPATH:$(cd .. && pwd)" >> venv/bin/activate

echo "Setup complete. Virtual environment created and configured."
