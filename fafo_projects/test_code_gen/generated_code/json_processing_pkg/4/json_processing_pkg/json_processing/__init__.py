"""JSON Processing Package

A comprehensive package for JSON file processing, validation, and directory operations.
"""

from .basic_operations import (
    load_json_from_file,
    save_json_to_file,
    dict_to_json_string,
    parse_json_string,
    load_json_string_from_file,
    save_json_string_to_file,
    validate_json_schema
)

from .schema_operations import (
    get_json_dir_example,
    get_json_dir_schema,
    generate_json_schema_from_json
)

from .advanced_operations import (
    load_directory_to_json,
    store_json_to_directory
)

__version__ = "0.1.0"

__all__ = [
    # Basic operations
    "load_json_from_file",
    "save_json_to_file",
    "dict_to_json_string",
    "parse_json_string",
    "load_json_string_from_file",
    "save_json_string_to_file",
    "validate_json_schema",
    # Schema operations
    "get_json_dir_example",
    "get_json_dir_schema",
    "generate_json_schema_from_json",
    # Advanced operations
    "load_directory_to_json",
    "store_json_to_directory",
]
