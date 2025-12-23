# file_processing Package

A Python package for common file processing operations including reading, writing, and managing files and directories.

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
    "/path/to/dir1": {
        "/path/to/dir1/subdir1": {},
        "/path/to/dir1/subdir2": {}
    }
}
create_directory_structure(structure)

# Check if file exists
if file_exists("/path/to/file.txt"):
    print("File exists!")

# Check if directory exists
if dir_exists("/path/to/directory"):
    print("Directory exists!")
```

## Function Signatures

### save_text_to_file(content: str, directory: str, filename: str) -> bool

Write text content to a file in the specified directory.

**Parameters:**
- `content` (str): The text content to write to the file
- `directory` (str): The directory path where the file should be saved
- `filename` (str): The name of the file to create

**Returns:**
- `bool`: True if the file was successfully written, False otherwise

### read_file_content(filepath: str) -> str

Read and return the content of a single file.

**Parameters:**
- `filepath` (str): The path to the file to read

**Returns:**
- `str`: The content of the file, or an empty string if the file cannot be read

### create_directory_structure(structure: dict) -> bool

Create nested directories based on a dictionary structure.

**Parameters:**
- `structure` (dict): A dictionary representing the directory structure to create. Keys are directory paths, values are nested dictionaries for subdirectories.

**Returns:**
- `bool`: True if all directories were successfully created, False otherwise

**Example structure:**
```python
{
    "/path/to/dir1": {
        "/path/to/dir1/subdir1": {},
        "/path/to/dir1/subdir2": {
            "/path/to/dir1/subdir2/subsubdir": {}
        }
    },
    "/path/to/dir2": {}
}
```

### file_exists(filepath: str) -> bool

Check if a file exists at the specified path.

**Parameters:**
- `filepath` (str): The path to the file to check

**Returns:**
- `bool`: True if the file exists and is a file (not a directory), False otherwise

### dir_exists(filepath: str) -> bool

Check if a directory exists at the specified path.

**Parameters:**
- `filepath` (str): The path to the directory to check

**Returns:**
- `bool`: True if the directory exists and is a directory (not a file), False otherwise

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

