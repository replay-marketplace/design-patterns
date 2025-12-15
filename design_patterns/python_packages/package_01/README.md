# Package 01

A Python package providing five utility functions for common tasks.

## Installation

Install the package in editable mode using pip:

```bash
pip install -e .
```

Or install from the directory:

```bash
cd package_01
pip install -e .
```

## Usage

After installation, you can import and use the functions in your Python code:

```python
from package_01 import (
    function_one,
    function_two,
    function_three,
    function_four,
    function_five,
)

# Function 1: String manipulation
result = function_one("world", prefix="Hello ", suffix="!")
print(result)  # Output: Hello world!

# Function 2: Calculate average
avg = function_two([1, 2, 3, 4, 5])
print(avg)  # Output: 3.0

# Function 3: Email validation
is_valid = function_three("user@example.com")
print(is_valid)  # Output: True

# Function 4: Remove duplicates
unique = function_four([1, 2, 2, 3, 1, 4])
print(unique)  # Output: [1, 2, 3, 4]

# Function 5: Date formatting
date_str = function_five(7)  # 7 days from today
print(date_str)  # Output: 2025-01-20 (example)
```

## Functions

### `function_one(text, prefix="", suffix="")`
Adds a prefix and/or suffix to a text string.

### `function_two(numbers)`
Calculates the average of a list of numbers.

### `function_three(email)`
Validates if a string is a valid email address format.

### `function_four(items, reverse=False)`
Removes duplicates from a list while preserving order.

### `function_five(days=0)`
Gets a formatted date string for a date N days from today.

## Development

This package uses standard Python packaging. The package structure is:

```
package_01/
├── package_01/
│   ├── __init__.py
│   ├── function_1.py
│   ├── function_2.py
│   ├── function_3.py
│   ├── function_4.py
│   └── function_5.py
├── setup.py
└── README.md
```

## License

MIT License (or specify your preferred license)

