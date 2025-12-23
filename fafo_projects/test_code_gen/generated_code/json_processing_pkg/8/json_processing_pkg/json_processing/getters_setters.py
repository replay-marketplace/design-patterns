"""Getter and setter functions for JSON schemas and examples."""

import json
import os
from typing import Any, Dict


def get_json_dir_example() -> dict:
    """Returns an example of the json_dir file structure.
    
    Returns:
        Dictionary representing an example directory structure
    """
    return {
        "type": "directory",
        "name": "example_project",
        "children": [
            {
                "type": "file",
                "name": "README.md",
                "content": "# Example Project\n\nThis is an example project structure.\n"
            },
            {
                "type": "directory",
                "name": "src",
                "children": [
                    {
                        "type": "file",
                        "name": "main.py",
                        "content": "# Main application file\n\nif __name__ == '__main__':\n    print('Hello, World!')\n"
                    },
                    {
                        "type": "file",
                        "name": "utils.py",
                        "content": "# Utility functions\n\ndef helper():\n    pass\n"
                    }
                ]
            },
            {
                "type": "directory",
                "name": "tests",
                "children": [
                    {
                        "type": "file",
                        "name": "test_main.py",
                        "content": "# Test file\n\nimport pytest\n\ndef test_example():\n    assert True\n"
                    }
                ]
            }
        ]
    }


def get_json_dir_schema() -> dict:
    """Returns the JSON schema for directory structure validation.
    
    Returns:
        Dictionary representing the JSON schema
    """
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Directory Structure Schema",
        "description": "Schema for validating directory and file structures",
        "definitions": {
            "file": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "const": "file"
                    },
                    "name": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": ["type", "name", "content"],
                "additionalProperties": False
            },
            "directory": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "const": "directory"
                    },
                    "name": {
                        "type": "string"
                    },
                    "children": {
                        "type": "array",
                        "items": {
                            "oneOf": [
                                {"$ref": "#/definitions/file"},
                                {"$ref": "#/definitions/directory"}
                            ]
                        }
                    }
                },
                "required": ["type", "name", "children"],
                "additionalProperties": False
            }
        },
        "oneOf": [
            {"$ref": "#/definitions/file"},
            {"$ref": "#/definitions/directory"}
        ]
    }


def _infer_type(value: Any) -> str:
    """Infer JSON schema type from Python value.
    
    Args:
        value: Python value to infer type from
        
    Returns:
        JSON schema type string
    """
    if isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "number"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, list):
        return "array"
    elif isinstance(value, dict):
        return "object"
    elif value is None:
        return "null"
    else:
        return "string"


def _generate_schema_from_dict(data: Dict) -> Dict:
    """Generate JSON schema from a dictionary.
    
    Args:
        data: Dictionary to generate schema from
        
    Returns:
        JSON schema dictionary
    """
    schema = {
        "type": "object",
        "properties": {},
        "required": []
    }
    
    for key, value in data.items():
        schema["required"].append(key)
        
        if isinstance(value, dict):
            schema["properties"][key] = _generate_schema_from_dict(value)
        elif isinstance(value, list):
            if len(value) > 0:
                item_type = _infer_type(value[0])
                if item_type == "object":
                    schema["properties"][key] = {
                        "type": "array",
                        "items": _generate_schema_from_dict(value[0])
                    }
                else:
                    schema["properties"][key] = {
                        "type": "array",
                        "items": {"type": item_type}
                    }
            else:
                schema["properties"][key] = {
                    "type": "array",
                    "items": {}
                }
        else:
            schema["properties"][key] = {
                "type": _infer_type(value)
            }
    
    return schema


def generate_json_schema_from_json(input_json_file: str) -> bool:
    """Generate JSON schema from a JSON file and save it to the same location.
    
    Args:
        input_json_file: Path to input JSON file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Load the JSON file
        with open(input_json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Generate schema
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Generated Schema",
            "description": f"Auto-generated schema from {os.path.basename(input_json_file)}"
        }
        
        if isinstance(data, dict):
            schema.update(_generate_schema_from_dict(data))
        elif isinstance(data, list):
            schema["type"] = "array"
            if len(data) > 0 and isinstance(data[0], dict):
                schema["items"] = _generate_schema_from_dict(data[0])
            else:
                schema["items"] = {"type": _infer_type(data[0]) if len(data) > 0 else "string"}
        else:
            schema["type"] = _infer_type(data)
        
        # Generate output filename
        base_path = os.path.dirname(input_json_file)
        base_name = os.path.splitext(os.path.basename(input_json_file))[0]
        output_file = os.path.join(base_path, f"{base_name}_schema.json")
        
        # Save schema
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception as e:
        print(f"Error generating schema: {e}")
        return False
