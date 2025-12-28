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
from src.agent_chat import chat_agent_code_json, chat_agent_code_json_anthropic





def test_01():
    files = [
        {"path": "add.py", "contents": ""},
        {"path": "README.md", "contents": "`add(a: int, b: int) -> int`"},
    ]

    tree = DirTree()
    tree.json_to_tree(files)
    tree.print_dir_tree()

    files_dict = tree.generate_file_dict()
    files_json_string = json.dumps(files_dict, indent=2)
    print("\n================================================\n")
    print("Files JSON String:")
    print("==================================================\n")
    print(files_json_string)
    

    # Generate string from files_dict
    files_string = ""
    for path, content in files_dict.items():
        files_string += f"{path}: {content}\n"
    print(files_string)

    #prompts = (f"Implement the add function in the add.py file. Update the README.md to make it nicer.  {files_string}")
    prompts = (f"Implement the add function in the add.py file. {files_string}")
    response, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json_anthropic(prompts)
    
    print("Response:")
    print(response)
    print("-"*100)
    print(f"Input prompt word count: {input_prompt_word_count}")
    print(f"Output prompt word count: {output_prompt_word_count}")

def dir_tree_to_string(tree: DirTree) -> str:
    files_dict = tree.generate_file_dict()
    files_json_string = json.dumps(files_dict, indent=2)
    print("\n================================================\n")
    print("Files JSON String:")
    print("==================================================\n")
    print(files_json_string)
    

    # Generate string from files_dict
    files_string = ""
    for path, content in files_dict.items():
        files_string += f"{path}: {content}\n"
    print(files_string)

    return files_json_string



def test_02():
    
    files = [
        {"path": "project_name/README_API_SIGNATURE.md", "contents": "# API Signature\n\n`function_name(size: int, name: string) -> int` - <Description>\n\n"},
        {"path": "project_name/src/__init__.py", "contents": ""},
        {"path": "project_name/tests/test.py", "contents": ""},
        {"path": "project_name/tests/run_tests.sh", "contents": "# Test runner that sets PYTHONPATH and runs tests\n"},
        {"path": "project_name/tests/setup.sh", "contents": "# Make python env, install requirements, set PYTHONPATH in venv activation\n"},
        {"path": "project_name/tests/requirements.txt", "contents": ""},
        {"path": "project_name/tests/README.md", "contents": "# Absolute minimum possible readme, just one line how to run the test\n"},
    ]

    tree = DirTree()
    tree.json_to_tree(files)        # To do: rename to dict_to_tree
    tree.print_dir_tree(words=True, contents=False, state=True)

    files_string = dir_tree_to_string(tree)
    print("\n================================================\n")
    print(type(files_string))
    print(files_string)
    print("==================================================\n")


    #tree.print_simple()

    count = tree.change_dir_state("project_name/tests", State.HIDDEN)
    tree.print_dir_tree(state=True)
    print(f"Number of states updated: {count}")
    exit()

    print("Sending prompt to agent...")
    prompts = (f"Implement a simple calculator that adds two numbers. Use this dir template for how to structure the code: {files_string}")
    print(prompts)
    #response, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json(prompts)
    response_string, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json_anthropic(prompts)
    print("\n\nResponse:")
    print(response_string)
    print("-"*100)
    print(f"Input prompt word count: {input_prompt_word_count}")
    print(f"Output prompt word count: {output_prompt_word_count}")
    print("Done")


    # Convert the response back into a dict
    response_dict = json.loads(response_string)
    
    print(type(response_dict))
    print(response_dict)

    # Convert the response back into a dir tree
    tree.json_to_tree(response_dict)
    tree.print_dir_tree(words=True, contents=False, state=True)

    tree.set_dir_to_invisible("calculator/src")
    tree.print_dir_tree(words=True, contents=False, state=True)

    # Next Step: mark the code and self tests as hidden
    
    # Next Step: Generate blind tests
    # Next Step: Execute Self Tests, record output of test results. Generates summary
    # Next Step: Execute Blind Tests, record output of test results. Generates summary
    # Issues in tests, do self loop debug to fix. 
    # Record into the reports, how many tests passed, failed, how many loops of fixing happened, and then final test results. 
    # Assign overall score for the project. 
    # Create back the project gen dir structure with 1/ 2/ etc.




# Example: Access node attributes
def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    #test_01()
    test_02()


if __name__ == "__main__":
    main()