"""Dict to JSON string function - Convert dict to JSON string."""

import json


def dict_to_json_string(data: dict, pretty: bool = False) -> str:
    """
    Convert a dictionary to a JSON string.

    Args:
        data: The dictionary to convert to JSON string.
        pretty: If True, format the JSON with indentation. Default is False.

    Returns:
        A JSON string representation of the dictionary.

    Example:
        >>> data = {'key': 'value', 'number': 42}
        >>> json_str = dict_to_json_string(data, pretty=True)
        >>> print(json_str)
        {
          "key": "value",
          "number": 42
        }
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")
    if not isinstance(pretty, bool):
        raise TypeError("pretty must be a boolean")
    
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        return json.dumps(data, ensure_ascii=False)


