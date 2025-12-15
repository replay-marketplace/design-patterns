"""
Validate JSON schema function - Validate structure.
"""

try:
    import jsonschema
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False


def validate_json_schema(data: dict, schema: dict) -> bool:
    """
    Validate a dictionary against a JSON schema.

    Args:
        data: The dictionary data to validate.
        schema: The JSON schema dictionary to validate against.

    Returns:
        True if the data matches the schema, False otherwise. Returns False if jsonschema is not installed.

    Example:
        >>> schema = {"type": "object", "properties": {"key": {"type": "string"}}}
        >>> validate_json_schema({"key": "value"}, schema)
        True
    """
    if not JSONSCHEMA_AVAILABLE:
        return False
    
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except Exception:
        return False

