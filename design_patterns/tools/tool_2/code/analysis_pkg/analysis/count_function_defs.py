"""Count function definitions function - Returns the LoC in requirements.txt."""

import os
from pathlib import Path


def count_function_defs(dir: str) -> int:
    """
    Searches for "requirements.txt" file in given dir and returns the Lines of Code in the file.
    If it finds multiple "requirements.txt" files it errors out.

    Args:
        dir: The directory path to search for requirements.txt in.

    Returns:
        The number of lines in the requirements.txt file.

    Raises:
        ValueError: If no requirements.txt is found or multiple are found.

    Example:
        >>> result = count_function_defs("/path/to/directory")
        >>> print(result)
        15
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    requirements_files = []
    
    for root, dirs, files in os.walk(dir):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        
        for file in files:
            if file == "requirements.txt":
                requirements_files.append(Path(root) / file)
    
    if len(requirements_files) == 0:
        raise ValueError(f"No requirements.txt file found in directory '{dir}'")
    if len(requirements_files) > 1:
        raise ValueError(f"Multiple requirements.txt files found in directory '{dir}': {[str(f) for f in requirements_files]}")
    
    # Read the requirements.txt file and count lines
    requirements_path = requirements_files[0]
    try:
        with open(requirements_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Count non-empty lines (excluding comments and blank lines)
            loc = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
            return loc
    except Exception as e:
        raise ValueError(f"Error reading requirements.txt: {e}")



