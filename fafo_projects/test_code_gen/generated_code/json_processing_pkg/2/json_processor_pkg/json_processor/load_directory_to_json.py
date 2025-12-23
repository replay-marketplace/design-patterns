"""
Load directory structure to JSON.
"""

import os


def load_directory_to_json(directory: str) -> dict:
    """
    Convert a directory structure to JSON format (always recursive).
    
    Args:
        directory (str): Path to the directory to convert
    
    Returns:
        dict: JSON representation of the directory structure
    
    Raises:
        FileNotFoundError: If the directory does not exist
        NotADirectoryError: If the path is not a directory
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    def process_directory(path):
        """
        Recursively process a directory.
        
        Args:
            path (str): Path to process
        
        Returns:
            dict: JSON representation
        """
        name = os.path.basename(path)
        
        if os.path.isfile(path):
            # It's a file
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                # If file can't be read as text, store error message
                content = f"[Binary file or read error: {str(e)}]"
            
            return {
                "type": "file",
                "name": name,
                "content": content
            }
        
        elif os.path.isdir(path):
            # It's a directory
            children = []
            
            try:
                entries = sorted(os.listdir(path))
                for entry in entries:
                    entry_path = os.path.join(path, entry)
                    children.append(process_directory(entry_path))
            except PermissionError:
                pass  # Skip directories we can't read
            
            return {
                "type": "directory",
                "name": name,
                "children": children
            }
    
    return process_directory(directory)
