"""Count lines of code function - Returns total lines of text in directory."""

import os
from pathlib import Path


def count_loc(dir: str) -> int:
    """
    Returns total lines of text in directory (recursively).

    Args:
        dir: The directory path to count lines in.

    Returns:
        The total number of lines of text in all files in the directory.

    Example:
        >>> result = count_loc("/path/to/directory")
        >>> print(result)
        150
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    total_lines = 0
    
    for root, dirs, files in os.walk(dir):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        
        for file in files:
            file_path = Path(root) / file
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    total_lines += sum(1 for _ in f)
            except (UnicodeDecodeError, PermissionError, IsADirectoryError):
                # Skip binary files or files we can't read
                continue
    
    return total_lines



