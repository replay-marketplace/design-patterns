"""
Load JSON string from file function - Load JSON string from file.
"""

import sys
import os
import importlib.util

# Import from pkg_file_processing - handle both development and installed scenarios
def _import_read_file_content():
    """Import read_file_content from pkg_file_processing."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pkg_file_path = os.path.join(
        current_dir, '..', '..', '..', 'pkg_file_processing', 'package', 'code', 'read_file_content.py'
    )
    pkg_file_path = os.path.abspath(pkg_file_path)
    
    if os.path.exists(pkg_file_path):
        spec = importlib.util.spec_from_file_location("read_file_content", pkg_file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.read_file_content
    else:
        pkg_file_processing_path = os.path.join(
            current_dir, '..', '..', '..', 'pkg_file_processing', 'package'
        )
        pkg_file_processing_path = os.path.abspath(pkg_file_processing_path)
        if pkg_file_processing_path not in sys.path:
            sys.path.insert(0, pkg_file_processing_path)
        from code.read_file_content import read_file_content
        return read_file_content

read_file_content = _import_read_file_content()


def load_json_string_from_file(filepath: str) -> str:
    """
    Load JSON content from a file as a string.

    Args:
        filepath: The path to the JSON file to load.

    Returns:
        The JSON content as a string. Returns empty string if file doesn't exist or can't be read.

    Example:
        >>> json_str = load_json_string_from_file("/tmp/data.json")
        >>> isinstance(json_str, str)
        True
    """
    return read_file_content(filepath)

