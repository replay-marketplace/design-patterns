"""
Simple test program that uses pkg_code_gen to generate projects from prompt_list.txt.
"""

import os
import sys
import csv
import ast

# Add the pkg_code_gen package to the path
package_path = os.path.join(
    os.path.dirname(__file__), 
    '..', 
    '..', 
    'design_patterns', 
    'tools', 
    'tool_1', 
    'code', 
    'pkg_code_gen', 
    'package'
)
package_path = os.path.abspath(package_path)
sys.path.insert(0, package_path)

from pkg_code_gen import code_gen

def main():
    code_gen_dir = os.path.join(current_dir, "generated_code")
    result_path = code_gen(
        prompt="hello world in c++",
        code_gen_dir_path=code_gen_dir,
        project_name="test")



'''
def parse_prompt_list(file_path):
    """Parse prompt_list.txt and return list of (project_name, prompt) tuples."""
    projects = []
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return projects
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            
            try:
                # Parse the line which has format: "project_name", "prompt",
                # Remove trailing comma if present
                if line.endswith(','):
                    line = line[:-1]
                
                # Use ast.literal_eval to safely parse the tuple
                # The line should be a tuple of two strings
                parsed = ast.literal_eval(f"({line})")
                if len(parsed) == 2:
                    project_name, prompt = parsed
                    projects.append((project_name, prompt))
                else:
                    print(f"Warning: Line {line_num} has invalid format, skipping: {line}")
            except Exception as e:
                print(f"Warning: Could not parse line {line_num}, skipping: {line}")
                print(f"  Error: {e}")
    
    return projects


def main():
    """Generate projects from prompt_list.txt using pkg_code_gen."""
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is required but not set")
        sys.exit(1)
    
    # Set up paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code_gen_dir = os.path.join(current_dir, "generated_code")
    prompt_list_path = os.path.join(current_dir, "prompt_list.txt")
    
    # Parse prompt list
    print("Reading prompt_list.txt...")
    projects = parse_prompt_list(prompt_list_path)
    
    if not projects:
        print("Error: No valid projects found in prompt_list.txt")
        sys.exit(1)
    
    print(f"Found {len(projects)} projects to generate")
    print(f"Output directory: {code_gen_dir}\n")
    
    # Generate each project
    successful = 0
    failed = 0
    
    for idx, (project_name, prompt) in enumerate(projects, 1):
        print(f"\n[{idx}/{len(projects)}] Generating: {project_name}")
        print(f"  Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
        
        try:
            result_path = code_gen(
                prompt=prompt,
                code_gen_dir_path=code_gen_dir,
                project_name=project_name
            )
            
            print(f"  ✓ Success! Generated at: {result_path}")
            successful += 1
            
        except Exception as e:
            print(f"  ✗ Error generating {project_name}: {e}")
            failed += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Generation complete!")
    print(f"  Successful: {successful}/{len(projects)}")
    print(f"  Failed: {failed}/{len(projects)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

'''