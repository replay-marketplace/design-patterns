"""Parse JSON string to dictionary"""

import json


def parse_json_string(json_str: str) -> dict:
    """Parse JSON string to dict.
    
    Args:
        json_str: JSON string to parse
        
    Returns:
        Dictionary parsed from JSON string, or empty dict if parsing fails
    """
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, Exception):
        return {}
