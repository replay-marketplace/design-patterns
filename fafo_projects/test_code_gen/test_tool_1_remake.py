"""
Simple test program that uses pkg_code_gen to generate projects from prompt_list.txt.
"""

import os
import sys
import csv
import ast
import subprocess

# Add the pkg_code_gen package to the path
package_path = os.path.join(
    os.path.dirname(__file__), 
    '..', 
    '..', 
    'design_patterns', 
    'tools', 
    'tool_1', 
    'code', 
    'pkg_code_gen', 
    'package'
)
package_path = os.path.abspath(package_path)
sys.path.insert(0, package_path)

from pkg_code_gen import code_gen

def generate_and_setup_project(prompt, project_name, code_gen_dir, template_dir):
    """
    Generate a project from a prompt and set up the setup_and_run.sh script.
    
    Args:
        prompt: The prompt string for code generation
        project_name: The name of the project
        code_gen_dir: Directory where generated code will be stored
        template_dir: Directory containing the template files
    
    Returns:
        The result path of the generated project, or None if setup_and_run.sh is not found
    """
    print(f"   DEBUG: project_name = {project_name}")
    print(f"   DEBUG: code_gen_dir = {code_gen_dir}")
    print(f"   DEBUG: template_dir = {template_dir}")
    result_path = code_gen(
        prompt=prompt,
        code_gen_dir_path=code_gen_dir,
        project_name=project_name,
        template_dir_path=template_dir)
    print(f"   DEBUG: result_path = {result_path}")

    print(result_path)

    # Somewhere in the result_path/ there is a setup_and_run.sh file. First find it, and then chmod to +x and run it
    setup_and_run_path = None
    for root, dirs, files in os.walk(result_path):
        if "setup_and_run.sh" in files:
            setup_and_run_path = os.path.join(root, "setup_and_run.sh")
            break
    
    if setup_and_run_path is None:
        print(f"Error: setup_and_run.sh not found in {result_path}")
        return None
    
    os.chmod(setup_and_run_path, 0o755)
    
    print(result_path)
    return result_path


def queue_code_gen_pkg(project_names_and_prompts_list):
        # ================================================================
    #                           Code Gen
    # ================================================================
    project_name = "code_gen_pkg"
    prompt = """
Generate a Python package that implements the following file processing functions:
Code Gen
1. `code_gen(prompt: str, code_gen_dir_path: str, project_name: str)`           - Code generation
1. `code_gen(prompt: str, code_gen_dir_path: str, project_name: str, template_dir_path: str)` - Code generation, uses the template_dir_path and the code in it as the initial starting point for the code, by sending this code to the agent via JSON within the prompt.  

### Description
It stores all projects into a dir called code_gen, in a dir based on project_name. 
When creating a new project dir, always initialize the next_counter_dir.txt so that you can increment it and generate multiple versions under the same project name. 

Use these 4 packages:

1. agent_chat_pkg: pip3 install -e ../agent_chat_pkg/2/agent_chat_pkg 
- `simple_chat(prompt: str) -> str` - Send a prompt to Claude and return the response
- `chat_agent_code_config(prompt: str, system: str) -> str` - Send a prompt with custom system message and low temperature
- `chat_agent_code_json(prompt: str, agent_type: str) -> str` - Send a prompt and get a JSON-only response


2. String Processing: pip3 install -e ../string_processing_pkg/2/agent_chat_pkg 


3. File Processing:   design_patterns/tools/tool_1/code/pkg_file_processing/README.md


5. JSON Processing:   design_patterns/tools/tool_1/code/pkg_json_processing/README.md
    """
    project_names_and_prompts_list.append((project_name, prompt))



def queue_string_processing_pkg(project_names_and_prompts_list):
    # ================================================================
    #                           String Processing
    # ================================================================
    project_name = "string_processing_pkg"
    prompt = """
Generate a Python package that implements the following file processing functions:
String Processing

#### Basic
- `append_string(base: str, addition: str) -> str` - Concatenate strings
- `search_and_delete(text: str, pattern: str) -> str` - Find and remove
- `search_and_replace(text: str, old: str, new: str) -> str` - Find and replace
- `strip_markdown(text: str) -> str` - Remove markdown formatting

#### Analysis
- `count_tokens(text: str) -> int` - Estimate token count
    """
    project_names_and_prompts_list.append((project_name, prompt))

def queue_file_processing_pkg(project_names_and_prompts_list):
    # ================================================================
    #                           File Processing
    # ================================================================
    project_name = "file_processing_pkg"
    prompt = """
Generate a Python package that implements the following file processing functions:
File Processing
- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file
- `read_file_content(filepath: str) -> str` - Read single file
- `create_directory_structure(structure: dict) -> bool` - Create nested directories
- `file_exists(filepath: str) -> bool` - Check existence
- `dir_exists(filepath: str) -> bool` - Check existence
    """
    project_names_and_prompts_list.append((project_name, prompt))

def queue_agent_chat_pkg(project_names_and_prompts_list):
    # ================================================================
    #                           Agent Chat
    # ================================================================
    project_name = "agent_chat_pkg"
    prompt = """
Generate a Python package that implements the following file processing functions:
Agent Chat
#### Basic:
- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_config(prompt, system) -> str` - Control randomness, low temp, no max token
- `chat_agent_code_json(prompt, agent_type)` - Responds only with JSON code; picks system based on agent_type

### Description
Use Anthropic AI, use model model="claude-sonnet-4-5-20250929", with max tokens set to 16k.
    """
    project_names_and_prompts_list.append((project_name, prompt))

   

