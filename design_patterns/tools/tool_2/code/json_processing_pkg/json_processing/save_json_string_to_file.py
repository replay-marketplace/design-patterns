"""Save JSON string to file function - Save JSON string to file."""

from pathlib import Path


def save_json_string_to_file(json_str: str, filepath: str) -> bool:
    """
    Save a JSON string to a file.

    Args:
        json_str: The JSON string to save.
        filepath: The path where the JSON file should be saved.

    Returns:
        True if the file was successfully saved, False otherwise.

    Example:
        >>> json_str = '{"key": "value", "number": 42}'
        >>> result = save_json_string_to_file(json_str, "/tmp/data.json")
        >>> print(result)
        True
    """
    if not isinstance(json_str, str):
        raise TypeError("json_str must be a string")
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    
    try:
        # Create parent directories if they don't exist
        filepath_obj = Path(filepath)
        filepath_obj.parent.mkdir(parents=True, exist_ok=True)
        
        # Write JSON string to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
        
        return True
    except Exception:
        return False



