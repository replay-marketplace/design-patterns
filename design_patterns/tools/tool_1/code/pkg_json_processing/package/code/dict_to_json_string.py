"""
Dict to JSON string function - Convert dict to JSON string.
"""

import json


def dict_to_json_string(data: dict, pretty: bool) -> str:
    """
    Convert a dictionary to a JSON string.

    Args:
        data: The dictionary to convert to JSON string.
        pretty: If True, format the JSON with indentation. If False, use compact format.

    Returns:
        The JSON string representation of the dictionary. Returns empty string if conversion fails.

    Example:
        >>> dict_to_json_string({"key": "value"}, True)
        '{\\n  "key": "value"\\n}'
    """
    try:
        if pretty:
            return json.dumps(data, indent=2, ensure_ascii=False)
        else:
            return json.dumps(data, ensure_ascii=False)
    except Exception:
        return ""

