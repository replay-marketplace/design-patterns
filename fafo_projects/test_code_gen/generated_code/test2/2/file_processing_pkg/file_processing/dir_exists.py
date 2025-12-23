"""
dir_exists function.
"""

import os


def dir_exists(filepath: str) -> bool:
    """
    Check if a directory exists at the specified path.
    
    Args:
        filepath (str): The path to the directory to check
    
    Returns:
        bool: True if the directory exists and is a directory (not a file), False otherwise
    """
    try:
        # Check if path exists and is a directory
        return os.path.exists(filepath) and os.path.isdir(filepath)
    except Exception as e:
        # Return False if any error occurs
        return False

