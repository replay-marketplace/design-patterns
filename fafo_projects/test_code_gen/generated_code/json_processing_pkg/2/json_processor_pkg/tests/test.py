"""
Test file for the json_processor package.
"""

import os
import json
import tempfile
import shutil
from json_processor import (
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


def test_load_save_json_file():
    """Test loading and saving JSON files."""
    print("Testing load_json_from_file and save_json_to_file...")
    
    test_data = {"name": "test", "value": 123, "nested": {"key": "value"}}
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        # Test save
        result = save_json_to_file(test_data, temp_file)
        assert result == True, "save_json_to_file should return True"
        
        # Test load
        loaded_data = load_json_from_file(temp_file)
        assert loaded_data == test_data, "Loaded data should match original"
        
        print("  ✓ Load and save JSON file tests passed")
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)


def test_dict_json_string_conversion():
    """Test dict to JSON string conversion."""
    print("Testing dict_to_json_string and parse_json_string...")
    
    test_data = {"name": "test", "value": 123}
    
    # Test conversion to string
    json_str = dict_to_json_string(test_data, pretty=False)
    assert isinstance(json_str, str), "Should return a string"
    
    # Test pretty formatting
    json_str_pretty = dict_to_json_string(test_data, pretty=True)
    assert len(json_str_pretty) > len(json_str), "Pretty format should be longer"
    
    # Test parsing back
    parsed_data = parse_json_string(json_str)
    assert parsed_data == test_data, "Parsed data should match original"
    
    print("  ✓ Dict/JSON string conversion tests passed")


def test_json_string_file_operations():
    """Test JSON string file operations."""
    print("Testing load_json_string_from_file and save_json_string_to_file...")
    
    test_json_str = '{"name": "test", "value": 123}'
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        # Test save
        result = save_json_string_to_file(test_json_str, temp_file)
        assert result == True, "save_json_string_to_file should return True"
        
        # Test load
        loaded_str = load_json_string_from_file(temp_file)
        assert json.loads(loaded_str) == json.loads(test_json_str), "Loaded JSON should match original"
        
        print("  ✓ JSON string file operations tests passed")
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)


def test_validate_json_schema():
    """Test JSON schema validation."""
    print("Testing validate_json_schema...")
    
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "value": {"type": "number"}
        },
        "required": ["name"]
    }
    
    valid_data = {"name": "test", "value": 123}
    invalid_data = {"value": 123}  # Missing required 'name'
    
    assert validate_json_schema(valid_data, schema) == True, "Valid data should pass"
    assert validate_json_schema(invalid_data, schema) == False, "Invalid data should fail"
    
    print("  ✓ JSON schema validation tests passed")


def test_json_dir_helpers():
    """Test JSON directory helper functions."""
    print("Testing get_json_dir_example and get_json_dir_schema...")
    
    example = get_json_dir_example()
    assert isinstance(example, dict), "Example should be a dict"
    assert "type" in example, "Example should have 'type' field"
    assert example["type"] == "directory", "Example should be a directory"
    
    schema = get_json_dir_schema()
    assert isinstance(schema, dict), "Schema should be a dict"
    assert "type" in schema, "Schema should have 'type' field"
    
    print("  ✓ JSON directory helper tests passed")


def test_generate_json_schema():
    """Test JSON schema generation."""
    print("Testing generate_json_schema_from_json...")
    
    test_data = {"name": "test", "value": 123, "active": True}
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
        json.dump(test_data, f)
    
    try:
        schema_file = generate_json_schema_from_json(temp_file)
        assert os.path.exists(schema_file), "Schema file should be created"
        
        schema = load_json_from_file(schema_file)
        assert isinstance(schema, dict), "Schema should be a dict"
        
        print("  ✓ JSON schema generation tests passed")
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)
        if 'schema_file' in locals() and os.path.exists(schema_file):
            os.unlink(schema_file)


