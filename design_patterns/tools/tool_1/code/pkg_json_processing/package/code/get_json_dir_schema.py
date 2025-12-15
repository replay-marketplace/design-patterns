"""
Get JSON dir schema function - Returns the schema of the json_dir file.
"""


def get_json_dir_schema() -> dict:
    """
    Returns the JSON schema for the json_dir file structure.

    Returns:
        A dictionary representing the JSON schema for json_dir structure.

    Example:
        >>> schema = get_json_dir_schema()
        >>> isinstance(schema, dict)
        True
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

