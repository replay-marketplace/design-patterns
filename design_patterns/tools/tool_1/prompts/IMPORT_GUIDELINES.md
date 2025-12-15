# Cross-Package Import Guidelines

## Problem
When packages use `find_packages()` in `setup.py`, the package name becomes the directory name. If all packages use `code/` as the directory name, this causes:
1. Namespace conflicts (both packages have a `code` package)
2. Import issues (`from pkg_file_processing.code import ...` doesn't work)
3. Need for complex dynamic import workarounds

## Solution: Use Package Name as Directory (RECOMMENDED)

**Use the package name as the directory name, NOT `code/`:**

```
pkg_file_processing/
├── package/
│   ├── pkg_file_processing/   ✅ Use package name
│   │   ├── __init__.py
│   │   └── read_file_content.py
│   └── setup.py
```

This allows direct imports: `from pkg_file_processing import read_file_content`

See `FIX_NAMESPACE_CONFLICT.md` for migration guide.

## Alternative: Dynamic Import Pattern (If you must use `code/`)

When a package needs to import from another package in the same codebase, use this pattern:

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

## For Prompt Writers

When specifying package structure, use this:

```
## Package Structure

The package directory must be named after the package (e.g., `pkg_package_name/`), NOT `code/`:

```
pkg_package_name/
├── package/
│   ├── pkg_package_name/     # Use package name, NOT "code"
│   │   ├── __init__.py
│   │   └── function.py
│   └── setup.py
```

This ensures:
- Unique namespaces for each package
- Direct imports work: `from pkg_package_name import function`
- No namespace conflicts
- `find_packages()` correctly identifies package names
```

If cross-package imports are needed:
- Direct imports work: `from pkg_file_processing import read_file_content`
- No need for complex import workarounds

