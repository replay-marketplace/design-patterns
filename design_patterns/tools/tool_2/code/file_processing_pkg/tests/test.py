"""Tests for file_processing package."""

import os
import sys
import tempfile
import shutil

# Add parent directory to path to import package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

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
    
    try:
        # Create temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:
            # Test basic save
            result = save_text_to_file("Hello World", tmpdir, "test.txt")
            assert result is True
            
            # Verify file was created
            filepath = os.path.join(tmpdir, "test.txt")
            assert file_exists(filepath)
            
            # Verify content
            content = read_file_content(filepath)
            assert content == "Hello World"
            
            print("✓ save_text_to_file test passed")
            
            # Test with nested directory
            nested_dir = os.path.join(tmpdir, "nested", "subdir")
            result = save_text_to_file("Nested content", nested_dir, "nested.txt")
            assert result is True
            assert file_exists(os.path.join(nested_dir, "nested.txt"))
            
            print("✓ save_text_to_file nested directory test passed")
    except Exception as e:
        print(f"✗ save_text_to_file test failed: {e}")
        raise


def test_read_file_content():
    """Test read_file_content function."""
    print("\nTesting read_file_content...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test file
            filepath = os.path.join(tmpdir, "read_test.txt")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("Test content\nLine 2")
            
            # Read file
            content = read_file_content(filepath)
            assert "Test content" in content
            assert "Line 2" in content
            
            print("✓ read_file_content test passed")
            
            # Test FileNotFoundError
            try:
                read_file_content(os.path.join(tmpdir, "nonexistent.txt"))
                assert False, "Should have raised FileNotFoundError"
            except FileNotFoundError:
                print("✓ read_file_content FileNotFoundError test passed")
    except Exception as e:
        print(f"✗ read_file_content test failed: {e}")
        raise


def test_create_directory_structure():
    """Test create_directory_structure function."""
    print("\nTesting create_directory_structure...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = os.path.join(tmpdir, "test_structure")
            
            structure = {
                base_dir: {
                    "subdir1": {},
                    "subdir2": {
                        "nested": {}
                    },
                    "subdir3": {}
                }
            }
            
            result = create_directory_structure(structure)
            assert result is True
            
            # Verify directories exist
            assert dir_exists(base_dir)
            assert dir_exists(os.path.join(base_dir, "subdir1"))
            assert dir_exists(os.path.join(base_dir, "subdir2"))
            assert dir_exists(os.path.join(base_dir, "subdir2", "nested"))
            assert dir_exists(os.path.join(base_dir, "subdir3"))
            
            print("✓ create_directory_structure test passed")
    except Exception as e:
        print(f"✗ create_directory_structure test failed: {e}")
        raise


def test_file_exists():
    """Test file_exists function."""
    print("\nTesting file_exists...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Test existing file
            filepath = os.path.join(tmpdir, "test_file.txt")
            with open(filepath, 'w') as f:
                f.write("test")
            
            assert file_exists(filepath) is True
            print("✓ file_exists (existing file) test passed")
            
            # Test non-existing file
            assert file_exists(os.path.join(tmpdir, "nonexistent.txt")) is False
            print("✓ file_exists (non-existing file) test passed")
            
            # Test directory (should return False)
            assert file_exists(tmpdir) is False
            print("✓ file_exists (directory) test passed")
    except Exception as e:
        print(f"✗ file_exists test failed: {e}")
        raise


def test_dir_exists():
    """Test dir_exists function."""
    print("\nTesting dir_exists...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Test existing directory
            assert dir_exists(tmpdir) is True
            print("✓ dir_exists (existing directory) test passed")
            
            # Test non-existing directory
            assert dir_exists(os.path.join(tmpdir, "nonexistent")) is False
            print("✓ dir_exists (non-existing directory) test passed")
            
            # Test file (should return False)
            filepath = os.path.join(tmpdir, "test_file.txt")
            with open(filepath, 'w') as f:
                f.write("test")
            assert dir_exists(filepath) is False
            print("✓ dir_exists (file) test passed")
    except Exception as e:
        print(f"✗ dir_exists test failed: {e}")
        raise


if __name__ == "__main__":
    test_save_text_to_file()
    test_read_file_content()
    test_create_directory_structure()
    test_file_exists()
    test_dir_exists()
    print("\nAll tests completed!")


