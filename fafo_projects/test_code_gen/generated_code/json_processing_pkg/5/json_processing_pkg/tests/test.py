import pytest
import os
import json
import tempfile
import shutil
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


class TestBasicFunctions:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_data = {"name": "test", "value": 123, "nested": {"key": "value"}}
    
    def teardown_method(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_save_and_load_json_from_file(self):
        filepath = os.path.join(self.test_dir, "test.json")
        assert save_json_to_file(self.test_data, filepath)
        loaded_data = load_json_from_file(filepath)
        assert loaded_data == self.test_data
    
    def test_dict_to_json_string(self):
        json_str = dict_to_json_string(self.test_data, pretty=True)
        assert isinstance(json_str, str)
        assert "name" in json_str
        assert "test" in json_str
        
        json_str_compact = dict_to_json_string(self.test_data, pretty=False)
        assert len(json_str_compact) < len(json_str)
    
    def test_parse_json_string(self):
        json_str = json.dumps(self.test_data)
        parsed_data = parse_json_string(json_str)
        assert parsed_data == self.test_data
    
    def test_load_json_string_from_file(self):
        filepath = os.path.join(self.test_dir, "test.json")
        with open(filepath, 'w') as f:
            json.dump(self.test_data, f)
        
        json_str = load_json_string_from_file(filepath)
        assert isinstance(json_str, str)
        assert json.loads(json_str) == self.test_data
    
    def test_save_json_string_to_file(self):
        json_str = json.dumps(self.test_data)
        filepath = os.path.join(self.test_dir, "test.json")
        assert save_json_string_to_file(json_str, filepath)
        
        with open(filepath, 'r') as f:
            loaded_data = json.load(f)
        assert loaded_data == self.test_data
    
    def test_validate_json_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "value": {"type": "number"}
            },
            "required": ["name", "value"]
        }
        assert validate_json_schema(self.test_data, schema)
        
        invalid_data = {"name": "test"}
        assert not validate_json_schema(invalid_data, schema)


class TestGettersSetters:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
    
    def teardown_method(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_get_json_dir_example(self):
        example = get_json_dir_example()
        assert isinstance(example, dict)
        assert "type" in example
        assert example["type"] == "directory"
    
    def test_get_json_dir_schema(self):
        schema = get_json_dir_schema()
        assert isinstance(schema, dict)
        assert "type" in schema
    
    def test_generate_json_schema_from_json(self):
        test_data = {"name": "test", "value": 123, "items": [1, 2, 3]}
        filepath = os.path.join(self.test_dir, "test.json")
        with open(filepath, 'w') as f:
            json.dump(test_data, f)
        
        assert generate_json_schema_from_json(filepath)
        
        schema_path = os.path.join(self.test_dir, "test_schema.json")
        assert os.path.exists(schema_path)


class TestAdvancedFunctions:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
    
    def teardown_method(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_load_directory_to_json(self):
        # Create test directory structure
        os.makedirs(os.path.join(self.test_dir, "subdir"))
        with open(os.path.join(self.test_dir, "file1.txt"), 'w') as f:
            f.write("content1")
        with open(os.path.join(self.test_dir, "subdir", "file2.txt"), 'w') as f:
            f.write("content2")
        
        json_data = load_directory_to_json(self.test_dir)
        assert json_data["type"] == "directory"
        assert "children" in json_data
        assert len(json_data["children"]) > 0
    
    def test_store_json_to_directory(self):
        json_data = {
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
        
        assert store_json_to_directory(json_data, self.test_dir)
        assert os.path.exists(os.path.join(self.test_dir, "test.txt"))
        assert os.path.exists(os.path.join(self.test_dir, "subdir", "nested.txt"))
        
        with open(os.path.join(self.test_dir, "test.txt"), 'r') as f:
            assert f.read() == "test content"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

