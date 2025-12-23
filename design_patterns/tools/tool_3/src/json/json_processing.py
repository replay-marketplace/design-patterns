"""JSON processing functions for file, dict, string operations and directory conversion."""

import json
import os
from pathlib import Path
from typing import Dict, Any
import jsonschema
from jsonschema import validate, ValidationError


# ============================================================================
# Basic: File / Dict / String / Helper
# ============================================================================

def load_json_from_file(filepath: str) -> dict:
    """
    Load JSON from file and return as dictionary.

    Args:
        filepath: Path to the JSON file.

    Returns:
        dict: The parsed JSON data as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        ValueError: If filepath is invalid.

    Example:
        >>> data = load_json_from_file("config.json")
        >>> print(data)
    """
    if not filepath or not isinstance(filepath, str):
        raise ValueError("filepath must be a non-empty string")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file {filepath}: {str(e)}", e.doc, e.pos)
    except Exception as e:
        raise Exception(f"Error reading file {filepath}: {str(e)}")


def save_json_to_file(data: dict, filepath: str) -> bool:
    """
    Save dictionary to JSON file.

    Args:
        data: Dictionary to save as JSON.
        filepath: Path where to save the JSON file.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If filepath is invalid or data is not serializable.

    Example:
        >>> data = {"name": "John", "age": 30}
        >>> save_json_to_file(data, "output.json")
        True
    """
    if not filepath or not isinstance(filepath, str):
        raise ValueError("filepath must be a non-empty string")

    if not isinstance(data, dict):
        raise ValueError("data must be a dictionary")

    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except (TypeError, ValueError) as e:
        raise ValueError(f"Data is not JSON serializable: {str(e)}")
    except Exception as e:
        raise Exception(f"Error writing file {filepath}: {str(e)}")


def dict_to_json_string(data: dict, pretty: bool = False) -> str:
    """
    Convert dictionary to JSON string.

    Args:
        data: Dictionary to convert.
        pretty: If True, format with indentation. Default is False.

    Returns:
        str: JSON string representation of the dictionary.

    Raises:
        ValueError: If data is not serializable.

    Example:
        >>> data = {"name": "John", "age": 30}
        >>> json_str = dict_to_json_string(data, pretty=True)
        >>> print(json_str)
    """
    if not isinstance(data, dict):
        raise ValueError("data must be a dictionary")

    try:
        if pretty:
            return json.dumps(data, indent=2, ensure_ascii=False)
        else:
            return json.dumps(data, ensure_ascii=False)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Data is not JSON serializable: {str(e)}")


def parse_json_string(json_str: str) -> dict:
    """
    Parse JSON string to dictionary.

    Args:
        json_str: JSON string to parse.

    Returns:
        dict: Parsed JSON as dictionary.

    Raises:
        json.JSONDecodeError: If the string contains invalid JSON.
        ValueError: If json_str is invalid.

    Example:
        >>> json_str = '{"name": "John", "age": 30}'
        >>> data = parse_json_string(json_str)
        >>> print(data)
    """
    if not json_str or not isinstance(json_str, str):
        raise ValueError("json_str must be a non-empty string")

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON string: {str(e)}", e.doc, e.pos)


def load_json_string_from_file(filepath: str) -> str:
    """
    Load JSON string from file without parsing.

    Args:
        filepath: Path to the JSON file.

    Returns:
        str: The raw JSON string content from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If filepath is invalid.

    Example:
        >>> json_str = load_json_string_from_file("config.json")
        >>> print(json_str)
    """
    if not filepath or not isinstance(filepath, str):
        raise ValueError("filepath must be a non-empty string")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        raise Exception(f"Error reading file {filepath}: {str(e)}")