def queue_agent_chat_pkg_deepseek(project_names_and_prompts_list):
    # ================================================================
    #                           Agent Chat
    # ================================================================
    project_name = "agent_chat_pkg_deepseek"
    prompt = """
Generate a Python package that implements the following file processing functions:
Agent Chat
`simple_chat(prompt: str) -> str` - Send prompt, return response

Use DeepSeek API, set it up for code generation. 
from deepseek import DeepSeekAPI
    """
    project_names_and_prompts_list.append((project_name, prompt))





def queue_json_processing_pkg(project_names_and_prompts_list):
        # ================================================================
    #                           JSON Processing
    # ================================================================
    project_name = "json_processing_pkg"
    prompt = """
Generate a Python package that implements the following file processing functions:
JSON Processing

#### Basic:       File / Dict / String  / Helper
- `load_json_from_file(filepath: str) -> dict` - Load JSON from file
- `save_json_to_file(data: dict, filepath: str) -> bool` - Save JSON to file
- `dict_to_json_string(data: dict, pretty: bool) -> str` - Convert dict to JSON string
- `parse_json_string(json_str: str) -> dict` - Parse JSON string to dict
- `load_json_string_from_file(filepath: str) -> str` - Load JSON string from file
- `save_json_string_to_file(json_str: str, filepath: str) -> bool` - Save JSON string to file
- `validate_json_schema(data: dict, schema: dict) -> bool` - Validate structure

#### Getters / Setters
- `get_json_dir_example()` - Returns an example of the json_dir file
- `get_json_dir_schema()` - Returns the schema of the json_dir file
- `generate_json_schema_from_json(input_json_file)` - Saves to the same location

#### Advanced
- `load_directory_to_json(directory: str) -> dict` - Directory to JSON, always recursive
- `store_json_to_directory()`

MUST USE THIS python package: File Processing:  pip3 install -e ../file_processing_pkg/5/file_processing_pkg/
- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file to specified directory
- `read_file_content(filepath: str) -> str` - Read single file and return its content
- `create_directory_structure(structure: dict) -> bool` - Create nested directories from dictionary structure
- `file_exists(filepath: str) -> bool` - Check if file exists
- `dir_exists(filepath: str) -> bool` - Check if directory exists

    """
    project_names_and_prompts_list.append((project_name, prompt))


def nouse():  
    """


    """






def queue_code_gen_pkg(project_names_and_prompts_list):
    # ================================================================
    #                           Code Gen
    # ================================================================
    project_name = "code_gen_pkg"
    prompt = """
Generate a Python package that implements the following file processing functions:
Code Gen
1. `code_gen(prompt: str, code_gen_dir_path: str, project_name: str)`           - Code generation
1. `code_gen(prompt: str, code_gen_dir_path: str, project_name: str, template_dir_path: str)` - Code generation, uses the template_dir_path and the code in it as the initial starting point for the code, by sending this code to the agent via JSON within the prompt.  

### Description
It stores all projects into a dir called code_gen, in a dir based on project_name. 
When creating a new project dir, always initialize the next_counter_dir.txt so that you can increment it and generate multiple versions under the same project name. 

Use these 4 packages:

1. agent_chat_pkg: pip3 install -e ../agent_chat_pkg/2/agent_chat_pkg 
- `simple_chat(prompt: str) -> str` - Send a prompt to Claude and return the response
- `chat_agent_code_config(prompt: str, system: str) -> str` - Send a prompt with custom system message and low temperature
- `chat_agent_code_json(prompt: str, agent_type: str) -> str` - Send a prompt and get a JSON-only response


2. String Processing: pip3 install -e ../string_processing_pkg/2/agent_chat_pkg 



2. File Processing:  ../file_processing_pkg/5/agent_chat_pkg 
- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file to specified directory
- `read_file_content(filepath: str) -> str` - Read single file and return its content
- `create_directory_structure(structure: dict) -> bool` - Create nested directories from dictionary structure
- `file_exists(filepath: str) -> bool` - Check if file exists
- `dir_exists(filepath: str) -> bool` - Check if directory exists


4. JSON Processing:   design_patterns/tools/tool_1/code/pkg_json_processing/README.md
    """
   

def queue_hello_world(project_names_and_prompts_list):
    project_name = "hello"
    prompt = "hello world in python. It should contain functions: 1) hello, 2) goodbye, 3) see ya later. Also make a file called README_API_SIGNATURE.md file, list all the functions and their signatures."
    project_names_and_prompts_list.append((project_name, prompt))


def main():
    # Set up paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code_gen_dir = os.path.join(current_dir, "generated_code")
    template_dir = os.path.join(current_dir, "templates/python_pkg_01/template")
    
    project_names_and_prompts_list = []


    # Add prompts to the Queue
    #queue_hello_world(project_names_and_prompts_list)
    
    
    
    #queue_string_processing_pkg(project_names_and_prompts_list)
    #queue_file_processing_pkg(project_names_and_prompts_list)
    #queue_agent_chat_pkg(project_names_and_prompts_list)
    queue_agent_chat_pkg_deepseek(project_names_and_prompts_list)
    #queue_json_processing_pkg(project_names_and_prompts_list)
    #queue_code_gen_pkg(project_names_and_prompts_list)
    
    '''
    TO DO:
    - seperate json into 2 libs. it's too big, and it get confused, stops using existing packages.
    '''
    



    # ================================================================
    #                           GENERATION LOOP
    # ================================================================
    for project_name, prompt in project_names_and_prompts_list: 
        
        print(f"\n\nGenerating project: {project_name}")
        result_path = generate_and_setup_project(
            prompt=prompt,
            project_name=project_name,
            code_gen_dir=code_gen_dir,
            template_dir=template_dir
        )
        if result_path is not None:
            print(f"✓ Generated project: {result_path}")
        else:
            print(f"Error: Failed to generate project: {project_name}")


if __name__ == "__main__":
    main()

