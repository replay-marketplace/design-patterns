"""Count file types function - Returns a list of tuples with file type and count."""

import os
from pathlib import Path
from typing import List, Tuple
from collections import Counter


def count_file_types(dir: str) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples with file type (ex. "*.py") and corresponding count.

    Args:
        dir: The directory path to count file types in.

    Returns:
        A list of tuples, where each tuple contains (file_extension, count).
        File extensions are returned with the dot prefix (e.g., ".py", ".txt").

    Example:
        >>> result = count_file_types("/path/to/directory")
        >>> print(result)
        [('.py', 10), ('.txt', 5), ('.md', 3)]
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    file_extensions = []
    
    for root, dirs, files in os.walk(dir):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        
        for file in files:
            file_path = Path(file)
            extension = file_path.suffix
            # Use empty string for files without extension
            if not extension:
                extension = "(no extension)"
            file_extensions.append(extension)
    
    # Count occurrences of each extension
    extension_counts = Counter(file_extensions)
    
    # Convert to list of tuples and sort by count (descending)
    result = sorted(extension_counts.items(), key=lambda x: x[1], reverse=True)
    
    return result



