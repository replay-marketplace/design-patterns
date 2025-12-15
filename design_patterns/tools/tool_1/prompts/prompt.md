
# Dir Structure

```
code/

├── package_01/                      # uses package_01 functions to make larger functions
│   ├── package  
│   │   ├── code
│   │   │   ├── __init__.py
│   │   │   ├── function_1.py
│   │   │   ├── function_2.py
│   │   │   └── README.md
│   │   ├── setup.py  
│   ├── tests/
│   │   └── test.py 
│   │   └── ci.yml

├── package_02/                      # uses package_02 functions to make larger functions
│   ├── package  
│   │   ├── code
│   │   │   ├── __init__.py
│   │   │   ├── function_1.py
│   │   │   ├── function_2.py
│   │   │   └── README.md
│   │   ├── setup.py  
│   ├── tests/
│   │   └── test.py
│   │   └── ci.yml

├── package_02/                      # uses package_03 functions to make larger functions
│   ├── package  
│   │   ├── code
│   │   │   ├── __init__.py
│   │   │   ├── code_gen.py
│   │   │   └── README.md
│   │   ├── setup.py  
│   ├── tests/
│   │   └── ci.yml
│   │   └── prompts/
│   │   │   └── prompt_01.md
│   │   │   └── prompt_02.md
│   │   │   └── prompt_03.md
│   │   └── templates/
│   │   │   └── template_01/
│   │   │   └── template_02/

├── main.py
├── setup.sh                    # starts python env, installs dependencies 
└── README.md
└── requirements.txt
```





# Functions / Building Blocks


## 1. Agent Chat

#### Basic:
- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_config(prompt, system) -> str` - Control randomness, low temp, no max token
- `chat_agent_code_json(prompt, agent_type)` - Responds only with JSON code; picks system based on agent_type

## 2. String Processing

#### Basic
- `append_string(base: str, addition: str) -> str` - Concatenate strings
- `search_and_delete(text: str, pattern: str) -> str` - Find and remove
- `search_and_replace(text: str, old: str, new: str) -> str` - Find and replace
- `strip_markdown(text: str) -> str` - Remove markdown formatting

#### Analysis
- `count_tokens(text: str) -> int` - Estimate token count



## 3. File Processing

- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file
- `read_file_content(filepath: str) -> str` - Read single file
- `create_directory_structure(structure: dict) -> bool` - Create nested directories
- `file_exists(filepath: str) -> bool` - Check existence
- `dir_exists(filepath: str) -> bool` - Check existence


## 4. JSON Processing

#### Basic:       File / Dict / String  / Helper
- `load_json_from_file(filepath: str) -> dict` - Load JSON from file
- `save_json_to_file(data: dict, filepath: str) -> bool` - Save JSON to file
- `dict_to_json_string(data: dict, pretty: bool) -> str` - Convert dict to JSON string
- `parse_json_string(json_str: str) -> dict` - Parse JSON string to dict
- `load_json_string_from_file(filepath: str) -> str` - Load JSON string from file
- `save_json_string_to_file(json_str: str, filepath: str) -> bool` - Save JSON string to file
- `validate_json_schema(data: dict, schema: dict) -> bool` - Validate structure

#### Getters / Setters
- `get_json_dir_example()` - Returns an example of the json_dir file
- `get_json_dir_schema()` - Returns the schema of the json_dir file
- `generate_json_schema_from_json(input_json_file)` - Saves to the same location

#### Advanced
- `load_directory_to_json(directory: str) -> dict` - Directory to JSON, always recursive
- `store_json_to_directory()`


## 5. Package_03 - Code Gen
1. `code_gen(prompt, template)` - Generates a program
1. `code_gen(prompt)`           - Generates a program







# Code Gen


## 2. String Processing

#### Basic
- `append_string(base: str, addition: str) -> str` - Concatenate strings
- `search_and_delete(text: str, pattern: str) -> str` - Find and remove
- `search_and_replace(text: str, old: str, new: str) -> str` - Find and replace
- `strip_markdown(text: str) -> str` - Remove markdown formatting

#### Analysis
- `count_tokens(text: str) -> int` - Estimate token count


Example dir structure
```
code/
├── pkg_string_processing/                      
│   ├── package  
│   │   ├── code
│   │   │   ├── __init__.py
│   │   │   ├── function_1.py           # Rename to function names
│   │   │   ├── function_2.py           # Rename to function names
│   │   │   └── README.md               # Extreamly simple (install, function signatures)
│   │   ├── setup.py  
│   ├── tests/
│   │   └── test.py 
│   │   └── ci.yml
```