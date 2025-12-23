"""Basic JSON processing functions."""

import json
import os
from typing import Union

# Import from file_processing package
try:
    from file_processing import (
        save_text_to_file,
        read_file_content,
        file_exists
    )
except ImportError:
    raise ImportError("file_processing package is required. Install with: pip3 install -e ../file_processing_pkg/5/file_processing_pkg/")


def load_json_from_file(filepath: str) -> dict:
    """Load JSON from file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Dictionary containing the JSON data
        
    Raises:
        FileNotFoundError: If file does not exist
        ValueError: If file contains invalid JSON
    """
    if not file_exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    content = read_file_content(filepath)
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {filepath}: {str(e)}")


def save_json_to_file(data: dict, filepath: str) -> bool:
    """Save JSON to file.
    
    Args:
        data: Dictionary to save as JSON
        filepath: Path where to save the file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        directory = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        
        if not directory:
            directory = "."
        
        return save_text_to_file(json_str, directory, filename)
    except Exception as e:
        print(f"Error saving JSON to file: {str(e)}")
        return False


def dict_to_json_string(data: dict, pretty: bool = True) -> str:
    """Convert dict to JSON string.
    
    Args:
        data: Dictionary to convert
        pretty: If True, format with indentation; if False, compact format
        
    Returns:
        JSON string representation
    """
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        return json.dumps(data, separators=(',', ':'), ensure_ascii=False)


def parse_json_string(json_str: str) -> dict:
    """Parse JSON string to dict.
    
    Args:
        json_str: JSON string to parse
        
    Returns:
        Dictionary parsed from JSON
        
    Raises:
        ValueError: If string is not valid JSON
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {str(e)}")


def load_json_string_from_file(filepath: str) -> str:
    """Load JSON string from file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Raw JSON string content
        
    Raises:
        FileNotFoundError: If file does not exist
    """
    if not file_exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return read_file_content(filepath)


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
        
        directory = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        
        if not directory:
            directory = "."
        
        return save_text_to_file(json_str, directory, filename)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON string: {str(e)}")
        return False
    except Exception as e:
        print(f"Error saving JSON string to file: {str(e)}")
        return False


def validate_json_schema(data: dict, schema: dict) -> bool:
    """Validate structure of JSON data against a simple schema.
    
    Args:
        data: Dictionary to validate
        schema: Dictionary mapping keys to expected types
        
    Returns:
        True if data matches schema, False otherwise
        
    Example:
        schema = {"name": str, "age": int, "active": bool}
        data = {"name": "John", "age": 30, "active": True}
        validate_json_schema(data, schema)  # Returns True
    """
    try:
        for key, expected_type in schema.items():
            if key not in data:
                return False
            
            if not isinstance(data[key], expected_type):
                return False
        
        return True
    except Exception:
        return False
