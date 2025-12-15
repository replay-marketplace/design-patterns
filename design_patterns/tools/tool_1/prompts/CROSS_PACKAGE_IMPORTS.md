# Cross-Package Import Issue Explanation

## What Happened

### The Error
```
ModuleNotFoundError: No module named 'pkg_file_processing'
```

### Root Cause

1. **Package Structure**: Each package has `package/code/` where `code` is the Python package directory
2. **setup.py uses `find_packages()`**: This finds `code` as the package name, not `pkg_file_processing`
3. **When installed**: The package is imported as `from code import ...`, not `from pkg_file_processing.code import ...`
4. **Cross-package imports failed**: We tried `from pkg_file_processing.code.read_file_content import read_file_content`, but:
   - The installed package name is `code`, not `pkg_file_processing`
   - Both packages have a `code` package, causing namespace conflicts

### Why It Failed

```python
# What we tried (WRONG):
from pkg_file_processing.code.read_file_content import read_file_content

# What actually exists when installed:
from code.read_file_content import read_file_content  # But which 'code' package?
```

## Solution Implemented

We used `importlib.util` to dynamically load modules from file paths, which works in both:
- **Development mode**: Loads directly from file system paths
- **Installed mode**: Falls back to path-based imports

## What to Add to Your Prompt

Add this section to your package development prompts:

---

## Cross-Package Imports

**IMPORTANT**: If this package needs to import functions from other packages in the same codebase (e.g., `pkg_file_processing`, `pkg_string_processing`):

### The Problem
- When `setup.py` uses `find_packages()`, it finds `code` as the package name
- Cross-package imports like `from pkg_file_processing.code import ...` will fail
- Both packages have a `code` package, causing namespace conflicts

### The Solution
Use dynamic imports with `importlib.util` to handle both development and installed scenarios:

```python
import os
import sys
import importlib.util

def _import_function_from_other_package():
    """Import function from another package - handles both dev and installed modes."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    other_pkg_path = os.path.join(
        current_dir, '..', '..', '..', 'other_package_name', 'package', 'code', 'function_file.py'
    )
    other_pkg_path = os.path.abspath(other_pkg_path)
    
    if os.path.exists(other_pkg_path):
        # Development mode: load directly from file path
        spec = importlib.util.spec_from_file_location("function_name", other_pkg_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.function_name
    else:
        # Installed mode: add to path and import
        other_pkg_dir = os.path.join(
            current_dir, '..', '..', '..', 'other_package_name', 'package'
        )
        other_pkg_dir = os.path.abspath(other_pkg_dir)
        if other_pkg_dir not in sys.path:
            sys.path.insert(0, other_pkg_dir)
        from code.function_file import function_name
        return function_name

function_name = _import_function_from_other_package()
```

### Requirements
1. **All cross-package imports** must use this dynamic import pattern
2. **Import helper functions** should be named `_import_function_name()` (private)
3. **Path calculation** should be relative: `'..', '..', '..', 'other_package_name', 'package', 'code', 'function_file.py'`
4. **Test both modes**: Ensure imports work in development (file exists) and installed (path-based) scenarios

### Example
If `pkg_json_processing` needs `read_file_content` from `pkg_file_processing`:

```python
# In pkg_json_processing/package/code/load_json_from_file.py
def _import_read_file_content():
    """Import read_file_content from pkg_file_processing."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pkg_file_path = os.path.join(
        current_dir, '..', '..', '..', 'pkg_file_processing', 'package', 'code', 'read_file_content.py'
    )
    pkg_file_path = os.path.abspath(pkg_file_path)
    
    if os.path.exists(pkg_file_path):
        spec = importlib.util.spec_from_file_location("read_file_content", pkg_file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.read_file_content
    else:
        pkg_file_processing_path = os.path.join(
            current_dir, '..', '..', '..', 'pkg_file_processing', 'package'
        )
        pkg_file_processing_path = os.path.abspath(pkg_file_processing_path)
        if pkg_file_processing_path not in sys.path:
            sys.path.insert(0, pkg_file_processing_path)
        from code.read_file_content import read_file_content
        return read_file_content

read_file_content = _import_read_file_content()
```

---

## Alternative: Better Package Structure (Future Improvement)

For future packages, consider using proper namespace packages:

```python
# In setup.py:
setup(
    name="pkg-file-processing",
    packages=['pkg_file_processing.code'],
    package_dir={'pkg_file_processing.code': 'code'},
    # ... rest of setup
)
```

Then imports would work as: `from pkg_file_processing.code import ...`

But this requires restructuring existing packages, so the dynamic import solution is the pragmatic choice for now.

