"""Count words function - Returns total words in directory."""

import os
from pathlib import Path
import re


def count_words(dir: str, text: str = None) -> int:
    """
    Returns total words in directory (recursively).
    If text is provided, counts occurrences of that text pattern.
    If text is None, counts all words in all files.

    Args:
        dir: The directory path to count words in.
        text: Optional text pattern to search for. If None, counts all words.

    Returns:
        The total number of words (or occurrences of text pattern) in the directory.

    Example:
        >>> result = count_words("/path/to/directory")
        >>> print(result)
        5000
    """
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    dir_path = Path(dir)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir}")
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {dir}")
    
    total_words = 0
    
    for root, dirs, files in os.walk(dir):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        
        for file in files:
            file_path = Path(root) / file
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if text is None:
                        # Count all words (sequences of alphanumeric characters)
                        words = re.findall(r'\b\w+\b', content)
                        total_words += len(words)
                    else:
                        # Count occurrences of the text pattern
                        total_words += content.count(text)
            except (UnicodeDecodeError, PermissionError, IsADirectoryError):
                # Skip binary files or files we can't read
                continue
    
    return total_words


