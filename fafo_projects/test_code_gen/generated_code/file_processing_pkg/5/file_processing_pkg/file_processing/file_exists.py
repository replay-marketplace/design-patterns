"""Check if a file exists."""

import os
from pathlib import Path


def file_exists(filepath: str) -> bool:
    """Check if a file exists at the specified path.
    
    Args:
        filepath: The path to the file to check
    
    Returns:
        bool: True if the file exists and is a file, False otherwise
    
    Example:
        >>> file_exists("/tmp/test.txt")
        True
        >>> file_exists("/tmp/nonexistent.txt")
        False
    """
    try:
        path = Path(filepath)
        return path.exists() and path.is_file()
    except (OSError, ValueError):
        # Handle invalid paths or OS errors
        return False
    except Exception:
        # Handle any other unexpected errors
        return False
