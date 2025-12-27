

Example dir structure
```
<package_name>_pkg/
├── setup.py              ← At root (standard Python practice)
├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
├── <package_name>/          ← Package directory
│   ├── __init__.py
│   ├── <function_1>.py         # Empty
│   ├── <function_2>.py         # Empty
└── tests/
    ├── test.py
    ├── setup_and_run.sh
    ├── requirements.txt
    └── venv/
```



# Hiarchy of Packages

## Level 2 - top
Code Gen

## Level 1 - bottom
1. JSON processing

## Level 0 - bottom
1. string processing    design_patterns/tools/tool_1/code/pkg_string_processing/README.md
2. file processing      design_patterns/tools/tool_1/code/pkg_file_processing/README.md
3. agent chat           design_patterns/tools/tool_1/code/pkg_agent_chat/README.md
4. analysis (?)         NEW 








# Functions / Building Blocks

===================================================================================================================
                                                    AGENT CHAT - done2
===================================================================================================================

Implement this in tool_4/src/agent_chat.py

## 1. Agent Chat

### Basic:
- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_json(prompt)` -> string, int, int - Sets up agent to respond only with JSON code, sets temperature to low, no max token length for coding. Returns JSON string, input_prompt_word_count, output_prompt_word_count. 

### Description
Use DeepSeek for the LLM agent. 


[
  {
    "path": "src/main.py",
    "contents": "..."
  },
  {
    "path": "src/utils.py",
    "contents": "..."
  }
]

## Import Strategy (Avoid sys.path.insert and pip install -e)

**PYTHONPATH in setup.sh **
- In `setup.sh`: After creating venv, add `export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"` to venv/bin/activate
- Or set it in a test runner script `run_tests.sh`: `PYTHONPATH="$(dirname "$0")/.." python test.py`
- Test files use clean imports: `from module1 import add, sub`



===================================================================================================================
                                                    STRING PROCESSING - done
===================================================================================================================

Implement this in design_patterns/tools/tool_2/code/

## 2. String Processing

### Basic
- `append_string(base: str, addition: str) -> str` - Concatenate strings
- `search_and_delete(text: str, pattern: str) -> str` - Find and remove
- `search_and_replace(text: str, old: str, new: str) -> str` - Find and replace
- `strip_markdown(text: str) -> str` - Remove markdown formatting

Example dir structure
```
<package_name>_pkg/
├── setup.py              ← At root (standard Python practice)
├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
├── <package_name>/          ← Package directory
│   ├── __init__.py
│   ├── <function_1>.py         # Empty
│   ├── <function_2>.py         # Empty
└── tests/
    ├── test.py
    ├── setup_and_run.sh
    ├── requirements.txt
    └── venv/
```

===================================================================================================================
                                                   FILE PROCESSING - done
===================================================================================================================

Implement this in design_patterns/tools/tool_2/code/

## 3. File Processing

- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file
- `read_file_content(filepath: str) -> str` - Read single file
- `create_directory_structure(structure: dict) -> bool` - Create nested directories
- `file_exists(filepath: str) -> bool` - Check existence
- `dir_exists(filepath: str) -> bool` - Check existence

Example dir structure
```
<package_name>_pkg/
├── setup.py              ← At root (standard Python practice)
├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
├── <package_name>/          ← Package directory
│   ├── __init__.py
│   ├── <function_1>.py         # Empty
│   ├── <function_2>.py         # Empty
└── tests/
    ├── test.py
    ├── setup_and_run.sh
    ├── requirements.txt
    └── venv/
```


===================================================================================================================
                                                   ANALYSIS - DONE
===================================================================================================================

Implement this in design_patterns/tools/tool_2/code/

## 3. Analysis

### Basic: Dir/File counter mechanics
- `count_loc(dir: string) -> int` - Returns total lines of text in directory
- `count_words(dir: string, text: string) -> int` - Returns total words in dir
- `count_files(dir: string) -> int` - Returns the number of files in dir
- `count_file_types(dir: string)` -> List[Tuple[str, int]] - Returns a list of tuples, with file type (ex. "*.py") and corresponding count
- `get_path_to_file(dir: string, filename: string) -> string` - searches all files in the given dir for the given filename and returns the path to it

