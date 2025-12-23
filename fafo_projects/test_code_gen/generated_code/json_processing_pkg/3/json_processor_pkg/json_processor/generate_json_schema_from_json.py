"""
Generate JSON schema from JSON file.
"""

import json
import os
from typing import Any, Dict


def generate_json_schema_from_json(input_json_file: str) -> bool:
    """
    Generate and save JSON schema from a JSON file.
    Saves the schema to the same location with '_schema.json' suffix.
    
    Args:
        input_json_file (str): Path to input JSON file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Load the JSON file
        with open(input_json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Generate schema
        schema = _infer_schema(data)
        
        # Create output filename
        base_name = os.path.splitext(input_json_file)[0]
        schema_file = f"{base_name}_schema.json"
        
        # Save schema
        with open(schema_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        print(f"Schema saved to: {schema_file}")
        return True
    except Exception as e:
        print(f"Error generating schema: {e}")
        return False


def _infer_schema(data: Any) -> Dict:
    """
    Infer JSON schema from data.
    
    Args:
        data: Data to infer schema from
    
    Returns:
        dict: Inferred JSON schema
    """
    if data is None:
        return {"type": "null"}
    elif isinstance(data, bool):
        return {"type": "boolean"}
    elif isinstance(data, int):
        return {"type": "integer"}
    elif isinstance(data, float):
        return {"type": "number"}
    elif isinstance(data, str):
        return {"type": "string"}
    elif isinstance(data, list):
        if len(data) == 0:
            return {"type": "array", "items": {}}
        # Infer schema from first item
        item_schema = _infer_schema(data[0])
        return {"type": "array", "items": item_schema}
    elif isinstance(data, dict):
        properties = {}
        required = []
        for key, value in data.items():
            properties[key] = _infer_schema(value)
            required.append(key)
        return {
            "type": "object",
            "properties": properties,
            "required": required
        }
    else:
        return {}
