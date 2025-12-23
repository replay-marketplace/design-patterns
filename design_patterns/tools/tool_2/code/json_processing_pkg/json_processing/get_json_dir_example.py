"""Get JSON dir example function - Returns an example of the json_dir file."""


def get_json_dir_example() -> str:
    """
    Returns an example of the json_dir file structure.

    Returns:
        A JSON string containing an example of the json_dir file structure.

    Example:
        >>> example = get_json_dir_example()
        >>> print(example)
        {
          "files": {
            "file1.txt": "content1",
            "file2.txt": "content2"
          },
          "directories": {
            "subdir1": {
              "files": {
                "file3.txt": "content3"
              }
            }
          }
        }
    """
    example = {
        "files": {
            "file1.txt": "content1",
            "file2.txt": "content2"
        },
        "directories": {
            "subdir1": {
                "files": {
                    "file3.txt": "content3"
                },
                "directories": {}
            }
        }
    }
    
    import json
    return json.dumps(example, indent=2, ensure_ascii=False)


