"""
Test file for the json_processor package.
"""

import os
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
    store_json_to_directory,
)


def test_basic_json_operations():
    """Test basic JSON file operations."""
    print("Testing basic JSON operations...")
    
    # Create a temporary directory for testing
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test data
        test_data = {
            "name": "Test",
            "value": 42,
            "items": [1, 2, 3],
            "nested": {"key": "value"}
        }
        
        # Test save and load
        filepath = os.path.join(temp_dir, "test.json")
        assert save_json_to_file(test_data, filepath), "Failed to save JSON"
        loaded_data = load_json_from_file(filepath)
        assert loaded_data == test_data, "Loaded data doesn't match"
        
        # Test dict to JSON string
        json_str = dict_to_json_string(test_data, pretty=True)
        assert isinstance(json_str, str), "JSON string conversion failed"
        assert "Test" in json_str, "JSON string missing data"
        
        # Test parse JSON string
        parsed_data = parse_json_string(json_str)
        assert parsed_data == test_data, "Parsed data doesn't match"
        
        # Test load/save JSON string from/to file
        str_filepath = os.path.join(temp_dir, "test_str.json")
        assert save_json_string_to_file(json_str, str_filepath), "Failed to save JSON string"
        loaded_str = load_json_string_from_file(str_filepath)
        assert loaded_str == json_str, "Loaded JSON string doesn't match"
        
        print("✓ Basic JSON operations passed")
    
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


def test_json_schema_validation():
    """Test JSON schema validation."""
    print("Testing JSON schema validation...")
    
    # Test data
    data = {
        "name": "John",
        "age": 30
    }
    
    # Valid schema
    valid_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["name", "age"]
    }
    
    # Invalid schema (age should be number, not string)
    invalid_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "string"}
        },
        "required": ["name", "age"]
    }
    
    assert validate_json_schema(data, valid_schema), "Valid schema validation failed"
    assert not validate_json_schema(data, invalid_schema), "Invalid schema should fail"
    
    print("✓ JSON schema validation passed")


def test_json_dir_helpers():
    """Test JSON directory helper functions."""
    print("Testing JSON directory helpers...")
    
    # Test get example
    example = get_json_dir_example()
    assert isinstance(example, dict), "Example should be a dict"
    assert example.get("type") == "directory", "Example should be a directory"
    assert "children" in example, "Example should have children"
    
    # Test get schema
    schema = get_json_dir_schema()
    assert isinstance(schema, dict), "Schema should be a dict"
    assert "$schema" in schema, "Schema should have $schema field"
    
    # Validate example against schema
    assert validate_json_schema(example, schema), "Example should validate against schema"
    
    print("✓ JSON directory helpers passed")


