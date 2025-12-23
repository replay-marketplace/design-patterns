"""Read content from a file."""

from pathlib import Path


def read_file_content(filepath: str) -> str:
    """Read and return the content of a single file.
    
    Args:
        filepath: The path to the file to read
    
    Returns:
        str: The content of the file as a string
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the file cannot be read due to permissions
        IOError: If there is an error reading the file
    
    Example:
        >>> content = read_file_content("/tmp/test.txt")
        >>> print(content)
        Hello World
    """
    file_path = Path(filepath)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    if not file_path.is_file():
        raise IOError(f"Path is not a file: {filepath}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except PermissionError:
        raise PermissionError(f"Permission denied reading file: {filepath}")
    except Exception as e:
        raise IOError(f"Error reading file {filepath}: {str(e)}")
