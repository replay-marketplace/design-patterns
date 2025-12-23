"""
Parse JSON string to dict.
"""

import json


def parse_json_string(json_str: str) -> dict:
    """
    Parse JSON string to dictionary.
    
    Args:
        json_str (str): JSON string to parse
    
    Returns:
        dict: Parsed dictionary
    
    Raises:
        json.JSONDecodeError: If the string contains invalid JSON
    """
    return json.loads(json_str)
