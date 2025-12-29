"""Directory-level code generation functions."""

import os
from typing import Tuple, Optional
from src.agent_chat import chat_agent_code_json
from src.json import load_directory_to_json, store_json_to_directory, parse_json_string


def code_gen_dir(
    prompt: str,
    generated_code_dir_path: str,
    template_dir_path: Optional[str] = None
) -> Tuple[str, int, int]:
    """
    Generate code in a directory using a prompt and optionally a template.

    Args:
        prompt: The user prompt describing what code to generate.
        generated_code_dir_path: Path to the directory where generated code will be written.
        template_dir_path: Optional path to a template directory. If provided, files from
                         this directory will be loaded and passed as context to the LLM.

    Returns:
        Tuple[str, int, int]: A tuple containing:
            - Path to the directory where code was written
            - Total input tokens (word count)
            - Total output tokens (word count)

    Raises:
        ValueError: If prompt or generated_code_dir_path is invalid.
        FileNotFoundError: If template_dir_path is provided but doesn't exist.
        Exception: If code generation or file operations fail.

    Example:
        >>> dir_path, input_count, output_count = code_gen_dir(
        ...     "Create a hello world Python script",
        ...     "/tmp/generated"
        ... )
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("prompt must be a non-empty string")

    if not generated_code_dir_path or not isinstance(generated_code_dir_path, str):
        raise ValueError("generated_code_dir_path must be a non-empty string")

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

    # Create the output directory if it doesn't exist
    os.makedirs(generated_code_dir_path, exist_ok=True)

    # Store the JSON structure to the directory
    try:
        store_json_to_directory(code_structure, generated_code_dir_path)
    except Exception as e:
        raise Exception(f"Failed to store generated code to directory: {str(e)}")

    # Write .reports.md file
    reports_path = os.path.join(generated_code_dir_path, ".reports.md")
    try:
        with open(reports_path, 'w', encoding='utf-8') as f:
            f.write(f"input_prompt_word_count = {input_prompt_word_count}\n")
            f.write(f"output_prompt_word_count = {output_prompt_word_count}\n")
    except Exception as e:
        # Non-critical error, log but don't fail
        print(f"Warning: Failed to write .reports.md: {str(e)}")

    return generated_code_dir_path, input_prompt_word_count, output_prompt_word_count

