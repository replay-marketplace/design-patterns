"""
Create directory structure function - Create nested directories.
"""

import os
from pathlib import Path


def create_directory_structure(structure: dict) -> bool:
    """
    Create nested directories based on a dictionary structure.

    Args:
        structure: A dictionary where keys are directory paths and values are either:
                  - None (for empty directories)
                  - Another dict (for nested directories)
                  - A list of filenames (for files to create as empty)

    Returns:
        True if all directories were successfully created, False otherwise.

    Example:
        >>> structure = {
        ...     "parent": {
        ...         "child1": None,
        ...         "child2": ["file1.txt", "file2.txt"]
        ...     }
        ... }
        >>> create_directory_structure(structure)
        True
    """
    try:
        def _create_structure(base_path: str, struct: dict):
            """Recursively create directory structure."""
            for key, value in struct.items():
                current_path = os.path.join(base_path, key)
                
                # Create directory
                Path(current_path).mkdir(parents=True, exist_ok=True)
                
                # If value is a list, create empty files
                if isinstance(value, list):
                    for filename in value:
                        filepath = os.path.join(current_path, filename)
                        Path(filepath).touch()
                # If value is a dict, recurse
                elif isinstance(value, dict):
                    _create_structure(current_path, value)
                # If value is None, directory is created (already done above)
        
        _create_structure("", structure)
        return True
    except Exception:
        return False

