# API Signature

## Basic Functions

- `load_json_from_file(filepath: str) -> dict` - Load JSON from file
- `save_json_to_file(data: dict, filepath: str) -> bool` - Save JSON to file
- `dict_to_json_string(data: dict, pretty: bool = True) -> str` - Convert dict to JSON string
- `parse_json_string(json_str: str) -> dict` - Parse JSON string to dict
- `load_json_string_from_file(filepath: str) -> str` - Load JSON string from file
- `save_json_string_to_file(json_str: str, filepath: str) -> bool` - Save JSON string to file
- `validate_json_schema(data: dict, schema: dict) -> bool` - Validate structure

## Getters / Setters

- `get_json_dir_example() -> dict` - Returns an example of the json_dir file
- `get_json_dir_schema() -> dict` - Returns the schema of the json_dir file
- `generate_json_schema_from_json(input_json_file: str) -> bool` - Saves to the same location

## Advanced

- `load_directory_to_json(directory: str) -> dict` - Directory to JSON, always recursive
- `store_json_to_directory(json_data: dict, base_path: str) -> bool` - Store JSON structure to directory

