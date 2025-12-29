"""Count Python functions function - Returns function count and list of all function names using ast."""

import os
import ast
from pathlib import Path
from typing import Tuple, List


def count_python_functions(dir: str) -> Tuple[int, List[str]]:
    """
    Use ast python lib to make a list of all functions defined in given dir. 
    Returns the function count and all function names.

    Args:
        dir: The directory path to analyze Python functions in.

    Returns:
        A tuple containing:
        - Total number of functions (int)
        - List of all function names (List[str])

    Example:
        >>> count, functions = count_python_functions("/path/to/directory")
        >>> print(f"Total functions: {count}")
        >>> print(f"Functions: {functions}")
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    all_functions = []
    
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
                            # Handle function definitions
                            if isinstance(node, ast.FunctionDef):
                                all_functions.append(node.name)
                            # Handle async function definitions
                            elif isinstance(node, ast.AsyncFunctionDef):
                                all_functions.append(node.name)
                    
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
    unique_functions = []
    seen = set()
    for func in all_functions:
        if func not in seen:
            unique_functions.append(func)
            seen.add(func)
    
    return len(unique_functions), unique_functions



