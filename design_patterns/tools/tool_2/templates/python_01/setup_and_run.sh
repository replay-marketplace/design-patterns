#!/bin/bash
# Setup virtual env
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the program
python main.py