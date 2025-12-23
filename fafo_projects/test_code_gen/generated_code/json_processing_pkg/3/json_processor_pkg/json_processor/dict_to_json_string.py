"""
Convert dict to JSON string.
"""

import json


def dict_to_json_string(data: dict, pretty: bool = False) -> str:
    """
    Convert dictionary to JSON string.
    
    Args:
        data (dict): Dictionary to convert
        pretty (bool): Whether to format with indentation
    
    Returns:
        str: JSON string
    """
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        return json.dumps(data, ensure_ascii=False)
