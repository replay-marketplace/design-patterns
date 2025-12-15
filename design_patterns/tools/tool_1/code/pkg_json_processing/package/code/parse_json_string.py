"""
Parse JSON string function - Parse JSON string to dict.
"""

import json


def parse_json_string(json_str: str) -> dict:
    """
    Parse a JSON string into a dictionary.

    Args:
        json_str: The JSON string to parse.

    Returns:
        The parsed JSON data as a dictionary. Returns empty dict if parsing fails.

    Example:
        >>> parse_json_string('{"key": "value"}')
        {'key': 'value'}
    """
    try:
        return json.loads(json_str)
    except Exception:
        return {}

