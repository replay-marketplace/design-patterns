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
    validate_json_schema
)


class TestJSONProcessing:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        self.test_dir = tempfile.mkdtemp()
        yield
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_save_and_load_json_from_file(self):
        """Test saving and loading JSON from file"""
        test_data = {'name': 'John', 'age': 30, 'city': 'New York'}
        filepath = os.path.join(self.test_dir, 'test.json')
        
        # Save JSON
        result = save_json_to_file(test_data, filepath)
        assert result is True
        assert os.path.exists(filepath)
        
        # Load JSON
        loaded_data = load_json_from_file(filepath)
        assert loaded_data == test_data

    def test_load_json_from_nonexistent_file(self):
        """Test loading JSON from non-existent file"""
        filepath = os.path.join(self.test_dir, 'nonexistent.json')
        result = load_json_from_file(filepath)
        assert result == {}

    def test_dict_to_json_string_pretty(self):
        """Test converting dict to pretty JSON string"""
        test_data = {'name': 'John', 'age': 30}
        json_str = dict_to_json_string(test_data, pretty=True)
        
        assert isinstance(json_str, str)
        assert 'name' in json_str
        assert 'John' in json_str
        assert '\n' in json_str  # Pretty format includes newlines

    def test_dict_to_json_string_compact(self):
        """Test converting dict to compact JSON string"""
        test_data = {'name': 'John', 'age': 30}
        json_str = dict_to_json_string(test_data, pretty=False)
        
        assert isinstance(json_str, str)
        assert 'name' in json_str
        assert 'John' in json_str

    def test_parse_json_string(self):
        """Test parsing JSON string to dict"""
        json_str = '{"name": "John", "age": 30}'
        result = parse_json_string(json_str)
        
        assert isinstance(result, dict)
        assert result['name'] == 'John'
        assert result['age'] == 30

    def test_parse_invalid_json_string(self):
        """Test parsing invalid JSON string"""
        json_str = '{invalid json}'
        result = parse_json_string(json_str)
        assert result == {}

    def test_load_json_string_from_file(self):
        """Test loading JSON string from file"""
        test_data = {'name': 'Alice', 'age': 25}
        filepath = os.path.join(self.test_dir, 'test.json')
        
        # Save JSON first
        save_json_to_file(test_data, filepath)
        
        # Load as string
        json_str = load_json_string_from_file(filepath)
        assert isinstance(json_str, str)
        assert 'Alice' in json_str
        
        # Verify it can be parsed back
        parsed = json.loads(json_str)
        assert parsed == test_data

    def test_load_json_string_from_nonexistent_file(self):
        """Test loading JSON string from non-existent file"""
        filepath = os.path.join(self.test_dir, 'nonexistent.json')
        result = load_json_string_from_file(filepath)
        assert result == ''

    def test_save_json_string_to_file(self):
        """Test saving JSON string to file"""
        json_str = '{"name": "Bob", "age": 35}'
        filepath = os.path.join(self.test_dir, 'test.json')
        
        result = save_json_string_to_file(json_str, filepath)
        assert result is True
        assert os.path.exists(filepath)
        
        # Verify content
        loaded = load_json_from_file(filepath)
        assert loaded['name'] == 'Bob'
        assert loaded['age'] == 35

    def test_validate_json_schema_valid(self):
        """Test validating JSON with valid schema"""
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'number'}
            },
            'required': ['name']
        }
        data = {'name': 'John', 'age': 30}
        
        result = validate_json_schema(data, schema)
        assert result is True

    def test_validate_json_schema_invalid(self):
        """Test validating JSON with invalid schema"""
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'number'}
            },
            'required': ['name']
        }
        data = {'age': 30}  # Missing required 'name'
        
        result = validate_json_schema(data, schema)
        assert result is False

    def test_validate_json_schema_type_mismatch(self):
        """Test validating JSON with type mismatch"""
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'number'}
            }
        }
        data = {'name': 'John', 'age': 'thirty'}  # age should be number
        
        result = validate_json_schema(data, schema)
        assert result is False

    def test_nested_json_structure(self):
        """Test handling nested JSON structures"""
        test_data = {
            'user': {
                'name': 'John',
                'address': {
                    'city': 'New York',
                    'zip': '10001'
                }
            },
            'items': [1, 2, 3]
        }
        filepath = os.path.join(self.test_dir, 'nested.json')
        
        # Save and load
        save_json_to_file(test_data, filepath)
        loaded_data = load_json_from_file(filepath)
        
        assert loaded_data == test_data
        assert loaded_data['user']['address']['city'] == 'New York'
        assert loaded_data['items'] == [1, 2, 3]

    def test_save_to_nonexistent_directory(self):
        """Test saving JSON to non-existent directory"""
        filepath = os.path.join(self.test_dir, 'subdir', 'test.json')
        test_data = {'key': 'value'}
        
        result = save_json_to_file(test_data, filepath)
        assert result is True
        assert os.path.exists(filepath)

    def test_empty_dict(self):
        """Test handling empty dictionary"""
        test_data = {}
        filepath = os.path.join(self.test_dir, 'empty.json')
        
        save_json_to_file(test_data, filepath)
        loaded_data = load_json_from_file(filepath)
        
        assert loaded_data == {}

    def test_unicode_characters(self):
        """Test handling Unicode characters"""
        test_data = {'name': '日本語', 'emoji': '😀', 'text': 'Héllo Wörld'}
        filepath = os.path.join(self.test_dir, 'unicode.json')
        
        save_json_to_file(test_data, filepath)
        loaded_data = load_json_from_file(filepath)
        
        assert loaded_data == test_data
