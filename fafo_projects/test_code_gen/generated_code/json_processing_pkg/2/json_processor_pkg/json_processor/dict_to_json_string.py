"""
Convert dictionary to JSON string.
"""

import json


def dict_to_json_string(data: dict, pretty: bool = False) -> str:
    """
    Convert a dictionary to a JSON string.
    
    Args:
        data (dict): Dictionary to convert
        pretty (bool): If True, format with indentation for readability
    
    Returns:
        str: JSON string representation of the dictionary
    """
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        return json.dumps(data, ensure_ascii=False)
