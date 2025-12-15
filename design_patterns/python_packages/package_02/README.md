# Package 02

A Python package providing one utility function that uses functionality from package_01.

## Installation

Install the package in editable mode using pip:

```bash
pip install -e .
```

Or install from the directory:

```bash
cd package_02
pip install -e .
```

**Note:** This package depends on `package_01`, so make sure to install `package_01` first:

```bash
cd ../package_01
pip install -e .
cd ../package_02
pip install -e .
```

## Usage

After installation, you can import and use the function in your Python code:

```python
from package_02 import function_one

# Create a greeting message
result = function_one("Alice")
print(result)  # Output: Hello Alice!

# Use a custom greeting
result = function_one("Bob", greeting="Hi")
print(result)  # Output: Hi Bob!
```

## Functions

### `function_one(name, greeting="Hello")`
Creates a formatted greeting message using `function_one` from `package_01`. This function demonstrates how `package_02` depends on and uses functionality from `package_01`.

## Dependencies

This package requires `package_01` to be installed, as it imports and uses `function_one` from that package.

## Development

This package uses standard Python packaging. The package structure is:

```
package_02/
├── package_02/
│   ├── __init__.py
│   └── function_1.py
├── setup.py
└── README.md
```

