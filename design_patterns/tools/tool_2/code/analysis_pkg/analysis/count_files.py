"""Count files function - Returns the number of files in directory."""

import os
from pathlib import Path


def count_files(dir: str) -> int:
    """
    Returns the number of files in directory (recursively).

    Args:
        dir: The directory path to count files in.

    Returns:
        The total number of files in the directory.

    Example:
        >>> result = count_files("/path/to/directory")
        >>> print(result)
        25
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    file_count = 0
    
    for root, dirs, files in os.walk(dir):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        
        file_count += len(files)
    
    return file_count


