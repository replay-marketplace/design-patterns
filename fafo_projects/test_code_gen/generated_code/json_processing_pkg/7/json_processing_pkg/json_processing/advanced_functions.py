"""Advanced JSON processing functions for directory operations."""

import os
from typing import Dict, List, Any

# Import from file_processing package
try:
    from file_processing import (
        save_text_to_file,
        read_file_content,
        create_directory_structure,
        file_exists,
        dir_exists
    )
except ImportError:
    raise ImportError("file_processing package is required. Install with: pip3 install -e ../file_processing_pkg/5/file_processing_pkg/")


def load_directory_to_json(directory: str) -> dict:
    """Load directory structure to JSON format (always recursive).
    
    Args:
        directory: Path to the directory to load
        
    Returns:
        Dictionary representing the directory structure with format:
        {
            "type": "directory",
            "name": "dirname",
            "children": [
                {"type": "file", "name": "filename", "content": "file content"},
                {"type": "directory", "name": "subdir", "children": [...]}
            ]
        }
        
    Raises:
        FileNotFoundError: If directory does not exist
    """
    if not dir_exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    def _process_directory(path: str) -> dict:
        """Recursively process directory."""
        result = {
            "type": "directory",
            "name": os.path.basename(path) or path,
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
                    # If we can't read the file, skip it
                    print(f"Warning: Could not read file {entry_path}: {str(e)}")
            elif os.path.isdir(entry_path):
                # Recursively process subdirectory
                subdir_data = _process_directory(entry_path)
                result["children"].append(subdir_data)
        
        return result
    
    return _process_directory(directory)


def store_json_to_directory(data: dict, base_directory: str) -> bool:
    """Store JSON structure to directory.
    
    Args:
        data: Dictionary with directory structure (same format as load_directory_to_json output)
        base_directory: Base path where to create the structure
        
    Returns:
        True if successful, False otherwise
        
    Example:
        data = {
            "type": "directory",
            "name": "mydir",
            "children": [
                {"type": "file", "name": "test.txt", "content": "hello"},
                {"type": "directory", "name": "subdir", "children": []}
            ]
        }
        store_json_to_directory(data, "/path/to/output")
    """
    try:
        if data.get("type") != "directory":
            print("Error: Root element must be a directory")
            return False
        
        # Create base directory if it doesn't exist
        if not dir_exists(base_directory):
            os.makedirs(base_directory, exist_ok=True)
        
        def _process_node(node: dict, current_path: str) -> bool:
            """Recursively process nodes."""
            if node.get("type") == "file":
                # Save file
                filename = node.get("name", "")
                content = node.get("content", "")
                
                if not filename:
                    print("Warning: File node missing name")
                    return True
                
                return save_text_to_file(content, current_path, filename)
            
            elif node.get("type") == "directory":
                # Create directory and process children
                dirname = node.get("name", "")
                
                if not dirname:
                    print("Warning: Directory node missing name")
                    return True
                
                new_path = os.path.join(current_path, dirname)
                
                # Create directory
                if not dir_exists(new_path):
                    os.makedirs(new_path, exist_ok=True)
                
                # Process children
                children = node.get("children", [])
                for child in children:
                    if not _process_node(child, new_path):
                        return False
                
                return True
            else:
                print(f"Warning: Unknown node type: {node.get('type')}")
                return True
        
        # Process all children of the root
        children = data.get("children", [])
        for child in children:
            if not _process_node(child, base_directory):
                return False
        
        return True
    
    except Exception as e:
        print(f"Error storing JSON to directory: {str(e)}")
        return False
