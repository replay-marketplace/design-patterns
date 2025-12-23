"""
Validate JSON against a schema.
"""

try:
    from jsonschema import validate, ValidationError
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False


def validate_json_schema(data: dict, schema: dict) -> bool:
    """
    Validate JSON data against a JSON schema.
    
    Args:
        data (dict): JSON data to validate
        schema (dict): JSON schema to validate against
    
    Returns:
        bool: True if valid, False otherwise
    
    Note:
        Requires jsonschema package to be installed.
        If not available, returns True with a warning.
    """
    if not JSONSCHEMA_AVAILABLE:
        print("Warning: jsonschema package not installed. Validation skipped.")
        print("Install with: pip install jsonschema")
        return True
    
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        print(f"Validation error: {e.message}")
        return False
    except Exception as e:
        print(f"Error during validation: {e}")
        return False
