from anytree import Node, RenderTree
from anytree.exporter import JsonExporter, DictExporter
import json
import os
import shutil

from src.dir_tree.dir_tree import DirTree, Node_Dir, File, State
from src.project_tree.project_tree import ProjectTree, ProjectNode
from src.agent_chat import chat_agent_code_json, chat_agent_code_json_anthropic

import asyncio
from claude_agent_sdk import (
    ClaudeSDKClient, ClaudeAgentOptions,
    AssistantMessage, TextBlock
)




def print_header(msg: str) -> None:
    print()
    print("==================================================")
    print(msg)
    print("==================================================")




async def get_response(client, prompt):
    """Send prompt, return text response."""
    await client.query(prompt)
    response = ""
    async for message in client.receive_response():
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    response += block.text
    return response

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    math_node.dir = "/Users/jvasiljevic/continue/gh/design-patterns/design_patterns/tools/tool_4/code_gen/claude/math"
    
    calculate_node = project_tree.add_node("calculate", dependencies=["math"])
    calculate_node.apis = ["calculate(a: int, b: int, operation: str) -> int"]
    calculate_node.prompt = """
    Implement a python program that can calculate the result of two numbers based on the operation.
    """
    calculate_node.dir = "/Users/jvasiljevic/continue/gh/design-patterns/design_patterns/tools/tool_4/code_gen/claude/calculate"

    template_files = [
            {"path": "README_API_SIGNATURE.md", "contents": "# API Signature\n\n`from <relative_path>.filename import <function_name> <function_name>(size: int, name: string) -> int` - <Description>\n\n"},
            {"path": "README_tests.md", "contents": "# Absolute minimum possible readme, just two commands on how to run setup.sh and then run_tests.sh from this directory.\n"},
            {"path": "src/__init__.py", "contents": ""},
            {"path": "tests/test.py", "contents": "import unittest\n\nclass TestClass(unittest.TestCase):\n    \"\"\"Test cases for [DESCRIBE WHAT YOU'RE TESTING].\"\"\"\n    \n    def test_example(self):\n        \"\"\"Test [DESCRIBE THIS TEST].\"\"\"\n        # TODO: Add your test assertions here\n        # self.assertEqual(actual, expected)\n        pass\n\n\nif __name__ == '__main__':\n    # Create test suite and run tests\n    loader = unittest.TestLoader()\n    suite = loader.loadTestsFromTestCase(TestClass)\n    runner = unittest.TextTestRunner(verbosity=2)\n    result = runner.run(suite)\n    \n    # Write test result to file\n    with open('../replay/test_bool.txt', 'w') as f:\n        if result.wasSuccessful():\n            f.write('PASSED')\n        else:\n            f.write('FAILED')"},
            {"path": "tests/run_tests.sh", "contents": "# Test runner that sets PYTHONPATH and runs tests\n"},
            {"path": "tests/setup.sh", "contents": "# Make python env, install requirements, set PYTHONPATH in venv activation\n"},
            {"path": "tests/requirements.txt", "contents": ""},
        ]

    # Convert template files to string
    template_files_string = ""
    for file in template_files:
        template_files_string += f"File: {file['path']}\n"
        template_files_string += f"Contents: {file['contents']}\n"
        template_files_string += "\n"

    system_prompt="""
        You are coder agent. 
        I will give you goals and dependencies that you must try to use. 
        Just do the coding work, and respond EXTREAMLY SHORTLY with status alike 'Done' or similar.
        """
    allowed_tools=["Read", "Edit", "Bash", "Write"]

    # Agent 1: A code reviewer
    agent1_options = ClaudeAgentOptions(
        system_prompt=f"""
        You are coder agent. 
        I will give you goals and dependencies that you must try to use. 
        Just do the coding work, and respond EXTREAMLY SHORTLY with status alike 'Done' or similar.
        
        You only operate in this one directory. 
        Store all your work in {math_node.dir}

        At the end run the tests and return the result.
        Respond with the directory path where you stored the work.
        
        """,
        allowed_tools=allowed_tools,
        cwd=math_node.dir
    )

    # Agent 2: A developer who responds to feedback
    agent2_options = ClaudeAgentOptions(
        system_prompt=system_prompt, 
        allowed_tools=allowed_tools,
        cwd=calculate_node.dir
    )

    """
    # Delete the directory if it exists
    if os.path.exists(math_node.dir):
        shutil.rmtree(math_node.dir)
    os.makedirs(math_node.dir)
    if os.path.exists(calculate_node.dir):
        shutil.rmtree(calculate_node.dir)
    os.makedirs(calculate_node.dir)
    """


    async with ClaudeSDKClient(agent1_options) as agent1, \
               ClaudeSDKClient(agent2_options) as agent2:

        prompt = ""
        prompt += math_node.prompt
        prompt += "\nMake these APIs available."
        # Convert math_node.apis to string
        math_node_apis_string = ""
        for api in math_node.apis:
            math_node_apis_string += f"{api}\n"
        prompt += math_node_apis_string
        
        prompt += "\nUse this project template: "
        prompt += template_files_string
        print("\nSending a msg to agent1...\n")
        print(prompt)
        answer = await get_response(agent1, prompt)
        print(f"💻 Agent1: {answer}")
        


asyncio.run(main())

