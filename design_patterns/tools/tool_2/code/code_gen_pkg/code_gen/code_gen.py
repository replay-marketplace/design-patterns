"""Code generation function - Generate code from prompts using LLM agents."""

import os
import tempfile
from pathlib import Path
from typing import Optional

from agent_chat.chat_agent_code_json import chat_agent_code_json
from analysis.count_files import count_files
from analysis.count_loc import count_loc
from analysis.count_python_functions import count_python_functions
from analysis.count_python_imports import count_python_imports
from file_processing.dir_exists import dir_exists
from file_processing.file_exists import file_exists
from file_processing.read_file_content import read_file_content
from file_processing.save_text_to_file import save_text_to_file
from json_processing.dict_to_json_string import dict_to_json_string
from json_processing.load_directory_to_json import load_directory_to_json
from json_processing.parse_json_string import parse_json_string
from json_processing.store_json_to_directory import store_json_to_directory


def _get_code_gen_base_dir() -> Path:
    """Get the base directory for code_gen output."""
    current_file = Path(__file__).resolve()
    tool_2_dir = current_file.parent.parent.parent.parent
    code_gen_dir = tool_2_dir / "code_gen"
    return code_gen_dir


def _get_next_version(project_dir: Path) -> int:
    """Get the next version number for a project."""
    latest_dir_file = project_dir / "latest_dir.txt"
    
    if latest_dir_file.exists():
        try:
            content = latest_dir_file.read_text().strip()
            if content:
                current_version = int(content)
                next_version = current_version + 1
            else:
                next_version = 1
        except (ValueError, FileNotFoundError):
            next_version = 1
    else:
        next_version = 1
    
    return next_version


def _update_latest_dir_txt(project_dir: Path, version: int):
    """Update latest_dir.txt with the current version."""
    latest_dir_file = project_dir / "latest_dir.txt"
    latest_dir_file.write_text(str(version))


def _update_latest_symlink(project_dir: Path, version: int):
    """Update the latest/ symlink to point to the current version."""
    latest_link = project_dir / "latest"
    version_dir = project_dir / str(version)
    
    # Remove existing symlink if it exists
    if latest_link.exists() or latest_link.is_symlink():
        if latest_link.is_symlink():
            latest_link.unlink()
        elif latest_link.is_dir():
            latest_link.rmdir()
        elif latest_link.is_file():
            latest_link.unlink()
    
    # Create new symlink (use relative path)
    try:
        # Use relative path for better portability
        relative_target = str(version_dir.relative_to(project_dir))
        latest_link.symlink_to(relative_target)
    except OSError:
        # On Windows or if symlink fails, create a junction or copy
        # For now, we'll just skip symlink creation on Windows
        pass


def _generate_reports_md(
    output_dir: Path,
    input_prompt_word_count: int,
    output_prompt_word_count: int
):
    """Generate .reports.md file with analysis metrics."""
    reports_file = output_dir / ".reports.md"
    
    # Calculate metrics
    count_loc_val = count_loc(str(output_dir))
    count_files_val = count_files(str(output_dir))
    count_python_imports_val, _ = count_python_imports(str(output_dir))
    count_python_functions_val, _ = count_python_functions(str(output_dir))
    
    # Generate report content
    report_content = f"""input_prompt_word_count = {input_prompt_word_count}     # prompt sent to the chat agent
output_prompt_word_count = {output_prompt_word_count}    # json response returned from agent. 
count_loc = {count_loc_val}
count_files = {count_files_val}
count_python_imports = {count_python_imports_val}
count_python_functions = {count_python_functions_val}
"""
    
    # Save report
    reports_file.write_text(report_content)


