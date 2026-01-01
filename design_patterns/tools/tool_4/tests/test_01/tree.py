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
import shutil


from src.dir_tree.dir_tree import DirTree, Node_Dir, File, State
from src.project_tree.project_tree import ProjectTree, ProjectNode
from src.agent_chat import chat_agent_code_json, chat_agent_code_json_anthropic

import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

# ========================================================
# Helper Functions
# ========================================================

def print_header(msg: str) -> None:
    print()
    print("==================================================")
    print(msg)
    print("==================================================")

def dir_tree_to_string_HELPER(tree: DirTree, msg: str) -> str:
    files_dict = tree.generate_file_dict()
    files_json_string = json.dumps(files_dict, indent=2)
    print(files_json_string)
    return files_json_string






def test_02(project_list: list[dict]):

    project_list = []
    project_list.append(
        {"name": "simple_calculator",
        "goal": "Implement a simple calculator that can add, sub, mult, div two numbers. Make sure to make FOUR SEPERATE FILES, one for each of the operations ( I am testing multi file setups)."})


    
    for project in project_list:
        project_name = project["name"]
        project_goal = project["goal"]

        OUTPUT_DIR = f"code_gen/{project_name}"
        RUN_LOCAL_DIR = "/Users/jvasiljevic/continue/gh/design-patterns/design_patterns/tools/tool_4/"
        LOCAL_DIR = "/Users/jvasiljevic/continue/gh/design-patterns/design_patterns/tools/tool_4/code_gen/"

        # ========================================================
        # Step 1: Initialize with template files
        # ========================================================
        print_header("Step 1: Initialize with template files...")
        files = [
            {"path": "README_API_SIGNATURE.md", "contents": "# API Signature\n\n`from <relative_path>.filename import <function_name> <function_name>(size: int, name: string) -> int` - <Description>\n\n"},
            {"path": "README_tests.md", "contents": "# Absolute minimum possible readme, just two commands on how to run setup.sh and then run_tests.sh from this directory.\n"},
            {"path": "src/__init__.py", "contents": ""},
            {"path": "tests/test.py", "contents": "import unittest\n\nclass TestClass(unittest.TestCase):\n    \"\"\"Test cases for [DESCRIBE WHAT YOU'RE TESTING].\"\"\"\n    \n    def test_example(self):\n        \"\"\"Test [DESCRIBE THIS TEST].\"\"\"\n        # TODO: Add your test assertions here\n        # self.assertEqual(actual, expected)\n        pass\n\n\nif __name__ == '__main__':\n    # Create test suite and run tests\n    loader = unittest.TestLoader()\n    suite = loader.loadTestsFromTestCase(TestClass)\n    runner = unittest.TextTestRunner(verbosity=2)\n    result = runner.run(suite)\n    \n    # Write test result to file\n    with open('../replay/test_bool.txt', 'w') as f:\n        if result.wasSuccessful():\n            f.write('PASSED')\n        else:\n            f.write('FAILED')"},
            {"path": "tests/run_tests.sh", "contents": "# Test runner that sets PYTHONPATH and runs tests\n"},
            {"path": "tests/setup.sh", "contents": "# Make python env, install requirements, set PYTHONPATH in venv activation\n"},
            {"path": "tests/requirements.txt", "contents": ""},
        ]

        tree = DirTree()
        tree.json_to_tree(files)        # To do: rename to dict_to_tree
        tree.print_dir_tree(words=True, contents=False, state=True)
        

        # ========================================================
        # Step 2: Send to Agent for code gen
        # ========================================================
        print_header("Step 2: Send to Agent for code gen...")
        files_string = dir_tree_to_string_HELPER(tree, "Initial dir tree...")

        prompt_imports = """**PYTHONPATH in setup.sh **
    - In `setup.sh`: After creating venv, add `export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"` to venv/bin/activate
    - Or set it in a test runner script `run_tests.sh`: `PYTHONPATH="$(dirname "$0")/.." python3 test.py`
    - Test files use clean imports: `from module1 import add, sub`"""
        
        prompts = (f"{project_goal}. Use this dir template for how to structure the code: {files_string}. IMPORT STRATEGY: {prompt_imports}")
        #print(prompts)
        #response_string, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json(prompts)
        response_string, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json_anthropic(prompts)
        print("\n\nResponse:")
        print(response_string)
        print()
        print(f"\nInput prompt word count: {input_prompt_word_count}")
        print(f"Output prompt word count: {output_prompt_word_count}")
        print("Done")



        # ========================================================
        # Step 3: Convert generated code back into dir tree
        # ========================================================
        print_header("Step 3: Convert generated code back into dir tree...")
        response_dict = json.loads(response_string)
        print(response_dict)
        tree.json_to_tree(response_dict) # Convert the response back into a dir tree
        tree.print_dir_tree(words=True, contents=False, state=True)



        # ========================================================
        # Step 4: Run the tests
        # ========================================================

        print_header("Step 4: Run the tests")
        # Store files from dir tree into files

        # Delete the code_gen/calculator directory if it exists
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)

        store_path = tree.store_files(OUTPUT_DIR)
        print(f"Stored files to: {store_path}")

        # From store_path, remove the LOCAL_DIR from the path
        #store_path = store_path.replace(LOCAL_DIR, "")
        #print(f"Store path: {store_path}")

        # Run setup.sh from the store_path directory
        os.system(f"cd {store_path}/tests/ && ./setup.sh")
        
        # Run run_tests.sh from the store_path directory
        os.system(f"cd {store_path}/tests/ && ./run_tests.sh")
        
        
        # ========================================================
        # Step 5: Setup for Blind Tests
        # ========================================================
        print_header("Step 5: Setup for Blind Tests...")
        
        test_name = "test_blind"
        files = [
            {"path": "tests/test_blind.py", "contents": """
    import unittest

    class TestClass(unittest.TestCase):
        \"\"\"Test cases for [DESCRIBE WHAT YOU'RE TESTING].\"\"\"
        
        def test_example(self):
            \"\"\"Test [DESCRIBE THIS TEST].\"\"\"
            # TODO: Add your test assertions here
            # self.assertEqual(actual, expected)
            pass

    if __name__ == '__main__':
        # Create test suite and run tests
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(TestClass)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Write test result to file
        with open('../replay/{test_name}_bool.txt', 'w') as f:
            if result.wasSuccessful():
                f.write('PASSED')
            else:
                f.write('FAILED')
        """}
        ]

        tree.add_files_to_dir_tree(files)        # To do: rename to dict_to_tree
        tree.print_dir_tree()
        
        # Make certain things hidden
        tree.change_dir_state("src", State.VISIBLE_PATH)
        tree.change_file_state("tests/test.py", State.HIDDEN)
        tree.print_dir_tree(state=True)





        files_string = dir_tree_to_string_HELPER(tree, "New Blind Tests...")

        prompt_imports = """**PYTHONPATH in setup.sh **
    - In `setup.sh`: After creating venv, add `export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"` to venv/bin/activate
    - Or set it in a test runner script `run_tests.sh`: `PYTHONPATH="$(dirname "$0")/.." python3 test.py`
    - Test files use clean imports: `from module1 import add, sub`"""
        
        prompts = (f"Implement a tests in test_blind.py file that tests the code based on the API signature in README_API_SIGNATURE.md. Don't forget to add test to run_tests.sh file. {files_string}. IMPORT STRATEGY: {prompt_imports}")
        #print(prompts)
        #response, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json(prompts)
        response_string, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json_anthropic(prompts)
        print("\n\nResponse:")
        print(response_string)
        print()
        print(f"\nInput prompt word count: {input_prompt_word_count}")
        print(f"Output prompt word count: {output_prompt_word_count}")
        print("Done")






        # ========================================================
        # Step 6: Convert generated code back into dir tree...
        # ========================================================
        print_header("Step 6: Convert generated code back into dir tree...")
        response_dict = json.loads(response_string)
        print(response_dict)

        # Convert the response back into a dir tree
        #tree.json_to_tree(response_dict)
        tree.add_files_to_dir_tree(response_dict)
        tree.change_dir_tree_state(State.VISIBLE)
        tree.print_dir_tree(words=True, contents=False, state=True)

        

        # ========================================================
        # Step 7: Store Code & Run the tests
        # ========================================================
        print_header("Step 7: Store Code & Run the tests...")
        # Store files from dir tree into files

        # Add empty dir replay to store results of tests. 
        tree.add_dir("replay/")
        tree.print_dir_tree()
        
        # Delete the code_gen/calculator directory if it exists
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)

        store_path = tree.store_files(OUTPUT_DIR)
        print(f"Stored files to: {store_path}")

        # Run setup.sh from the store_path directory
        os.system(f"cd {store_path}/tests/ && ./setup.sh")
        
        # Run run_tests.sh from the store_path directory & save the terminal output to a file
        # Redirect both stdout and stderr (2>&1) to capture tracebacks
        log_file_path = f"{store_path}/replay/run_tests.log"
        os.system(f"cd {store_path}/tests/ && ./run_tests.sh > {log_file_path} 2>&1")
        
        with open(log_file_path, "r") as file:
            terminal_output = file.read()
            print(f"\n\nTerminal output: {terminal_output}")

        exit()
        
        # ========================================================
        # Step 8: Fix errors in code
        # ========================================================
        print_header("Step 8: Fix errors in code...")

        print("\nTree before error fix:")
        tree.print_dir_tree(words=True, contents=True, state=True)


        # Load file store_path/replay/run_tests.log into a string
        with open(log_file_path, "r") as file:
            error_string = file.read()
        print(f"\n\nError string: {error_string}")

        files_string = dir_tree_to_string_HELPER(tree, "New Blind Tests...")
        prompt_error_fix = f"Fix the errors in the code. The errors are: {error_string}. The code is here: {files_string}"

        response_string, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json_anthropic(prompt_error_fix)
        print("\n\nResponse:")
        print(response_string)
        print()
        print(f"\nInput prompt word count: {input_prompt_word_count}")
        print(f"Output prompt word count: {output_prompt_word_count}")
        print("Done")


        # ========================================================
        # Step 9: Convert generated code back into dir tree...
        # ========================================================
        print_header("Step 9: Convert generated code back into dir tree...")
        response_dict = json.loads(response_string)
        print(response_dict)

        # Convert the response back into a dir tree
        #tree.json_to_tree(response_dict)
        tree.add_files_to_dir_tree(response_dict)
        tree.change_dir_tree_state(State.VISIBLE)
        print("\nTree after error fix:")
        tree.print_dir_tree(words=True, contents=True, state=True)
        

        # ========================================================
        # Step 10: Store Code & Run the tests
        # ========================================================
        print_header("Step 10: Store Code & Run the tests...")
        # Store files from dir tree into files

        # Delete the code_gen/calculator directory if it exists
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)

        store_path = tree.store_files(OUTPUT_DIR)
        print(f"Stored files to: {store_path}")

        # Run setup.sh from the store_path directory
        os.system(f"cd {store_path}/tests/ && ./setup.sh")
        
        # Run run_tests.sh from the store_path directory & save the terminal output to a file
        # Redirect both stdout and stderr (2>&1) to capture tracebacks
        log_file_path = f"{store_path}/replay/run_tests.log"
        os.system(f"cd {store_path}/tests/ && ./run_tests.sh > {log_file_path} 2>&1")
        
        with open(log_file_path, "r") as file:
            terminal_output = file.read()
            print(f"\n\nTerminal output: {terminal_output}")




    '''
    NEXT STEPs:
    1. Generate really good reports
    - tokens
    - debug attempts, test passes etc. 
    - summory of test failiures. (Histogram of words that describe the test error categories)    
    
    2. Multi block projects:
    - create multiple projects, that build on each other. 
    - implement multi-block debug: 
        - block tries to solve it's problem locally by identifying if it's integration code, or it files a problem to a dependency. 
        - dependency tries to repro, in a local test. then fix it locally. 
    - Define FSMs for the multi-block debug. 
        - in clude exit conditions, so that you don't get sutck in a loop. 
    
    '''

    exit()


