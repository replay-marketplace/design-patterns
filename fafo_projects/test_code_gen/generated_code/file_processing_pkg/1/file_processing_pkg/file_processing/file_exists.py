"""
file_exists function.
"""

import os


def file_exists(filepath: str) -> bool:
    """
    Check if a file exists at the specified path.
    
    Args:
        filepath (str): The path to the file to check
    
    Returns:
        bool: True if the file exists and is a file (not a directory), False otherwise
    """
    try:
        # Check if path exists and is a file
        return os.path.exists(filepath) and os.path.isfile(filepath)
    except Exception as e:
        # Return False if any error occurs
        return False

