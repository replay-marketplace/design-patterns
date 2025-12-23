"""Generate JSON schema from JSON function - Saves to the same location."""

import json
from pathlib import Path


def generate_json_schema_from_json(input_json_file: str) -> bool:
    """
    Generate a JSON schema from a JSON file and save it to the same location.

    The schema file will be saved with the same name but with "_schema.json" suffix.

    Args:
        input_json_file: The path to the input JSON file.

    Returns:
        True if the schema was successfully generated and saved, False otherwise.

    Example:
        >>> result = generate_json_schema_from_json("/tmp/data.json")
        >>> print(result)
        True
        # Creates /tmp/data_schema.json
    """
    if not isinstance(input_json_file, str):
        raise TypeError("input_json_file must be a string")
    
    try:
        # Load the JSON data
        filepath_obj = Path(input_json_file)
        if not filepath_obj.exists():
            raise FileNotFoundError(f"File not found: {input_json_file}")
        
        with open(input_json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Generate basic schema
        schema = _generate_schema_from_data(data)
        
        # Create output filepath
        schema_filepath = filepath_obj.parent / f"{filepath_obj.stem}_schema.json"
        
        # Save schema
        schema_filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(schema_filepath, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception:
        return False


def _generate_schema_from_data(data):
    """Generate a basic schema from JSON data."""
    if isinstance(data, dict):
        schema = {
            "type": "object",
            "properties": {}
        }
        for key, value in data.items():
            schema["properties"][key] = _get_type_schema(value)
        return schema
    elif isinstance(data, list):
        if len(data) > 0:
            return {
                "type": "array",
                "items": _get_type_schema(data[0])
            }
        else:
            return {"type": "array"}
    else:
        return _get_type_schema(data)


def _get_type_schema(value):
    """Get schema for a single value."""
    if isinstance(value, dict):
        return _generate_schema_from_data(value)
    elif isinstance(value, list):
        if len(value) > 0:
            return {
                "type": "array",
                "items": _get_type_schema(value[0])
            }
        else:
            return {"type": "array"}
    elif isinstance(value, str):
        return {"type": "string"}
    elif isinstance(value, int):
        return {"type": "integer"}
    elif isinstance(value, float):
        return {"type": "number"}
    elif isinstance(value, bool):
        return {"type": "boolean"}
    else:
        return {"type": "null"}

