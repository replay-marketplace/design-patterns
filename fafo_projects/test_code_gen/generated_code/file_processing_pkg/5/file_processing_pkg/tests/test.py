"""Test file for file_processing package."""

import os
import tempfile
import shutil
from pathlib import Path
import pytest

from file_processing import (
    save_text_to_file,
    read_file_content,
    create_directory_structure,
    file_exists,
    dir_exists,
)


class TestSaveTextToFile:
    """Tests for save_text_to_file function."""
    
    def test_save_text_to_file_success(self, tmp_path):
        """Test successfully saving text to a file."""
        content = "Hello, World!"
        filename = "test.txt"
        
        result = save_text_to_file(content, str(tmp_path), filename)
        
        assert result is True
        file_path = tmp_path / filename
        assert file_path.exists()
        assert file_path.read_text() == content
    
    def test_save_text_to_file_creates_directory(self, tmp_path):
        """Test that save_text_to_file creates directory if it doesn't exist."""
        new_dir = tmp_path / "new_directory"
        content = "Test content"
        filename = "test.txt"
        
        result = save_text_to_file(content, str(new_dir), filename)
        
        assert result is True
        assert new_dir.exists()
        assert (new_dir / filename).exists()
    
    def test_save_text_to_file_overwrites_existing(self, tmp_path):
        """Test that save_text_to_file overwrites existing files."""
        filename = "test.txt"
        file_path = tmp_path / filename
        file_path.write_text("Old content")
        
        new_content = "New content"
        result = save_text_to_file(new_content, str(tmp_path), filename)
        
        assert result is True
        assert file_path.read_text() == new_content


class TestReadFileContent:
    """Tests for read_file_content function."""
    
    def test_read_file_content_success(self, tmp_path):
        """Test successfully reading file content."""
        content = "Test content\nLine 2"
        file_path = tmp_path / "test.txt"
        file_path.write_text(content)
        
        result = read_file_content(str(file_path))
        
        assert result == content
    
    def test_read_file_content_empty_file(self, tmp_path):
        """Test reading an empty file."""
        file_path = tmp_path / "empty.txt"
        file_path.write_text("")
        
        result = read_file_content(str(file_path))
        
        assert result == ""
    
    def test_read_file_content_nonexistent_file(self, tmp_path):
        """Test reading a nonexistent file raises FileNotFoundError."""
        file_path = tmp_path / "nonexistent.txt"
        
        with pytest.raises(FileNotFoundError):
            read_file_content(str(file_path))
    
    def test_read_file_content_directory_path(self, tmp_path):
        """Test reading a directory path raises IOError."""
        with pytest.raises(IOError):
            read_file_content(str(tmp_path))


class TestCreateDirectoryStructure:
    """Tests for create_directory_structure function."""
    
    def test_create_simple_structure(self, tmp_path):
        """Test creating a simple directory structure."""
        structure = {
            "dir1": {},
            "dir2": {}
        }
        
        result = create_directory_structure(structure, str(tmp_path))
        
        assert result is True
        assert (tmp_path / "dir1").is_dir()
        assert (tmp_path / "dir2").is_dir()
    
    def test_create_nested_structure(self, tmp_path):
        """Test creating a nested directory structure."""
        structure = {
            "parent": {
                "child1": {},
                "child2": {
                    "grandchild": {}
                }
            }
        }
        
        result = create_directory_structure(structure, str(tmp_path))
        
        assert result is True
        assert (tmp_path / "parent").is_dir()
        assert (tmp_path / "parent" / "child1").is_dir()
        assert (tmp_path / "parent" / "child2").is_dir()
        assert (tmp_path / "parent" / "child2" / "grandchild").is_dir()
    
    def test_create_empty_structure(self, tmp_path):
        """Test creating an empty structure."""
        structure = {}
        
        result = create_directory_structure(structure, str(tmp_path))
        
        assert result is True
    
    def test_create_structure_existing_dirs(self, tmp_path):
        """Test creating structure with existing directories."""
        existing_dir = tmp_path / "existing"
        existing_dir.mkdir()
        
        structure = {
            "existing": {
                "new_child": {}
            }
        }
        
        result = create_directory_structure(structure, str(tmp_path))
        
        assert result is True
        assert (tmp_path / "existing" / "new_child").is_dir()


class TestFileExists:
    """Tests for file_exists function."""
    
    def test_file_exists_true(self, tmp_path):
        """Test file_exists returns True for existing file."""
        file_path = tmp_path / "test.txt"
        file_path.write_text("content")
        
        result = file_exists(str(file_path))
        
        assert result is True
    
    def test_file_exists_false_nonexistent(self, tmp_path):
        """Test file_exists returns False for nonexistent file."""
        file_path = tmp_path / "nonexistent.txt"
        
        result = file_exists(str(file_path))
        
        assert result is False
    
    def test_file_exists_false_for_directory(self, tmp_path):
        """Test file_exists returns False for directory."""
        result = file_exists(str(tmp_path))
        
        assert result is False
    
    def test_file_exists_invalid_path(self):
        """Test file_exists handles invalid paths gracefully."""
        result = file_exists("\0invalid")
        
        assert result is False


class TestDirExists:
    """Tests for dir_exists function."""
    
    def test_dir_exists_true(self, tmp_path):
        """Test dir_exists returns True for existing directory."""
        result = dir_exists(str(tmp_path))
        
        assert result is True
    
    def test_dir_exists_false_nonexistent(self, tmp_path):
        """Test dir_exists returns False for nonexistent directory."""
        dir_path = tmp_path / "nonexistent"
        
        result = dir_exists(str(dir_path))
        
        assert result is False
    
    def test_dir_exists_false_for_file(self, tmp_path):
        """Test dir_exists returns False for file."""
        file_path = tmp_path / "test.txt"
        file_path.write_text("content")
        
        result = dir_exists(str(file_path))
        
        assert result is False
    
    def test_dir_exists_nested_directory(self, tmp_path):
        """Test dir_exists works with nested directories."""
        nested_dir = tmp_path / "parent" / "child"
        nested_dir.mkdir(parents=True)
        
        result = dir_exists(str(nested_dir))
        
        assert result is True
    
    def test_dir_exists_invalid_path(self):
        """Test dir_exists handles invalid paths gracefully."""
        result = dir_exists("\0invalid")
        
        assert result is False


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_full_workflow(self, tmp_path):
        """Test a complete workflow using all functions."""
        # Create directory structure
        structure = {
            "project": {
                "src": {},
                "docs": {}
            }
        }
        assert create_directory_structure(structure, str(tmp_path)) is True
        
        # Verify directories exist
        assert dir_exists(str(tmp_path / "project")) is True
        assert dir_exists(str(tmp_path / "project" / "src")) is True
        
        # Save a file
        content = "# Project Documentation"
        assert save_text_to_file(content, str(tmp_path / "project" / "docs"), "README.md") is True
        
        # Verify file exists
        readme_path = tmp_path / "project" / "docs" / "README.md"
        assert file_exists(str(readme_path)) is True
        
        # Read file content
        read_content = read_file_content(str(readme_path))
        assert read_content == content
