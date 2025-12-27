'''
Use the python tree library, and make a simple structure. 
One leaf node, one parent node. 
Each node should contain:
1. name
2. list of strings, called "apis
3. list of strings, called "import_functions"

'''

from anytree import Node, RenderTree
from anytree.exporter import JsonExporter, DictExporter
import json
import os


from src.dir_tree.dir_tree import DirTree, Node_Dir, File, State
from src.agent_chat import chat_agent_code_json

# Example: Access node attributes
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
   

    '''
    print("Three node tree building...")

    prompt_00 = "calculate(a: int, b: int, compute_type: str) -> int - compute_type can be 'add' or 'mult'"
    prompt_01 = "add(a: int, b: int) -> int - Addition"
    prompt_02 = "mult(a: int, b: int) -> int - Multiplication"
    
    module_00_root = Node("module_00", prompt=prompt_00, apis=["calculate"], import_functions=[("module_01", "add"), ("module_02", "mult")])
    module_01      = Node("module_01", prompt=prompt_01, apis=["add"], import_functions=[], parent=module_00_root)
    module_02      = Node("module_02", prompt=prompt_02, apis=["mult"], import_functions=[], parent=module_00_root)


    for pre, fill, node in RenderTree(module_00_root):
        print(f"{pre}{node.name} - {node.apis} - {node.import_functions}")


    dict_exporter = DictExporter()
    tree_dict = dict_exporter.export(module_00_root)
    print(json.dumps(tree_dict, indent=2))


    # Read file into a string
    with open("tests/test_01/w01_dir.md", "r") as file:
        w01_dir_template = file.read()
    '''
    # ============================================================
    
    files = [
        {"path": "add.py", "contents": ""},
        {"path": "README.md", "contents": "`add(a: int, b: int) -> int`"},
    ]

    tree = DirTree()
    tree.json_to_tree(files)
    tree.print_dir_tree()

    files_dict = tree.generate_file_dict()
    print(json.dumps(files_dict, indent=2))

    # Generate string from files_dict
    files_string = ""
    for path, content in files_dict.items():
        files_string += f"{path}: {content}\n"
    print(files_string)

    prompts = (f"Implement the add function in the add.py file. Update the README.md to make it nicer.  {files_string}")
    response, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json(prompts)
    
    print("Response:")
    print(response)
    print("-"*100)
    print(f"Input prompt word count: {input_prompt_word_count}")
    print(f"Output prompt word count: {output_prompt_word_count}")

    # ============================================================




if __name__ == "__main__":
    main()