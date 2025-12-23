"""
read_file_content function.
"""

import os


def read_file_content(filepath: str) -> str:
    """
    Read and return the content of a single file.
    
    Args:
        filepath (str): The path to the file to read
    
    Returns:
        str: The content of the file, or an empty string if the file cannot be read
    """
    try:
        # Check if file exists and is a file (not a directory)
        if not os.path.exists(filepath):
            return ""
        
        if not os.path.isfile(filepath):
            return ""
        
        # Read and return the file content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return content
    
    except (IOError, OSError, PermissionError) as e:
        # Handle file reading errors
        return ""
    except UnicodeDecodeError as e:
        # Handle encoding errors
        return ""
    except Exception as e:
        # Handle any other unexpected errors
        return ""

