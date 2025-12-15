"""
Code generation function - Generate code using AI agent and store in project directories.
"""

import os
import sys
import importlib.util


# Import from pkg_agent_chat
def _import_chat_agent_code_json():
    """Import chat_agent_code_json from pkg_agent_chat."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pkg_path = os.path.join(
        current_dir, '..', '..', '..', '..', 'pkg_agent_chat', 'package', 'code', 'chat_agent_code_json.py'
    )
    pkg_path = os.path.abspath(pkg_path)
    
    if os.path.exists(pkg_path):
        spec = importlib.util.spec_from_file_location("chat_agent_code_json", pkg_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.chat_agent_code_json
    else:
        try:
            from pkg_agent_chat.code.chat_agent_code_json import chat_agent_code_json
            return chat_agent_code_json
        except ImportError:
            pkg_dir = os.path.join(
                current_dir, '..', '..', '..', '..', 'pkg_agent_chat', 'package'
            )
            pkg_dir = os.path.abspath(pkg_dir)
            if pkg_dir not in sys.path:
                sys.path.insert(0, pkg_dir)
            from code.chat_agent_code_json import chat_agent_code_json
            return chat_agent_code_json

chat_agent_code_json = _import_chat_agent_code_json()


# Import from pkg_file_processing
def _import_file_functions():
    """Import file functions from pkg_file_processing."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pkg_path = os.path.join(
        current_dir, '..', '..', '..', '..', 'pkg_file_processing', 'package', 'code'
    )
    pkg_path = os.path.abspath(pkg_path)
    
    functions = {}
    func_names = ['dir_exists', 'file_exists', 'save_text_to_file', 'read_file_content']
    
    if os.path.exists(pkg_path):
        for func_name in func_names:
            func_path = os.path.join(pkg_path, f'{func_name}.py')
            if os.path.exists(func_path):
                spec = importlib.util.spec_from_file_location(func_name, func_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                functions[func_name] = getattr(module, func_name)
    else:
        try:
            from pkg_file_processing.code import dir_exists, file_exists, save_text_to_file, read_file_content
            functions = {
                'dir_exists': dir_exists,
                'file_exists': file_exists,
                'save_text_to_file': save_text_to_file,
                'read_file_content': read_file_content
            }
        except ImportError:
            pkg_dir = os.path.join(
                current_dir, '..', '..', '..', '..', 'pkg_file_processing', 'package'
            )
            pkg_dir = os.path.abspath(pkg_dir)
            if pkg_dir not in sys.path:
                sys.path.insert(0, pkg_dir)
            from code import dir_exists, file_exists, save_text_to_file, read_file_content
            functions = {
                'dir_exists': dir_exists,
                'file_exists': file_exists,
                'save_text_to_file': save_text_to_file,
                'read_file_content': read_file_content
            }
    
    return functions

_file_funcs = _import_file_functions()
dir_exists = _file_funcs['dir_exists']
file_exists = _file_funcs['file_exists']
save_text_to_file = _file_funcs['save_text_to_file']
read_file_content = _file_funcs['read_file_content']


# Import from pkg_json_processing
def _import_json_functions():
    """Import JSON functions from pkg_json_processing."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pkg_path = os.path.join(
        current_dir, '..', '..', '..', '..', 'pkg_json_processing', 'package', 'code'
    )
    pkg_path = os.path.abspath(pkg_path)
    
    functions = {}
    func_names = ['load_directory_to_json', 'store_json_to_directory', 'dict_to_json_string']
    
    if os.path.exists(pkg_path):
        for func_name in func_names:
            func_path = os.path.join(pkg_path, f'{func_name}.py')
            if os.path.exists(func_path):
                spec = importlib.util.spec_from_file_location(func_name, func_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                functions[func_name] = getattr(module, func_name)
    else:
        try:
            from pkg_json_processing.code import load_directory_to_json, store_json_to_directory, dict_to_json_string
            functions = {
                'load_directory_to_json': load_directory_to_json,
                'store_json_to_directory': store_json_to_directory,
                'dict_to_json_string': dict_to_json_string
            }
        except ImportError:
            pkg_dir = os.path.join(
                current_dir, '..', '..', '..', '..', 'pkg_json_processing', 'package'
            )
            pkg_dir = os.path.abspath(pkg_dir)
            if pkg_dir not in sys.path:
                sys.path.insert(0, pkg_dir)
            from code import load_directory_to_json, store_json_to_directory, dict_to_json_string
            functions = {
                'load_directory_to_json': load_directory_to_json,
                'store_json_to_directory': store_json_to_directory,
                'dict_to_json_string': dict_to_json_string
            }
    
    return functions

_json_funcs = _import_json_functions()
load_directory_to_json = _json_funcs['load_directory_to_json']
store_json_to_directory = _json_funcs['store_json_to_directory']
dict_to_json_string = _json_funcs['dict_to_json_string']


def _get_next_version_dir(project_dir: str) -> int:
    """
    Get the next version directory number for a project.
    Creates next_counter_dir.txt if it doesn't exist.
    
    Args:
        project_dir: The project directory path.
        
    Returns:
        The next version number.
    """
    counter_file = os.path.join(project_dir, 'next_counter_dir.txt')
    
    if file_exists(counter_file):
        try:
            content = read_file_content(counter_file).strip()
            current_count = int(content) if content else 0
        except (ValueError, Exception):
            current_count = 0
    else:
        current_count = 0
    
    next_count = current_count + 1
    
    # Save the next count
    save_text_to_file(str(next_count), project_dir, 'next_counter_dir.txt')
    
    return next_count


def code_gen(prompt: str, code_gen_dir_path: str, project_name: str, template_dir_path: str = None) -> str:
    """
    Generate code using AI agent and store in project directory.
    
    Args:
        prompt: The prompt to send to the code generation agent.
        code_gen_dir_path: The base directory path where code_gen projects are stored.
        project_name: The name of the project (creates a subdirectory with this name).
        template_dir_path: Optional path to a template directory to use as starting point.
                          The template code will be loaded as JSON and included in the prompt.
    
    Returns:
        The path to the generated code directory.
    
    Example:
        >>> path = code_gen("Create a simple Flask app", "/tmp/code_gen", "my_app")
        >>> print(path)
        '/tmp/code_gen/my_app/1'
    """
    # Create code_gen base directory if it doesn't exist
    if not dir_exists(code_gen_dir_path):
        os.makedirs(code_gen_dir_path, exist_ok=True)
    
    # Create project directory
    project_dir = os.path.join(code_gen_dir_path, project_name)
    if not dir_exists(project_dir):
        os.makedirs(project_dir, exist_ok=True)
    
    # Get next version directory number
    version_num = _get_next_version_dir(project_dir)
    version_dir = os.path.join(project_dir, str(version_num))
    
    # Build the prompt for the agent
    # Add instructions for JSON directory structure format
    json_format_instructions = """
IMPORTANT: You must respond with a JSON object representing a directory structure.
The JSON must follow this format:
{
  "type": "directory",
  "name": "project_name",
  "children": [
    {
      "type": "file",
      "name": "filename.py",
      "content": "file content here"
    },
    {
      "type": "directory",
      "name": "subdirectory",
      "children": [...]
    }
  ]
}
"""
    
    agent_prompt = f"""{prompt}

{json_format_instructions}"""
    
    # If template is provided, load it as JSON and include in prompt
    if template_dir_path and dir_exists(template_dir_path):
        template_json = load_directory_to_json(template_dir_path)
        template_json_str = dict_to_json_string(template_json, pretty=True)
        
        agent_prompt = f"""{prompt}

Use the following template code structure as a starting point. The template is provided as a JSON directory structure:

```json
{template_json_str}
```

Generate code based on this template structure.

{json_format_instructions}"""
    
    # Generate code using the agent
    try:
        response = chat_agent_code_json(agent_prompt, agent_type="code")
        
        # The response should be a JSON directory structure
        # If it's not in the expected format, try to extract it
        if isinstance(response, dict) and response.get("type") == "directory":
            code_structure = response
        elif isinstance(response, dict) and "directory" in response:
            code_structure = response["directory"]
        elif isinstance(response, dict) and "code" in response:
            code_structure = response["code"]
        else:
            # Assume the entire response is the directory structure
            code_structure = response
        
        # Store the generated code to the version directory
        if store_json_to_directory(code_structure, version_dir):
            return version_dir
        else:
            raise ValueError("Failed to store generated code to directory")
            
    except Exception as e:
        raise RuntimeError(f"Code generation failed: {str(e)}")

