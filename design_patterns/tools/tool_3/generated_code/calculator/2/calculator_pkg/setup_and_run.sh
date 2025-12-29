#!/bin/bash
# Setup and run tests

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    pip install -q -r requirements.txt
fi

python -m pytest tests/test_calculator.py -v

