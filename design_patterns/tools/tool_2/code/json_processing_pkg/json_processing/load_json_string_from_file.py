"""Load JSON string from file function - Load JSON string from file."""

from pathlib import Path


def load_json_string_from_file(filepath: str) -> str:
    """
    Load JSON content from a file as a string (without parsing).

    Args:
        filepath: The path to the JSON file to load.

    Returns:
        The JSON content as a string.

    Raises:
        FileNotFoundError: If the file does not exist.

    Example:
        >>> json_str = load_json_string_from_file("/tmp/data.json")
        >>> print(json_str)
        {"key": "value"}
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    
    filepath_obj = Path(filepath)
    if not filepath_obj.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content


