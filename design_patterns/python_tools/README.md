# Python Tools Utils

A simple local Python package with utility functions for testing and development.

## Installation

### For Use in Other Projects (Recommended)

If you want to use this package in other Python projects that have their own virtual environments:

1. **Activate your project's virtual environment:**
   ```bash
   # Example: if your project is in pattern_01_voice_one_shot/code/v0.1/
   cd pattern_01_voice_one_shot/code/v0.1/
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

2. **Install the package from the python_tools directory:**
   ```bash
   # Option 1: Use absolute path (most reliable)
   pip install -e /Users/jvasiljevic/continue/gh/design-patterns/design_patterns/python_tools
   
   # Option 2: Use relative path (from pattern_01_voice_one_shot/code/v0.1/)
   pip install -e ../../../python_tools
   
   # Note: Adjust the relative path based on your project's location
   # The path should point to the directory containing setup.py
   ```

   The `-e` flag installs in "editable" mode, so changes to the package code are immediately available without reinstalling.

### Alternative: Install from python_tools Directory

You can also install it from the package directory itself:

```bash
cd python_tools
pip install -e .
```

**Note:** This installs it in whatever Python environment is currently active. If you want to use it in a specific project, make sure that project's virtual environment is activated first.

## Usage

Once installed, you can import and use the functions from anywhere in your repository:

```python
from python_tools_utils.function_a import add_numbers
from python_tools_utils.function_b import multiply_numbers

# Or import both at once
from python_tools_utils import add_numbers, multiply_numbers

# Use the functions
result1 = add_numbers(5, 3)        # Returns 8
result2 = multiply_numbers(4, 7)   # Returns 28
```

## Available Functions

### `add_numbers(a, b)`
Adds two numbers together.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:**
- `float`: The sum of a and b

**Example:**
```python
>>> add_numbers(2, 3)
5
```

### `multiply_numbers(a, b)`
Multiplies two numbers together.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:**
- `float`: The product of a and b

**Example:**
```python
>>> multiply_numbers(2, 3)
6
```

## Testing

You can test the functions by running Python in the repository:

```python
python3
>>> from python_tools_utils import add_numbers, multiply_numbers
>>> add_numbers(10, 20)
30
>>> multiply_numbers(5, 6)
30
```

## Package Structure

```
python_tools/
├── python_tools_utils/
│   ├── __init__.py
│   ├── function_a.py      # add_numbers function
│   └── function_b.py      # multiply_numbers function
├── setup.py
└── README.md
```

## Notes

- This is a **local package** - no publishing or registration needed
- Install with `pip install -e .` for editable mode
- Changes to the code are immediately available after installation
- **Each project needs to install it separately** in its own virtual environment
- Use the path to `python_tools/` directory when installing from other projects
- The `-e` (editable) flag means you don't need to reinstall after making changes to the package code

## Example: Installing in a Project

Let's say you have a project at `pattern_01_voice_one_shot/code/v0.1/`:

```bash
# 1. Navigate to your project
cd pattern_01_voice_one_shot/code/v0.1/

# 2. Activate the project's virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install the package using absolute path (recommended)
pip install -e /Users/jvasiljevic/continue/gh/design-patterns/design_patterns/python_tools

# OR use relative path (three levels up from v0.1/)
pip install -e ../../../python_tools

# 4. Now you can use it in your project
python
>>> from python_tools_utils import add_numbers, multiply_numbers
>>> add_numbers(5, 3)
8
```

**Important:** The path must point to the directory containing `setup.py`. If you get an error about "not a valid editable requirement", try:
- Using an absolute path instead of relative
- Verifying the path exists: `ls /path/to/python_tools/setup.py`
- Making sure you're in the correct directory when using relative paths

