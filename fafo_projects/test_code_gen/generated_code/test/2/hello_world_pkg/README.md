# hello_world Package

A simple Python package demonstrating basic package structure.

## Installation

```bash
cd hello_world_pkg
pip install -e .
```

## Usage

```python
from hello_world import say_hello, say_world

# Use the functions
say_hello()
say_world()
```

## Function Signatures

### say_hello()

Prints "Hello" to the console.

**Parameters:**
- None

**Returns:**
- None

### say_world()

Prints "World" to the console.

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
