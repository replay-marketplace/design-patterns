"""Project-level code generation functions with versioning."""

import os
from typing import Tuple, Optional
from src.agent_chat import chat_agent_code_json
from src.json import load_directory_to_json, store_json_to_directory, parse_json_string


def _get_next_version(project_dir: str) -> int:
    """
    Get the next version number for a project.

    Args:
        project_dir: Path to the project directory.

    Returns:
        int: The next version number (starts at 1 if no versions exist).
    """
    latest_dir_file = os.path.join(project_dir, "latest_dir.txt")

    if os.path.exists(latest_dir_file):
        try:
            with open(latest_dir_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content.isdigit():
                    return int(content) + 1
        except Exception:
            pass

    return 1


def _update_latest_dir(project_dir: str, version: int) -> None:
    """
    Update the latest_dir.txt file with the new version number.

    Args:
        project_dir: Path to the project directory.
        version: The version number to write.
    """
    latest_dir_file = os.path.join(project_dir, "latest_dir.txt")
    os.makedirs(project_dir, exist_ok=True)

    with open(latest_dir_file, 'w', encoding='utf-8') as f:
        f.write(str(version))


def _update_latest_symlink(project_dir: str, version: int) -> None:
    """
    Create or update the 'latest' symlink to point to the latest version directory.

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
        except Exception:
            pass

    # Create new symlink
    try:
        os.symlink(str(version), latest_link)
    except OSError:
        # On Windows or if symlink creation fails, we'll skip it
        # This is a non-critical feature
        pass


def code_gen_project(
    prompt: str,
    project_name: str,
    generated_code_dir_path: str,
    template_dir_path: Optional[str] = None
) -> Tuple[str, int, int]:
    """
    Generate code for a project with versioning support.

    Projects are stored in a directory structure with versioning:
    generated_code/
    ├── <project_name>/
    │   ├── latest_dir.txt      # Tracks latest version number
    │   ├── latest/              # Symlink to latest version
    │   ├── 1/                   # Version 1
    │   ├── 2/                   # Version 2
    │   └── 3/                   # Version 3 (latest)

    Args:
        prompt: The user prompt describing what code to generate.
        project_name: Name of the project (used as directory name).
        generated_code_dir_path: Base path where projects are stored (e.g., "generated_code").
        template_dir_path: Optional path to a template directory. If provided, files from
                         this directory will be loaded and passed as context to the LLM.

    Returns:
        Tuple[str, int, int]: A tuple containing:
            - Path to the directory where code was written (version directory)
            - Total input tokens (word count)
            - Total output tokens (word count)

    Raises:
        ValueError: If prompt, project_name, or generated_code_dir_path is invalid.
        FileNotFoundError: If template_dir_path is provided but doesn't exist.
        Exception: If code generation or file operations fail.

    Example:
        >>> dir_path, input_count, output_count = code_gen_project(
        ...     "Create a Python web scraper",
        ...     "web_scraper",
        ...     "generated_code"
        ... )
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("prompt must be a non-empty string")

    if not project_name or not isinstance(project_name, str):
        raise ValueError("project_name must be a non-empty string")

    if not generated_code_dir_path or not isinstance(generated_code_dir_path, str):
        raise ValueError("generated_code_dir_path must be a non-empty string")

    # Build project directory path
    project_dir = os.path.join(generated_code_dir_path, project_name)

    # Get next version number
    version = _get_next_version(project_dir)

    # Create version directory path
    version_dir = os.path.join(project_dir, str(version))

    # Build the full prompt
    full_prompt = prompt

    # If template is provided, load it and include in prompt
    if template_dir_path:
        if not os.path.exists(template_dir_path):
            raise FileNotFoundError(f"Template directory not found: {template_dir_path}")

        if not os.path.isdir(template_dir_path):
            raise ValueError(f"Template path is not a directory: {template_dir_path}")

        # Load template directory to JSON
        template_json = load_directory_to_json(template_dir_path)
        template_json_str = str(template_json)  # Convert to string for prompt

        # Enhance prompt with template context
        full_prompt = (
            f"Template directory structure (JSON format):\n{template_json_str}\n\n"
            f"User request: {prompt}\n\n"
            "Generate code based on the template structure and user request. "
            "Return the complete directory structure as JSON in the same format as the template."
        )

    # Call the chat agent to generate JSON code
    json_string, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json(full_prompt)

    # Parse the JSON response
    try:
        code_structure = parse_json_string(json_string)
    except Exception as e:
        raise ValueError(f"Failed to parse JSON response from agent: {str(e)}\nJSON: {json_string}")

    # Create the version directory
    os.makedirs(version_dir, exist_ok=True)

    # Store the JSON structure to the version directory
    try:
        store_json_to_directory(code_structure, version_dir)
    except Exception as e:
        raise Exception(f"Failed to store generated code to directory: {str(e)}")

    # Write .reports.md file in the version directory
    reports_path = os.path.join(version_dir, ".reports.md")
    try:
        with open(reports_path, 'w', encoding='utf-8') as f:
            f.write(f"input_prompt_word_count = {input_prompt_word_count}\n")
            f.write(f"output_prompt_word_count = {output_prompt_word_count}\n")
    except Exception as e:
        # Non-critical error, log but don't fail
        print(f"Warning: Failed to write .reports.md: {str(e)}")

    # Update latest_dir.txt
    _update_latest_dir(project_dir, version)

    # Update latest symlink
    _update_latest_symlink(project_dir, version)

    return version_dir, input_prompt_word_count, output_prompt_word_count

