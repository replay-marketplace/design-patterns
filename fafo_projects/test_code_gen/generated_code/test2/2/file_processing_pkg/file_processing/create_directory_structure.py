"""
create_directory_structure function.
"""

import os


def create_directory_structure(structure: dict) -> bool:
    """
    Create nested directories based on a dictionary structure.
    
    The structure dictionary should have directory paths as keys and nested
    dictionaries as values. An empty dictionary means no subdirectories.
    
    Example:
        {
            "/path/to/dir1": {
                "/path/to/dir1/subdir1": {},
                "/path/to/dir1/subdir2": {
                    "/path/to/dir1/subdir2/subsubdir": {}
                }
            },
            "/path/to/dir2": {}
        }
    
    Args:
        structure (dict): A dictionary representing the directory structure
    
    Returns:
        bool: True if all directories were successfully created, False otherwise
    """
    try:
        def create_dirs(struct):
            """Recursively create directories from structure."""
            for path, subdirs in struct.items():
                # Create the directory if it doesn't exist
                os.makedirs(path, exist_ok=True)
                
                # Recursively create subdirectories
                if subdirs:
                    create_dirs(subdirs)
        
        # Handle empty structure
        if not structure:
            return True
        
        # Create the directory structure
        create_dirs(structure)
        
        return True
    except Exception as e:
        # Return False if any error occurs
        return False

