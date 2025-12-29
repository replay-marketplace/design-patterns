import os
import subprocess
from pathlib import Path
from typing import Dict, List, Any
from anytree import Node, RenderTree

from src.agent_chat import chat_agent_code_json
from src.agent_chat import simple_chat
from src.json import store_json_to_directory


from src.code_gen import code_gen_project

def build_tree(dir_path, prefix="", ignore=[r"node_modules", r"\.test\.", r"\.spec\."]):
        entries = sorted(os.listdir(dir_path))
        entries = [e for e in entries if not any(re.search(p, e) for p in ignore)]
        
        lines = []
        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + entry)
            
            full_path = os.path.join(dir_path, entry)
            if os.path.isdir(full_path):
                new_prefix = prefix + ("    " if is_last else "│   ")
                lines.append(build_tree(full_path, new_prefix, ignore))
        
        return "\n".join(lines)

def test_01_single_module():

    print("================================================")
    print("Test 01 - Single Module")
    print("================================================")

    
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    do_code_gen = False
    if (do_code_gen == True):
        print("\nProject Code Generation...")
        prompt = """
        Implement a calculator. 
        You pass in two numbers, and a string that says 'add', 'sub', 'mult', 'div'. 
        The function returns the result.
        Write some test cases."""

        path, tokens_in, tokens_out = code_gen_project(
            prompt="Implement a calculator. You pass in two numbers, and a string that says 'add', 'sub', 'mult', 'div'. The function returns the result.",
            project_name="calculator",
            generated_code_dir_path="generated_code",
            template_dir_path="templates/python_pkg_01/template/")

        print(path, tokens_in, tokens_out)
 
    else:
        # *** REMOVE WHEN DOING A FULL RUN ***
        #path = "generated_code/calculator/latest"
        path = "generated_code/calculator/3"
        print("path: ", path)
        

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    do_run_tests = False
    if (do_run_tests == True):

        print("\nRunning the tests...")

        # Find the path to the setup_and_run.sh file
        setup_and_run_path = None
        for root, dirs, files in os.walk(path):
            if "setup_and_run.sh" in files:
                setup_and_run_path = os.path.join(root, "setup_and_run.sh")
                break

        print("setup_and_run_path: ", setup_and_run_path)
        
        # Convert to absolute path
        setup_and_run_path = os.path.abspath(setup_and_run_path)
        print("setup_and_run_path (absolute): ", setup_and_run_path)

        # chmod +x the setup_and_run.sh file
        os.chmod(setup_and_run_path, 0o755)

        # Run the setup_and_run.sh script using bash
        # Change to the script's directory to ensure relative paths work correctly
        script_dir = os.path.dirname(setup_and_run_path)
        subprocess.run(["bash", setup_and_run_path], cwd=script_dir)


    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print("\nGenerating the directory structure...")
    import os
    import re

    

    print(build_tree(path))

    # Put the build_tree into a string
    tree_string = build_tree(path)
    print(tree_string)


    # Make a new dir that's a combo of path + "tests"
    new_dir = path + "/calculator/"

    # Ls the new_dir
    print("ls -la ", new_dir)
    os.system("ls -la " + new_dir)



    #path, tokens_in, tokens_out = code_gen_dir(
    #    prompt: str,
    #    generated_code_dir_path: str,
    #    template_dir_path: Optional[str] = None


    

def test_01_hello_world():
    #code_dir = code_gen(
    #    prompt="hello world in python, and print more stuff in the terminal",
    #    project_name="hello_world",
    #    generated_code_dir_path="generated_code")

    a = 0
    print(a)

def stage_impl(root, w01_dir_template: str):

    test_01_single_module()

    return

    print("here")    


    # ==============================================================
    # Create the directory structure
    # 1. Extract all module names from the tree
    # 2. LLM : give it to the LLM, the list of module and the w01_dir_template, and ask it to create the directory structure.
    # ==============================================================
    
    '''
    module_names_list = []
    for pre, fill, node in RenderTree(root):
        module_names_list.append(node.name)

    print(module_names_list)
    '''


    '''
    # ==============================================================
    # Generate a simple project - Simple Test
    # ==============================================================
    path, tokens_in, tokens_out = code_gen_project(
                                    prompt="Python hello world.",
                                    project_name="code_gen",
                                    generated_code_dir_path="generated_code",
                                    template_dir_path="templates/python_pkg_01/template/")
    print(path, tokens_in, tokens_out)
    '''

    # ==============================================================
    # Generate Empty Directory Structure
    # ==============================================================

    # Read w01_dir_template into a string
    with open("tests/test_01/w01_dir.md", "r") as file:
        w01_dir_template = file.read()
    print(w01_dir_template) 

    # Convert module_names_list into a string
    module_names_list_str = ",".join(module_names_list)
    print(module_names_list_str)

    
    prompt=f"Generate the directory structure based on the template.  \n\n Module names: {module_names_list_str}, \n\n Template:{w01_dir_template}"
    print("--------------------------------")
    print("Prompt")
    print("--------------------------------")
    print(prompt)

    path, tokens_in, tokens_out = code_gen_project(
                                    prompt=prompt,
                                    project_name="code_gen",
                                    generated_code_dir_path="generated_code",
                                    template_dir_path="templates/python_pkg_01/template/")
    print(path, tokens_in, tokens_out)



    

    '''
    # ==============================================================
    # Code Gen a single module
    # ==============================================================
    code_dir = code_gen(
        prompt="Implement instructions in module_02/replay/prompt.md",
        project_name="code_gen",
        generated_code_dir_path="generated_code",
        template_dir_path="generated_code/empty_dir/latest/")
    


    code_dict = code_gen(
        prompt="Implement what is writen in th prompt.md", 
        generated_code_dir_path="generated_code/code_gen/3/module_00/",
        template_dir_path="generated_code/code_gen/3/module_00/")

    print(code_dict)

    '''





