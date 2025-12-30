#!/bin/bash
# Make python env, install requirements, set PYTHONPATH in venv activation

cd "$(dirname "$0")"

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements if any
if [ -s requirements.txt ]; then
    pip install -r requirements.txt
fi

# Add PYTHONPATH to venv activation script
echo '' >> venv/bin/activate
echo '# Add project root to PYTHONPATH' >> venv/bin/activate
echo 'export PYTHONPATH="${PYTHONPATH}:'$(cd .. && pwd)'"' >> venv/bin/activate

echo "Setup complete. Run 'source venv/bin/activate' to activate the environment."