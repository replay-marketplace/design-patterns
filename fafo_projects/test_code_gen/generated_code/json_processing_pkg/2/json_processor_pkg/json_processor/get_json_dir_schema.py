"""
Get JSON directory structure schema.
"""


def get_json_dir_schema() -> dict:
    """
    Returns the JSON schema for directory structures.
    
    Returns:
        dict: JSON schema for validating directory structures
    """
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["type", "name"],
        "properties": {
            "type": {
                "type": "string",
                "enum": ["directory", "file"]
            },
            "name": {
                "type": "string"
            },
            "content": {
                "type": "string"
            },
            "children": {
                "type": "array",
                "items": {
                    "$ref": "#"
                }
            }
        },
        "if": {
            "properties": {
                "type": {"const": "file"}
            }
        },
        "then": {
            "required": ["content"]
        },
        "else": {
            "required": ["children"]
        }
    }
