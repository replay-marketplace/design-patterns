# hello_world Package

A simple Python package demonstrating basic package structure with hello world functionality.

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

### greet(name: str = "World")

Prints a greeting message.

**Parameters:**
- name (str, optional): The name to greet. Defaults to "World".

**Returns:**
- str: The greeting message

### say_goodbye(name: str = "World")

Prints a goodbye message.

**Parameters:**
- name (str, optional): The name to say goodbye to. Defaults to "World".

**Returns:**
- str: The goodbye message

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.
