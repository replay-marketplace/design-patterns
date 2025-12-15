"""
Store JSON to directory function - Store JSON structure to directory.
"""

import os
from pathlib import Path
from pkg_file_processing.code.save_text_to_file import save_text_to_file


def store_json_to_directory(json_data: dict, target_directory: str) -> bool:
    """
    Store a JSON directory structure to the filesystem.

    Args:
        json_data: The JSON dictionary representing the directory structure.
        target_directory: The path where the directory structure should be created.

    Returns:
        True if the structure was successfully created, False otherwise.

    Example:
        >>> data = {"type": "directory", "name": "test", "children": [{"type": "file", "name": "file.txt", "content": "test"}]}
        >>> store_json_to_directory(data, "/tmp/output")
        True
    """
    try:
        if json_data.get("type") != "directory":
            return False
        
        # Create base directory
        base_path = os.path.join(target_directory, json_data.get("name", ""))
        Path(base_path).mkdir(parents=True, exist_ok=True)
        
        # Process children recursively
        children = json_data.get("children", [])
        for child in children:
            if child.get("type") == "file":
                file_name = child.get("name", "")
                content = child.get("content", "")
                if file_name:
                    save_text_to_file(content, base_path, file_name)
            elif child.get("type") == "directory":
                _store_directory_recursive(child, base_path)
        
        return True
    except Exception:
        return False


def _store_directory_recursive(json_data: dict, parent_path: str) -> None:
    """
    Recursively store directory structure from JSON.
    """
    try:
        dir_name = json_data.get("name", "")
        if not dir_name:
            return
        
        dir_path = os.path.join(parent_path, dir_name)
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        children = json_data.get("children", [])
        for child in children:
            if child.get("type") == "file":
                file_name = child.get("name", "")
                content = child.get("content", "")
                if file_name:
                    save_text_to_file(content, dir_path, file_name)
            elif child.get("type") == "directory":
                _store_directory_recursive(child, dir_path)
    except Exception:
        pass

