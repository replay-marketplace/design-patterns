"""Get JSON dir schema function - Returns the schema of the json_dir file."""


def get_json_dir_schema() -> str:
    """
    Returns the schema of the json_dir file structure.

    Returns:
        A JSON string containing the schema definition for json_dir files.

    Example:
        >>> schema = get_json_dir_schema()
        >>> print(schema)
        {
          "type": "object",
          "properties": {
            "files": {
              "type": "object",
              "additionalProperties": {
                "type": "string"
              }
            },
            "directories": {
              "type": "object",
              "additionalProperties": {
                "$ref": "#"
              }
            }
          }
        }
    """
    schema = {
        "type": "object",
        "properties": {
            "files": {
                "type": "object",
                "additionalProperties": {
                    "type": "string"
                }
            },
            "directories": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                }
            }
        }
    }
    
    import json
    return json.dumps(schema, indent=2, ensure_ascii=False)


