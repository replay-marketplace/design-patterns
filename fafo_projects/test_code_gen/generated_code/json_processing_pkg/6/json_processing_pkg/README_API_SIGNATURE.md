# API Signature

## JSON Processing Functions

### Basic Functions

- `load_json_from_file(filepath: str) -> dict` - Load JSON from file
- `save_json_to_file(data: dict, filepath: str) -> bool` - Save JSON to file
- `dict_to_json_string(data: dict, pretty: bool) -> str` - Convert dict to JSON string
- `parse_json_string(json_str: str) -> dict` - Parse JSON string to dict
- `load_json_string_from_file(filepath: str) -> str` - Load JSON string from file
- `save_json_string_to_file(json_str: str, filepath: str) -> bool` - Save JSON string to file
- `validate_json_schema(data: dict, schema: dict) -> bool` - Validate structure

## Usage

```python
from json_processing import (
    load_json_from_file,
    save_json_to_file,
    dict_to_json_string,
    parse_json_string,
    load_json_string_from_file,
    save_json_string_to_file,
    validate_json_schema
)

# Load JSON from file
data = load_json_from_file('data.json')

# Save JSON to file
save_json_to_file({'key': 'value'}, 'output.json')

# Convert dict to JSON string
json_str = dict_to_json_string({'key': 'value'}, pretty=True)

# Parse JSON string
data = parse_json_string('{"key": "value"}')

# Validate JSON schema
schema = {'type': 'object', 'properties': {'name': {'type': 'string'}}}
is_valid = validate_json_schema({'name': 'John'}, schema)
```
