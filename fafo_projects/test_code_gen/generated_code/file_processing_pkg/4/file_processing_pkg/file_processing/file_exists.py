"""
file_exists function.
"""

import os


def file_exists(filepath: str) -> bool:
    """
    Check if a file exists at the given path.
    
    Args:
        filepath (str): The path to check
    
    Returns:
        bool: True if the file exists and is a file, False otherwise
    """
    return os.path.isfile(filepath)
