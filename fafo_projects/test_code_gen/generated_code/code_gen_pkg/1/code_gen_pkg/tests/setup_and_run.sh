#!/bin/bash
# Setup virtual env
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install the package in development mode
if [ -f ../setup.py ]; then
    pip install -e ..
else
    PACKAGE_DIR=$(find .. -maxdepth 1 -type d ! -path .. ! -path ../tests -exec test -f {}/setup.py \; -print | head -1)
    if [ -z "$PACKAGE_DIR" ]; then
        echo "Error: setup.py not found"
        exit 1
    fi
    pip install -e "$PACKAGE_DIR"
fi

# Run the tests
python test.py
