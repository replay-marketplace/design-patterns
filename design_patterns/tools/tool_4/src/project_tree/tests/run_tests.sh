#!/bin/bash
# Test runner that sets PYTHONPATH and runs tests

PYTHONPATH="$(dirname "$0")/.." python3 test.py


