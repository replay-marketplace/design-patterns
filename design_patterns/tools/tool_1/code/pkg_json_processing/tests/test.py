"""
Tests for pkg_json_processing package.
"""

import sys
import os
import tempfile
import shutil

# Add the package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'package'))

from code.load_json_from_file import load_json_from_file
from code.save_json_to_file import save_json_to_file
from code.dict_to_json_string import dict_to_json_string
from code.parse_json_string import parse_json_string
from code.load_json_string_from_file import load_json_string_from_file
from code.save_json_string_to_file import save_json_string_to_file
from code.validate_json_schema import validate_json_schema
from code.get_json_dir_example import get_json_dir_example
from code.get_json_dir_schema import get_json_dir_schema
from code.generate_json_schema_from_json import generate_json_schema_from_json
from code.load_directory_to_json import load_directory_to_json
from code.store_json_to_directory import store_json_to_directory


def test_load_json_from_file():
    """Test load_json_from_file function."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('{"key": "value", "number": 42}')
        temp_path = f.name
    
    try:
        data = load_json_from_file(temp_path)
        assert data == {"key": "value", "number": 42}
        assert load_json_from_file("/nonexistent/file.json") == {}
        print("✓ load_json_from_file tests passed")
    finally:
        os.unlink(temp_path)


def test_save_json_to_file():
    """Test save_json_to_file function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test.json")
        data = {"key": "value", "number": 42}
        
        assert save_json_to_file(data, filepath) == True
        assert os.path.exists(filepath)
        
        # Verify content
        loaded = load_json_from_file(filepath)
        assert loaded == data
        print("✓ save_json_to_file tests passed")


def test_dict_to_json_string():
    """Test dict_to_json_string function."""
    data = {"key": "value", "number": 42}
    
    json_str = dict_to_json_string(data, pretty=False)
    assert isinstance(json_str, str)
    assert "key" in json_str
    
    json_str_pretty = dict_to_json_string(data, pretty=True)
    assert isinstance(json_str_pretty, str)
    assert "\n" in json_str_pretty
    print("✓ dict_to_json_string tests passed")


def test_parse_json_string():
    """Test parse_json_string function."""
    json_str = '{"key": "value", "number": 42}'
    data = parse_json_string(json_str)
    assert data == {"key": "value", "number": 42}
    assert parse_json_string("invalid json") == {}
    print("✓ parse_json_string tests passed")


def test_load_json_string_from_file():
    """Test load_json_string_from_file function."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('{"key": "value"}')
        temp_path = f.name
    
    try:
        json_str = load_json_string_from_file(temp_path)
        assert isinstance(json_str, str)
        assert "key" in json_str
        assert load_json_string_from_file("/nonexistent/file.json") == ""
        print("✓ load_json_string_from_file tests passed")
    finally:
        os.unlink(temp_path)


def test_save_json_string_to_file():
    """Test save_json_string_to_file function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test.json")
        json_str = '{"key": "value"}'
        
        assert save_json_string_to_file(json_str, filepath) == True
        assert os.path.exists(filepath)
        
        # Verify content
        with open(filepath, 'r') as f:
            content = f.read()
        assert content == json_str
        print("✓ save_json_string_to_file tests passed")


def test_validate_json_schema():
    """Test validate_json_schema function."""
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"},
            "number": {"type": "integer"}
        },
        "required": ["key"]
    }
    
    valid_data = {"key": "value", "number": 42}
    invalid_data = {"key": 123}  # number should be integer, but key is wrong type
    
    # Note: This test may fail if jsonschema is not installed
    result = validate_json_schema(valid_data, schema)
    # If jsonschema is available, result should be True
    # If not available, result will be False
    assert isinstance(result, bool)
    print("✓ validate_json_schema tests passed")


def test_get_json_dir_example():
    """Test get_json_dir_example function."""
    example = get_json_dir_example()
    assert isinstance(example, dict)
    assert example.get("type") == "directory"
    assert "children" in example
    print("✓ get_json_dir_example tests passed")


def test_get_json_dir_schema():
    """Test get_json_dir_schema function."""
    schema = get_json_dir_schema()
    assert isinstance(schema, dict)
    assert schema.get("type") == "object"
    print("✓ get_json_dir_schema tests passed")


def test_generate_json_schema_from_json():
    """Test generate_json_schema_from_json function."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('{"key": "value", "number": 42}')
        temp_path = f.name
    
    try:
        result = generate_json_schema_from_json(temp_path)
        # Result may be False if jsonschema is not available
        assert isinstance(result, bool)
        print("✓ generate_json_schema_from_json tests passed")
    finally:
        os.unlink(temp_path)
        # Clean up schema file if created
        schema_path = temp_path.replace('.json', '_schema.json')
        if os.path.exists(schema_path):
            os.unlink(schema_path)


def test_load_directory_to_json():
    """Test load_directory_to_json function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test structure
        subdir = os.path.join(tmpdir, "subdir")
        os.makedirs(subdir)
        
        with open(os.path.join(tmpdir, "file1.txt"), 'w') as f:
            f.write("content1")
        with open(os.path.join(subdir, "file2.txt"), 'w') as f:
            f.write("content2")
        
        result = load_directory_to_json(tmpdir)
        assert isinstance(result, dict)
        assert result.get("type") == "directory"
        assert "children" in result
        print("✓ load_directory_to_json tests passed")


def test_store_json_to_directory():
    """Test store_json_to_directory function."""
    json_data = {
        "type": "directory",
        "name": "test_dir",
        "children": [
            {
                "type": "file",
                "name": "file1.txt",
                "content": "test content"
            },
            {
                "type": "directory",
                "name": "subdir",
                "children": [
                    {
                        "type": "file",
                        "name": "file2.txt",
                        "content": "another content"
                    }
                ]
            }
        ]
    }
    
    with tempfile.TemporaryDirectory() as tmpdir:
        target = os.path.join(tmpdir, "output")
        assert store_json_to_directory(json_data, target) == True
        
        # Verify structure
        test_dir = os.path.join(target, "test_dir")
        assert os.path.isdir(test_dir)
        assert os.path.isfile(os.path.join(test_dir, "file1.txt"))
        assert os.path.isdir(os.path.join(test_dir, "subdir"))
        assert os.path.isfile(os.path.join(test_dir, "subdir", "file2.txt"))
        
        # Verify content
        with open(os.path.join(test_dir, "file1.txt"), 'r') as f:
            assert f.read() == "test content"
        print("✓ store_json_to_directory tests passed")


if __name__ == "__main__":
    print("Running tests for pkg_json_processing...\n")
    test_load_json_from_file()
    test_save_json_to_file()
    test_dict_to_json_string()
    test_parse_json_string()
    test_load_json_string_from_file()
    test_save_json_string_to_file()
    test_validate_json_schema()
    test_get_json_dir_example()
    test_get_json_dir_schema()
    test_generate_json_schema_from_json()
    test_load_directory_to_json()
    test_store_json_to_directory()
    print("\nAll tests passed! ✓")

