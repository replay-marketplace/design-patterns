"""Project generator module that creates code projects based on prompts."""

import os
import tempfile
from typing import Optional

from coder_platform.coder_agent.src.coder import coder
from coder_platform.file_processing.src.file_manager import store_files_into_dir, load_files_from_dir


def generate_project(project_goal_prompt: str, output_dir: Optional[str] = None) -> str:
    """Generate a project based on the given prompt.
    
    Args:
        project_goal_prompt: A string describing the project goal/requirements.
        output_dir: Optional directory path to store the generated project.
                   If not provided, a temporary directory will be created.
    
    Returns:
        str: The directory path containing the generated project files.
    """
    if not project_goal_prompt or not project_goal_prompt.strip():
        raise ValueError("Project goal prompt cannot be empty")
    
    # Generate code using the coder agent
    agent_response = coder(project_goal_prompt)
    
    # Determine output directory
    if output_dir is None:
        output_dir = tempfile.mkdtemp(prefix="generated_project_")
    else:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
    
    # Store the generated files into the directory
    stored_path = store_files_into_dir(agent_response, output_dir)
    
    return stored_path
