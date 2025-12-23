"""Convert dictionary to JSON string"""

import json


def dict_to_json_string(data: dict, pretty: bool) -> str:
    """Convert dict to JSON string.
    
    Args:
        data: Dictionary to convert
        pretty: If True, format with indentation; if False, compact format
        
    Returns:
        JSON string representation of the dictionary
    """
    try:
        if pretty:
            return json.dumps(data, indent=2, ensure_ascii=False)
        else:
            return json.dumps(data, ensure_ascii=False)
    except Exception:
        return '{}'
