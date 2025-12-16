# hello_world Package

A simple Python package demonstrating basic package structure.

## Installation

```bash
cd hello_world_pkg
pip install -e .
```

## Usage

```python
from hello_world import greet, say_goodbye

# Use the functions
greet()
say_goodbye()
```

## Function Signatures

### greet()

Prints a greeting message to the console.

**Parameters:**
- None

**Returns:**
- None

### say_goodbye()

Prints a goodbye message to the console.

**Parameters:**
- None

**Returns:**
- None

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.