def test_generate_schema_from_json():
    """Test schema generation from JSON file."""
    print("Testing schema generation...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create test JSON file
        test_data = {
            "name": "Test",
            "count": 5,
            "active": True,
            "tags": ["a", "b"],
            "metadata": {"key": "value"}
        }
        
        json_file = os.path.join(temp_dir, "test.json")
        save_json_to_file(test_data, json_file)
        
        # Generate schema
        assert generate_json_schema_from_json(json_file), "Schema generation failed"
        
        # Check schema file exists
        schema_file = os.path.join(temp_dir, "test_schema.json")
        assert os.path.exists(schema_file), "Schema file not created"
        
        # Load and validate schema
        schema = load_json_from_file(schema_file)
        assert schema.get("type") == "object", "Schema should be object type"
        assert "properties" in schema, "Schema should have properties"
        
        print("✓ Schema generation passed")
    
    finally:
        shutil.rmtree(temp_dir)


def test_directory_to_json():
    """Test loading directory structure to JSON."""
    print("Testing directory to JSON conversion...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create test directory structure
        os.makedirs(os.path.join(temp_dir, "subdir"))
        
        with open(os.path.join(temp_dir, "file1.txt"), 'w') as f:
            f.write("Content 1")
        
        with open(os.path.join(temp_dir, "subdir", "file2.txt"), 'w') as f:
            f.write("Content 2")
        
        # Load to JSON
        json_structure = load_directory_to_json(temp_dir)
        
        # Validate structure
        assert json_structure.get("type") == "directory", "Root should be directory"
        assert "children" in json_structure, "Should have children"
        assert len(json_structure["children"]) == 2, "Should have 2 children"
        
        # Find file1.txt
        file1 = next((c for c in json_structure["children"] if c["name"] == "file1.txt"), None)
        assert file1 is not None, "file1.txt not found"
        assert file1["type"] == "file", "file1.txt should be a file"
        assert file1["content"] == "Content 1", "file1.txt content mismatch"
        
        print("✓ Directory to JSON conversion passed")
    
    finally:
        shutil.rmtree(temp_dir)


def test_json_to_directory():
    """Test storing JSON structure to directory."""
    print("Testing JSON to directory conversion...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create JSON structure
        json_structure = {
            "type": "directory",
            "name": "test_project",
            "children": [
                {
                    "type": "file",
                    "name": "README.md",
                    "content": "# Test Project"
                },
                {
                    "type": "directory",
                    "name": "src",
                    "children": [
                        {
                            "type": "file",
                            "name": "main.py",
                            "content": "print('Hello')\n"
                        }
                    ]
                }
            ]
        }
        
        # Store to directory
        assert store_json_to_directory(json_structure, temp_dir), "Failed to store JSON to directory"
        
        # Verify structure
        project_dir = os.path.join(temp_dir, "test_project")
        assert os.path.exists(project_dir), "Project directory not created"
        assert os.path.isdir(project_dir), "Project should be a directory"
        
        readme_path = os.path.join(project_dir, "README.md")
        assert os.path.exists(readme_path), "README.md not created"
        
        with open(readme_path, 'r') as f:
            content = f.read()
            assert content == "# Test Project", "README.md content mismatch"
        
        src_dir = os.path.join(project_dir, "src")
        assert os.path.exists(src_dir), "src directory not created"
        
        main_path = os.path.join(src_dir, "main.py")
        assert os.path.exists(main_path), "main.py not created"
        
        print("✓ JSON to directory conversion passed")
    
    finally:
        shutil.rmtree(temp_dir)


def test_round_trip():
    """Test round-trip conversion: directory -> JSON -> directory."""
    print("Testing round-trip conversion...")
    
    temp_dir1 = tempfile.mkdtemp()
    temp_dir2 = tempfile.mkdtemp()
    
    try:
        # Create original structure
        os.makedirs(os.path.join(temp_dir1, "src"))
        
        with open(os.path.join(temp_dir1, "README.md"), 'w') as f:
            f.write("# Original")
        
        with open(os.path.join(temp_dir1, "src", "app.py"), 'w') as f:
            f.write("# App code")
        
        # Convert to JSON
        json_structure = load_directory_to_json(temp_dir1)
        
        # Convert back to directory
        store_json_to_directory(json_structure, temp_dir2)
        
        # Verify
        restored_dir = os.path.join(temp_dir2, os.path.basename(temp_dir1))
        assert os.path.exists(restored_dir), "Restored directory not found"
        
        readme_path = os.path.join(restored_dir, "README.md")
        assert os.path.exists(readme_path), "README.md not restored"
        
        with open(readme_path, 'r') as f:
            assert f.read() == "# Original", "README.md content not preserved"
        
        print("✓ Round-trip conversion passed")
    
    finally:
        shutil.rmtree(temp_dir1)
        shutil.rmtree(temp_dir2)


if __name__ == "__main__":
    print("Running json_processor tests...\n")
    
    test_basic_json_operations()
    test_json_schema_validation()
    test_json_dir_helpers()
    test_generate_schema_from_json()
    test_directory_to_json()
    test_json_to_directory()
    test_round_trip()
    
    print("\n" + "="*50)
    print("All tests passed! ✓")
    print("="*50)
