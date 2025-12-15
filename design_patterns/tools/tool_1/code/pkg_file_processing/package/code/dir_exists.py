"""
Directory exists function - Check directory existence.
"""

import os


def dir_exists(filepath: str) -> bool:
    """
    Check if a directory exists at the given path.

    Args:
        filepath: The path to the directory to check.

    Returns:
        True if the directory exists, False otherwise.

    Example:
        >>> dir_exists("/tmp")
        True
    """
    return os.path.isdir(filepath)

