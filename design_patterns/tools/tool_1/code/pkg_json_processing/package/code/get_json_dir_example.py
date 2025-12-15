"""
Get JSON dir example function - Returns an example of the json_dir file.
"""


def get_json_dir_example() -> dict:
    """
    Returns an example of the json_dir file structure.

    Returns:
        A dictionary representing an example json_dir structure.

    Example:
        >>> example = get_json_dir_example()
        >>> isinstance(example, dict)
        True
    """
    return {
        "type": "directory",
        "name": "example_dir",
        "children": [
            {
                "type": "file",
                "name": "file1.txt",
                "content": "Example content"
            },
            {
                "type": "directory",
                "name": "subdir",
                "children": [
                    {
                        "type": "file",
                        "name": "file2.txt",
                        "content": "Another example"
                    }
                ]
            }
        ]
    }

