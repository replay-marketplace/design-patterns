"""
Load JSON string from file function - Load JSON string from file.
"""

from pkg_file_processing.code.read_file_content import read_file_content


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

