"""Advanced operations for directory-JSON conversion."""

import os
import json
from typing import Dict, List, Any
from pathlib import Path


def load_directory_to_json(directory: str) -> dict:
    """Load directory structure to JSON format (always recursive).
    
    Args:
        directory: Path to the directory to convert
        
    Returns:
        Dictionary representing the directory structure
        
    Raises:
        FileNotFoundError: If the directory doesn't exist
        NotADirectoryError: If the path is not a directory
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    def _process_path(path: str) -> dict:
        """Recursively process a path and return its JSON representation."""
        name = os.path.basename(path)
        
        if os.path.isfile(path):
            # Read file content
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                # Handle binary files
                with open(path, 'rb') as f:
                    content = f"<binary file: {len(f.read())} bytes>"
            except Exception as e:
                content = f"<error reading file: {str(e)}>"
            
            return {
                "type": "file",
                "name": name,
                "content": content
            }
        else:
            # Process directory
            children = []
            try:
                entries = sorted(os.listdir(path))
                for entry in entries:
                    entry_path = os.path.join(path, entry)
                    children.append(_process_path(entry_path))
            except PermissionError:
                pass  # Skip directories we can't read
            
            return {
                "type": "directory",
                "name": name,
                "children": children
            }
    
    return _process_path(directory)


def store_json_to_directory(json_data: dict, base_path: str) -> bool:
    """Store JSON structure to directory.
    
    Args:
        json_data: Dictionary representing the directory structure
        base_path: Base path where the structure will be created
        
    Returns:
        True if successful, False otherwise
    """
    try:
        def _create_from_json(data: dict, current_path: str) -> None:
            """Recursively create files and directories from JSON."""
            if data.get("type") == "file":
                # Create file
                file_path = os.path.join(current_path, data["name"])
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                content = data.get("content", "")
                # Skip binary file placeholders
                if not content.startswith("<binary file:") and not content.startswith("<error reading file:"):
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
            elif data.get("type") == "directory":
                # Create directory
                dir_path = os.path.join(current_path, data["name"])
                os.makedirs(dir_path, exist_ok=True)
                
                # Process children
                for child in data.get("children", []):
                    _create_from_json(child, dir_path)
        
        _create_from_json(json_data, base_path)
        return True
        
    except Exception as e:
        print(f"Error storing JSON to directory: {e}")
        return False


def _get_file_info(filepath: str) -> Dict[str, Any]:
    """Get file information including size and modification time.
    
    Args:
        filepath: Path to the file
        
    Returns:
        Dictionary with file information
    """
    stat = os.stat(filepath)
    return {
        "size": stat.st_size,
        "modified": stat.st_mtime,
        "created": stat.st_ctime
    }


def load_directory_to_json_with_metadata(directory: str, include_metadata: bool = True) -> dict:
    """Load directory structure to JSON with optional metadata.
    
    Args:
        directory: Path to the directory to convert
        include_metadata: Whether to include file metadata (size, timestamps)
        
    Returns:
        Dictionary representing the directory structure with metadata
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    def _process_path(path: str) -> dict:
        """Recursively process a path with metadata."""
        name = os.path.basename(path)
        result = {}
        
        if os.path.isfile(path):
            result["type"] = "file"
            result["name"] = name
            
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    result["content"] = f.read()
            except UnicodeDecodeError:
                with open(path, 'rb') as f:
                    result["content"] = f"<binary file: {len(f.read())} bytes>"
            except Exception as e:
                result["content"] = f"<error reading file: {str(e)}>"
            
            if include_metadata:
                result["metadata"] = _get_file_info(path)
        else:
            result["type"] = "directory"
            result["name"] = name
            children = []
            
            try:
                entries = sorted(os.listdir(path))
                for entry in entries:
                    entry_path = os.path.join(path, entry)
                    children.append(_process_path(entry_path))
            except PermissionError:
                pass
            
            result["children"] = children
            
            if include_metadata:
                result["metadata"] = _get_file_info(path)
        
        return result
    
    return _process_path(directory)