def code_gen(
    prompt: str,
    project_name: str,
    template_dir_path: Optional[str] = None
) -> str:
    """
    Generate code from a prompt using LLM agents.
    
    Args:
        prompt: The prompt describing what code to generate.
        project_name: The name of the project (used for directory organization).
        template_dir_path: Optional path to a template directory to use as starting point.
    
    Returns:
        The path to the generated code directory.
    
    Raises:
        ValueError: If prompt or project_name is invalid.
        RuntimeError: If code generation fails.
    
    Example:
        >>> result_dir = code_gen("Create a hello world function", "hello_world")
        >>> print(result_dir)
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("prompt must be a non-empty string")
    if not project_name or not isinstance(project_name, str):
        raise ValueError("project_name must be a non-empty string")
    
    # Get base directory
    code_gen_base = _get_code_gen_base_dir()
    code_gen_base.mkdir(parents=True, exist_ok=True)
    
    # Create project directory
    project_dir = code_gen_base / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize latest_dir.txt if it doesn't exist
    latest_dir_file = project_dir / "latest_dir.txt"
    if not latest_dir_file.exists():
        latest_dir_file.write_text("0")
    
    # Get next version
    version = _get_next_version(project_dir)
    version_dir = project_dir / str(version)
    version_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Prepare the prompt with explicit JSON format instructions
        json_format_instructions = """
IMPORTANT: You must respond with a JSON object in the json_dir format. The JSON structure must follow this exact format:

{
    "files": {
        "filename.py": "file content here",
        "README.md": "readme content here"
    },
    "directories": {
        "subdirectory_name": {
            "files": {
                "file_in_subdir.py": "content here"
            },
            "directories": {}
        }
    }
}

The root JSON object must have "files" and/or "directories" keys. Files are stored in the "files" object as key-value pairs (filename -> content). Subdirectories are stored in the "directories" object, where each key is a directory name and the value is another object with "files" and "directories" keys.
"""
        
        final_prompt = f"""{prompt}

{json_format_instructions}

Return ONLY the JSON structure. No markdown, no explanations, just the JSON."""
        
        # If template is provided, load it and include in prompt
        if template_dir_path:
            if not dir_exists(template_dir_path):
                raise ValueError(f"Template directory does not exist: {template_dir_path}")
            
            # Load template directory to JSON
            template_json = load_directory_to_json(template_dir_path)
            template_json_str = dict_to_json_string(template_json, pretty=True)
            
            # Enhance prompt with template
            final_prompt = f"""Template code structure (in json_dir format):
{template_json_str}

User request: {prompt}

{json_format_instructions}

Generate code based on the template structure above, incorporating the user's request. Return the complete code structure as JSON in the json_dir format."""
        
        # Call chat agent to generate code
        json_response, input_word_count, output_word_count = chat_agent_code_json(final_prompt)
        
        # Parse JSON response
        try:
            code_structure = parse_json_string(json_response)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON response from agent: {str(e)}")
        
        # Save JSON to temporary file (keep content for error messages)
        json_content_for_debug = json_response  # Keep a copy for error messages
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            tmp_file.write(json_response)
            tmp_json_path = tmp_file.name
        
        try:
            # Store JSON structure to directory
            # Note: store_json_to_directory now raises RuntimeError on failure
            store_json_to_directory(tmp_json_path, str(version_dir))
            
            # Verify that files were actually created (safety check)
            files_in_dir = list(version_dir.rglob("*"))
            # Filter out directories and .reports.md (which is created later)
            actual_files = [f for f in files_in_dir if f.is_file() and f.name != ".reports.md"]
            if not actual_files:
                raise RuntimeError(
                    f"No files were created in the output directory. "
                    f"The JSON structure may be empty or invalid.\n"
                    f"JSON content (first 1000 chars): {json_content_for_debug[:1000]}"
                )
        except Exception as e:
            # Enhance error message with JSON content if it's a RuntimeError
            if isinstance(e, RuntimeError) and "Failed to store JSON" in str(e):
                raise RuntimeError(
                    f"{str(e)}\n"
                    f"JSON content received from agent (first 1000 chars):\n{json_content_for_debug[:1000]}"
                ) from e
            raise
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_json_path):
                os.unlink(tmp_json_path)
        
        # Generate reports
        _generate_reports_md(
            version_dir,
            input_word_count,
            output_word_count
        )
        
        # Update latest_dir.txt with the version we just created
        _update_latest_dir_txt(project_dir, version)
        
        # Update latest symlink
        _update_latest_symlink(project_dir, version)
        
        return str(version_dir)
        
    except Exception as e:
        raise RuntimeError(f"Code generation failed: {str(e)}")

