"""Create directory structure function - Create nested directories."""

import os
from pathlib import Path


def create_directory_structure(structure: dict) -> bool:
    """
    Create nested directory structure from a dictionary.

    The dictionary structure should represent the directory hierarchy.
    Keys are directory names, and values can be:
    - None or empty dict: creates an empty directory
    - dict: creates a subdirectory with nested structure
    - str: creates a file with that content (not implemented in this version)

    Args:
        structure: A dictionary representing the directory structure.
                  The root key should be the base directory path.

    Returns:
        True if the directory structure was successfully created, False otherwise.

    Example:
        >>> structure = {
        ...     "/tmp/test": {
        ...         "subdir1": {},
        ...         "subdir2": {
        ...             "nested": {}
        ...         }
        ...     }
        ... }
        >>> result = create_directory_structure(structure)
        >>> print(result)
        True
    """
    if not isinstance(structure, dict):
        raise TypeError("structure must be a dictionary")
    
    try:
        def _create_dirs(base_path: str, dir_dict: dict):
            """Recursively create directories."""
            for key, value in dir_dict.items():
                current_path = os.path.join(base_path, key)
                
                if isinstance(value, dict):
                    # Create directory and recurse
                    Path(current_path).mkdir(parents=True, exist_ok=True)
                    if value:  # If dict is not empty, recurse
                        _create_dirs(current_path, value)
                else:
                    # Create directory (value is None or other type)
                    Path(current_path).mkdir(parents=True, exist_ok=True)
        
        # Process the structure dictionary
        for base_path, dir_dict in structure.items():
            if isinstance(dir_dict, dict):
                # Create base directory
                Path(base_path).mkdir(parents=True, exist_ok=True)
                # Create nested structure
                if dir_dict:
                    _create_dirs(base_path, dir_dict)
            else:
                # Just create the base directory
                Path(base_path).mkdir(parents=True, exist_ok=True)
        
        return True
    except Exception:
        return False



