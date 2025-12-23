# hello_world Package

A simple Python package demonstrating basic package structure with greeting functions.

## Installation

```bash
cd hello_world_pkg
pip install -e .
```

## Usage

```python
from hello_world import hello, goodbye, see_ya_later

# Use the functions
print(hello())           # Output: Hello, World!
print(goodbye())         # Output: Goodbye, World!
print(see_ya_later())    # Output: See ya later, World!
```

## Function Signatures

### hello()

Returns a hello world greeting.

**Parameters:**
- None

**Returns:**
- str: The greeting message "Hello, World!"

### goodbye()

Returns a goodbye world message.

**Parameters:**
- None

**Returns:**
- str: The goodbye message "Goodbye, World!"

### see_ya_later()

Returns a see ya later world message.

**Parameters:**
- None

**Returns:**
- str: The see ya later message "See ya later, World!"

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

