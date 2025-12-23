"""
Save JSON to file.
"""

import json
import os


def save_json_to_file(data: dict, filepath: str) -> bool:
    """
    Save dictionary data to a JSON file.
    
    Args:
        data (dict): Data to save
        filepath (str): Output file path
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON to file: {e}")
        return False
