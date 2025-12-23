"""Directory exists function - Check directory existence."""

import os


def dir_exists(filepath: str) -> bool:
    """
    Check if a directory exists at the given path.

    Args:
        filepath: The path to the directory to check.

    Returns:
        True if the directory exists, False otherwise.

    Example:
        >>> result = dir_exists("/tmp/test")
        >>> print(result)
        True
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    
    return os.path.isdir(filepath)


