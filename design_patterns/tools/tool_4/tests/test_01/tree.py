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
from src.agent_chat import chat_agent_code_json, chat_agent_code_json_anthropic


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
        "goal": "Implement a simple calculator that adds two numbers."})


    
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
            {"path": "README_API_SIGNATURE.md", "contents": "# API Signature\n\n`function_name(size: int, name: string) -> int` - <Description>\n\n"},
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

        # Convert the response back into a dir tree
        tree.json_to_tree(response_dict)
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



# Example: Access node attributes
def main():
    os.system('cls' if os.name == 'nt' else 'clear')


    project_list = []
    '''
    project_list.append(
        {"name": "simple_calculator",
        "goal": "Implement a simple calculator that adds two numbers."})
    project_list.append(
        {"name": "mm",
        "goal": "Implement a simple matrix multiplication that multiplies two matrices."})
    project_list.append(
        {"name": "subtract",
        "goal": "Implement a function that subtracts two numbers."})
    project_list.append(
        {"name": "multiply",
        "goal": "Implement a function that multiplies two numbers."})
    project_list.append(
        {"name": "divide",
        "goal": "Implement a function that divides two numbers, handling division by zero errors."})
    project_list.append(
        {"name": "power",
        "goal": "Implement a function that calculates x raised to the power of y."})
    project_list.append(
        {"name": "factorial",
        "goal": "Implement a function that calculates the factorial of a non-negative integer."})
    project_list.append(
        {"name": "fibonacci",
        "goal": "Implement a function that returns the nth Fibonacci number."})
    project_list.append(
        {"name": "gcd",
        "goal": "Implement a function that calculates the greatest common divisor of two integers."})
    project_list.append(
        {"name": "lcm",
        "goal": "Implement a function that calculates the least common multiple of two integers."})
    project_list.append(
        {"name": "is_prime",
        "goal": "Implement a function that checks if a number is prime."})
    '''
    project_list.append(
        {"name": "binary_search",
        "goal": "Implement binary search algorithm that finds an element in a sorted array."})
    project_list.append(
        {"name": "linear_search",
        "goal": "Implement linear search algorithm that finds an element in an array."})
    project_list.append(
        {"name": "bubble_sort",
        "goal": "Implement bubble sort algorithm that sorts an array of integers."})
    project_list.append(
        {"name": "selection_sort",
        "goal": "Implement selection sort algorithm that sorts an array of integers."})
    project_list.append(
        {"name": "insertion_sort",
        "goal": "Implement insertion sort algorithm that sorts an array of integers."})
    project_list.append(
        {"name": "reverse_string",
        "goal": "Implement a function that reverses a string."})
    project_list.append(
        {"name": "palindrome_check",
        "goal": "Implement a function that checks if a string is a palindrome."})
    project_list.append(
        {"name": "count_words",
        "goal": "Implement a function that counts the number of words in a string."})
    project_list.append(
        {"name": "stack",
        "goal": "Implement a stack data structure with push, pop, and peek operations."})
    project_list.append(
        {"name": "queue",
        "goal": "Implement a queue data structure with enqueue, dequeue, and front operations."})
    project_list.append(
        {"name": "linked_list",
        "goal": "Implement a linked list data structure with insert, delete, and search operations."})
    project_list.append(
        {"name": "merge_sort",
        "goal": "Implement merge sort algorithm that sorts an array using divide and conquer approach."})
    project_list.append(
        {"name": "quick_sort",
        "goal": "Implement quick sort algorithm that sorts an array using partitioning and recursion."})
    project_list.append(
        {"name": "merge_sorted_arrays",
        "goal": "Implement a function that merges two sorted arrays into a single sorted array."})
    project_list.append(
        {"name": "two_sum",
        "goal": "Implement a function that finds two numbers in an array that add up to a target value."})
    project_list.append(
        {"name": "binary_tree",
        "goal": "Implement a binary tree data structure with insert, search, and traversal operations."})
    project_list.append(
        {"name": "hash_table",
        "goal": "Implement a hash table data structure with put, get, and delete operations."})
    project_list.append(
        {"name": "depth_first_search",
        "goal": "Implement depth-first search algorithm for traversing a graph represented as an adjacency list."})
    project_list.append(
        {"name": "breadth_first_search",
        "goal": "Implement breadth-first search algorithm for traversing a graph represented as an adjacency list."})
    project_list.append(
        {"name": "anagram_check",
        "goal": "Implement a function that checks if two strings are anagrams of each other."})
    project_list.append(
        {"name": "longest_common_prefix",
        "goal": "Implement a function that finds the longest common prefix among an array of strings."})
    project_list.append(
        {"name": "coin_change",
        "goal": "Implement a function that finds the minimum number of coins needed to make a target amount using dynamic programming."})
    
    
    test_02(project_list)


if __name__ == "__main__":
    main()