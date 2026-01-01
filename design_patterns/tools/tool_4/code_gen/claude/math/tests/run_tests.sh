#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Set PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(cd .. && pwd)

# Run tests
python test.py
