"""
dir_exists function.
"""

import os


def dir_exists(filepath: str) -> bool:
    """
    Check if a directory exists at the given path.
    
    Args:
        filepath (str): The path to check
    
    Returns:
        bool: True if the directory exists and is a directory, False otherwise
    """
    return os.path.isdir(filepath)
