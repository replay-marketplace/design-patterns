"""
Load JSON from file function - Load JSON from file.
"""

import json
from pkg_file_processing.code.read_file_content import read_file_content


def load_json_from_file(filepath: str) -> dict:
    """
    Load JSON data from a file.

    Args:
        filepath: The path to the JSON file to load.

    Returns:
        The parsed JSON data as a dictionary. Returns empty dict if file doesn't exist or can't be parsed.

    Example:
        >>> data = load_json_from_file("/tmp/data.json")
        >>> isinstance(data, dict)
        True
    """
    try:
        content = read_file_content(filepath)
        if not content:
            return {}
        return json.loads(content)
    except Exception:
        return {}

