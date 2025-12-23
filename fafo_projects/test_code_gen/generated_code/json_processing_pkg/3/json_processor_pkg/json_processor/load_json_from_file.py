"""
Load JSON from file.
"""

import json
import os


def load_json_from_file(filepath: str) -> dict:
    """
    Load JSON data from a file.
    
    Args:
        filepath (str): Path to the JSON file
    
    Returns:
        dict: Parsed JSON data
    
    Raises:
        FileNotFoundError: If the file does not exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
