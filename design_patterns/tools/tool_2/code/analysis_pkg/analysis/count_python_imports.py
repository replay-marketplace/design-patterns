"""Count Python imports function - Returns total imports and list of all imports using ast."""

import os
import ast
from pathlib import Path
from typing import Tuple, List


def count_python_imports(dir: str) -> Tuple[int, List[str]]:
    """
    Use ast python lib to make a list of all imported functions, code, libraries, 
    local or remote, all types. Returns the total number of imports and the list of all imports.

    Args:
        dir: The directory path to analyze Python imports in.

    Returns:
        A tuple containing:
        - Total number of imports (int)
        - List of all import names (List[str])

    Example:
        >>> count, imports = count_python_imports("/path/to/directory")
        >>> print(f"Total imports: {count}")
        >>> print(f"Imports: {imports}")
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    all_imports = []
    
    for root, dirs, files in os.walk(dir):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        
        for file in files:
            if file.endswith('.py'):
                file_path = Path(root) / file
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    try:
                        tree = ast.parse(content, filename=str(file_path))
                        
                        for node in ast.walk(tree):
                            # Handle import statements: import module
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    all_imports.append(alias.name)
                            
                            # Handle from imports: from module import name
                            elif isinstance(node, ast.ImportFrom):
                                if node.module:
                                    for alias in node.names:
                                        # Include both module and imported name
                                        if alias.asname:
                                            all_imports.append(f"{node.module}.{alias.name} as {alias.asname}")
                                        else:
                                            all_imports.append(f"{node.module}.{alias.name}")
                                else:
                                    # Relative imports (from . import ...)
                                    for alias in node.names:
                                        all_imports.append(f".{alias.name}")
                    
                    except SyntaxError:
                        # Skip files with syntax errors
                        continue
                    except Exception:
                        # Skip files we can't parse
                        continue
                
                except (UnicodeDecodeError, PermissionError, IsADirectoryError):
                    # Skip files we can't read
                    continue
    
    # Remove duplicates while preserving order
    unique_imports = []
    seen = set()
    for imp in all_imports:
        if imp not in seen:
            unique_imports.append(imp)
            seen.add(imp)
    
    return len(unique_imports), unique_imports


