"""Save JSON string to file"""

import os
import sys

# Add the file_processing_pkg to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../file_processing_pkg/5/file_processing_pkg')))

from file_processing import save_text_to_file, create_directory_structure


def save_json_string_to_file(json_str: str, filepath: str) -> bool:
    """Save JSON string to file.
    
    Args:
        json_str: JSON string to save
        filepath: Path where the file should be saved
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Extract directory and filename
        directory = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        
        # If no directory specified, use current directory
        if not directory:
            directory = '.'
        
        # Create directory structure if it doesn't exist
        if directory != '.' and not os.path.exists(directory):
            # Build directory structure dict
            parts = directory.split(os.sep)
            structure = {}
            current = structure
            for part in parts:
                if part:
                    current[part] = {}
                    current = current[part]
            create_directory_structure(structure)
        
        # Save the JSON string to file
        return save_text_to_file(json_str, directory, filename)
    except Exception:
        return False
