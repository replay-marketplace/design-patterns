# How to Add a New Function to This Package

Write instructions for an agent on how to add a new function to this python package. 
Include all the steps required. 

# Instructions

## Step 1: Create a New Function File

Create a new Python file in the `package_01/` directory following the naming convention:
- File name: `function_N.py` where N is the next sequential number (e.g., if the last function is `function_5.py`, create `function_6.py`)

## Step 2: Write the Function Code

In the new file, include:
1. **Module docstring** at the top describing what the function does:
   ```python
   """
   Function N: Brief description of the function's purpose.
   """
   ```

2. **Function definition** with:
   - Descriptive function name following the pattern: `function_N` (e.g., `function_six`)
   - Type hints for all parameters and return type
   - Comprehensive docstring including:
     - Description of what the function does
     - `Args:` section listing all parameters with types and descriptions
     - `Returns:` section describing the return value
     - `Raises:` section if the function can raise exceptions
     - `Example:` section with a usage example using doctest format

3. **Function implementation**

Example structure:
```python
"""
Function 6: Brief description.
"""


def function_six(param1: type, param2: type = default) -> return_type:
    """
    Detailed description of what the function does.

    Args:
        param1: Description of param1.
        param2: Description of param2 (optional).

    Returns:
        Description of what is returned.

    Raises:
        ValueError: When this error occurs.

    Example:
        >>> function_six("example", 42)
        'expected output'
    """
    # Implementation here
    pass
```

## Step 3: Update `__init__.py`

Add the new function to the package's `__init__.py` file:

1. **Add the import statement** at the top with the other imports:
   ```python
   from .function_N import function_N
   ```

2. **Add the function name to `__all__`** list:
   ```python
   __all__ = [
       "function_one",
       "function_two",
       # ... existing functions ...
       "function_N",  # Add the new function here
   ]
   ```

## Step 4: Verify the Package Structure

Ensure that:
- The new function file follows the same naming and structure conventions as existing functions
- The function is properly imported and exported in `__init__.py`
- Type hints are used consistently
- Docstrings follow the same format as existing functions

## Step 5: Test the New Function (Optional but Recommended)

Test that the new function can be imported and used:
```python
from package_01 import function_N

# Test the function
result = function_N(...)
```

## Notes

- The `setup.py` file uses `find_packages()`, so it will automatically include new Python files in the package
- Maintain consistency with existing function naming, documentation style, and code structure
- Follow Python best practices for type hints and docstrings
- Ensure the function is useful and well-documented for package users