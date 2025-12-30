#!/bin/bash
# Make python env, install requirements, set PYTHONPATH in venv activation

cd "$(dirname "$0")"

# Create virtual environment
python3 -m venv venv

# Add PYTHONPATH to venv activation script
echo 'export PYTHONPATH="${PYTHONPATH}:$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"' >> venv/bin/activate

# Activate and install requirements
source venv/bin/activate

if [ -s requirements.txt ]; then
    pip install -r requirements.txt
fi

# Create replay directory if it doesn't exist
mkdir -p ../replay
