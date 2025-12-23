#!/bin/bash
# Set up python venv, install requirements, run tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pytest tests/