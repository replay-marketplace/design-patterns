"""JSON Processing Package

Provides utilities for JSON file operations, validation, and directory conversion.
"""

from .basic_functions import (
    load_json_from_file,
    save_json_to_file,
    dict_to_json_string,
    parse_json_string,
    load_json_string_from_file,
    save_json_string_to_file,
    validate_json_schema
)

from .getters_setters import (
    get_json_dir_example,
    get_json_dir_schema,
    generate_json_schema_from_json
)

from .advanced_functions import (
    load_directory_to_json,
    store_json_to_directory
)

__all__ = [
    'load_json_from_file',
    'save_json_to_file',
    'dict_to_json_string',
    'parse_json_string',
    'load_json_string_from_file',
    'save_json_string_to_file',
    'validate_json_schema',
    'get_json_dir_example',
    'get_json_dir_schema',
    'generate_json_schema_from_json',
    'load_directory_to_json',
    'store_json_to_directory'
]

__version__ = "0.1.0"

