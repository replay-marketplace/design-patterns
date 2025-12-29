"""Load JSON from file function - Load JSON from file."""

import json
from pathlib import Path


def load_json_from_file(filepath: str) -> dict:
    """
    Load JSON data from a file.

    Args:
        filepath: The path to the JSON file to load.

    Returns:
        A dictionary containing the parsed JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.

    Example:
        >>> data = load_json_from_file("/tmp/data.json")
        >>> print(data)
        {'key': 'value'}
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    
    filepath_obj = Path(filepath)
    if not filepath_obj.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data



