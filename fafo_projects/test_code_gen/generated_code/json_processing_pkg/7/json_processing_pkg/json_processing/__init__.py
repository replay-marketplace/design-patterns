"""JSON Processing Package

Provides utilities for JSON file processing, validation, and directory operations.
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
    'load_directory_to_json',
    'store_json_to_directory'
]

__version__ = '0.1.0'
