"""
Validate JSON schema.
"""

import jsonschema
from jsonschema import validate, ValidationError


def validate_json_schema(data: dict, schema: dict) -> bool:
    """
    Validate JSON data against a schema.
    
    Args:
        data (dict): Data to validate
        schema (dict): JSON schema
    
    Returns:
        bool: True if valid, False otherwise
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
