"""File management module for storing and loading files from directories."""

import os
import uuid
from typing import List, Dict
from datetime import datetime


def store_files_into_dir(agent_response: str, output_dir_path: str) -> str:
    """Store the agent response content into a file in the specified directory.
    
    Args:
        agent_response: The content to store in the file.
        output_dir_path: The directory path where the file should be stored.
        
    Returns:
        The full path to the stored file.
    """
    # Create directory if it doesn't exist
    os.makedirs(output_dir_path, exist_ok=True)
    
    # Generate a unique filename using timestamp and UUID
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    filename = f"response_{timestamp}_{unique_id}.txt"
    
    # Full path for the file
    file_path = os.path.join(output_dir_path, filename)
    
    # Write content to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(agent_response)
    
    return file_path


def load_files_from_dir(output_dir_path: str) -> List[Dict[str, str]]:
    """Load all files from the specified directory.
    
    Args:
        output_dir_path: The directory path to load files from.
        
    Returns:
        A list of dictionaries, each containing 'filename' and 'content' keys.
    """
    files_list = []
    
    # Check if directory exists
    if not os.path.exists(output_dir_path):
        return files_list
    
    if not os.path.isdir(output_dir_path):
        return files_list
    
    # Iterate through all files in the directory
    for filename in os.listdir(output_dir_path):
        file_path = os.path.join(output_dir_path, filename)
        
        # Only process files, not directories
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                files_list.append({
                    'filename': filename,
                    'content': content
                })
            except (IOError, UnicodeDecodeError):
                # Skip files that can't be read
                continue
    
    return files_list
