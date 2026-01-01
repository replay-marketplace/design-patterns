# API Signature

`from claude_sdk.coder.src.code_generator import code_gen_project`

## Functions

### `code_gen_project(prompt: str, project_name: str) -> str`

Creates a new project in the output_dir with the given project_name, uses Claude SDK to generate code based on the prompt, stores the code there, and returns the path to the project.

**Parameters:**
- `prompt` (str): The prompt describing what code to generate
- `project_name` (str): The name of the project directory to create

**Returns:**
- `str`: The absolute path to the created project directory

**Example:**
```python
from claude_sdk.coder.src.code_generator import code_gen_project

path = code_gen_project(
    prompt="Create a function that calculates fibonacci numbers",
    project_name="fibonacci_project"
)
print(f"Project created at: {path}")
```
