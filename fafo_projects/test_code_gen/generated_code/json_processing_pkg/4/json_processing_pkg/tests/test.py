import pytest
import os
import json
import tempfile
import shutil
from pathlib import Path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_data():
    """Sample JSON data for testing."""
    return {
        "name": "test",
        "value": 42,
        "nested": {
            "key": "value"
        },
        "list": [1, 2, 3]
    }


class TestBasicFunctions:
    def test_save_and_load_json_from_file(self, temp_dir, sample_data):
        filepath = os.path.join(temp_dir, "test.json")
        assert save_json_to_file(sample_data, filepath)
        loaded_data = load_json_from_file(filepath)
        assert loaded_data == sample_data

    def test_dict_to_json_string_pretty(self, sample_data):
        json_str = dict_to_json_string(sample_data, pretty=True)
        assert isinstance(json_str, str)
        assert "name" in json_str
        assert "\n" in json_str  # Pretty print includes newlines

    def test_dict_to_json_string_compact(self, sample_data):
        json_str = dict_to_json_string(sample_data, pretty=False)
        assert isinstance(json_str, str)
        assert "name" in json_str

    def test_parse_json_string(self, sample_data):
        json_str = json.dumps(sample_data)
        parsed_data = parse_json_string(json_str)
        assert parsed_data == sample_data

    def test_parse_invalid_json_string(self):
        with pytest.raises(Exception):
            parse_json_string("invalid json")

    def test_load_json_string_from_file(self, temp_dir, sample_data):
        filepath = os.path.join(temp_dir, "test.json")
        with open(filepath, 'w') as f:
            json.dump(sample_data, f)
        json_str = load_json_string_from_file(filepath)
        assert isinstance(json_str, str)
        assert json.loads(json_str) == sample_data

    def test_save_json_string_to_file(self, temp_dir, sample_data):
        filepath = os.path.join(temp_dir, "test.json")
        json_str = json.dumps(sample_data)
        assert save_json_string_to_file(json_str, filepath)
        with open(filepath, 'r') as f:
            loaded_data = json.load(f)
        assert loaded_data == sample_data

    def test_validate_json_schema_valid(self):
        data = {"name": "test", "age": 30}
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"}
            },
            "required": ["name", "age"]
        }
        assert validate_json_schema(data, schema)

    def test_validate_json_schema_invalid(self):
        data = {"name": "test", "age": "thirty"}  # age should be number
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"}
            },
            "required": ["name", "age"]
        }
        assert not validate_json_schema(data, schema)


class TestGettersSetters:
    def test_get_json_dir_example(self):
        example = get_json_dir_example()
        assert isinstance(example, dict)
        assert "type" in example
        assert example["type"] == "directory"

    def test_get_json_dir_schema(self):
        schema = get_json_dir_schema()
        assert isinstance(schema, dict)
        assert "type" in schema

    def test_generate_json_schema_from_json(self, temp_dir, sample_data):
        json_file = os.path.join(temp_dir, "test.json")
        save_json_to_file(sample_data, json_file)
        assert generate_json_schema_from_json(json_file)
        schema_file = os.path.join(temp_dir, "test_schema.json")
        assert os.path.exists(schema_file)


class TestAdvancedFunctions:
    def test_load_directory_to_json(self, temp_dir):
        # Create test directory structure
        os.makedirs(os.path.join(temp_dir, "subdir"))
        with open(os.path.join(temp_dir, "file1.txt"), 'w') as f:
            f.write("content1")
        with open(os.path.join(temp_dir, "subdir", "file2.txt"), 'w') as f:
            f.write("content2")
        
        result = load_directory_to_json(temp_dir)
        assert result["type"] == "directory"
        assert "children" in result
        assert len(result["children"]) > 0

    def test_store_json_to_directory(self, temp_dir):
        json_data = {
            "type": "directory",
            "name": "test_dir",
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
        
        assert store_json_to_directory(json_data, temp_dir)
        assert os.path.exists(os.path.join(temp_dir, "test_dir", "test.txt"))
        assert os.path.exists(os.path.join(temp_dir, "test_dir", "subdir", "nested.txt"))
        
        with open(os.path.join(temp_dir, "test_dir", "test.txt"), 'r') as f:
            assert f.read() == "test content"

    def test_roundtrip_directory_json(self, temp_dir):
        # Create original structure
        original_dir = os.path.join(temp_dir, "original")
        os.makedirs(original_dir)
        with open(os.path.join(original_dir, "file.txt"), 'w') as f:
            f.write("content")
        
        # Convert to JSON
        json_data = load_directory_to_json(original_dir)
        
        # Store back
        restored_dir = os.path.join(temp_dir, "restored")
        os.makedirs(restored_dir)
        store_json_to_directory(json_data, restored_dir)
        
        # Verify
        restored_file = os.path.join(restored_dir, json_data["name"], "file.txt")
        assert os.path.exists(restored_file)
        with open(restored_file, 'r') as f:
            assert f.read() == "content"
