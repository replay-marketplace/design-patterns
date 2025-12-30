#!/bin/bash
# Make python env, install requirements, set PYTHONPATH in venv activation
cd "$(dirname "$0")"
python3 -m venv venv
source venv/bin/activate

# Add PYTHONPATH to venv activation script
echo 'export PYTHONPATH="${PYTHONPATH}:$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"' >> venv/bin/activate

# Install requirements if any
if [ -s requirements.txt ]; then
    pip install -r requirements.txt
fi

# Create replay directory for test results
mkdir -p ../replay
