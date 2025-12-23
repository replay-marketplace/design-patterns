# hello_world Package

A simple Python package for greeting and saying goodbye.

## Installation

```bash
cd hello_world_pkg
pip install -e .
```

## Usage

```python
from hello_world import greet, say_goodbye

# Use the functions
print(greet())  # Output: Hello, World!
print(greet("Alice"))  # Output: Hello, Alice!

print(say_goodbye())  # Output: Goodbye, World!
print(say_goodbye("Bob"))  # Output: Goodbye, Bob!
```

## Function Signatures

### greet(name: str = "World") -> str

Generates a greeting message.

**Parameters:**
- `name` (str, optional): The name to greet. Defaults to "World".

**Returns:**
- `str`: A greeting message in the format "Hello, {name}!"

### say_goodbye(name: str = "World") -> str

Generates a goodbye message.

**Parameters:**
- `name` (str, optional): The name to say goodbye to. Defaults to "World".

**Returns:**
- `str`: A goodbye message in the format "Goodbye, {name}!"

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

