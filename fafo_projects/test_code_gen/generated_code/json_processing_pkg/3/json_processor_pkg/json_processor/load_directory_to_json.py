"""
Load directory to JSON.
"""

import os


def load_directory_to_json(directory: str) -> dict:
    """
    Recursively load directory structure to JSON format.
    
    Args:
        directory (str): Path to directory
    
    Returns:
        dict: Directory structure as JSON
    
    Raises:
        FileNotFoundError: If the directory does not exist
        NotADirectoryError: If the path is not a directory
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Not a directory: {directory}")
    
    return _load_node(directory)


def _load_node(path: str) -> dict:
    """
    Load a single node (file or directory) to JSON format.
    
    Args:
        path (str): Path to the node
    
    Returns:
        dict: Node representation in JSON format
    """
    name = os.path.basename(path)
    
    if os.path.isfile(path):
        # Load file content
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Binary file, encode as base64 or skip
            content = "[Binary file - content not loaded]"
        except Exception as e:
            content = f"[Error reading file: {e}]"
        
        return {
            "type": "file",
            "name": name,
            "content": content
        }
    elif os.path.isdir(path):
        # Load directory children
        children = []
        try:
            entries = sorted(os.listdir(path))
            for entry in entries:
                entry_path = os.path.join(path, entry)
                children.append(_load_node(entry_path))
        except PermissionError:
            pass  # Skip directories we can't read
        
        return {
            "type": "directory",
            "name": name,
            "children": children
        }
    else:
        # Unknown type (symlink, etc.)
        return {
            "type": "unknown",
            "name": name
        }
