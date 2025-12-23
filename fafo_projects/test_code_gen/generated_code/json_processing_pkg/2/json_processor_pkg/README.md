# json_processor Package

A comprehensive Python package for JSON file processing, including basic operations, schema validation, and advanced directory-to-JSON conversion.

## Installation

```bash
cd json_processor_pkg
pip install -e .
```

For schema validation support, install with:

```bash
pip install -e .
pip install jsonschema
```

## Usage

```python
from json_processor import (
    load_json_from_file,
    save_json_to_file,
    dict_to_json_string,
    parse_json_string,
    load_json_string_from_file,
    save_json_string_to_file,
    validate_json_schema,
    get_json_dir_example,
    get_json_dir_schema,
    generate_json_schema_from_json,
    load_directory_to_json,
    store_json_to_directory
)

# Basic operations
data = load_json_from_file("data.json")
save_json_to_file(data, "output.json")

# String operations
json_str = dict_to_json_string(data, pretty=True)
parsed = parse_json_string(json_str)

# Schema validation
schema = get_json_dir_schema()
is_valid = validate_json_schema(data, schema)

# Directory operations
json_structure = load_directory_to_json("/path/to/directory")
store_json_to_directory(json_structure, "/output/path")

# Schema generation
schema_file = generate_json_schema_from_json("data.json")
```

## Function Signatures

### Basic Operations

#### `load_json_from_file(filepath: str) -> dict`

Load JSON data from a file.

**Parameters:**
- `filepath` (str): Path to the JSON file

**Returns:**
- `dict`: Parsed JSON data as a dictionary

**Raises:**
- `FileNotFoundError`: If the file does not exist
- `json.JSONDecodeError`: If the file contains invalid JSON

---

#### `save_json_to_file(data: dict, filepath: str) -> bool`

Save dictionary data to a JSON file.

**Parameters:**
- `data` (dict): Dictionary to save as JSON
- `filepath` (str): Path where the JSON file will be saved

**Returns:**
- `bool`: True if successful, False otherwise

---

#### `dict_to_json_string(data: dict, pretty: bool = False) -> str`

Convert a dictionary to a JSON string.

**Parameters:**
- `data` (dict): Dictionary to convert
- `pretty` (bool): If True, format with indentation for readability

**Returns:**
- `str`: JSON string representation of the dictionary

---

#### `parse_json_string(json_str: str) -> dict`

Parse a JSON string to a dictionary.

**Parameters:**
- `json_str` (str): JSON string to parse

**Returns:**
- `dict`: Parsed dictionary

**Raises:**
- `json.JSONDecodeError`: If the string is not valid JSON

---

#### `load_json_string_from_file(filepath: str) -> str`

Load JSON content from a file as a string (without parsing).

**Parameters:**
- `filepath` (str): Path to the JSON file

**Returns:**
- `str`: Raw JSON string content

**Raises:**
- `FileNotFoundError`: If the file does not exist

---

#### `save_json_string_to_file(json_str: str, filepath: str) -> bool`

Save a JSON string directly to a file.

**Parameters:**
- `json_str` (str): JSON string to save
- `filepath` (str): Path where the file will be saved

**Returns:**
- `bool`: True if successful, False otherwise

---

#### `validate_json_schema(data: dict, schema: dict) -> bool`

Validate JSON data against a JSON schema.

**Parameters:**
- `data` (dict): JSON data to validate
- `schema` (dict): JSON schema to validate against

**Returns:**
- `bool`: True if valid, False otherwise

**Note:** Requires jsonschema package to be installed.

---

### Helper Functions

#### `get_json_dir_example() -> dict`

Returns an example of a JSON directory structure.

**Returns:**
- `dict`: Example JSON directory structure

---

#### `get_json_dir_schema() -> dict`

Returns the JSON schema for directory structures.

**Returns:**
- `dict`: JSON schema for validating directory structures

---

#### `generate_json_schema_from_json(input_json_file: str) -> str`

Generate a JSON schema from a JSON file and save it to the same location.

**Parameters:**
- `input_json_file` (str): Path to the input JSON file

**Returns:**
- `str`: Path to the generated schema file

**Raises:**
- `FileNotFoundError`: If the input file does not exist

---

### Advanced Operations

#### `load_directory_to_json(directory: str) -> dict`

Convert a directory structure to JSON format (always recursive).

**Parameters:**
- `directory` (str): Path to the directory to convert

**Returns:**
- `dict`: JSON representation of the directory structure with the following format:
  ```json
  {
    "type": "directory",
    "name": "directory_name",
    "children": [
      {
        "type": "file",
        "name": "filename.txt",
        "content": "file content"
      },
      {
        "type": "directory",
        "name": "subdirectory",
        "children": [...]
      }
    ]
  }
  ```

**Raises:**
- `FileNotFoundError`: If the directory does not exist
- `NotADirectoryError`: If the path is not a directory

---

#### `store_json_to_directory(json_structure: dict, output_path: str) -> bool`

Create a directory structure from a JSON representation.

**Parameters:**
- `json_structure` (dict): JSON structure to convert to directories/files
- `output_path` (str): Base path where the structure will be created

**Returns:**
- `bool`: True if successful, False otherwise

---

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

## Features

- **Basic JSON Operations**: Load, save, parse, and convert JSON data
- **String Operations**: Work with JSON as strings without parsing
- **Schema Validation**: Validate JSON against schemas (requires jsonschema)
- **Schema Generation**: Automatically generate schemas from JSON files
- **Directory Conversion**: Convert entire directory structures to/from JSON
- **Recursive Processing**: All directory operations are fully recursive
- **Error Handling**: Comprehensive error handling and informative messages
- **UTF-8 Support**: Full Unicode support for international characters

## License

MIT License
