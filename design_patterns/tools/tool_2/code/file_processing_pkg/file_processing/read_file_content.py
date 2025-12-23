"""Read file content function - Read single file."""


def read_file_content(filepath: str) -> str:
    """
    Read the content of a single file.

    Args:
        filepath: The path to the file to read.

    Returns:
        The content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If filepath is not a string.

    Example:
        >>> content = read_file_content("/tmp/test.txt")
        >>> print(content)
        'Hello World'
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        raise IOError(f"Error reading file {filepath}: {e}")


