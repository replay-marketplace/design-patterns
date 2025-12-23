"""Advanced JSON processing functions for directory operations."""

import os
import sys
from typing import Dict, List, Any

# Import from file_processing_pkg
try:
    from file_processing import (
        save_text_to_file,
        read_file_content,
        create_directory_structure,
        file_exists,
        dir_exists
    )
except ImportError:
    print("Warning: file_processing package not found. Some functions may not work.")
    # Provide fallback implementations
    def save_text_to_file(content: str, directory: str, filename: str) -> bool:
        try:
            os.makedirs(directory, exist_ok=True)
            filepath = os.path.join(directory, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except:
            return False
    
    def read_file_content(filepath: str) -> str:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def create_directory_structure(structure: dict) -> bool:
        try:
            for path in structure.keys():
                os.makedirs(path, exist_ok=True)
            return True
        except:
            return False
    
    def file_exists(filepath: str) -> bool:
        return os.path.isfile(filepath)
    
    def dir_exists(filepath: str) -> bool:
        return os.path.isdir(filepath)


def load_directory_to_json(directory: str) -> dict:
    """Load directory structure to JSON format (always recursive).
    
    Args:
        directory: Path to directory to convert
        
    Returns:
        Dictionary representing the directory structure
        
    Raises:
        FileNotFoundError: If directory doesn't exist
    """
    if not dir_exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    def _process_directory(path: str) -> dict:
        """Recursively process directory."""
        result = {
            "type": "directory",
            "name": os.path.basename(path),
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
                    content = read_file_content(entry_path)
                    result["children"].append({
                        "type": "file",
                        "name": entry,
                        "content": content
                    })
                except Exception as e:
                    # If file can't be read, include it with empty content
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
        def _create_structure(data: dict, current_path: str) -> bool:
            """Recursively create directory structure."""
            if data.get("type") == "file":
                # Create file
                directory = os.path.dirname(current_path)
                filename = os.path.basename(current_path)
                content = data.get("content", "")
                
                if directory and not dir_exists(directory):
                    os.makedirs(directory, exist_ok=True)
                
                return save_text_to_file(content, directory if directory else ".", filename)
            
            elif data.get("type") == "directory":
                # Create directory
                if not dir_exists(current_path):
                    os.makedirs(current_path, exist_ok=True)
                
                # Process children
                children = data.get("children", [])
                for child in children:
                    child_name = child.get("name", "")
                    child_path = os.path.join(current_path, child_name)
                    if not _create_structure(child, child_path):
                        return False
                
                return True
            
            return False
        
        # Start processing from the root
        root_name = json_data.get("name", "root")
        root_path = os.path.join(base_path, root_name)
        
        return _create_structure(json_data, root_path)
    
    except Exception as e:
        print(f"Error storing JSON to directory: {e}")
        return False
