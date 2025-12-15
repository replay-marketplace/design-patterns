
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
1. `code_gen(prompt: str, project_name: str)`           - Code generation
1. `code_gen(prompt: str, project_name: str, template_dir_path: str)` - Code generation, uses the dir and the code in it as the initial starting point. 

### Description
User provides the prompt, and it uses the chat_agent_code_json() to generate code. 
It stores all projects into a dir called code_gen, in a dir based on project_name. 
When creating a new project dir, always initialize the next_counter_dir.txt so that you can increment it and generate multiple versions under the same project name. 

code_gen/
├── website/                     # project folder
│   ├── next_counter_dir.txt     # keeps track of the current count of dir names, and provides the agent with the next name of the folder within this project. This gets created everytime a new project folder is created.
│   ├── 1/
│   ├── 2/                       # the latest generated project code. 
├── app/                         # project folder
│   ├── next_counter_dir.txt  
│   ├── 1/
│   ├── 2/




# Hiarchy of Packages

## Level 2 - bottom
Code Gen

## Level 1 - bottom
1. JSON processing

## Level 0 - bottom
1. string processing    design_patterns/tools/tool_1/code/pkg_string_processing/README.md
2. file processing      design_patterns/tools/tool_1/code/pkg_file_processing/README.md
3. agent chat           design_patterns/tools/tool_1/code/pkg_agent_chat/README.md




# Code Gen



## 2. String Processing

#### Basic
- `append_string(base: str, addition: str) -> str` - Concatenate strings
- `search_and_delete(text: str, pattern: str) -> str` - Find and remove
- `search_and_replace(text: str, old: str, new: str) -> str` - Find and replace
- `strip_markdown(text: str) -> str` - Remove markdown formatting

#### Analysis
- `count_tokens(text: str) -> int` - Estimate token count





## 1. Agent Chat

#### Basic:
- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_config(prompt, system) -> str` - Control randomness, low temp, no max token
- `chat_agent_code_json(prompt, agent_type)` - Responds only with JSON code; picks system based on agent_type




## 3. File Processing

- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file
- `read_file_content(filepath: str) -> str` - Read single file
- `create_directory_structure(structure: dict) -> bool` - Create nested directories
- `file_exists(filepath: str) -> bool` - Check existence
- `dir_exists(filepath: str) -> bool` - Check existence






# ---------------------------------



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


# ---------------------------------


## 5. Package_03 - Code Gen
1. `code_gen(prompt: str, code_gen_dir_path: str, project_name: str)`           - Code generation
1. `code_gen(prompt: str, code_gen_dir_path: str, project_name: str, template_dir_path: str)` - Code generation, uses the template_dir_path and the code in it as the initial starting point for the code, by sending this code to the agent via JSON within the prompt.  

### Description
User provides the prompt, and it uses the chat_agent_code_json() to generate code. 
It stores all projects into a dir called code_gen, in a dir based on project_name. 
When creating a new project dir, always initialize the next_counter_dir.txt so that you can increment it and generate multiple versions under the same project name. 

Example dir structure for code_gen:
```
code_gen/
├── website/                     # project folder
│   ├── next_counter_dir.txt     # keeps track of the current count of dir names, and provides the agent with the next name of the folder within this project. This gets created everytime a new project folder is created.
│   ├── 1/
│   ├── 2/                       # the latest generated project code. 
├── app/                         # project folder
│   ├── next_counter_dir.txt  
│   ├── 1/
│   ├── 2/



Use these available python packages:
1. String Processing: design_patterns/tools/tool_1/code/pkg_string_processing/README.md
2. File Processing:   design_patterns/tools/tool_1/code/pkg_file_processing/README.md
3. Agent Chat:   design_patterns/tools/tool_1/code/pkg_agent_chat/README.md
4. JSON Processing:   design_patterns/tools/tool_1/code/pkg_json_processing/README.md


Example dir structure
```
code/
├── pkg_code_gen/                      
│   ├── package  
│   │   ├── pkg_code_gen                # Package name
│   │   │   ├── __init__.py
│   │   │   ├── function_1.py           # Rename to function names
│   │   │   ├── function_2.py           # Rename to function names
│   │   ├── setup.py  
│   ├── tests/
│   │   └── test.py 
│   └── README.md               # Extreamly simple (install, function signatures)
```

Also make .github/workflows/pkg_code_gen.yml, the name of the workflow should be same as file name. 

