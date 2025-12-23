# file_processing Package

A Python package for file and directory processing operations.

## Installation

```bash
cd file_processing_pkg
pip install -e .
```

## Usage

```python
from file_processing import (
    save_text_to_file,
    read_file_content,
    create_directory_structure,
    file_exists,
    dir_exists
)

# Write text to a file
save_text_to_file("Hello, World!", "/path/to/dir", "hello.txt")

# Read file content
content = read_file_content("/path/to/file.txt")

# Create nested directories
structure = {
    "parent": {
        "child1": {},
        "child2": {
            "grandchild": {}
        }
    }
}
create_directory_structure(structure)

# Check if file exists
if file_exists("/path/to/file.txt"):
    print("File exists")

# Check if directory exists
if dir_exists("/path/to/directory"):
    print("Directory exists")
```

## Function Signatures

### save_text_to_file(content: str, directory: str, filename: str) -> bool

Write text content to a file in the specified directory.

**Parameters:**
- `content` (str): The text content to write
- `directory` (str): The directory path where the file will be saved
- `filename` (str): The name of the file

**Returns:**
- `bool`: True if successful, False otherwise

### read_file_content(filepath: str) -> str

Read and return the content of a file.

**Parameters:**
- `filepath` (str): The path to the file to read

**Returns:**
- `str`: The content of the file

### create_directory_structure(structure: dict) -> bool

Create nested directories from a dictionary structure.

**Parameters:**
- `structure` (dict): A nested dictionary representing the directory structure

**Returns:**
- `bool`: True if successful, False otherwise

### file_exists(filepath: str) -> bool

Check if a file exists at the given path.

**Parameters:**
- `filepath` (str): The path to check

**Returns:**
- `bool`: True if the file exists, False otherwise

### dir_exists(filepath: str) -> bool

Check if a directory exists at the given path.

**Parameters:**
- `filepath` (str): The path to check

**Returns:**
- `bool`: True if the directory exists, False otherwise

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.
