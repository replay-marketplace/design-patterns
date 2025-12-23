# hello_world Package

A simple Python package that demonstrates basic package structure with Hello World functionality.

## Installation

```bash
cd hello_world_pkg
pip install -e .
```

## Usage

```python
from hello_world import print_hello_world, get_hello_world

# Print Hello World to console
print_hello_world()

# Get Hello World as a string
message = get_hello_world()
print(message)
```

## Function Signatures

### print_hello_world()

Prints 'Hello, World!' to the console.

**Parameters:**
- None

**Returns:**
- None

### get_hello_world()

Returns the string 'Hello, World!'.

**Parameters:**
- None

**Returns:**
- str: The string 'Hello, World!'

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

