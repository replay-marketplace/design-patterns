# code_gen Package

A Python package for AI-powered code generation with version management.

## Installation

```bash
cd code_gen_pkg
pip install -e .
```

## Usage

```python
from code_gen import code_gen

# Basic code generation
result_path = code_gen(
    prompt="Create a simple calculator package with add and subtract functions",
    code_gen_dir_path="./generated_code",
    project_name="calculator"
)

print(f"Code generated at: {result_path}")

# Code generation with template
result_path = code_gen(
    prompt="Create a data processing package",
    code_gen_dir_path="./generated_code",
    project_name="data_processor",
    template_dir_path="./my_template"
)
```

## Function Signatures

### code_gen(prompt, code_gen_dir_path, project_name, template_dir_path=None)

Generate code using an AI agent and save to the filesystem with automatic version management.

**Parameters:**
- `prompt` (str): The code generation prompt describing what to generate
- `code_gen_dir_path` (str): Base directory where all generated code projects will be stored
- `project_name` (str): Name of the project (creates a subdirectory)
- `template_dir_path` (str, optional): Path to a template directory to use as starting point

**Returns:**
- `str`: Path to the generated project version directory (e.g., "./code_gen/my_project/v1")

**Features:**
- Automatic version management (v1, v2, v3, etc.)
- Stores generation prompt for reference
- Optional template-based generation
- Creates directory structure from JSON

## Directory Structure

Generated projects are organized as follows:

```
code_gen_dir_path/
└── project_name/
    ├── next_counter_dir.txt  # Tracks next version number
    ├── v1/
    │   ├── _generation_prompt.txt
    │   └── [generated files]
    ├── v2/
    │   ├── _generation_prompt.txt
    │   └── [generated files]
    └── ...
```

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

## Notes

- The `chat_agent_code_json()` function is a placeholder that should be replaced with actual AI agent integration
- Each project maintains its own version counter
- Templates are read as JSON directory structures and included in the AI prompt
- All generated code is saved with the original prompt for reproducibility
