"""
Load JSON string from file.
"""

import os


def load_json_string_from_file(filepath: str) -> str:
    """
    Load JSON content from a file as a string (without parsing).
    
    Args:
        filepath (str): Path to the JSON file
    
    Returns:
        str: Raw JSON string content
    
    Raises:
        FileNotFoundError: If the file does not exist
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
