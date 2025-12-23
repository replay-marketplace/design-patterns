# json_processor Package

A comprehensive Python package for JSON file processing with basic and advanced operations.

## Installation

```bash
cd json_processor_pkg
pip install -e .
```

## Usage

```python
from json_processor import (
    load_json_from_file,
    save_json_to_file,
    dict_to_json_string,
    parse_json_string,
    validate_json_schema,
    load_directory_to_json,
    store_json_to_directory,
    generate_json_schema_from_json
)

# Load JSON from file
data = load_json_from_file('data.json')

# Save JSON to file
save_json_to_file(data, 'output.json')

# Convert dict to JSON string
json_str = dict_to_json_string(data, pretty=True)

# Load entire directory structure to JSON
dir_json = load_directory_to_json('my_directory')

# Store JSON back to directory structure
store_json_to_directory(dir_json, 'output_directory')
```

## Function Signatures

### Basic Functions

#### load_json_from_file(filepath: str) -> dict
Load JSON data from a file.

**Parameters:**
- `filepath` (str): Path to the JSON file

**Returns:**
- dict: Parsed JSON data

#### save_json_to_file(data: dict, filepath: str) -> bool
Save dictionary data to a JSON file.

**Parameters:**
- `data` (dict): Data to save
- `filepath` (str): Output file path

**Returns:**
- bool: True if successful, False otherwise

#### dict_to_json_string(data: dict, pretty: bool = False) -> str
Convert dictionary to JSON string.

**Parameters:**
- `data` (dict): Dictionary to convert
- `pretty` (bool): Whether to format with indentation

**Returns:**
- str: JSON string

#### parse_json_string(json_str: str) -> dict
Parse JSON string to dictionary.

**Parameters:**
- `json_str` (str): JSON string to parse

**Returns:**
- dict: Parsed dictionary

#### load_json_string_from_file(filepath: str) -> str
Load raw JSON string from file.

**Parameters:**
- `filepath` (str): Path to the JSON file

**Returns:**
- str: Raw JSON string

#### save_json_string_to_file(json_str: str, filepath: str) -> bool
Save JSON string directly to file.

**Parameters:**
- `json_str` (str): JSON string to save
- `filepath` (str): Output file path

**Returns:**
- bool: True if successful, False otherwise

#### validate_json_schema(data: dict, schema: dict) -> bool
Validate JSON data against a schema.

**Parameters:**
- `data` (dict): Data to validate
- `schema` (dict): JSON schema

**Returns:**
- bool: True if valid, False otherwise

### Getters / Setters

#### get_json_dir_example() -> dict
Returns an example of the json_dir file structure.

**Returns:**
- dict: Example directory structure in JSON format

#### get_json_dir_schema() -> dict
Returns the schema of the json_dir file.

**Returns:**
- dict: JSON schema for directory structure

#### generate_json_schema_from_json(input_json_file: str) -> bool
Generate and save JSON schema from a JSON file.

**Parameters:**
- `input_json_file` (str): Path to input JSON file

**Returns:**
- bool: True if successful, False otherwise

### Advanced Functions

#### load_directory_to_json(directory: str) -> dict
Recursively load directory structure to JSON format.

**Parameters:**
- `directory` (str): Path to directory

**Returns:**
- dict: Directory structure as JSON

#### store_json_to_directory(data: dict, output_dir: str) -> bool
Store JSON directory structure to actual filesystem.

**Parameters:**
- `data` (dict): JSON directory structure
- `output_dir` (str): Output directory path

**Returns:**
- bool: True if successful, False otherwise

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.
