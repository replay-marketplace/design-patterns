"""
Save JSON to file function - Save JSON to file.
"""

import json
import os
from pathlib import Path


def save_json_to_file(data: dict, filepath: str) -> bool:
    """
    Save JSON data to a file.

    Args:
        data: The dictionary data to save as JSON.
        filepath: The path to the file where JSON should be saved.

    Returns:
        True if the file was successfully written, False otherwise.

    Example:
        >>> save_json_to_file({"key": "value"}, "/tmp/data.json")
        True
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(filepath)
        if directory:
            Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Write JSON to file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception:
        return False

