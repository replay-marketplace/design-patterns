"""Create nested directory structures."""

import os
from pathlib import Path
from typing import Dict, Any


def create_directory_structure(structure: dict, base_path: str = ".") -> bool:
    """Create nested directories from a dictionary structure.
    
    Args:
        structure: A dictionary where keys are directory names and values are
                  nested dictionaries representing subdirectories. Empty dict
                  means no subdirectories.
        base_path: The base path where the structure should be created.
                  Defaults to current directory.
    
    Returns:
        bool: True if all directories were successfully created, False otherwise
    
    Example:
        >>> structure = {
        ...     "parent": {
        ...         "child1": {},
        ...         "child2": {
        ...             "grandchild": {}
        ...         }
        ...     }
        ... }
        >>> create_directory_structure(structure)
        True
    """
    try:
        base = Path(base_path)
        
        def _create_dirs(struct: dict, current_path: Path) -> None:
            """Recursively create directories from structure."""
            for dir_name, subdirs in struct.items():
                # Create the directory
                new_path = current_path / dir_name
                new_path.mkdir(parents=True, exist_ok=True)
                
                # Recursively create subdirectories if any
                if isinstance(subdirs, dict) and subdirs:
                    _create_dirs(subdirs, new_path)
        
        _create_dirs(structure, base)
        return True
        
    except (OSError, PermissionError, TypeError) as e:
        # Handle file system errors and type errors
        return False
    except Exception as e:
        # Handle any other unexpected errors
        return False
