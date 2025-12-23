#!/bin/bash
# Setup and run tests

set -e

echo "Installing test dependencies..."
pip install -r requirements.txt

echo "Installing package in development mode..."
pip install -e ..

echo "Running tests..."
python -m pytest test.py -v --cov=deepseek_chat --cov-report=term-missing

echo "Tests completed successfully!"
