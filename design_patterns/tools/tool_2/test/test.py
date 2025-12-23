"""
Simple test script to test the code_gen function.

Use the code_gen function to generate code from design_patterns/tools/tool_2/code/code_gen_pkg/code_gen/README_API_SIGNATURE.md

- `code_gen(prompt: str, project_name: str) -> str` - Code generation, returns the dir with the code
- `code_gen(prompt: str, project_name: str, template_dir_path: str) -> str` - Code generation, uses the dir and the code in it as the initial starting point.
"""

import os
import sys
from pathlib import Path

# Add the code_gen_pkg to the path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
code_gen_pkg_path = project_root / "design_patterns" / "tools" / "tool_2" / "code" / "code_gen_pkg"
sys.path.insert(0, str(code_gen_pkg_path))

from code_gen.code_gen import code_gen


def main():
    """Test the code_gen function with a simple hello world prompt."""
    print("Testing code_gen function...")
    print("=" * 50)
    
    # Simple hello world prompt
    prompt = "Create a simple Python hello world function that prints 'Hello, World!'"
    project_name = "hello_world"
    
    print(f"Prompt: {prompt}")
    print(f"Project name: {project_name}")
    print()

    # Set up paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code_gen_dir = os.path.join(current_dir, "generated_code")
    template_dir = os.path.join(current_dir, "../test_code_gen/templates/python_pkg_01/template")
    
    
    try:
        # Call code_gen without template
        result_path = code_gen(
            prompt=prompt,
            project_name=project_name,
            template_dir_path=template_dir
        )
        
        print(f"✓ Code generation successful!")
        print(f"Generated code directory: {result_path}")
        print()
        
        # Verify the directory exists
        if os.path.exists(result_path):
            print(f"✓ Generated directory exists: {result_path}")
            
            # List some files in the directory
            files = list(Path(result_path).rglob("*.py"))
            if files:
                print(f"✓ Found {len(files)} Python file(s):")
                for f in files[:5]:  # Show first 5 files
                    print(f"  - {f.relative_to(result_path)}")
        else:
            print(f"✗ Generated directory does not exist: {result_path}")
            
    except Exception as e:
        print(f"✗ Error during code generation: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    print()
    print("=" * 50)
    print("Test completed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
