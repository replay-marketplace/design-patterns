"""Get path to file function - Searches for a filename in directory and returns its path."""

import os
from pathlib import Path


def get_path_to_file(dir: str, filename: str) -> str:
    """
    Searches all files in the given dir for the given filename and returns the path to it.
    Returns the first match found. Raises ValueError if file is not found.

    Args:
        dir: The directory path to search in.
        filename: The filename to search for.

    Returns:
        The full path to the file as a string.

    Raises:
        ValueError: If the file is not found in the directory.

    Example:
        >>> result = get_path_to_file("/path/to/directory", "README.md")
        >>> print(result)
        '/path/to/directory/README.md'
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    for root, dirs, files in os.walk(dir):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        
        for file in files:
            if file == filename:
                file_path = Path(root) / file
                return str(file_path.absolute())
    
    raise ValueError(f"File '{filename}' not found in directory '{dir}'")



