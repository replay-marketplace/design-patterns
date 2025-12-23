# API Signature

## File Processing Functions

- `save_text_to_file(content: str, directory: str, filename: str) -> bool` - Write text file to specified directory
- `read_file_content(filepath: str) -> str` - Read single file and return its content
- `create_directory_structure(structure: dict) -> bool` - Create nested directories from dictionary structure
- `file_exists(filepath: str) -> bool` - Check if file exists
- `dir_exists(filepath: str) -> bool` - Check if directory exists

## Usage Examples

```python
from file_processing import (
    save_text_to_file,
    read_file_content,
    create_directory_structure,
    file_exists,
    dir_exists
)

# Save text to file
save_text_to_file("Hello World", "/tmp", "test.txt")

# Read file content
content = read_file_content("/tmp/test.txt")

# Create directory structure
structure = {
    "parent": {
        "child1": {},
        "child2": {
            "grandchild": {}
        }
    }
}
create_directory_structure(structure)

# Check existence
if file_exists("/tmp/test.txt"):
    print("File exists")

if dir_exists("/tmp"):
    print("Directory exists")
```
