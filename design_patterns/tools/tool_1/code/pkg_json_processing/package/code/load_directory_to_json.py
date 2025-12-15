"""
Load directory to JSON function - Directory to JSON, always recursive.
"""

import os
from pathlib import Path
from pkg_file_processing.code.read_file_content import read_file_content


def load_directory_to_json(directory: str) -> dict:
    """
    Load a directory structure into a JSON representation (always recursive).

    Args:
        directory: The path to the directory to load.

    Returns:
        A dictionary representing the directory structure. Returns empty dict if directory doesn't exist.

    Example:
        >>> data = load_directory_to_json("/tmp/test_dir")
        >>> isinstance(data, dict)
        True
    """
    try:
        if not os.path.isdir(directory):
            return {}
        
        result = {
            "type": "directory",
            "name": os.path.basename(directory) or directory,
            "children": []
        }
        
        # Walk through directory recursively
        for root, dirs, files in os.walk(directory):
            # Get relative path from the base directory
            rel_path = os.path.relpath(root, directory)
            
            if rel_path == ".":
                # We're at the root directory
                for file in files:
                    file_path = os.path.join(root, file)
                    content = read_file_content(file_path)
                    result["children"].append({
                        "type": "file",
                        "name": file,
                        "content": content
                    })
                
                # Process subdirectories
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    result["children"].append(_load_directory_recursive(dir_path, directory))
            else:
                # This will be handled by the recursive function
                break
        
        return result
    except Exception:
        return {}


def _load_directory_recursive(dir_path: str, base_dir: str) -> dict:
    """
    Recursively load a directory into JSON structure.
    """
    try:
        result = {
            "type": "directory",
            "name": os.path.basename(dir_path),
            "children": []
        }
        
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            
            if os.path.isdir(item_path):
                result["children"].append(_load_directory_recursive(item_path, base_dir))
            elif os.path.isfile(item_path):
                content = read_file_content(item_path)
                result["children"].append({
                    "type": "file",
                    "name": item,
                    "content": content
                })
        
        return result
    except Exception:
        return {
            "type": "directory",
            "name": os.path.basename(dir_path),
            "children": []
        }

