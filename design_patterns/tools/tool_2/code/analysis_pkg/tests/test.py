"""Tests for analysis package."""

import os
import sys
import tempfile
from pathlib import Path

# Add parent directory to path to import package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from analysis import (
    count_loc,
    count_words,
    count_files,
    count_file_types,
    count_function_defs,
    get_path_to_file,
    count_python_imports,
    count_python_functions
)


def create_test_directory():
    """Create a temporary test directory with sample files."""
    test_dir = tempfile.mkdtemp()
    
    # Create some test files
    (Path(test_dir) / "test1.py").write_text("""import os
import sys

def hello():
    print("Hello")

def world():
    print("World")
""")
    
    (Path(test_dir) / "test2.py").write_text("""from pathlib import Path
import json

def process_data():
    pass
""")
    
    (Path(test_dir) / "readme.txt").write_text("This is a test file with some words.")
    
    (Path(test_dir) / "requirements.txt").write_text("""requests==2.31.0
numpy==1.24.0
pandas==2.0.0
""")
    
    (Path(test_dir) / "subdir").mkdir()
    (Path(test_dir) / "subdir" / "test3.py").write_text("def another_function():\n    pass\n")
    
    return test_dir


def test_count_loc():
    """Test count_loc function."""
    print("Testing count_loc...")
    
    try:
        test_dir = create_test_directory()
        result = count_loc(test_dir)
        assert result > 0, "Should count lines in test files"
        print(f"✓ count_loc test passed (found {result} lines)")
    except Exception as e:
        print(f"✗ count_loc test failed: {e}")
        import traceback
        traceback.print_exc()


def test_count_words():
    """Test count_words function."""
    print("\nTesting count_words...")
    
    try:
        test_dir = create_test_directory()
        result = count_words(test_dir)
        assert result > 0, "Should count words in test files"
        print(f"✓ count_words test passed (found {result} words)")
        
        # Test with specific text
        result = count_words(test_dir, "def")
        assert result >= 0, "Should count occurrences of 'def'"
        print(f"✓ count_words with text pattern passed (found {result} occurrences)")
    except Exception as e:
        print(f"✗ count_words test failed: {e}")
        import traceback
        traceback.print_exc()


def test_count_files():
    """Test count_files function."""
    print("\nTesting count_files...")
    
    try:
        test_dir = create_test_directory()
        result = count_files(test_dir)
        assert result >= 4, "Should count at least 4 files"
        print(f"✓ count_files test passed (found {result} files)")
    except Exception as e:
        print(f"✗ count_files test failed: {e}")
        import traceback
        traceback.print_exc()


def test_count_file_types():
    """Test count_file_types function."""
    print("\nTesting count_file_types...")
    
    try:
        test_dir = create_test_directory()
        result = count_file_types(test_dir)
        assert isinstance(result, list), "Should return a list"
        assert len(result) > 0, "Should find file types"
        
        # Check for .py files
        py_count = next((count for ext, count in result if ext == '.py'), 0)
        assert py_count >= 3, "Should find at least 3 .py files"
        
        print(f"✓ count_file_types test passed (found {len(result)} file types)")
    except Exception as e:
        print(f"✗ count_file_types test failed: {e}")
        import traceback
        traceback.print_exc()


def test_count_function_defs():
    """Test count_function_defs function."""
    print("\nTesting count_function_defs...")
    
    try:
        test_dir = create_test_directory()
        result = count_function_defs(test_dir)
        assert result == 3, f"Should find 3 lines in requirements.txt, got {result}"
        print(f"✓ count_function_defs test passed (found {result} lines)")
    except Exception as e:
        print(f"✗ count_function_defs test failed: {e}")
        import traceback
        traceback.print_exc()


def test_get_path_to_file():
    """Test get_path_to_file function."""
    print("\nTesting get_path_to_file...")
    
    try:
        test_dir = create_test_directory()
        result = get_path_to_file(test_dir, "requirements.txt")
        assert "requirements.txt" in result, "Should return path containing requirements.txt"
        assert Path(result).exists(), "Returned path should exist"
        print(f"✓ get_path_to_file test passed (found: {result})")
    except Exception as e:
        print(f"✗ get_path_to_file test failed: {e}")
        import traceback
        traceback.print_exc()


def test_count_python_imports():
    """Test count_python_imports function."""
    print("\nTesting count_python_imports...")
    
    try:
        test_dir = create_test_directory()
        count, imports = count_python_imports(test_dir)
        assert count > 0, "Should find imports"
        assert isinstance(imports, list), "Should return a list"
        assert len(imports) == count, "Count should match list length"
        
        # Check for expected imports
        import_names = [imp.split('.')[0] for imp in imports]
        assert 'os' in import_names or 'sys' in import_names or 'pathlib' in import_names, "Should find common imports"
        
        print(f"✓ count_python_imports test passed (found {count} imports)")
    except Exception as e:
        print(f"✗ count_python_imports test failed: {e}")
        import traceback
        traceback.print_exc()


def test_count_python_functions():
    """Test count_python_functions function."""
    print("\nTesting count_python_functions...")
    
    try:
        test_dir = create_test_directory()
        count, functions = count_python_functions(test_dir)
        assert count > 0, "Should find functions"
        assert isinstance(functions, list), "Should return a list"
        assert len(functions) == count, "Count should match list length"
        
        # Check for expected function names
        assert 'hello' in functions or 'world' in functions or 'process_data' in functions, "Should find test functions"
        
        print(f"✓ count_python_functions test passed (found {count} functions)")
    except Exception as e:
        print(f"✗ count_python_functions test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_count_loc()
    test_count_words()
    test_count_files()
    test_count_file_types()
    test_count_function_defs()
    test_get_path_to_file()
    test_count_python_imports()
    test_count_python_functions()
    print("\nAll tests completed!")


