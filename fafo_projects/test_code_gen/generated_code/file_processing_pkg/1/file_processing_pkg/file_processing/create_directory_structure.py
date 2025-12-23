"""
create_directory_structure function.
"""

import os


def create_directory_structure(structure: dict) -> bool:
    """
    Create nested directories based on a dictionary structure.
    
    The dictionary should have directory paths as keys and nested dictionaries as values.
    An empty dictionary as a value means no subdirectories.
    
    Example:
        {
            "/path/to/dir1": {
                "/path/to/dir1/subdir1": {},
                "/path/to/dir1/subdir2": {}
            },
            "/path/to/dir2": {}
        }
    
    Args:
        structure (dict): A dictionary representing the directory structure to create
    
    Returns:
        bool: True if all directories were successfully created, False otherwise
    """
    try:
        def create_dirs(dir_dict):
            """Recursively create directories from the structure."""
            for dir_path, subdirs in dir_dict.items():
                # Create the directory if it doesn't exist
                os.makedirs(dir_path, exist_ok=True)
                
                # Recursively create subdirectories
                if subdirs:
                    create_dirs(subdirs)
        
        # Create all directories
        create_dirs(structure)
        return True
    except Exception as e:
        # Return False if any error occurs
        return False

