"""Save JSON to file function - Save JSON to file."""

import json
from pathlib import Path


def save_json_to_file(data: dict, filepath: str) -> bool:
    """
    Save a dictionary as JSON to a file.

    Args:
        data: The dictionary to save as JSON.
        filepath: The path where the JSON file should be saved.

    Returns:
        True if the file was successfully saved, False otherwise.

    Example:
        >>> data = {'key': 'value', 'number': 42}
        >>> result = save_json_to_file(data, "/tmp/data.json")
        >>> print(result)
        True
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    
    try:
        # Create parent directories if they don't exist
        filepath_obj = Path(filepath)
        filepath_obj.parent.mkdir(parents=True, exist_ok=True)
        
        # Write JSON to file with pretty formatting
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception:
        return False


