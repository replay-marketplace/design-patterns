# Test Code Generation

A simple test program that uses the `pkg_code_gen` package to generate a hello world program.

## Usage

1. Make sure you have the `OPENAI_API_KEY` environment variable set:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

2. Run the test program:
   ```bash
   python test_hello_world.py
   ```

3. The generated hello world program will be created in the `generated_code/hello_world/` directory.

## Requirements

- Python 3.8+
- OpenAI API key
- The `pkg_code_gen` package (located at `design_patterns/tools/tool_1/code/pkg_code_gen/`)

