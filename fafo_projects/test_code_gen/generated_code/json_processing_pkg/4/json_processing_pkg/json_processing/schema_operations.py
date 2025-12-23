"""Schema operations for JSON directory structures."""

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
                "content": "# Example Project\n\nThis is an example project structure."
            },
            {
                "type": "directory",
                "name": "src",
                "children": [
                    {
                        "type": "file",
                        "name": "main.py",
                        "content": "# Main application file\n\nif __name__ == '__main__':\n    print('Hello, World!')"
                    },
                    {
                        "type": "file",
                        "name": "__init__.py",
                        "content": ""
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
                        "content": "# Test file\n\nimport pytest\n\ndef test_example():\n    assert True"
                    }
                ]
            }
        ]
    }


def get_json_dir_schema() -> dict:
    """Returns the JSON schema for the json_dir file structure.
    
    Returns:
        Dictionary representing the JSON schema
    """
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Directory Structure Schema",
        "description": "Schema for representing file system directory structures in JSON",
        "definitions": {
            "file": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "const": "file"
                    },
                    "name": {
                        "type": "string",
                        "description": "Name of the file"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content of the file"
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
                        "type": "string",
                        "description": "Name of the directory"
                    },
                    "children": {
                        "type": "array",
                        "description": "Child files and directories",
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


def _infer_schema_from_value(value: Any) -> Dict:
    """Infer JSON schema from a value.
    
    Args:
        value: Value to infer schema from
        
    Returns:
        Dictionary representing the inferred schema
    """
    if value is None:
        return {"type": "null"}
    elif isinstance(value, bool):
        return {"type": "boolean"}
    elif isinstance(value, int):
        return {"type": "integer"}
    elif isinstance(value, float):
        return {"type": "number"}
    elif isinstance(value, str):
        return {"type": "string"}
    elif isinstance(value, list):
        if len(value) == 0:
            return {"type": "array", "items": {}}
        # Infer from first item
        item_schema = _infer_schema_from_value(value[0])
        return {"type": "array", "items": item_schema}
    elif isinstance(value, dict):
        properties = {}
        required = []
        for key, val in value.items():
            properties[key] = _infer_schema_from_value(val)
            required.append(key)
        return {
            "type": "object",
            "properties": properties,
            "required": required
        }
    else:
        return {}


def generate_json_schema_from_json(input_json_file: str) -> bool:
    """Generate JSON schema from a JSON file and save it to the same location.
    
    Args:
        input_json_file: Path to the input JSON file
        
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
        
        # Merge with inferred schema
        inferred = _infer_schema_from_value(data)
        schema.update(inferred)
        
        # Determine output file path
        base_path = os.path.splitext(input_json_file)[0]
        output_file = f"{base_path}_schema.json"
        
        # Save schema
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        print(f"Schema generated and saved to: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error generating schema: {e}")
        return False
