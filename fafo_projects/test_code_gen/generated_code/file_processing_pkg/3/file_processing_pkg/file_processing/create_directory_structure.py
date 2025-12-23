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
        structure (dict): A dictionary representing the directory structure to create
    
    Returns:
        bool: True if all directories were successfully created, False otherwise
    """
    try:
        # Handle empty structure
        if not structure:
            return True
        
        # Recursively create directories
        def create_dirs(struct):
            for path, subdirs in struct.items():
                # Create the directory if it doesn't exist
                if not os.path.exists(path):
                    os.makedirs(path, exist_ok=True)
                
                # Recursively create subdirectories
                if subdirs:
                    create_dirs(subdirs)
        
        create_dirs(structure)
        return True
    
    except (IOError, OSError, PermissionError) as e:
        # Handle directory creation errors
        return False
    except Exception as e:
        # Handle any other unexpected errors
        return False

