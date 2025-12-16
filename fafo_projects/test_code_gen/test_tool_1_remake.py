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
    result_path = code_gen(
        prompt=prompt,
        code_gen_dir_path=code_gen_dir,
        project_name="pkg",
        template_dir_path=template_dir)

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

def main():
    # Set up paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code_gen_dir = os.path.join(current_dir, "generated_code")
    template_dir = os.path.join(current_dir, "templates/python_pkg_01")
    

    # File Processing
    project_name_1 = "file_processing_pkg"
    prompt_1 = """
Generate a Python package that implements the following file processing functions:
File Processing
- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file
- `read_file_content(filepath: str) -> str` - Read single file
- `create_directory_structure(structure: dict) -> bool` - Create nested directories
- `file_exists(filepath: str) -> bool` - Check existence
- `dir_exists(filepath: str) -> bool` - Check existence
    """



    generate_and_setup_project(
        prompt=prompt_1,
        project_name=project_name_1,
        code_gen_dir=code_gen_dir,
        template_dir=template_dir
    )


if __name__ == "__main__":
    main()

