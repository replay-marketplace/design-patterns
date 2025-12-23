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

def main():
    # Set up paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code_gen_dir = os.path.join(current_dir, "generated_code")
    template_dir = os.path.join(current_dir, "templates/python_pkg_01")
    project_name = "test"
    result_path = code_gen(
        prompt="hello world",
        code_gen_dir_path=code_gen_dir,
        project_name=project_name,
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
        return
    
    os.chmod(setup_and_run_path, 0o755)
    #subprocess.run([setup_and_run_path])


    print(result_path)


if __name__ == "__main__":
    main()

