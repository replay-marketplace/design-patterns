"""
save_text_to_file function.
"""

import os


def save_text_to_file(content: str, directory: str, filename: str) -> bool:
    """
    Write text content to a file in the specified directory.
    
    Args:
        content (str): The text content to write
        directory (str): The directory path where the file will be saved
        filename (str): The name of the file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        
        # Construct full file path
        filepath = os.path.join(directory, filename)
        
        # Write content to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False
