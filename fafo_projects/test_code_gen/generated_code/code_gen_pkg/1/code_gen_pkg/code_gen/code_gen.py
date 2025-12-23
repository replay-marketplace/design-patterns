"""
Code generation function using AI agent.
"""

import os
import json
from pathlib import Path
from typing import Optional


def chat_agent_code_json(prompt: str) -> dict:
    """
    Placeholder for AI agent that generates code structure as JSON.
    
    Args:
        prompt: The code generation prompt
        
    Returns:
        dict: JSON directory structure with generated code
    """
    # This is a placeholder - in real implementation, this would call an AI agent
    # For now, return a basic structure
    return {
        "type": "directory",
        "name": "generated_project",
        "children": [
            {
                "type": "file",
                "name": "README.md",
                "content": f"# Generated Project\n\nGenerated from prompt: {prompt}\n"
            }
        ]
    }


def read_directory_structure(dir_path: str) -> dict:
    """
    Read a directory structure and convert it to JSON format.
    
    Args:
        dir_path: Path to the directory to read
        
    Returns:
        dict: JSON representation of the directory structure
    """
    path = Path(dir_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Directory not found: {dir_path}")
    
    def build_tree(p: Path) -> dict:
        if p.is_file():
            with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            return {
                "type": "file",
                "name": p.name,
                "content": content
            }
        else:
            children = []
            for child in sorted(p.iterdir()):
                if child.name.startswith('.'):
                    continue
                children.append(build_tree(child))
            return {
                "type": "directory",
                "name": p.name,
                "children": children
            }
    
    return build_tree(path)


def write_directory_structure(structure: dict, base_path: str):
    """
    Write a JSON directory structure to the filesystem.
    
    Args:
        structure: JSON directory structure
        base_path: Base path where to write the structure
    """
    def write_node(node: dict, current_path: Path):
        if node["type"] == "file":
            current_path.parent.mkdir(parents=True, exist_ok=True)
            with open(current_path, 'w', encoding='utf-8') as f:
                f.write(node.get("content", ""))
        elif node["type"] == "directory":
            current_path.mkdir(parents=True, exist_ok=True)
            for child in node.get("children", []):
                child_path = current_path / child["name"]
                write_node(child, child_path)
    
    base = Path(base_path)
    write_node(structure, base)


def get_next_version_number(project_dir: Path) -> int:
    """
    Get the next version number for a project.
    
    Args:
        project_dir: Path to the project directory
        
    Returns:
        int: Next version number
    """
    counter_file = project_dir / "next_counter_dir.txt"
    
    if counter_file.exists():
        with open(counter_file, 'r') as f:
            counter = int(f.read().strip())
    else:
        counter = 1
    
    # Write the next counter
    with open(counter_file, 'w') as f:
        f.write(str(counter + 1))
    
    return counter


def code_gen(
    prompt: str,
    code_gen_dir_path: str,
    project_name: str,
    template_dir_path: Optional[str] = None
) -> str:
    """
    Generate code using AI agent and save to filesystem.
    
    Args:
        prompt: The code generation prompt
        code_gen_dir_path: Base directory for all generated code projects
        project_name: Name of the project
        template_dir_path: Optional path to template directory to use as starting point
        
    Returns:
        str: Path to the generated project version directory
    """
    # Create base code_gen directory if it doesn't exist
    base_dir = Path(code_gen_dir_path)
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Create project directory
    project_dir = base_dir / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # Get next version number
    version_num = get_next_version_number(project_dir)
    version_dir = project_dir / f"v{version_num}"
    version_dir.mkdir(parents=True, exist_ok=True)
    
    # Build the prompt for the AI agent
    full_prompt = prompt
    
    if template_dir_path:
        # Read template directory structure
        template_structure = read_directory_structure(template_dir_path)
        template_json = json.dumps(template_structure, indent=2)
        
        full_prompt = f"""{prompt}

Use the following template structure as a starting point:

```json
{template_json}
```

Generate code based on this template structure.
"""
    
    # Call AI agent to generate code structure
    generated_structure = chat_agent_code_json(full_prompt)
    
    # Write the generated structure to filesystem
    write_directory_structure(generated_structure, str(version_dir))
    
    # Save the prompt for reference
    prompt_file = version_dir / "_generation_prompt.txt"
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(full_prompt)
    
    return str(version_dir)
