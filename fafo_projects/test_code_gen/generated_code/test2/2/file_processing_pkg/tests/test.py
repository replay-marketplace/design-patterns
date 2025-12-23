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
        content = "Hello, World!\nThis is a test file."
        result = save_text_to_file(content, temp_dir, "test.txt")
        assert result == True, "Failed to save file"
        
        # Verify file exists and content is correct
        filepath = os.path.join(temp_dir, "test.txt")
        assert os.path.exists(filepath), "File was not created"
        
        with open(filepath, 'r') as f:
            saved_content = f.read()
        assert saved_content == content, "File content does not match"
        
        # Test with non-existent directory
        result = save_text_to_file(content, "/nonexistent/path", "test.txt")
        assert result == False, "Should return False for invalid directory"
        
        print("  ✓ save_text_to_file tests passed")
    finally:
        # Cleanup
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
        assert read_content == content, "Read content does not match"
        
        # Test with non-existent file
        result = read_file_content("/nonexistent/file.txt")
        assert result == "", "Should return empty string for non-existent file"
        
        print("  ✓ read_file_content tests passed")
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


def test_create_directory_structure():
    """Test create_directory_structure function."""
    print("Testing create_directory_structure...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test creating nested directories
        structure = {
            os.path.join(temp_dir, "dir1"): {
                os.path.join(temp_dir, "dir1", "subdir1"): {},
                os.path.join(temp_dir, "dir1", "subdir2"): {
                    os.path.join(temp_dir, "dir1", "subdir2", "subsubdir"): {}
                }
            },
            os.path.join(temp_dir, "dir2"): {}
        }
        
        result = create_directory_structure(structure)
        assert result == True, "Failed to create directory structure"
        
        # Verify directories were created
        assert os.path.exists(os.path.join(temp_dir, "dir1")), "dir1 not created"
        assert os.path.exists(os.path.join(temp_dir, "dir1", "subdir1")), "subdir1 not created"
        assert os.path.exists(os.path.join(temp_dir, "dir1", "subdir2")), "subdir2 not created"
        assert os.path.exists(os.path.join(temp_dir, "dir1", "subdir2", "subsubdir")), "subsubdir not created"
        assert os.path.exists(os.path.join(temp_dir, "dir2")), "dir2 not created"
        
        # Test with empty structure
        result = create_directory_structure({})
        assert result == True, "Should handle empty structure"
        
        print("  ✓ create_directory_structure tests passed")
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


def test_file_exists():
    """Test file_exists function."""
    print("Testing file_exists...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create a test file
        filepath = os.path.join(temp_dir, "test.txt")
        with open(filepath, 'w') as f:
            f.write("test")
        
        # Test with existing file
        assert file_exists(filepath) == True, "Should return True for existing file"
        
        # Test with non-existent file
        assert file_exists(os.path.join(temp_dir, "nonexistent.txt")) == False, "Should return False for non-existent file"
        
        # Test with directory (should return False)
        assert file_exists(temp_dir) == False, "Should return False for directory"
        
        print("  ✓ file_exists tests passed")
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


def test_dir_exists():
    """Test dir_exists function."""
    print("Testing dir_exists...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test with existing directory
        assert dir_exists(temp_dir) == True, "Should return True for existing directory"
        
        # Test with non-existent directory
        assert dir_exists(os.path.join(temp_dir, "nonexistent")) == False, "Should return False for non-existent directory"
        
        # Create a file and test (should return False)
        filepath = os.path.join(temp_dir, "test.txt")
        with open(filepath, 'w') as f:
            f.write("test")
        assert dir_exists(filepath) == False, "Should return False for file"
        
        print("  ✓ dir_exists tests passed")
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_save_text_to_file()
    test_read_file_content()
    test_create_directory_structure()
    test_file_exists()
    test_dir_exists()
    
    print("\nAll tests passed!")

