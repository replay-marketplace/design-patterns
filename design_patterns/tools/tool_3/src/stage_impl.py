import os
from pathlib import Path
from typing import Dict, List, Any
from anytree import Node, RenderTree

from src.agent_chat import chat_agent_code_json
from src.agent_chat import simple_chat
from src.json import store_json_to_directory

from src.code_gen import code_gen

def stage_impl(root, w01_dir_template: str):

    print("here")    


    # ==============================================================
    # Create the directory structure
    # 1. Extract all module names from the tree
    # 2. LLM : give it to the LLM, the list of module and the w01_dir_template, and ask it to create the directory structure.
    # ==============================================================
    
    module_names_list = []
    for pre, fill, node in RenderTree(root):
        module_names_list.append(node.name)

    print(module_names_list)

    '''
    code_dir = code_gen(
        prompt="hello world in python, and print more stuff in the terminal",
        project_name="hello_world",
        generated_code_dir_path="generated_code")
    '''

    
    # ==============================================================
    # Generate the directory structure
    # ==============================================================
    '''
    code_dir = code_gen(
        prompt=f"Generate emtpy directory structure for a python project with these module names: {module_names_list}, based on this template: {w01_dir_template}",
        project_name="empty_dir",
        generated_code_dir_path="generated_code")
    '''

    # ==============================================================
    # Sove the prompt text into the prompt files
    # ==============================================================

    for pre, fill, node in RenderTree(root):
        print(node.name)
        prompt = node.prompt
        print(prompt)

        # Write prompt into the prompt.md file located in the node.name/replay/prompt.md
        base_dir = "generated_code/empty_dir/latest/"
        prompt_file_path = os.path.join(base_dir,node.name, "replay", "prompt.md")
        with open(prompt_file_path, "w") as file:
            file.write(prompt)


    # ==============================================================
    # Code Gen a single module
    # ==============================================================
    code_dir = code_gen(
        prompt="Implement instructions in module_02/replay/prompt.md",
        project_name="code_gen",
        generated_code_dir_path="generated_code",
        template_dir_path="generated_code/empty_dir/latest/")




    
    