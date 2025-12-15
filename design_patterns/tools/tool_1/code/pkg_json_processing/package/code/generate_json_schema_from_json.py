"""
Generate JSON schema from JSON function - Saves to the same location.
"""

import os
from .load_json_from_file import load_json_from_file
from .save_json_to_file import save_json_to_file

try:
    import jsonschema
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False


def generate_json_schema_from_json(input_json_file: str) -> bool:
    """
    Generate a JSON schema from a JSON file and save it to the same location.

    Args:
        input_json_file: The path to the JSON file to generate schema from.

    Returns:
        True if the schema was successfully generated and saved, False otherwise.

    Example:
        >>> generate_json_schema_from_json("/tmp/data.json")
        True
    """
    if not JSONSCHEMA_AVAILABLE:
        return False
    
    try:
        # Load the JSON data
        data = load_json_from_file(input_json_file)
        if not data:
            return False
        
        # Generate schema using jsonschema
        # Note: jsonschema doesn't have a built-in generator, so we'll use a simple approach
        # For a more robust solution, you might want to use a library like genson
        schema = _infer_schema(data)
        
        # Save schema to same location with _schema suffix
        base_path = os.path.splitext(input_json_file)[0]
        schema_file = f"{base_path}_schema.json"
        
        return save_json_to_file(schema, schema_file)
    except Exception:
        return False


def _infer_schema(data, root=True):
    """
    Infer a basic JSON schema from data structure.
    This is a simple implementation - for production use, consider using genson or similar.
    """
    if isinstance(data, dict):
        schema = {
            "type": "object",
            "properties": {},
            "required": []
        }
        for key, value in data.items():
            schema["properties"][key] = _infer_schema(value, root=False)
            schema["required"].append(key)
        return schema
    elif isinstance(data, list):
        if len(data) > 0:
            item_schema = _infer_schema(data[0], root=False)
            return {
                "type": "array",
                "items": item_schema
            }
        else:
            return {
                "type": "array",
                "items": {}
            }
    elif isinstance(data, bool):
        return {"type": "boolean"}
    elif isinstance(data, int):
        return {"type": "integer"}
    elif isinstance(data, float):
        return {"type": "number"}
    elif isinstance(data, str):
        return {"type": "string"}
    elif data is None:
        return {"type": "null"}
    else:
        return {}