def test_load_directory_to_json():
    """Test loading directory structure to JSON."""
    print("Testing load_directory_to_json...")
    
    # Create a temporary directory structure
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create test structure
        os.makedirs(os.path.join(temp_dir, "subdir"))
        with open(os.path.join(temp_dir, "file1.txt"), 'w') as f:
            f.write("content1")
        with open(os.path.join(temp_dir, "subdir", "file2.txt"), 'w') as f:
            f.write("content2")
        
        # Load to JSON
        result = load_directory_to_json(temp_dir)
        
        assert isinstance(result, dict), "Result should be a dict"
        assert result["type"] == "directory", "Root should be a directory"
        assert "children" in result, "Should have children"
        assert len(result["children"]) == 2, "Should have 2 children"
        
        print("  ✓ Load directory to JSON tests passed")
    finally:
        shutil.rmtree(temp_dir)


def test_store_json_to_directory():
    """Test storing JSON structure to directory."""
    print("Testing store_json_to_directory...")
    
    json_structure = {
        "type": "directory",
        "name": "test_root",
        "children": [
            {
                "type": "file",
                "name": "test.txt",
                "content": "test content"
            },
            {
                "type": "directory",
                "name": "subdir",
                "children": [
                    {
                        "type": "file",
                        "name": "nested.txt",
                        "content": "nested content"
                    }
                ]
            }
        ]
    }
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        result = store_json_to_directory(json_structure, temp_dir)
        assert result == True, "store_json_to_directory should return True"
        
        # Verify structure
        assert os.path.exists(os.path.join(temp_dir, "test_root")), "Root directory should exist"
        assert os.path.exists(os.path.join(temp_dir, "test_root", "test.txt")), "File should exist"
        assert os.path.exists(os.path.join(temp_dir, "test_root", "subdir", "nested.txt")), "Nested file should exist"
        
        # Verify content
        with open(os.path.join(temp_dir, "test_root", "test.txt"), 'r') as f:
            content = f.read()
            assert content == "test content", "File content should match"
        
        print("  ✓ Store JSON to directory tests passed")
    finally:
        shutil.rmtree(temp_dir)


def test_round_trip_directory_json():
    """Test round-trip conversion: directory -> JSON -> directory."""
    print("Testing round-trip directory <-> JSON conversion...")
    
    # Create original directory
    original_dir = tempfile.mkdtemp()
    
    try:
        # Create test structure
        os.makedirs(os.path.join(original_dir, "subdir"))
        with open(os.path.join(original_dir, "file1.txt"), 'w') as f:
            f.write("content1")
        with open(os.path.join(original_dir, "subdir", "file2.txt"), 'w') as f:
            f.write("content2")
        
        # Convert to JSON
        json_structure = load_directory_to_json(original_dir)
        
        # Convert back to directory
        output_dir = tempfile.mkdtemp()
        store_json_to_directory(json_structure, output_dir)
        
        # Verify structure matches
        original_name = os.path.basename(original_dir)
        recreated_root = os.path.join(output_dir, original_name)
        
        assert os.path.exists(recreated_root), "Recreated root should exist"
        assert os.path.exists(os.path.join(recreated_root, "file1.txt")), "File should exist"
        assert os.path.exists(os.path.join(recreated_root, "subdir", "file2.txt")), "Nested file should exist"
        
        # Verify content
        with open(os.path.join(recreated_root, "file1.txt"), 'r') as f:
            assert f.read() == "content1", "Content should match"
        
        print("  ✓ Round-trip conversion tests passed")
    finally:
        shutil.rmtree(original_dir)
        if 'output_dir' in locals():
            shutil.rmtree(output_dir)


if __name__ == "__main__":
    print("Running json_processor tests...\n")
    
    test_load_save_json_file()
    test_dict_json_string_conversion()
    test_json_string_file_operations()
    test_validate_json_schema()
    test_json_dir_helpers()
    test_generate_json_schema()
    test_load_directory_to_json()
    test_store_json_to_directory()
    test_round_trip_directory_json()
    
    print("\n" + "="*50)
    print("All tests passed!")
    print("="*50)
