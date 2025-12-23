import pytest
import json
import os
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
    load_directory_to_json,
    store_json_to_directory
)


class TestBasicFunctions:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test.json")
        self.test_data = {"name": "test", "value": 123, "nested": {"key": "value"}}

    def teardown_method(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_save_and_load_json_from_file(self):
        assert save_json_to_file(self.test_data, self.test_file)
        loaded_data = load_json_from_file(self.test_file)
        assert loaded_data == self.test_data

    def test_dict_to_json_string_pretty(self):
        json_str = dict_to_json_string(self.test_data, pretty=True)
        assert isinstance(json_str, str)
        assert "name" in json_str
        assert "\n" in json_str

    def test_dict_to_json_string_compact(self):
        json_str = dict_to_json_string(self.test_data, pretty=False)
        assert isinstance(json_str, str)
        assert "name" in json_str

    def test_parse_json_string(self):
        json_str = json.dumps(self.test_data)
        parsed_data = parse_json_string(json_str)
        assert parsed_data == self.test_data

    def test_parse_invalid_json_string(self):
        with pytest.raises(ValueError):
            parse_json_string("invalid json")

    def test_load_json_string_from_file(self):
        with open(self.test_file, 'w') as f:
            json.dump(self.test_data, f)
        json_str = load_json_string_from_file(self.test_file)
        assert isinstance(json_str, str)
        assert json.loads(json_str) == self.test_data

    def test_save_json_string_to_file(self):
        json_str = json.dumps(self.test_data)
        assert save_json_string_to_file(json_str, self.test_file)
        with open(self.test_file, 'r') as f:
            loaded_data = json.load(f)
        assert loaded_data == self.test_data

    def test_validate_json_schema_valid(self):
        schema = {
            "name": str,
            "value": int,
            "nested": dict
        }
        assert validate_json_schema(self.test_data, schema)

    def test_validate_json_schema_invalid(self):
        schema = {
            "name": str,
            "value": str,
            "nested": dict
        }
        assert not validate_json_schema(self.test_data, schema)

    def test_load_nonexistent_file(self):
        with pytest.raises(FileNotFoundError):
            load_json_from_file("/nonexistent/file.json")


class TestAdvancedFunctions:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()

    def teardown_method(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_load_directory_to_json_simple(self):
        os.makedirs(os.path.join(self.test_dir, "subdir"))
        with open(os.path.join(self.test_dir, "file1.txt"), 'w') as f:
            f.write("content1")
        with open(os.path.join(self.test_dir, "subdir", "file2.txt"), 'w') as f:
            f.write("content2")
        
        result = load_directory_to_json(self.test_dir)
        assert result["type"] == "directory"
        assert len(result["children"]) == 2

    def test_load_directory_to_json_recursive(self):
        os.makedirs(os.path.join(self.test_dir, "level1", "level2"))
        with open(os.path.join(self.test_dir, "level1", "level2", "deep.txt"), 'w') as f:
            f.write("deep content")
        
        result = load_directory_to_json(self.test_dir)
        assert result["type"] == "directory"
        level1 = [c for c in result["children"] if c["name"] == "level1"][0]
        assert level1["type"] == "directory"
        level2 = [c for c in level1["children"] if c["name"] == "level2"][0]
        assert level2["type"] == "directory"

    def test_store_json_to_directory(self):
        json_structure = {
            "type": "directory",
            "name": "root",
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
        
        output_dir = os.path.join(self.test_dir, "output")
        assert store_json_to_directory(json_structure, output_dir)
        assert os.path.exists(os.path.join(output_dir, "test.txt"))
        assert os.path.exists(os.path.join(output_dir, "subdir", "nested.txt"))
        
        with open(os.path.join(output_dir, "test.txt"), 'r') as f:
            assert f.read() == "test content"

    def test_load_empty_directory(self):
        result = load_directory_to_json(self.test_dir)
        assert result["type"] == "directory"
        assert result["children"] == []

    def test_store_and_load_roundtrip(self):
        json_structure = {
            "type": "directory",
            "name": "test",
            "children": [
                {
                    "type": "file",
                    "name": "data.txt",
                    "content": "some data"
                }
            ]
        }
        
        output_dir = os.path.join(self.test_dir, "roundtrip")
        store_json_to_directory(json_structure, output_dir)
        loaded = load_directory_to_json(output_dir)
        
        assert loaded["type"] == "directory"
        assert len(loaded["children"]) == 1
        assert loaded["children"][0]["name"] == "data.txt"
        assert loaded["children"][0]["content"] == "some data"