### Python Code Analysis
- `count_python_imports(dir: string) -> Tuple[int, List[str]]` - Use ast python lib to make a list of all imported functions, code, libraries, local or remote, all types. Returns the total number of imports and the list of all imports. 
-`count_python_functions(dir: string) -> Tuple[int, List[str]]` - Use ast python lib to make a list of all functions defined in given dir. Returns the function count and all function names. 

Example dir structure
```
<package_name>_pkg/
├── setup.py              ← At root (standard Python practice)
├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
├── <package_name>/          ← Package directory
│   ├── __init__.py
│   ├── <function_1>.py         # Empty
│   ├── <function_2>.py         # Empty
└── tests/
    ├── test.py
    ├── setup_and_run.sh
    ├── requirements.txt
    └── venv/
```


===================================================================================================================
                                                   JSON PROCESSING - done
===================================================================================================================

Implement this in design_patterns/tools/tool_3/src/json/

## 4. JSON Processing

### Basic:       File / Dict / String  / Helper
- `load_json_from_file(filepath: str) -> dict` - Load JSON from file
- `save_json_to_file(data: dict, filepath: str) -> bool` - Save JSON to file
- `dict_to_json_string(data: dict, pretty: bool) -> str` - Convert dict to JSON string
- `parse_json_string(json_str: str) -> dict` - Parse JSON string to dict
- `load_json_string_from_file(filepath: str) -> str` - Load JSON string from file
- `save_json_string_to_file(json_str: str, filepath: str) -> bool` - Save JSON string to file
- `validate_json_schema(data: dict, schema: dict) -> bool` - Validate structure

### Getters / Setters
- `get_json_dir_example() -> string` - Returns an example of the json_dir file
- `get_json_dir_schema() -> string` - Returns the schema of the json_dir file
- `generate_json_schema_from_json(input_json_file)` - Saves to the same location

### Advanced
- `load_directory_to_json(directory: str) -> dict` - Directory to JSON, always recursive
- `store_json_to_directory()`




===================================================================================================================
                                                   CODE GEN - wip
===================================================================================================================

Implement this in tool_3/src/code_gen/

## 5. Package_03 - Code Gen

### Dir-Level Functions
1. `code_gen_dir(prompt: str, generated_code_dir_path: str) -> Tuple[str, int, int]` - Code generation. It returns 1) path to the dir where it wrote into, 2) total input tokens, 3) total output tokens
2. `code_gen_dir(prompt: str, generated_code_dir_path: str, template_dir_path: str) -> Tuple[str, int, int]` - Code generation. It loads in the files from template_dir_path and passes them as input. It returns 1) path to the dir where it wrote into, 2) total input tokens, 3) total output tokens

#### Description
User provides the prompt, and it uses the chat_agent_code_json() to generate code. 

### Project-Level functions
1. `code_gen_project(prompt: str, project_name: str, generated_code_dir_path: str) -> Tuple[str, int, int]` - Code generation, returns the dir with the code
1. `code_gen_project(prompt: str, project_name: str, generated_code_dir_path: str, template_dir_path: str) -> Tuple[str, int, int]` - Code generation, uses the dir and the code in it as the initial starting point. 

#### Description
User provides the prompt, and it uses the chat_agent_code_json() to generate code. 
It stores all projects into a dir called code_gen, in a dir based on project_name. 
When creating a new project dir, always initialize the latest_dir.txt so that you can increment it and generate multiple versions under the same project name. 
Set output code dir to tool_2/code_gen/
```
generated_code/
├── website/                     # Project folder
│   ├── latest_dir.txt           # Keeps track of the latest dir name
|   ├── latest/                  # A directory that is virtually linked to the latest generated project code. 
│   ├── 1/
│   │   ├── .reports.md              # A hidden file that CodeGen will write reports into
│   ├── 2/
│   ├── 3/                       # The latest generated project code. 
├── app/                         # Project folder
│   ├── latest_dir.txt
|   ├── latest/
│   ├── 1/
│   ├── 2/
│   ├── 3/
```