def save_json_string_to_file(json_str: str, filepath: str) -> bool:
    """
    Save JSON string to file.

    Args:
        json_str: JSON string to save.
        filepath: Path where to save the file.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If filepath or json_str is invalid.

    Example:
        >>> json_str = '{"name": "John", "age": 30}'
        >>> save_json_string_to_file(json_str, "output.json")
        True
    """
    if not filepath or not isinstance(filepath, str):
        raise ValueError("filepath must be a non-empty string")

    if not json_str or not isinstance(json_str, str):
        raise ValueError("json_str must be a non-empty string")

    try:
        # Validate JSON before saving
        json.loads(json_str)

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
        return True
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {str(e)}")
    except Exception as e:
        raise Exception(f"Error writing file {filepath}: {str(e)}")


def validate_json_schema(data: dict, schema: dict) -> bool:
    """
    Validate dictionary structure against JSON schema.

    Args:
        data: Dictionary to validate.
        schema: JSON schema dictionary to validate against.

    Returns:
        bool: True if data matches schema, False otherwise.

    Raises:
        ValidationError: If data does not match schema.
        ValueError: If data or schema is invalid.

    Example:
        >>> data = {"name": "John", "age": 30}
        >>> schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        >>> validate_json_schema(data, schema)
        True
    """
    if not isinstance(data, dict):
        raise ValueError("data must be a dictionary")

    if not isinstance(schema, dict):
        raise ValueError("schema must be a dictionary")

    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        raise ValidationError(f"Schema validation failed: {str(e)}")
    except jsonschema.SchemaError as e:
        raise ValueError(f"Invalid schema: {str(e)}")


# ============================================================================
# Getters / Setters
# ============================================================================

def get_json_dir_example() -> str:
    """
    Returns an example of the json_dir file.

    Returns:
        str: JSON string containing the example directory structure.

    Example:
        >>> example = get_json_dir_example()
        >>> print(example)
    """
    example_file = os.path.join(os.path.dirname(__file__), "json_template_example.json")
    return load_json_string_from_file(example_file)


def get_json_dir_schema() -> str:
    """
    Returns the schema of the json_dir file.

    Returns:
        str: JSON string containing the schema for directory structure.

    Example:
        >>> schema = get_json_dir_schema()
        >>> print(schema)
    """
    schema_file = os.path.join(os.path.dirname(__file__), "json_template_schema.json")
    return load_json_string_from_file(schema_file)


def generate_json_schema_from_json(input_json_file: str) -> bool:
    """
    Generate JSON schema from a JSON file and save it to the same location.

    Args:
        input_json_file: Path to the input JSON file.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If input_json_file is invalid.

    Example:
        >>> generate_json_schema_from_json("data.json")
        True
        # Creates data_schema.json in the same directory
    """
    if not input_json_file or not isinstance(input_json_file, str):
        raise ValueError("input_json_file must be a non-empty string")

    if not os.path.exists(input_json_file):
        raise FileNotFoundError(f"File not found: {input_json_file}")

    try:
        # Load the JSON data
        data = load_json_from_file(input_json_file)

        # Generate schema using genson library if available, otherwise use a simple approach
        try:
            from genson import SchemaBuilder
            builder = SchemaBuilder()
            builder.add_object(data)
            schema = builder.to_schema()

            # Add schema metadata
            schema["$schema"] = "http://json-schema.org/draft-07/schema#"
            if "title" not in schema:
                schema["title"] = "Generated Schema"

            # Save schema to same location with _schema suffix
            base_path = Path(input_json_file)
            schema_file = base_path.parent / f"{base_path.stem}_schema{base_path.suffix}"
            save_json_to_file(schema, str(schema_file))
            return True
        except ImportError:
            # Fallback: create a basic schema structure
            # This is a simplified schema generator
            schema = _generate_basic_schema(data)
            schema["$schema"] = "http://json-schema.org/draft-07/schema#"
            schema["title"] = "Generated Schema"

            base_path = Path(input_json_file)
            schema_file = base_path.parent / f"{base_path.stem}_schema{base_path.suffix}"
            save_json_to_file(schema, str(schema_file))
            return True

    except Exception as e:
        raise Exception(f"Error generating schema: {str(e)}")


