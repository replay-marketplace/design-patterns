"""
Tests for pkg_code_gen package.
"""

import os
import sys
import tempfile
import shutil

# Add package to path
package_path = os.path.join(os.path.dirname(__file__), '..', 'package')
sys.path.insert(0, package_path)

from pkg_code_gen import code_gen


def test_code_gen_basic():
    """Test basic code generation without template."""
    # This test requires OPENAI_API_KEY to be set
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is required but not set")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        code_gen_dir = os.path.join(tmpdir, "code_gen")
        project_name = "test_project"
        
        try:
            result = code_gen(
                prompt="Create a simple Python hello world script",
                code_gen_dir_path=code_gen_dir,
                project_name=project_name
            )
            
            assert os.path.exists(result), f"Generated directory should exist: {result}"
            assert os.path.isdir(result), f"Result should be a directory: {result}"
            
            # Check that next_counter_dir.txt was created
            project_dir = os.path.join(code_gen_dir, project_name)
            counter_file = os.path.join(project_dir, "next_counter_dir.txt")
            assert os.path.exists(counter_file), "next_counter_dir.txt should exist"
            
            print("✓ Basic code generation test passed")
        except Exception as e:
            print(f"✗ Basic code generation test failed: {e}")
            raise


def test_code_gen_with_template():
    """Test code generation with template."""
    # This test requires OPENAI_API_KEY to be set
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is required but not set")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        code_gen_dir = os.path.join(tmpdir, "code_gen")
        project_name = "test_project_template"
        
        # Create a simple template
        template_dir = os.path.join(tmpdir, "template")
        os.makedirs(template_dir, exist_ok=True)
        template_file = os.path.join(template_dir, "main.py")
        with open(template_file, 'w') as f:
            f.write("# Template file\nprint('Hello')\n")
        
        try:
            result = code_gen(
                prompt="Modify the template to print 'Hello World'",
                code_gen_dir_path=code_gen_dir,
                project_name=project_name,
                template_dir_path=template_dir
            )
            
            assert os.path.exists(result), f"Generated directory should exist: {result}"
            assert os.path.isdir(result), f"Result should be a directory: {result}"
            
            print("✓ Code generation with template test passed")
        except Exception as e:
            print(f"✗ Code generation with template test failed: {e}")
            raise


if __name__ == "__main__":
    print("Running pkg_code_gen tests...")
    test_code_gen_basic()
    test_code_gen_with_template()
    print("All tests completed!")

