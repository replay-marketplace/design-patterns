"""
File exists function - Check file existence.
"""

import os


def file_exists(filepath: str) -> bool:
    """
    Check if a file exists at the given path.

    Args:
        filepath: The path to the file to check.

    Returns:
        True if the file exists, False otherwise.

    Example:
        >>> file_exists("/tmp/test.txt")
        False
    """
    return os.path.isfile(filepath)

