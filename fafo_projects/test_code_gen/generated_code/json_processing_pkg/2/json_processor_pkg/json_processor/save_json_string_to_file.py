"""
Save JSON string to file.
"""

import os


def save_json_string_to_file(json_str: str, filepath: str) -> bool:
    """
    Save a JSON string directly to a file.
    
    Args:
        json_str (str): JSON string to save
        filepath (str): Path where the file will be saved
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
        
        return True
    except Exception as e:
        print(f"Error saving JSON string to file: {e}")
        return False
