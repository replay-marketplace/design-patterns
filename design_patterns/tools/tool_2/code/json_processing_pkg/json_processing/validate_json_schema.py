"""Validate JSON schema function - Validate structure."""

import json


def validate_json_schema(data: dict, schema: dict) -> bool:
    """
    Validate that a dictionary matches a given schema structure.

    This is a basic validation that checks:
    - Required keys exist
    - Key types match (basic type checking)

    Args:
        data: The dictionary to validate.
        schema: A schema dictionary defining the expected structure.
                Format: {"key": "type"} where type can be "str", "int", "float", "bool", "dict", "list"

    Returns:
        True if the data matches the schema, False otherwise.

    Example:
        >>> data = {'name': 'John', 'age': 30}
        >>> schema = {'name': 'str', 'age': 'int'}
        >>> result = validate_json_schema(data, schema)
        >>> print(result)
        True
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")
    if not isinstance(schema, dict):
        raise TypeError("schema must be a dictionary")
    
    # Check that all required keys from schema exist in data
    for key, expected_type in schema.items():
        if key not in data:
            return False
        
        # Basic type checking
        value = data[key]
        type_map = {
            'str': str,
            'int': int,
            'float': float,
            'bool': bool,
            'dict': dict,
            'list': list,
        }
        
        if expected_type in type_map:
            if not isinstance(value, type_map[expected_type]):
                return False
    
    return True



