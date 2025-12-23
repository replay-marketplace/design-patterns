"""Validate JSON against schema"""

import jsonschema
from jsonschema import validate, ValidationError


def validate_json_schema(data: dict, schema: dict) -> bool:
    """Validate JSON data against a schema.
    
    Args:
        data: Dictionary to validate
        schema: JSON schema to validate against
        
    Returns:
        True if data is valid according to schema, False otherwise
    """
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError:
        return False
    except Exception:
        return False