def _generate_basic_schema(data: Any) -> dict:
    """
    Generate a basic JSON schema from data structure.

    Args:
        data: The data to generate schema from.

    Returns:
        dict: Basic JSON schema.
    """
    if isinstance(data, dict):
        schema = {"type": "object", "properties": {}, "required": []}
        for key, value in data.items():
            schema["properties"][key] = _generate_basic_schema(value)
            schema["required"].append(key)
        return schema
    elif isinstance(data, list):
        if len(data) > 0:
            return {"type": "array", "items": _generate_basic_schema(data[0])}
        else:
            return {"type": "array"}
    elif isinstance(data, str):
        return {"type": "string"}
    elif isinstance(data, int):
        return {"type": "integer"}
    elif isinstance(data, float):
        return {"type": "number"}
    elif isinstance(data, bool):
        return {"type": "boolean"}
    elif data is None:
        return {"type": "null"}
    else:
        return {"type": "string"}  # Default fallback


# ============================================================================
# Advanced
# ============================================================================

def load_directory_to_json(directory: str) -> dict:
    """
    Convert directory structure to JSON representation (always recursive).

    The output follows the json_dir format:
    {
        "files": {"filename": "content"},
        "directories": {"dirname": {...}}
    }

    Args:
        directory: Path to the directory to convert.

    Returns:
        dict: JSON structure representing the directory with files and subdirectories.

    Raises:
        FileNotFoundError: If directory does not exist.
        ValueError: If directory is invalid.

    Example:
        >>> json_data = load_directory_to_json("/path/to/dir")
        >>> print(json_data)
    """
    if not directory or not isinstance(directory, str):
        raise ValueError("directory must be a non-empty string")

    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    if not os.path.isdir(directory):
        raise ValueError(f"Path is not a directory: {directory}")

    result = {"files": {}, "directories": {}}

    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            if os.path.isfile(item_path):
                # Read file content
                try:
                    with open(item_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    result["files"][item] = content
                except UnicodeDecodeError:
                    # Binary file - store as base64 or skip
                    # For now, we'll skip binary files or store a placeholder
                    result["files"][item] = f"[Binary file: {item}]"
                except Exception as e:
                    result["files"][item] = f"[Error reading file: {str(e)}]"

            elif os.path.isdir(item_path):
                # Recursively process subdirectory
                result["directories"][item] = load_directory_to_json(item_path)

    except Exception as e:
        raise Exception(f"Error processing directory {directory}: {str(e)}")

    return result


def store_json_to_directory(data: dict, directory: str) -> bool:
    """
    Store JSON directory structure to filesystem.

    Takes a JSON structure in the json_dir format and recreates the directory
    structure with files.

    Args:
        data: JSON structure with "files" and "directories" keys.
        directory: Target directory path where to store the structure.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If data or directory is invalid.

    Example:
        >>> data = {
        ...     "files": {"file1.txt": "content1"},
        ...     "directories": {"subdir": {"files": {"file2.txt": "content2"}}}
        ... }
        >>> store_json_to_directory(data, "/path/to/output")
        True
    """
    if not isinstance(data, dict):
        raise ValueError("data must be a dictionary")

    if not directory or not isinstance(directory, str):
        raise ValueError("directory must be a non-empty string")

    # Validate structure
    if "files" not in data or "directories" not in data:
        raise ValueError('data must contain "files" and "directories" keys')

    if not isinstance(data["files"], dict):
        raise ValueError('data["files"] must be a dictionary')

    if not isinstance(data["directories"], dict):
        raise ValueError('data["directories"] must be a dictionary')

    try:
        # Create target directory
        os.makedirs(directory, exist_ok=True)

        # Write files
        for filename, content in data["files"].items():
            file_path = os.path.join(directory, filename)
            # Create parent directories if needed (for nested file paths)
            parent_dir = os.path.dirname(file_path)
            if parent_dir and parent_dir != directory:
                os.makedirs(parent_dir, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(content))

        # Recursively process subdirectories
        for dirname, subdir_data in data["directories"].items():
            subdir_path = os.path.join(directory, dirname)
            store_json_to_directory(subdir_data, subdir_path)

        return True

    except Exception as e:
        raise Exception(f"Error storing JSON to directory {directory}: {str(e)}")

