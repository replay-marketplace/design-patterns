"""Load directory to JSON function - Directory to JSON, always recursive."""

import os
from pathlib import Path
from .save_json_to_file import save_json_to_file


def load_directory_to_json(directory: str) -> dict:
    """
    Load a directory structure into a JSON representation (always recursive).

    The JSON structure follows the json_dir format:
    {
        "files": {
            "filename": "content"
        },
        "directories": {
            "dirname": {
                "files": {...},
                "directories": {...}
            }
        }
    }

    Args:
        directory: The path to the directory to load.

    Returns:
        A dictionary representing the directory structure.

    Raises:
        NotADirectoryError: If the path is not a directory.

    Example:
        >>> data = load_directory_to_json("/tmp/test_dir")
        >>> print(data)
        {
          "files": {
            "file1.txt": "content1"
          },
          "directories": {
            "subdir": {
              "files": {
                "file2.txt": "content2"
              },
              "directories": {}
            }
          }
        }
    """
    if not isinstance(directory, str):
        raise TypeError("directory must be a string")
    
    dir_path = Path(directory)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    result = {
        "files": {},
        "directories": {}
    }
    
    # Process all items in the directory
    for item in sorted(dir_path.iterdir()):
        if item.is_file():
            # Read file content
            try:
                with open(item, 'r', encoding='utf-8') as f:
                    content = f.read()
                result["files"][item.name] = content
            except Exception:
                # If file can't be read as text, store empty string
                result["files"][item.name] = ""
        elif item.is_dir():
            # Recursively process subdirectory
            result["directories"][item.name] = load_directory_to_json(str(item))
    
    return result


