"""
Save text to file function - Write text file.
"""

import os
from pathlib import Path


def save_text_to_file(content: str, directory: str, filename: str) -> bool:
    """
    Write text content to a file in the specified directory.

    Args:
        content: The text content to write to the file.
        directory: The directory path where the file should be created.
        filename: The name of the file to create.

    Returns:
        True if the file was successfully written, False otherwise.

    Example:
        >>> save_text_to_file("Hello World", "/tmp", "test.txt")
        True
    """
    try:
        # Create directory if it doesn't exist
        Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Create full file path
        filepath = os.path.join(directory, filename)
        
        # Write content to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception:
        return False

