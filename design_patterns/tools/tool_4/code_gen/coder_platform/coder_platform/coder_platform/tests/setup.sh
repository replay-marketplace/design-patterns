#!/bin/bash

# Make python env, install requirements, set PYTHONPATH in venv activation
cd "$(dirname "$0")"

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements if they exist
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Set PYTHONPATH in venv activation script
PROJECT_ROOT="$(cd ../../.. && pwd)"
echo "export PYTHONPATH=\"$PROJECT_ROOT:\$PYTHONPATH\"" >> venv/bin/activate

# Create replay directory for test results
mkdir -p ../replay

echo "Setup complete. Run 'source venv/bin/activate' to activate the environment."
