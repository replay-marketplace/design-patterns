"""
create_directory_structure function.
"""

import os


def create_directory_structure(structure: dict, base_path: str = ".") -> bool:
    """
    Create nested directories from a dictionary structure.
    
    Args:
        structure (dict): A nested dictionary representing the directory structure.
                         Keys are directory names, values are nested dictionaries.
        base_path (str): The base path where the structure will be created (default: current directory)
    
    Returns:
        bool: True if successful, False otherwise
    
    Example:
        structure = {
            "parent": {
                "child1": {},
                "child2": {
                    "grandchild": {}
                }
            }
        }
        create_directory_structure(structure)
    """
    try:
        for name, subdirs in structure.items():
            # Create the current directory
            dir_path = os.path.join(base_path, name)
            os.makedirs(dir_path, exist_ok=True)
            
            # Recursively create subdirectories
            if isinstance(subdirs, dict) and subdirs:
                create_directory_structure(subdirs, dir_path)
        
        return True
    except Exception as e:
        print(f"Error creating directory structure: {e}")
        return False
