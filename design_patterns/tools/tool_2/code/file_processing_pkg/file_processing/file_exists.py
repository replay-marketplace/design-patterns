"""File exists function - Check file existence."""

import os


def file_exists(filepath: str) -> bool:
    """
    Check if a file exists at the given path.

    Args:
        filepath: The path to the file to check.

    Returns:
        True if the file exists, False otherwise.

    Example:
        >>> result = file_exists("/tmp/test.txt")
        >>> print(result)
        True
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    
    return os.path.isfile(filepath)


