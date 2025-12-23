"""
read_file_content function.
"""


def read_file_content(filepath: str) -> str:
    """
    Read and return the content of a file.
    
    Args:
        filepath (str): The path to the file to read
    
    Returns:
        str: The content of the file
    
    Raises:
        FileNotFoundError: If the file does not exist
        IOError: If there's an error reading the file
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        raise IOError(f"Error reading file: {e}")
