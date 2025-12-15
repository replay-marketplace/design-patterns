"""
Tests for pkg_file_processing package.
"""

import sys
import os
import tempfile
import shutil

# Add the package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'package'))

from code.save_text_to_file import save_text_to_file
from code.read_file_content import read_file_content
from code.create_directory_structure import create_directory_structure
from code.file_exists import file_exists
from code.dir_exists import dir_exists


def test_save_text_to_file():
    """Test save_text_to_file function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Test basic save
        assert save_text_to_file("Hello World", tmpdir, "test.txt") == True
        assert file_exists(os.path.join(tmpdir, "test.txt")) == True
        
        # Test with nested directory
        nested_dir = os.path.join(tmpdir, "nested")
        assert save_text_to_file("Test content", nested_dir, "nested.txt") == True
        assert file_exists(os.path.join(nested_dir, "nested.txt")) == True
        
        # Verify content
        content = read_file_content(os.path.join(tmpdir, "test.txt"))
        assert content == "Hello World"
    
    print("✓ save_text_to_file tests passed")


def test_read_file_content():
    """Test read_file_content function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file = os.path.join(tmpdir, "read_test.txt")
        with open(test_file, 'w') as f:
            f.write("Test content\nLine 2")
        
        # Test reading
        content = read_file_content(test_file)
        assert "Test content" in content
        assert "Line 2" in content
        
        # Test non-existent file
        content = read_file_content(os.path.join(tmpdir, "nonexistent.txt"))
        assert content == ""
    
    print("✓ read_file_content tests passed")


def test_create_directory_structure():
    """Test create_directory_structure function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        
        structure = {
            "parent": {
                "child1": None,
                "child2": ["file1.txt", "file2.txt"],
                "child3": {
                    "grandchild": None
                }
            }
        }
        
        assert create_directory_structure(structure) == True
        
        # Verify directories exist
        assert dir_exists("parent") == True
        assert dir_exists("parent/child1") == True
        assert dir_exists("parent/child2") == True
        assert dir_exists("parent/child3") == True
        assert dir_exists("parent/child3/grandchild") == True
        
        # Verify files exist
        assert file_exists("parent/child2/file1.txt") == True
        assert file_exists("parent/child2/file2.txt") == True
    
    print("✓ create_directory_structure tests passed")


def test_file_exists():
    """Test file_exists function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file = os.path.join(tmpdir, "exists_test.txt")
        with open(test_file, 'w') as f:
            f.write("test")
        
        assert file_exists(test_file) == True
        assert file_exists(os.path.join(tmpdir, "nonexistent.txt")) == False
        assert file_exists(tmpdir) == False  # Directory, not file
    
    print("✓ file_exists tests passed")


def test_dir_exists():
    """Test dir_exists function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        assert dir_exists(tmpdir) == True
        assert dir_exists(os.path.join(tmpdir, "nonexistent")) == False
        
        # Create a test file
        test_file = os.path.join(tmpdir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("test")
        
        assert dir_exists(test_file) == False  # File, not directory
    
    print("✓ dir_exists tests passed")


if __name__ == "__main__":
    print("Running tests for pkg_file_processing...\n")
    test_save_text_to_file()
    test_read_file_content()
    test_create_directory_structure()
    test_file_exists()
    test_dir_exists()
    print("\nAll tests passed! ✓")

