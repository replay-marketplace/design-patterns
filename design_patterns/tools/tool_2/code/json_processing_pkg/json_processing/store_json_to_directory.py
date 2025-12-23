"""Store JSON to directory function - Store JSON structure to directory."""

import os
import json
from pathlib import Path


def store_json_to_directory(json_filepath: str, output_directory: str) -> bool:
    """
    Store a JSON directory structure to an actual directory.

    The JSON should follow the json_dir format:
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
        json_filepath: The path to the JSON file containing the directory structure.
        output_directory: The path where the directory structure should be created.

    Returns:
        True if the directory structure was successfully created.
    
    Raises:
        RuntimeError: If the JSON structure is invalid, no files are created, or files cannot be created.
        TypeError: If json_filepath or output_directory are not strings.
        FileNotFoundError: If the JSON file does not exist.
        ValueError: If the JSON structure is invalid or empty.

    Example:
        >>> result = store_json_to_directory("/tmp/structure.json", "/tmp/output")
        >>> print(result)
        True
    """
    if not isinstance(json_filepath, str):
        raise TypeError("json_filepath must be a string")
    if not isinstance(output_directory, str):
        raise TypeError("output_directory must be a string")
    
    try:
        # Load JSON structure
        filepath_obj = Path(json_filepath)
        if not filepath_obj.exists():
            raise FileNotFoundError(f"File not found: {json_filepath}")
        
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validate JSON structure
        if not isinstance(data, dict):
            raise ValueError(f"JSON root must be a dictionary, got {type(data).__name__}")
        
        # Check if JSON has the expected structure
        if "files" not in data and "directories" not in data:
            raise ValueError(
                f"JSON structure must contain 'files' and/or 'directories' keys. "
                f"Got keys: {list(data.keys())}"
            )
        
        # Create output directory
        output_path = Path(output_directory)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Recursively create structure
        files_created = _create_directory_from_json(data, output_path)
        
        # Validate that at least one file was created
        if files_created == 0:
            raise ValueError(
                "No files were created from the JSON structure. "
                "The JSON may be empty or not in the expected format."
            )
        
        return True
    except Exception as e:
        # Re-raise with more context for debugging
        raise RuntimeError(f"Failed to store JSON to directory: {str(e)}") from e


def _create_directory_from_json(data: dict, base_path: Path) -> int:
    """
    Recursively create directory structure from JSON data.
    
    Returns:
        int: Number of files created
    """
    files_created = 0
    
    # Create files
    if "files" in data and isinstance(data["files"], dict):
        for filename, content in data["files"].items():
            file_path = base_path / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(content))
            files_created += 1
    
    # Create subdirectories
    if "directories" in data and isinstance(data["directories"], dict):
        for dirname, dir_data in data["directories"].items():
            subdir_path = base_path / dirname
            subdir_path.mkdir(parents=True, exist_ok=True)
            files_created += _create_directory_from_json(dir_data, subdir_path)
    
    return files_created

