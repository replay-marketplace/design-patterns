"""Basic JSON processing functions."""

import json
import os
from typing import Union
from jsonschema import validate, ValidationError


def load_json_from_file(filepath: str) -> dict:
    """Load JSON from file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Dictionary containing the JSON data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json_to_file(data: dict, filepath: str) -> bool:
    """Save JSON to file.
    
    Args:
        data: Dictionary to save as JSON
        filepath: Path where to save the file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON to file: {e}")
        return False


def dict_to_json_string(data: dict, pretty: bool = True) -> str:
    """Convert dict to JSON string.
    
    Args:
        data: Dictionary to convert
        pretty: If True, format with indentation
        
    Returns:
        JSON string representation
    """
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        return json.dumps(data, ensure_ascii=False)


def parse_json_string(json_str: str) -> dict:
    """Parse JSON string to dict.
    
    Args:
        json_str: JSON string to parse
        
    Returns:
        Dictionary parsed from JSON string
        
    Raises:
        json.JSONDecodeError: If string contains invalid JSON
    """
    return json.loads(json_str)


def load_json_string_from_file(filepath: str) -> str:
    """Load JSON string from file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Raw JSON string from file
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def save_json_string_to_file(json_str: str, filepath: str) -> bool:
    """Save JSON string to file.
    
    Args:
        json_str: JSON string to save
        filepath: Path where to save the file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Validate that it's valid JSON
        json.loads(json_str)
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
        return True
    except Exception as e:
        print(f"Error saving JSON string to file: {e}")
        return False


def validate_json_schema(data: dict, schema: dict) -> bool:
    """Validate JSON data against a schema.
    
    Args:
        data: JSON data to validate
        schema: JSON schema to validate against
        
    Returns:
        True if valid, False otherwise
    """
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        print(f"Validation error: {e.message}")
        return False
    except Exception as e:
        print(f"Error during validation: {e}")
        return False
