"""Load JSON from file"""

import json
import sys
import os

# Add the file_processing_pkg to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../file_processing_pkg/5/file_processing_pkg')))

from file_processing import read_file_content, file_exists


def load_json_from_file(filepath: str) -> dict:
    """Load JSON from file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Dictionary containing the JSON data, or empty dict if file doesn't exist or is invalid
    """
    try:
        if not file_exists(filepath):
            return {}
        
        content = read_file_content(filepath)
        if not content:
            return {}
        
        return json.loads(content)
    except (json.JSONDecodeError, Exception):
        return {}
