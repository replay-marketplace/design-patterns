#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo 'export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"' >> venv/bin/activate