def test_03_project_tree():

    # ========================================================
    # Step 1: Initialize a new ProjectTree...
    # ========================================================
    print_header("Step 1: Initialize a new ProjectTree...")
    
    if True:
        project_tree = ProjectTree(name="claude_sdk")
        
        # Add nodes (dependencies must be added first)
        coder = project_tree.add_node("coder")
        coder.apis = [
            "code_gen_project(prompt: str, project_name: str) -> str - Creates a new project in the output_dir with the given project_name, stores the code there, and returns the path to the project."
        ]
        coder.prompt = """
        Implement a python program that uses Claude SDK to generate code based on a prompt.
        The agent works only in the output_dir/project_name/, and ignores all other directories.
        Set output_dir to be the same dir as the tests.  
        The agent should write the code, and make some tests for the code. 
        It should also write a README_API_SIGNATURE.md file, and a README_tests.md file. 
        Then it should run the tests and return the result.
        Make sure to write some tests that actually generate code, and store it in the output_dir so I can see. 
        Make sure to use Claude SDK to generate the code. 
        import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Find all TODO comments and create a summary",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Glob", "Grep"])
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
        """
        
       
    
    if False:
        project_tree = ProjectTree(name="calculator")
        
        # Add nodes (dependencies must be added first)
        math_node = project_tree.add_node("math")
        math_node.apis = [
            "add(a: int, b: int) -> int", 
            "sub(a: int, b: int) -> int", 
            "mult(a: int, b: int) -> int", 
            "div(a: int, b: int) -> int"
        ]
        math_node.prompt = """
        Implement a python program that can add, sub, mult, div two numbers. 
        Make sure to make FOUR SEPERATE FILES, one for each of the operations ( I am testing multi file setups).
        """
        
        calculate_node = project_tree.add_node("calculate", dependencies=["math"])
        calculate_node.apis = ["calculate(a: int, b: int, operation: str) -> int"]
        calculate_node.prompt = """
        Implement a python program that can calculate the result of two numbers based on the operation.
        """

    if False:
        project_tree = ProjectTree(name="coder_platform")
        
        
        agent_node = project_tree.add_node(
            name="coder_agent", 
            dependencies=[],
            apis=["coder(prompt: str) -> str"], 
            prompt="""
            Implement a python program that uses anthropic model="claude-opus-4-5-20251101" to generate code based on a prompt. 
            The coder agent should set up an agent that returns a json object with the code.
            [ {"path": "main.py", "contents": "",
              {"path": "README_tests.md", "contents": ""}
            """
        )

        files_node = project_tree.add_node(
            name="file_processing", 
            dependencies=[],
            apis=[
                "store_files_into_dir(agent_response: str, output_dir_path: str) -> str - Returns stored path.",
                "load_files_from_dir(output_dir_path: str) -> List[Dict[str, str]] - Returns list of files in the directory.",
            ],
            prompt="""
            Implement a python program that can store files into a directory, and load files from a directory.
            """
        )

        coder_platform = project_tree.add_node(
            name="coder_platform", 
            dependencies=["coder_agent", "file_processing"],
            apis=[
                "generate_project(project_goal_prompt: str) -> str - Returns dir with generated project.",
            ],
            prompt="""
            Implement a python program that can generate code for a project based on a prompt.
            """
        )
        
    
    project_tree.print_tree(show_apis=True)

    # ========================================================
    # Step 2: Create the according Dir Tree...
    # ========================================================
    print_header("Step 2: Create the according Dir Tree...")
    
    template_files = [
            {"path": "README_API_SIGNATURE.md", "contents": "# API Signature\n\n`from <relative_path>.filename import <function_name> <function_name>(size: int, name: string) -> int` - <Description>\n\n"},
            {"path": "README_tests.md", "contents": "# Absolute minimum possible readme, just two commands on how to run setup.sh and then run_tests.sh from this directory.\n"},
            {"path": "src/__init__.py", "contents": ""},
            {"path": "tests/test.py", "contents": "import unittest\n\nclass TestClass(unittest.TestCase):\n    \"\"\"Test cases for [DESCRIBE WHAT YOU'RE TESTING].\"\"\"\n    \n    def test_example(self):\n        \"\"\"Test [DESCRIBE THIS TEST].\"\"\"\n        # TODO: Add your test assertions here\n        # self.assertEqual(actual, expected)\n        pass\n\n\nif __name__ == '__main__':\n    # Create test suite and run tests\n    loader = unittest.TestLoader()\n    suite = loader.loadTestsFromTestCase(TestClass)\n    runner = unittest.TextTestRunner(verbosity=2)\n    result = runner.run(suite)\n    \n    # Write test result to file\n    with open('../replay/test_bool.txt', 'w') as f:\n        if result.wasSuccessful():\n            f.write('PASSED')\n        else:\n            f.write('FAILED')"},
            {"path": "tests/run_tests.sh", "contents": "# Test runner that sets PYTHONPATH and runs tests\n"},
            {"path": "tests/setup.sh", "contents": "# Make python env, install requirements, set PYTHONPATH in venv activation\n"},
            {"path": "tests/requirements.txt", "contents": ""},
        ]
    
    
    
    {project_tree.name}
    # ========================================================
    # Step 3: Init dir tree...
    # ========================================================
    print_header("Step 3: Init dir tree...")
    dir_tree = DirTree()
    dir_tree.add_dir(project_tree.name, state=State.VISIBLE)
    for node in project_tree.get_nodes_in_dependency_order():
        print("\n Adding new node, and some files inside it...")
        print(node.name)
        dir_tree.add_dir(name=node.name, state=State.VISIBLE, dir=project_tree.name)
        dir_tree.add_files_to_dir_tree(files=template_files, dir=f"{project_tree.name}/{node.name}")
        node.dir = f"{project_tree.name}/{node.name}"
        dir_tree.print_dir_tree()
    
    project_tree.print_tree(show_apis=True)
    
    
    
    
    

    # Delete the code_gen/calculator directory if it exists (before processing nodes)
    OUTPUT_DIR = f"code_gen/{project_tree.name}"
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    
    for node in project_tree.get_nodes_in_dependency_order():
        # ========================================================
        # Step 4a: Code Gen...
        # ========================================================
        print_header(f"Step 4a: Code Gen... for node: {node.name}")
        
        print()
        prompt = node.prompt
        prompt += f"Implement these apis: {node.apis}"
        print(prompt)

        # Get the dependencies, but needs pointers to the APIs, or just pointer to the directory?
        if (node.dependencies):
            prompt_dependencies = "Use these functions as your imports:"
            count_dep = 0
            for dependency in node.dependencies:
                dependency_node = project_tree.get_node(dependency.name)
                one_dependency_prompt = f"{count_dep}: dir: {dependency_node.dir}, apis: {dependency_node.apis}"
                prompt_dependencies += f"{one_dependency_prompt}"
                count_dep += 1
            prompt += f"{prompt_dependencies}"


        # Set everything to visible
        print("\n\nDir tree - everything visible")
        dir_tree.change_dir_state(project_tree.name, state=State.VISIBLE)
        dir_tree.print_dir_tree(words=False, contents=False, state=True)

        
        

        # Hide all dir, except the current one being worked on
        for node_hidden in project_tree.get_nodes_in_dependency_order():
            if node_hidden.name != node.name:
                print(f"Hiding dir: {node_hidden.dir}")
                dir_tree.change_dir_state(node_hidden.dir, State.HIDDEN)


        # For dependencies, expose APIs and src/ paths
        if (node.dependencies):
            for dependency in node.dependencies:
                dependency_node = project_tree.get_node(dependency.name)
                dir_tree.change_dir_state(dependency_node.dir, State.HIDDEN)
                src_path = os.path.join(dependency_node.dir, "src")
                dir_tree.change_dir_state(src_path, State.VISIBLE_PATH)
                api_path = os.path.join(dependency_node.dir, "README_API_SIGNATURE.md")
                dir_tree.change_file_state(api_path, State.VISIBLE)
                requirements_path = os.path.join(dependency_node.dir, "tests/requirements.txt")
                dir_tree.change_file_state(requirements_path, State.VISIBLE)
        

        print("\n\nDir tree after visibility adjustments:")
        dir_tree.print_dir_tree(words=False, contents=False, state=True)
       

        
        # Get the files 
        files_dict = dir_tree.generate_file_dict()
        files_json_string = json.dumps(files_dict, indent=2)
        print(files_json_string)

        prompt += files_json_string

        print("\n\nFinal prompt:")
        print(prompt)




        
        response_string, input_prompt_word_count, output_prompt_word_count = chat_agent_code_json_anthropic(prompt)
        print("\n\nResponse:")
        print(response_string)
        print()
        print(f"\nInput prompt word count: {input_prompt_word_count}")
        print(f"Output prompt word count: {output_prompt_word_count}")
        print("Done")


        # ========================================================
        # Step 4b: Convert generated code back into dir tree
        # ========================================================
        print_header("Step 4b: Convert generated code back into dir tree...")
        response_dict = json.loads(response_string)
        print(response_dict)
        dir_tree.add_files_to_dir_tree(files=response_dict)
        dir_tree.print_dir_tree(words=True, contents=False, state=True)


        # ========================================================
        # Step 4c: Run the tests
        # ========================================================
        OUTPUT_DIR_MAIN = "code_gen"

        print_header("Step 4c: Run the tests")
        # Store files from dir tree into files

        store_path = dir_tree.store_files(OUTPUT_DIR)
        print(f"Stored files to: {store_path}")

        # Construct the full path to the tests directory
        # store_path is the absolute path to code_gen/calculator
        # node.dir is "calculator/calculate" or "calculator/math"
        # So the full path is: store_path/node.dir/tests/
        test_dir_path = os.path.join(store_path, node.dir, "tests")
        print(f"Test directory path: {test_dir_path}")

        # Run setup.sh & run_tests.sh from the test directory
        os.system(f"cd {test_dir_path} && ./setup.sh")
        os.system(f"cd {test_dir_path} && ./run_tests.sh")
        
    
    # ========================================================
    # FINALE DIR TREE
    # ========================================================
    print_header("FINAL DIR TREE...")
    dir_tree.print_dir_tree(words=True, contents=False, state=False)
    '''
    Next steps:

    1. add bling testing
    2. add project reuse. 
        - search through generated code for a matching project. 
        - check project name, api signatures and dependencies (?)
        - check if tests passed
        - eventually ad quality checking to the tests. 
        - pressure on top. if tests are light, and now we are piling on projects, we should go and trigger additional testing to the project below. 

    3. amazing replay/reports. 


    - clean up code, make function calls, so there is less code duplication
    - add debug to the Project Tree node loop. 
    - add more reports per project. 
        - save error issues. propagate to high level. 

    Add helper function for building Project Tree's fast. 
    - 


    '''


async def main():
    async for message in query(
        prompt="""
        In /Users/jvasiljevic/continue/gh/design-patterns/design_patterns/tools/tool_4/code_gen/ make a new dir called claude_project_03/.
        Implement a python hello world program.
        Commit it to github. 
        """,
        options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash", "Write"])
    ):
        print(message)  # Claude reads the file, finds the bug, edits it

asyncio.run(main())

'''
# Example: Access node attributes
def main():
    os.system('cls' if os.name == 'nt' else 'clear')


    if (False):
        project_list = []
        project_list.append(
            {"name": "simple_calculator",
            "goal": "Implement a simple calculator that adds two numbers."})
        project_list.append(
            {"name": "mm",
            "goal": "Implement a simple matrix multiplication that multiplies two matrices."})

        #test_02(project_list)


    #test_03_project_tree()

    test_04_claude_sdk()

if __name__ == "__main__":
    main()
'''