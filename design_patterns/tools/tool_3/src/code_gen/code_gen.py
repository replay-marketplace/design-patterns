"""Code generation functions using chat agent and JSON processing."""

import os
from pathlib import Path
from typing import Optional

from ..agent_chat import chat_agent_code_json
from ..json.json_processing import (
    parse_json_string,
    store_json_to_directory,
    load_directory_to_json,
    dict_to_json_string,
    get_json_dir_example,
)


def _get_next_version(project_dir: str) -> int:
    """
    Get the next version number for a project.
    
    Args:
        project_dir: Path to the project directory.
        
    Returns:
        int: The next version number (starts at 1 if no previous versions).
    """
    latest_dir_file = os.path.join(project_dir, "latest_dir.txt")
    
    if os.path.exists(latest_dir_file):
        try:
            with open(latest_dir_file, 'r') as f:
                content = f.read().strip()
                if content:
                    latest_version = int(content)
                    return latest_version + 1
        except (ValueError, IOError):
            pass
    
    return 1


def _update_latest_dir(project_dir: str, version: int) -> None:
    """
    Update the latest_dir.txt file with the current version.
    
    Args:
        project_dir: Path to the project directory.
        version: The version number to set as latest.
    """
    latest_dir_file = os.path.join(project_dir, "latest_dir.txt")
    os.makedirs(project_dir, exist_ok=True)
    
    with open(latest_dir_file, 'w') as f:
        f.write(str(version))


def _update_latest_symlink(project_dir: str, version: int) -> None:
    """
    Update or create the 'latest' symlink to point to the current version.
    
    Args:
        project_dir: Path to the project directory.
        version: The version number to link to.
    """
    latest_link = os.path.join(project_dir, "latest")
    version_dir = os.path.join(project_dir, str(version))
    
    # Remove existing symlink if it exists
    if os.path.exists(latest_link) or os.path.islink(latest_link):
        try:
            os.remove(latest_link)
        except OSError:
            pass
    
    # Create new symlink
    try:
        os.symlink(str(version), latest_link)
    except OSError as e:
        # On Windows or if symlink creation fails, we'll skip it
        # This is a best-effort operation
        pass


def _normalize_json_structure(data: dict) -> dict:
    """
    Normalize JSON structure to ensure it has the required 'files' and 'directories' keys.
    
    Args:
        data: The JSON dictionary to normalize.
        
    Returns:
        dict: Normalized dictionary with 'files' and 'directories' keys.
        
    Raises:
        ValueError: If the data cannot be normalized to the required structure.
    """
    if not isinstance(data, dict):
        raise ValueError(f"data must be a dictionary, got {type(data).__name__}")
    
    # If it already has the correct structure, validate and return
    if "files" in data and "directories" in data:
        if isinstance(data["files"], dict) and isinstance(data["directories"], dict):
            # Recursively normalize nested directories
            normalized_dirs = {}
            for dir_name, dir_data in data["directories"].items():
                if isinstance(dir_data, dict):
                    normalized_dirs[dir_name] = _normalize_json_structure(dir_data)
                else:
                    # Invalid directory structure, skip it
                    continue
            return {"files": data["files"], "directories": normalized_dirs}
    
    # Try to normalize the structure
    normalized = {"files": {}, "directories": {}}
    
    # If the data is a flat structure, try to organize it
    for key, value in data.items():
        if isinstance(value, dict):
            # Check if it looks like a directory structure
            if "files" in value or "directories" in value:
                try:
                    normalized["directories"][key] = _normalize_json_structure(value)
                except ValueError:
                    # If normalization fails, treat as a directory with files
                    normalized["directories"][key] = {"files": value, "directories": {}}
            else:
                # Treat as a directory with files
                normalized["directories"][key] = {"files": value, "directories": {}}
        elif isinstance(value, str):
            # Treat as a file
            normalized["files"][key] = value
        elif isinstance(value, (list, tuple)):
            # Convert list/tuple to string representation
            normalized["files"][key] = str(value)
        else:
            # Try to convert to string
            normalized["files"][key] = str(value)
    
    return normalized


def _write_reports_file(version_dir: str, input_word_count: int, output_word_count: int) -> None:
    """
    Write the .reports.md file with analysis data.
    
    Args:
        version_dir: Path to the version directory.
        input_word_count: Word count of the input prompt.
        output_word_count: Word count of the output JSON response.
    """
    reports_file = os.path.join(version_dir, ".reports.md")
    
    content = f"""input_prompt_word_count = {input_word_count}     # prompt sent to the chat agent
output_prompt_word_count = {output_word_count}    # json response returned from agent.
"""
    
    with open(reports_file, 'w') as f:
        f.write(content)


