"""Parse JSON string function - Parse JSON string to dict."""

import json


def parse_json_string(json_str: str) -> dict:
    """
    Parse a JSON string into a dictionary.

    Args:
        json_str: The JSON string to parse.

    Returns:
        A dictionary containing the parsed JSON data.

    Raises:
        json.JSONDecodeError: If the string contains invalid JSON.

    Example:
        >>> json_str = '{"key": "value", "number": 42}'
        >>> data = parse_json_string(json_str)
        >>> print(data)
        {'key': 'value', 'number': 42}
    """
    if not isinstance(json_str, str):
        raise TypeError("json_str must be a string")
    
    return json.loads(json_str)


