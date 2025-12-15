"""
Save JSON string to file function - Save JSON string to file.
"""

import os
from pathlib import Path


def save_json_string_to_file(json_str: str, filepath: str) -> bool:
    """
    Save a JSON string to a file.

    Args:
        json_str: The JSON string to save.
        filepath: The path to the file where JSON string should be saved.

    Returns:
        True if the file was successfully written, False otherwise.

    Example:
        >>> save_json_string_to_file('{"key": "value"}', "/tmp/data.json")
        True
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(filepath)
        if directory:
            Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Write JSON string to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
        
        return True
    except Exception:
        return False

