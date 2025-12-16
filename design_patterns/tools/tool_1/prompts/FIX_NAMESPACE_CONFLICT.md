# Fix: Namespace Conflict with `code/` Directory

## Problem

All packages use `package/code/` as the directory name, causing:
- Namespace conflicts (both packages have a `code` package)
- Import issues (`from pkg_file_processing.code import ...` doesn't work)
- Need for complex dynamic import workarounds

## Solution: Use Package Name as Directory

**Change**: `package/code/` → `package/pkg_package_name/`

### Example Structure

**BEFORE (WRONG)**:
```
pkg_file_processing/
├── package/
│   ├── code/              ❌ Generic name causes conflicts
│   │   ├── __init__.py
│   │   └── read_file_content.py
│   └── setup.py
```

**AFTER (CORRECT)**:
```
pkg_file_processing/
├── package/
│   ├── pkg_file_processing/   ✅ Unique namespace
│   │   ├── __init__.py
│   │   └── read_file_content.py
│   └── setup.py
```

## Benefits

1. **Unique namespaces**: Each package has its own namespace
2. **Direct imports**: `from pkg_file_processing import read_file_content`
3. **No conflicts**: Multiple packages can coexist
4. **Standard Python practice**: Matches Python packaging conventions

## Migration Steps

### 1. Rename Directory
```bash
cd pkg_file_processing/package/
mv code pkg_file_processing
```

### 2. Update setup.py
No changes needed - `find_packages()` will automatically find `pkg_file_processing`

### 3. Update Imports in Tests
```python
# BEFORE
from code.read_file_content import read_file_content

# AFTER
from pkg_file_processing.read_file_content import read_file_content
```

### 4. Update Cross-Package Imports
```python
# BEFORE (complex dynamic import)
def _import_read_file_content():
    # ... complex importlib.util code ...

# AFTER (simple direct import)
from pkg_file_processing import read_file_content
```

### 5. Update __init__.py
No changes needed - relative imports still work:
```python
from .read_file_content import read_file_content  # Still works
```

## Updated Prompt Template

When creating new packages, use this structure:

```
pkg_package_name/
├── package/
│   ├── pkg_package_name/     # Use package name, NOT "code"
│   │   ├── __init__.py
│   │   ├── function_1.py
│   │   └── function_2.py
│   └── setup.py
├── tests/
│   └── test.py
└── README.md
```

## Why This Works

- `find_packages()` finds `pkg_package_name` as the package
- When installed: `pip install -e .` makes it importable as `pkg_package_name`
- Cross-package imports: `from pkg_file_processing import read_file_content` works directly
- No namespace conflicts: Each package has a unique name



