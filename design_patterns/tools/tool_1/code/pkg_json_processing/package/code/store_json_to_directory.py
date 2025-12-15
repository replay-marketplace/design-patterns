"""
Store JSON to directory function - Store JSON structure to directory.
"""

import os
import sys
import importlib.util
from pathlib import Path

# Import from pkg_file_processing - handle both development and installed scenarios
def _import_save_text_to_file():
    """Import save_text_to_file from pkg_file_processing."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pkg_file_path = os.path.join(
        current_dir, '..', '..', '..', 'pkg_file_processing', 'package', 'code', 'save_text_to_file.py'
    )
    pkg_file_path = os.path.abspath(pkg_file_path)
    
    if os.path.exists(pkg_file_path):
        spec = importlib.util.spec_from_file_location("save_text_to_file", pkg_file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.save_text_to_file
    else:
        pkg_file_processing_path = os.path.join(
            current_dir, '..', '..', '..', 'pkg_file_processing', 'package'
        )
        pkg_file_processing_path = os.path.abspath(pkg_file_processing_path)
        if pkg_file_processing_path not in sys.path:
            sys.path.insert(0, pkg_file_processing_path)
        from code.save_text_to_file import save_text_to_file
        return save_text_to_file

save_text_to_file = _import_save_text_to_file()


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

