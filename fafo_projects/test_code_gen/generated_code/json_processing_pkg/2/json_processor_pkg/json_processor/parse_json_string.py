"""
Parse JSON string to dictionary.
"""

import json


def parse_json_string(json_str: str) -> dict:
    """
    Parse a JSON string to a dictionary.
    
    Args:
        json_str (str): JSON string to parse
    
    Returns:
        dict: Parsed dictionary
    
    Raises:
        json.JSONDecodeError: If the string is not valid JSON
    """
    return json.loads(json_str)
