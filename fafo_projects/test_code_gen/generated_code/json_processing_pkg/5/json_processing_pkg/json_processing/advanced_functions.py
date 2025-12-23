"""Advanced JSON processing functions for directory operations."""

import os
from typing import Dict, List, Any

try:
    from file_processing import (
        save_text_to_file,
        read_file_content,
        create_directory_structure,
        file_exists,
        dir_exists
    )
    FILE_PROCESSING_AVAILABLE = True
except ImportError:
    FILE_PROCESSING_AVAILABLE = False
    print("Warning: file_processing package not available. Using fallback implementations.")


# Fallback implementations if file_processing is not available
def _fallback_read_file_content(filepath: str) -> str:
    """Fallback implementation for reading file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def _fallback_save_text_to_file(content: str, directory: str, filename: str) -> bool:
    """Fallback implementation for saving text to file."""
    try:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception:
        return False


def _fallback_file_exists(filepath: str) -> bool:
    """Fallback implementation for checking file existence."""
    return os.path.isfile(filepath)


def _fallback_dir_exists(dirpath: str) -> bool:
    """Fallback implementation for checking directory existence."""
    return os.path.isdir(dirpath)


# Use file_processing functions if available, otherwise use fallbacks
if FILE_PROCESSING_AVAILABLE:
    _read_file = read_file_content
    _save_text = save_text_to_file
    _file_exists = file_exists
    _dir_exists = dir_exists
else:
    _read_file = _fallback_read_file_content
    _save_text = _fallback_save_text_to_file
    _file_exists = _fallback_file_exists
    _dir_exists = _fallback_dir_exists


def load_directory_to_json(directory: str) -> dict:
    """Load directory structure to JSON format (always recursive).
    
    Args:
        directory: Path to the directory to convert
        
    Returns:
        Dictionary representing the directory structure
        
    Raises:
        FileNotFoundError: If directory doesn't exist
    """
    if not _dir_exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    def _process_directory(path: str) -> dict:
        """Recursively process directory."""
        name = os.path.basename(path)
        result = {
            "type": "directory",
            "name": name if name else os.path.basename(os.path.normpath(path)),
            "children": []
        }
        
        try:
            entries = sorted(os.listdir(path))
        except PermissionError:
            return result
        
        for entry in entries:
            entry_path = os.path.join(path, entry)
            
            if os.path.isfile(entry_path):
                try:
                    content = _read_file(entry_path)
                    result["children"].append({
                        "type": "file",
                        "name": entry,
                        "content": content
                    })
                except Exception as e:
                    # If we can't read the file, include it with error message
                    result["children"].append({
                        "type": "file",
                        "name": entry,
                        "content": f"[Error reading file: {str(e)}]"
                    })
            elif os.path.isdir(entry_path):
                result["children"].append(_process_directory(entry_path))
        
        return result
    
    return _process_directory(directory)


def store_json_to_directory(json_data: dict, base_path: str) -> bool:
    """Store JSON structure to directory.
    
    Args:
        json_data: Dictionary representing directory structure
        base_path: Base path where to create the structure
        
    Returns:
        True if successful, False otherwise
    """
    try:
        def _process_node(node: dict, current_path: str) -> bool:
            """Recursively process JSON node."""
            if node.get("type") == "file":
                # Create file
                filename = node.get("name", "unnamed_file")
                content = node.get("content", "")
                return _save_text(content, current_path, filename)
            
            elif node.get("type") == "directory":
                # Create directory
                dir_name = node.get("name", "unnamed_dir")
                new_path = os.path.join(current_path, dir_name)
                os.makedirs(new_path, exist_ok=True)
                
                # Process children
                children = node.get("children", [])
                for child in children:
                    if not _process_node(child, new_path):
                        return False
                
                return True
            
            return False
        
        # Ensure base path exists
        os.makedirs(base_path, exist_ok=True)
        
        # If the root node is a directory, process its children in base_path
        if json_data.get("type") == "directory":
            children = json_data.get("children", [])
            for child in children:
                if not _process_node(child, base_path):
                    return False
            return True
        else:
            # If root is a file, process it directly
            return _process_node(json_data, base_path)
    
    except Exception as e:
        print(f"Error storing JSON to directory: {e}")
        return False

