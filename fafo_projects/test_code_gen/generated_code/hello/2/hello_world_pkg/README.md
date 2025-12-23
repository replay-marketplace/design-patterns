# hello_world Package

A simple Python package demonstrating basic package structure with greeting functions.

## Installation

```bash
cd hello_world_pkg
pip install -e .
```

## Usage

```python
from hello_world import say_hello, greet_user

# Print a classic greeting
print(say_hello())  # Output: Hello, World!

# Greet a specific user
print(greet_user("Alice"))  # Output: Hello, Alice!
```

## Function Signatures

### say_hello()

Returns a classic 'Hello, World!' greeting.

**Parameters:**
- None

**Returns:**
- `str`: The greeting message 'Hello, World!'

### greet_user(name)

Returns a personalized greeting for the given name.

**Parameters:**
- `name` (str): The name of the person to greet

**Returns:**
- `str`: A personalized greeting message

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

