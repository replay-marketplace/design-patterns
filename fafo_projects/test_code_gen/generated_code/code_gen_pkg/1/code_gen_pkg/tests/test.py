"""
Test file for the code_gen package.
"""

import os
import shutil
import tempfile
from pathlib import Path
from code_gen import code_gen


def test_code_gen_basic():
    """Test basic code generation without template."""
    print("Testing basic code generation...")
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        result_path = code_gen(
            prompt="Create a simple hello world package",
            code_gen_dir_path=temp_dir,
            project_name="test_project"
        )
        
        # Check that the version directory was created
        assert os.path.exists(result_path), f"Result path does not exist: {result_path}"
        assert "v1" in result_path, "First version should be v1"
        
        # Check that prompt file was saved
        prompt_file = Path(result_path) / "_generation_prompt.txt"
        assert prompt_file.exists(), "Prompt file should be saved"
        
        print(f"✓ Basic code generation test passed. Generated at: {result_path}")


def test_code_gen_with_template():
    """Test code generation with template directory."""
    print("Testing code generation with template...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a simple template directory
        template_dir = Path(temp_dir) / "template"
        template_dir.mkdir()
        (template_dir / "README.md").write_text("# Template README")
        
        code_gen_dir = Path(temp_dir) / "code_gen"
        
        result_path = code_gen(
            prompt="Create a calculator package",
            code_gen_dir_path=str(code_gen_dir),
            project_name="calculator",
            template_dir_path=str(template_dir)
        )
        
        assert os.path.exists(result_path), f"Result path does not exist: {result_path}"
        print(f"✓ Template-based code generation test passed. Generated at: {result_path}")


def test_version_increment():
    """Test that version numbers increment correctly."""
    print("Testing version increment...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate first version
        result1 = code_gen(
            prompt="Version 1",
            code_gen_dir_path=temp_dir,
            project_name="versioned_project"
        )
        
        # Generate second version
        result2 = code_gen(
            prompt="Version 2",
            code_gen_dir_path=temp_dir,
            project_name="versioned_project"
        )
        
        assert "v1" in result1, "First version should be v1"
        assert "v2" in result2, "Second version should be v2"
        assert result1 != result2, "Version paths should be different"
        
        # Check counter file exists
        counter_file = Path(temp_dir) / "versioned_project" / "next_counter_dir.txt"
        assert counter_file.exists(), "Counter file should exist"
        
        print(f"✓ Version increment test passed. v1: {result1}, v2: {result2}")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_code_gen_basic()
    test_code_gen_with_template()
    test_version_increment()
    
    print("\nAll tests passed!")