def code_gen(
    prompt: str,
    project_name: str,
    generated_code_dir_path: str,
    template_dir_path: Optional[str] = None
) -> str:
    """
    Generate code from a prompt using chat agent and store it in a versioned directory structure.
    
    Args:
        prompt: The user prompt describing what code to generate.
        project_name: Name of the project (used as directory name).
        generated_code_dir_path: Base path where generated code directories are stored.
        template_dir_path: Optional path to a template directory to use as starting point.
        
    Returns:
        str: Path to the generated code directory (version directory).
        
    Raises:
        ValueError: If prompt, project_name, or generated_code_dir_path is invalid.
        Exception: If code generation or storage fails.
        
    Example:
        >>> code_dir = code_gen("Create a simple hello world app", "hello_app", "/path/to/generated_code")
        >>> print(code_dir)
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("prompt must be a non-empty string")
    
    if not project_name or not isinstance(project_name, str):
        raise ValueError("project_name must be a non-empty string")
    
    if not generated_code_dir_path or not isinstance(generated_code_dir_path, str):
        raise ValueError("generated_code_dir_path must be a non-empty string")
    
    # Create project directory path
    project_dir = os.path.join(generated_code_dir_path, project_name)
    os.makedirs(project_dir, exist_ok=True)
    
    # Get the example JSON format to include in the prompt
    json_example = get_json_dir_example()
    
    # Prepare the prompt for the chat agent
    base_prompt = f"""{prompt}

IMPORTANT: You must respond with a JSON object in the following exact format:
{json_example}

The JSON must have exactly two top-level keys:
- "files": an object mapping filenames to their content (strings)
- "directories": an object mapping directory names to nested directory structures (each with the same "files" and "directories" structure)

Generate the code structure according to the requirements above."""
    
    enhanced_prompt = base_prompt
    
    # If template is provided, load it and include it in the prompt
    if template_dir_path:
        if not os.path.exists(template_dir_path):
            raise FileNotFoundError(f"Template directory not found: {template_dir_path}")
        
        if not os.path.isdir(template_dir_path):
            raise ValueError(f"Template path is not a directory: {template_dir_path}")
        
        # Load template directory to JSON
        template_json = load_directory_to_json(template_dir_path)
        template_json_str = dict_to_json_string(template_json, pretty=True)
        
        # Enhance prompt with template context
        enhanced_prompt = f"""{prompt}

Use the following existing code structure as a starting point:
{template_json_str}

IMPORTANT: You must respond with a JSON object in the following exact format:
{json_example}

The JSON must have exactly two top-level keys:
- "files": an object mapping filenames to their content (strings)
- "directories": an object mapping directory names to nested directory structures (each with the same "files" and "directories" structure)

Modify and extend the code according to the requirements above."""
    
    # Call chat agent to generate JSON code
    json_string, input_word_count, output_word_count = chat_agent_code_json(enhanced_prompt)
    
    # Parse the JSON response
    try:
        code_json = parse_json_string(json_string)
    except Exception as e:
        raise Exception(f"Failed to parse JSON response from chat agent: {str(e)}")
    
    # Normalize the JSON structure to ensure it has the required format
    try:
        code_json = _normalize_json_structure(code_json)
    except Exception as e:
        raise Exception(f"Failed to normalize JSON structure: {str(e)}. Received JSON: {json_string[:500]}")
    
    # Get next version number
    version = _get_next_version(project_dir)
    
    # Create version directory
    version_dir = os.path.join(project_dir, str(version))
    os.makedirs(version_dir, exist_ok=True)
    
    # Store JSON structure to directory
    try:
        store_json_to_directory(code_json, version_dir)
    except Exception as e:
        raise Exception(f"Failed to store generated code to directory: {str(e)}. JSON structure: {dict_to_json_string(code_json, pretty=True)[:500]}")
    
    # Write reports file
    _write_reports_file(version_dir, input_word_count, output_word_count)
    
    # Update latest_dir.txt
    _update_latest_dir(project_dir, version)
    
    # Update latest symlink
    _update_latest_symlink(project_dir, version)
    
    return version_dir