Into the .reports.md file, write the following analysis of the code generated in the dir. 
```
input_prompt_word_count = <int>     # prompt sent to the chat agent
output_prompt_word_count = <int>    # json response returned from agent. 
```

Use these available python packages:
1. Agent Chat: tool_3/src/agent_chat.py
2. JSON Processing: tool_3/src/json/













------ ADD BACK TO CODE GEN ------

### Code Gen Analysis Helper functions. 
-` count_requirements_loc(dir: string) -> int` - Searched for "requirements.txt" file in given dir, and returns the Lines of Code in the file. If it finds multiple "requirements.txt" files it errors out. 
- `count_readme_api_signature_md_loc() - int` - Searched for "README_API_SIGNATURE.md" file in given dir, and returns the Lines of Code in the file. If it finds multiple "requirements.txt" files it errors out. 
- `count_readme_api_signature_md_word_count() - int` - Searched for "README_API_SIGNATURE.md" file in given dir, and returns the total world count in the file. If it finds multiple "requirements.txt" files it errors out. 






### Getters / Setters
- `get_json_dir_example() -> string` - Returns an example of the json_dir file
- `get_json_dir_schema() -> string` - Returns the schema of the json_dir file
- `generate_json_schema_from_json(input_json_file)` - Saves to the same location



===================================================================================================================
                                                   DIR TREE
===================================================================================================================

Implement this in tool_4/src/dir_tree.py

1. class dir_tree, using tree python lib
Nodes: files and dir

Dir Attributes:

- tokens
- tokens_dirty


File Attributes: 
- path: str
- content: str

- file_type: Enum: "sw", "replay_infra"
- readonly: T/F

- tokens: int
- tokens_dirty: T/F





Pruning for Coders
Add a field for "view": 

1. Fully excluded
- completly non existent

2. path included, contents excluded. 
- readonly=True. 
- existance of file is known, but its contents are hidden, but the file is functional and it's there

3. Path & contents included. readonly=True

4. Path & contents included. readonly=False










Advanced
- How will agents specify edits? Full file replacement, diffs, or something like search/replace blocks?



class Mutability(Enum):
    MUTABLE = "mutable"
    IMMUTABLE = "immutable"

@dataclass
class DirTree:
    mutability: Mutability = Mutability.MUTABLE


# Option 3: common in many APIs
readonly: bool = False








Implement  2 modules, each with the structure below: module1, module2. 

## Module1:
`add(a: int, b: int) -> int'
`sub(a: int, b: int) -> int'

## Module2:
`calculate(a: int, b: int, type: str) -> int'  # Make sure to use add() and sub() from module!!!


Example dir structure
```
dir_structure/
├── module1/                        # module1     
│   ├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
│   ├── module1/
│   │   ├── __init__.py
│   │   ├── add.py
│   │   ├── sub.py
│   └── tests/
│       ├── test.py                 # Clean imports: `from module1 import add, sub` (no sys.path manipulation)
│       ├── run_tests.sh            # Test runner that sets PYTHONPATH and runs tests
│       ├── setup.sh                # Make python env, install requirements, set PYTHONPATH in venv activation
│       ├── requirements.txt
│       ├── README.md               # Absolute minimum possible readme, just one line how to run the test

│       └── venv/
└── module2/                        # module2     
    ├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
    ├── module2/
    │   ├── __init__.py
    │   ├── calculator.py
    └── tests/
        ├── test.py                 # Clean imports: `from module2 import calculate` (no sys.path manipulation)
        ├── run_tests.sh            # Test runner that sets PYTHONPATH and runs tests
        ├── setup.sh                # Make python env, install requirements, set PYTHONPATH in venv activation
        ├── README.md               # Absolute minimum possible readme, just one line how to run the test
        ├── requirements.txt
        └── venv/
```

## Import Strategy (Avoid sys.path.insert and pip install -e)

**PYTHONPATH in setup.sh **
- In `setup.sh`: After creating venv, add `export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"` to venv/bin/activate
- Or set it in a test runner script `run_tests.sh`: `PYTHONPATH="$(dirname "$0")/.." python test.py`
- Test files use clean imports: `from module1 import add, sub`
