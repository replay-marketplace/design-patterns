"""Tests for code_gen package."""

import os
import sys
from pathlib import Path


def test_code_gen_basic():
    """Test basic code_gen function without template."""
    print("Testing code_gen (basic, no template)...")
    
    # Check if API key is set
    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("⚠ Skipping code_gen test: DEEPSEEK_API_KEY not set")
        return
    
    try:
        from code_gen import code_gen
        
        prompt = "Create a simple Python hello world function that prints 'Hello, World!'"
        project_name = "test_hello_world"
        
        result_dir = code_gen(prompt=prompt, project_name=project_name)
        
        assert isinstance(result_dir, str)
        assert len(result_dir) > 0
        assert os.path.exists(result_dir), f"Generated directory does not exist: {result_dir}"
        
        # Check that .reports.md exists
        reports_file = Path(result_dir) / ".reports.md"
        assert reports_file.exists(), ".reports.md file not found"
        
        # Check reports content
        reports_content = reports_file.read_text()
        assert "input_prompt_word_count" in reports_content
        assert "output_prompt_word_count" in reports_content
        assert "count_loc" in reports_content
        assert "count_files" in reports_content
        assert "count_python_imports" in reports_content
        assert "count_python_functions" in reports_content
        
        print(f"✓ code_gen test passed")
        print(f"  Generated directory: {result_dir}")
        print(f"  Reports file exists: {reports_file.exists()}")
        
    except Exception as e:
        print(f"✗ code_gen test failed: {e}")
        import traceback
        traceback.print_exc()


def test_code_gen_with_template():
    """Test code_gen function with template."""
    print("\nTesting code_gen (with template)...")
    
    # Check if API key is set
    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("⚠ Skipping code_gen with template test: DEEPSEEK_API_KEY not set")
        return
    
    try:
        from code_gen import code_gen
        
        # Find a template directory (if available)
        current_file = Path(__file__).resolve()
        tool_2_dir = current_file.parent.parent.parent.parent
        template_dir = tool_2_dir / "templates" / "python_pkg_01" / "template"
        
        if not template_dir.exists():
            print(f"⚠ Skipping template test: Template directory not found at {template_dir}")
            return
        
        prompt = "Modify the package to add a new function called 'greet' that takes a name and returns a greeting"
        project_name = "test_with_template"
        
        result_dir = code_gen(
            prompt=prompt,
            project_name=project_name,
            template_dir_path=str(template_dir)
        )
        
        assert isinstance(result_dir, str)
        assert len(result_dir) > 0
        assert os.path.exists(result_dir), f"Generated directory does not exist: {result_dir}"
        
        # Check that .reports.md exists
        reports_file = Path(result_dir) / ".reports.md"
        assert reports_file.exists(), ".reports.md file not found"
        
        print(f"✓ code_gen with template test passed")
        print(f"  Generated directory: {result_dir}")
        
    except Exception as e:
        print(f"✗ code_gen with template test failed: {e}")
        import traceback
        traceback.print_exc()


def test_versioning():
    """Test that versioning works correctly."""
    print("\nTesting versioning...")
    
    # Check if API key is set
    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("⚠ Skipping versioning test: DEEPSEEK_API_KEY not set")
        return
    
    try:
        from code_gen import code_gen
        
        prompt = "Create a simple Python file with a function"
        project_name = "test_versioning"
        
        # Generate first version
        result_dir_1 = code_gen(prompt=prompt, project_name=project_name)
        version_1 = Path(result_dir_1).name
        
        # Generate second version
        result_dir_2 = code_gen(prompt=prompt, project_name=project_name)
        version_2 = Path(result_dir_2).name
        
        # Check that versions are different
        assert version_1 != version_2, "Versions should be different"
        
        # Check that latest_dir.txt exists and is updated
        project_dir = Path(result_dir_1).parent
        latest_dir_file = project_dir / "latest_dir.txt"
        assert latest_dir_file.exists(), "latest_dir.txt should exist"
        
        latest_version = int(latest_dir_file.read_text().strip())
        assert latest_version == int(version_2), f"latest_dir.txt should contain {version_2}, got {latest_version}"
        
        print(f"✓ Versioning test passed")
        print(f"  Version 1: {version_1}")
        print(f"  Version 2: {version_2}")
        print(f"  Latest version in latest_dir.txt: {latest_version}")
        
    except Exception as e:
        print(f"✗ Versioning test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_code_gen_basic()
    test_code_gen_with_template()
    test_versioning()
    print("\nAll tests completed!")
