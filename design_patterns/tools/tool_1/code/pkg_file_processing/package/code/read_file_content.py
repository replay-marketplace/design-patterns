"""
Read file content function - Read single file.
"""


def read_file_content(filepath: str) -> str:
    """
    Read the content of a single file.

    Args:
        filepath: The path to the file to read.

    Returns:
        The content of the file as a string. Returns empty string if file doesn't exist or can't be read.

    Example:
        >>> content = read_file_content("/tmp/test.txt")
        >>> len(content) > 0
        True
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ""

