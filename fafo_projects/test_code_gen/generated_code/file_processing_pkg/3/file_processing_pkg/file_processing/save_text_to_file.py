"""
save_text_to_file function.
"""

import os


def save_text_to_file(content: str, directory: str, filename: str) -> bool:
    """
    Write text content to a file in the specified directory.
    
    Args:
        content (str): The text content to write to the file
        directory (str): The directory path where the file should be saved
        filename (str): The name of the file to create
    
    Returns:
        bool: True if the file was successfully written, False otherwise
    """
    try:
        # Check if directory exists
        if not os.path.exists(directory):
            return False
        
        if not os.path.isdir(directory):
            return False
        
        # Create the full file path
        filepath = os.path.join(directory, filename)
        
        # Write the content to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    except (IOError, OSError, PermissionError) as e:
        # Handle file writing errors
        return False
    except Exception as e:
        # Handle any other unexpected errors
        return False

