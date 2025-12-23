"""
Store JSON structure to directory.
"""

import os


def store_json_to_directory(json_structure: dict, output_path: str) -> bool:
    """
    Create a directory structure from a JSON representation.
    
    Args:
        json_structure (dict): JSON structure to convert to directories/files
        output_path (str): Base path where the structure will be created
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        def create_from_json(structure, base_path):
            """
            Recursively create directory structure from JSON.
            
            Args:
                structure (dict): JSON structure node
                base_path (str): Current base path
            """
            if structure["type"] == "file":
                # Create file
                file_path = os.path.join(base_path, structure["name"])
                
                # Ensure parent directory exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                # Write file content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(structure.get("content", ""))
            
            elif structure["type"] == "directory":
                # Create directory
                dir_path = os.path.join(base_path, structure["name"])
                os.makedirs(dir_path, exist_ok=True)
                
                # Process children
                for child in structure.get("children", []):
                    create_from_json(child, dir_path)
        
        # Ensure output path exists
        os.makedirs(output_path, exist_ok=True)
        
        # Create structure
        create_from_json(json_structure, output_path)
        
        return True
    
    except Exception as e:
        print(f"Error creating directory structure: {e}")
        return False
