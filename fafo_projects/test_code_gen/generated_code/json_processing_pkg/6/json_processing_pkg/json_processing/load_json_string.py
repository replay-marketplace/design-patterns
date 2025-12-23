"""Load JSON string from file"""

import sys
import os

# Add the file_processing_pkg to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../file_processing_pkg/5/file_processing_pkg')))

from file_processing import read_file_content, file_exists


def load_json_string_from_file(filepath: str) -> str:
    """Load JSON string from file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        JSON string content from file, or empty string if file doesn't exist
    """
    try:
        if not file_exists(filepath):
            return ''
        
        content = read_file_content(filepath)
        return content if content else ''
    except Exception:
        return ''
