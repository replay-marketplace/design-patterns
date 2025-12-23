"""
Store JSON to directory.
"""

import os


def store_json_to_directory(data: dict, output_dir: str = ".") -> bool:
    """
    Store JSON directory structure to actual filesystem.
    
    Args:
        data (dict): JSON directory structure
        output_dir (str): Output directory path (default: current directory)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        _create_node(data, output_dir)
        return True
    except Exception as e:
        print(f"Error storing JSON to directory: {e}")
        return False


def _create_node(node: dict, parent_path: str) -> None:
    """
    Create a single node (file or directory) from JSON.
    
    Args:
        node (dict): Node representation in JSON format
        parent_path (str): Parent directory path
    """
    node_type = node.get("type")
    name = node.get("name")
    
    if not name:
        raise ValueError("Node must have a 'name' field")
    
    # Determine the full path
    if node_type == "directory":
        # For directory type, create it at parent_path/name
        full_path = os.path.join(parent_path, name)
    else:
        # For file type, also create at parent_path/name
        full_path = os.path.join(parent_path, name)
    
    if node_type == "file":
        # Create file
        content = node.get("content", "")
        
        # Ensure parent directory exists
        parent_dir = os.path.dirname(full_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    elif node_type == "directory":
        # Create directory
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        
        # Create children
        children = node.get("children", [])
        for child in children:
            _create_node(child, full_path)
    
    else:
        raise ValueError(f"Unknown node type: {node_type}")
