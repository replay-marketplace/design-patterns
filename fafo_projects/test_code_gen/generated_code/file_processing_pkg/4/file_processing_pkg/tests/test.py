"""
Test file for the file_processing package.
"""

import os
import shutil
import tempfile
from file_processing import (
    save_text_to_file,
    read_file_content,
    create_directory_structure,
    file_exists,
    dir_exists
)


def test_save_text_to_file():
    """Test save_text_to_file function."""
    print("Testing save_text_to_file...")
    
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test saving a file
        content = "Hello, World!"
        result = save_text_to_file(content, temp_dir, "test.txt")
        assert result == True, "save_text_to_file should return True"
        
        # Verify file was created
        filepath = os.path.join(temp_dir, "test.txt")
        assert os.path.exists(filepath), "File should exist"
        
        # Verify content
        with open(filepath, 'r') as f:
            saved_content = f.read()
        assert saved_content == content, "Content should match"
        
        print("  ✓ save_text_to_file works correctly")
    finally:
        # Clean up
        shutil.rmtree(temp_dir)


def test_read_file_content():
    """Test read_file_content function."""
    print("Testing read_file_content...")
    
    # Create a temporary file
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create a test file
        content = "Test content\nLine 2\nLine 3"
        filepath = os.path.join(temp_dir, "test.txt")
        with open(filepath, 'w') as f:
            f.write(content)
        
        # Test reading the file
        read_content = read_file_content(filepath)
        assert read_content == content, "Content should match"
        
        # Test reading non-existent file
        try:
            read_file_content(os.path.join(temp_dir, "nonexistent.txt"))
            assert False, "Should raise FileNotFoundError"
        except FileNotFoundError:
            pass
        
        print("  ✓ read_file_content works correctly")
    finally:
        # Clean up
        shutil.rmtree(temp_dir)


def test_create_directory_structure():
    """Test create_directory_structure function."""
    print("Testing create_directory_structure...")
    
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test creating nested directories
        structure = {
            "parent1": {
                "child1": {},
                "child2": {
                    "grandchild1": {}
                }
            },
            "parent2": {}
        }
        
        result = create_directory_structure(structure, temp_dir)
        assert result == True, "create_directory_structure should return True"
        
        # Verify directories were created
        assert os.path.isdir(os.path.join(temp_dir, "parent1")), "parent1 should exist"
        assert os.path.isdir(os.path.join(temp_dir, "parent1", "child1")), "child1 should exist"
        assert os.path.isdir(os.path.join(temp_dir, "parent1", "child2")), "child2 should exist"
        assert os.path.isdir(os.path.join(temp_dir, "parent1", "child2", "grandchild1")), "grandchild1 should exist"
        assert os.path.isdir(os.path.join(temp_dir, "parent2")), "parent2 should exist"
        
        print("  ✓ create_directory_structure works correctly")
    finally:
        # Clean up
        shutil.rmtree(temp_dir)


def test_file_exists():
    """Test file_exists function."""
    print("Testing file_exists...")
    
    # Create a temporary directory and file
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create a test file
        filepath = os.path.join(temp_dir, "test.txt")
        with open(filepath, 'w') as f:
            f.write("test")
        
        # Test existing file
        assert file_exists(filepath) == True, "file_exists should return True for existing file"
        
        # Test non-existent file
        assert file_exists(os.path.join(temp_dir, "nonexistent.txt")) == False, "file_exists should return False for non-existent file"
        
        # Test directory (should return False)
        assert file_exists(temp_dir) == False, "file_exists should return False for directory"
        
        print("  ✓ file_exists works correctly")
    finally:
        # Clean up
        shutil.rmtree(temp_dir)


def test_dir_exists():
    """Test dir_exists function."""
    print("Testing dir_exists...")
    
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test existing directory
        assert dir_exists(temp_dir) == True, "dir_exists should return True for existing directory"
        
        # Test non-existent directory
        assert dir_exists(os.path.join(temp_dir, "nonexistent")) == False, "dir_exists should return False for non-existent directory"
        
        # Create a file and test (should return False)
        filepath = os.path.join(temp_dir, "test.txt")
        with open(filepath, 'w') as f:
            f.write("test")
        assert dir_exists(filepath) == False, "dir_exists should return False for file"
        
        print("  ✓ dir_exists works correctly")
    finally:
        # Clean up
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_save_text_to_file()
    test_read_file_content()
    test_create_directory_structure()
    test_file_exists()
    test_dir_exists()
    
    print("\nAll tests passed!")
