"""Check if a directory exists."""

import os
from pathlib import Path


def dir_exists(filepath: str) -> bool:
    """Check if a directory exists at the specified path.
    
    Args:
        filepath: The path to the directory to check
    
    Returns:
        bool: True if the directory exists and is a directory, False otherwise
    
    Example:
        >>> dir_exists("/tmp")
        True
        >>> dir_exists("/nonexistent/directory")
        False
    """
    try:
        path = Path(filepath)
        return path.exists() and path.is_dir()
    except (OSError, ValueError):
        # Handle invalid paths or OS errors
        return False
    except Exception:
        # Handle any other unexpected errors
        return False
