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

from src.stage_impl import stage_impl




# Example: Access node attributes
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
   


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


    stage_impl(module_00_root, w01_dir_template)

if __name__ == "__main__":
    main()