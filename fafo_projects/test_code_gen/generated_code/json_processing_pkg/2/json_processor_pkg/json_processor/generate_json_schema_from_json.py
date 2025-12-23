"""
Generate JSON schema from JSON file.
"""

import json
import os
from .load_json_from_file import load_json_from_file
from .save_json_to_file import save_json_to_file


def infer_type(value):
    """
    Infer JSON schema type from a Python value.
    
    Args:
        value: Python value to infer type from
    
    Returns:
        str or list: JSON schema type(s)
    """
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "number"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, list):
        return "array"
    elif isinstance(value, dict):
        return "object"
    else:
        return "string"


def generate_schema_from_data(data):
    """
    Generate a JSON schema from data.
    
    Args:
        data: Data to generate schema from
    
    Returns:
        dict: Generated JSON schema
    """
    if isinstance(data, dict):
        schema = {
            "type": "object",
            "properties": {}
        }
        
        for key, value in data.items():
            schema["properties"][key] = generate_schema_from_data(value)
        
        return schema
    
    elif isinstance(data, list):
        schema = {
            "type": "array"
        }
        
        if data:
            # Infer schema from first item
            schema["items"] = generate_schema_from_data(data[0])
        
        return schema
    
    else:
        return {
            "type": infer_type(data)
        }


def generate_json_schema_from_json(input_json_file: str) -> str:
    """
    Generate a JSON schema from a JSON file and save it to the same location.
    
    Args:
        input_json_file (str): Path to the input JSON file
    
    Returns:
        str: Path to the generated schema file
    
    Raises:
        FileNotFoundError: If the input file does not exist
    """
    # Load the JSON data
    data = load_json_from_file(input_json_file)
    
    # Generate schema
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated Schema",
        "description": f"Auto-generated schema from {os.path.basename(input_json_file)}"
    }
    
    # Merge with inferred schema
    inferred = generate_schema_from_data(data)
    schema.update(inferred)
    
    # Determine output file path
    base_path = os.path.splitext(input_json_file)[0]
    schema_file = f"{base_path}_schema.json"
    
    # Save schema
    save_json_to_file(schema, schema_file)
    
    return schema_file
