"""
Get JSON directory schema.
"""


def get_json_dir_schema() -> dict:
    """
    Returns the schema of the json_dir file.
    
    Returns:
        dict: JSON schema for directory structure
    """
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Directory Structure Schema",
        "description": "Schema for representing file system directory structures in JSON",
        "type": "object",
        "required": ["type", "name"],
        "properties": {
            "type": {
                "type": "string",
                "enum": ["directory", "file"],
                "description": "Type of the node (directory or file)"
            },
            "name": {
                "type": "string",
                "description": "Name of the directory or file"
            },
            "children": {
                "type": "array",
                "description": "Child nodes (only for directories)",
                "items": {
                    "$ref": "#"
                }
            },
            "content": {
                "type": "string",
                "description": "File content (only for files)"
            }
        },
        "allOf": [
            {
                "if": {
                    "properties": {"type": {"const": "directory"}}
                },
                "then": {
                    "required": ["children"]
                }
            },
            {
                "if": {
                    "properties": {"type": {"const": "file"}}
                },
                "then": {
                    "required": ["content"]
                }
            }
        ]
    }
