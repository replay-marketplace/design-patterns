"""Tests for json_processing package."""

import os
import sys
import tempfile
import json
from pathlib import Path

# Add parent directory to path to import package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from json_processing import (
    load_json_from_file,
    save_json_to_file,
    dict_to_json_string,
    parse_json_string,
    load_json_string_from_file,
    save_json_string_to_file,
    validate_json_schema,
    get_json_dir_example,
    get_json_dir_schema,
    generate_json_schema_from_json,
    load_directory_to_json,
    store_json_to_directory
)


def test_load_json_from_file():
    """Test load_json_from_file function."""
    print("Testing load_json_from_file...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test JSON file
            test_data = {"key": "value", "number": 42}
            filepath = os.path.join(tmpdir, "test.json")
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(test_data, f)
            
            # Load JSON
            data = load_json_from_file(filepath)
            assert data == test_data
            print("✓ load_json_from_file test passed")
            
            # Test FileNotFoundError
            try:
                load_json_from_file(os.path.join(tmpdir, "nonexistent.json"))
                assert False, "Should have raised FileNotFoundError"
            except FileNotFoundError:
                print("✓ load_json_from_file FileNotFoundError test passed")
    except Exception as e:
        print(f"✗ load_json_from_file test failed: {e}")
        raise


def test_save_json_to_file():
    """Test save_json_to_file function."""
    print("\nTesting save_json_to_file...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            test_data = {"key": "value", "number": 42}
            filepath = os.path.join(tmpdir, "test.json")
            
            # Save JSON
            result = save_json_to_file(test_data, filepath)
            assert result is True
            
            # Verify file was created and content is correct
            with open(filepath, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
            assert loaded_data == test_data
            print("✓ save_json_to_file test passed")
    except Exception as e:
        print(f"✗ save_json_to_file test failed: {e}")
        raise


def test_dict_to_json_string():
    """Test dict_to_json_string function."""
    print("\nTesting dict_to_json_string...")
    
    try:
        test_data = {"key": "value", "number": 42}
        
        # Test compact format
        json_str = dict_to_json_string(test_data, pretty=False)
        assert isinstance(json_str, str)
        assert "key" in json_str
        print("✓ dict_to_json_string (compact) test passed")
        
        # Test pretty format
        json_str_pretty = dict_to_json_string(test_data, pretty=True)
        assert isinstance(json_str_pretty, str)
        assert "\n" in json_str_pretty  # Pretty format should have newlines
        print("✓ dict_to_json_string (pretty) test passed")
    except Exception as e:
        print(f"✗ dict_to_json_string test failed: {e}")
        raise


def test_parse_json_string():
    """Test parse_json_string function."""
    print("\nTesting parse_json_string...")
    
    try:
        json_str = '{"key": "value", "number": 42}'
        data = parse_json_string(json_str)
        assert data == {"key": "value", "number": 42}
        print("✓ parse_json_string test passed")
    except Exception as e:
        print(f"✗ parse_json_string test failed: {e}")
        raise


def test_load_json_string_from_file():
    """Test load_json_string_from_file function."""
    print("\nTesting load_json_string_from_file...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.json")
            json_content = '{"key": "value"}'
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(json_content)
            
            loaded_str = load_json_string_from_file(filepath)
            assert loaded_str == json_content
            print("✓ load_json_string_from_file test passed")
    except Exception as e:
        print(f"✗ load_json_string_from_file test failed: {e}")
        raise


def test_save_json_string_to_file():
    """Test save_json_string_to_file function."""
    print("\nTesting save_json_string_to_file...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            json_str = '{"key": "value", "number": 42}'
            filepath = os.path.join(tmpdir, "test.json")
            
            result = save_json_string_to_file(json_str, filepath)
            assert result is True
            
            # Verify content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            assert content == json_str
            print("✓ save_json_string_to_file test passed")
    except Exception as e:
        print(f"✗ save_json_string_to_file test failed: {e}")
        raise


def test_validate_json_schema():
    """Test validate_json_schema function."""
    print("\nTesting validate_json_schema...")
    
    try:
        data = {"name": "John", "age": 30}
        schema = {"name": "str", "age": "int"}
        
        result = validate_json_schema(data, schema)
        assert result is True
        print("✓ validate_json_schema (valid) test passed")
        
        # Test invalid schema
        invalid_data = {"name": "John", "age": "thirty"}
        result = validate_json_schema(invalid_data, schema)
        assert result is False
        print("✓ validate_json_schema (invalid) test passed")
    except Exception as e:
        print(f"✗ validate_json_schema test failed: {e}")
        raise


def test_get_json_dir_example():
    """Test get_json_dir_example function."""
    print("\nTesting get_json_dir_example...")
    
    try:
        example = get_json_dir_example()
        assert isinstance(example, str)
        # Parse to verify it's valid JSON
        data = json.loads(example)
        assert "files" in data
        assert "directories" in data
        print("✓ get_json_dir_example test passed")
    except Exception as e:
        print(f"✗ get_json_dir_example test failed: {e}")
        raise


def test_get_json_dir_schema():
    """Test get_json_dir_schema function."""
    print("\nTesting get_json_dir_schema...")
    
    try:
        schema = get_json_dir_schema()
        assert isinstance(schema, str)
        # Parse to verify it's valid JSON
        schema_data = json.loads(schema)
        assert "type" in schema_data
        print("✓ get_json_dir_schema test passed")
    except Exception as e:
        print(f"✗ get_json_dir_schema test failed: {e}")
        raise


def test_generate_json_schema_from_json():
    """Test generate_json_schema_from_json function."""
    print("\nTesting generate_json_schema_from_json...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test JSON file
            test_data = {"name": "John", "age": 30, "active": True}
            filepath = os.path.join(tmpdir, "test.json")
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(test_data, f)
            
            # Generate schema
            result = generate_json_schema_from_json(filepath)
            assert result is True
            
            # Verify schema file was created
            schema_filepath = os.path.join(tmpdir, "test_schema.json")
            assert os.path.exists(schema_filepath)
            
            # Verify schema content
            with open(schema_filepath, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            assert "type" in schema
            assert schema["type"] == "object"
            print("✓ generate_json_schema_from_json test passed")
    except Exception as e:
        print(f"✗ generate_json_schema_from_json test failed: {e}")
        raise


def test_load_directory_to_json():
    """Test load_directory_to_json function."""
    print("\nTesting load_directory_to_json...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test directory structure
            test_dir = Path(tmpdir) / "test_dir"
            test_dir.mkdir()
            
            (test_dir / "file1.txt").write_text("content1")
            (test_dir / "file2.txt").write_text("content2")
            
            subdir = test_dir / "subdir"
            subdir.mkdir()
            (subdir / "file3.txt").write_text("content3")
            
            # Load directory to JSON
            data = load_directory_to_json(str(test_dir))
            
            assert "files" in data
            assert "directories" in data
            assert "file1.txt" in data["files"]
            assert "file2.txt" in data["files"]
            assert "subdir" in data["directories"]
            assert "file3.txt" in data["directories"]["subdir"]["files"]
            print("✓ load_directory_to_json test passed")
    except Exception as e:
        print(f"✗ load_directory_to_json test failed: {e}")
        raise


def test_store_json_to_directory():
    """Test store_json_to_directory function."""
    print("\nTesting store_json_to_directory...")
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create JSON structure
            json_data = {
                "files": {
                    "file1.txt": "content1",
                    "file2.txt": "content2"
                },
                "directories": {
                    "subdir": {
                        "files": {
                            "file3.txt": "content3"
                        },
                        "directories": {}
                    }
                }
            }
            
            json_filepath = os.path.join(tmpdir, "structure.json")
            with open(json_filepath, 'w', encoding='utf-8') as f:
                json.dump(json_data, f)
            
            output_dir = os.path.join(tmpdir, "output")
            
            # Store JSON to directory
            result = store_json_to_directory(json_filepath, output_dir)
            assert result is True
            
            # Verify structure was created
            assert os.path.exists(os.path.join(output_dir, "file1.txt"))
            assert os.path.exists(os.path.join(output_dir, "file2.txt"))
            assert os.path.exists(os.path.join(output_dir, "subdir", "file3.txt"))
            
            # Verify content
            with open(os.path.join(output_dir, "file1.txt"), 'r', encoding='utf-8') as f:
                assert f.read() == "content1"
            print("✓ store_json_to_directory test passed")
    except Exception as e:
        print(f"✗ store_json_to_directory test failed: {e}")
        raise


if __name__ == "__main__":
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
    print("\nAll tests completed!")



