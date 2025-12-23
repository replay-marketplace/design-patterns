# API Signature

## Basic Functions

- `load_json_from_file(filepath: str) -> dict` - Load JSON from file
- `save_json_to_file(data: dict, filepath: str) -> bool` - Save JSON to file
- `dict_to_json_string(data: dict, pretty: bool = True) -> str` - Convert dict to JSON string
- `parse_json_string(json_str: str) -> dict` - Parse JSON string to dict
- `load_json_string_from_file(filepath: str) -> str` - Load JSON string from file
- `save_json_string_to_file(json_str: str, filepath: str) -> bool` - Save JSON string to file
- `validate_json_schema(data: dict, schema: dict) -> bool` - Validate structure

## Advanced Functions

- `load_directory_to_json(directory: str) -> dict` - Directory to JSON, always recursive
- `store_json_to_directory(data: dict, base_directory: str) -> bool` - Store JSON structure to directory
