"""
Get example JSON directory structure.
"""


def get_json_dir_example() -> dict:
    """
    Returns an example of a JSON directory structure.
    
    Returns:
        dict: Example JSON directory structure
    """
    return {
        "type": "directory",
        "name": "example_project",
        "children": [
            {
                "type": "file",
                "name": "README.md",
                "content": "# Example Project\n\nThis is an example project structure."
            },
            {
                "type": "file",
                "name": "config.json",
                "content": '{\n  "version": "1.0.0",\n  "name": "example"\n}'
            },
            {
                "type": "directory",
                "name": "src",
                "children": [
                    {
                        "type": "file",
                        "name": "main.py",
                        "content": "def main():\n    print('Hello, World!')\n\nif __name__ == '__main__':\n    main()"
                    },
                    {
                        "type": "directory",
                        "name": "utils",
                        "children": [
                            {
                                "type": "file",
                                "name": "__init__.py",
                                "content": ""
                            },
                            {
                                "type": "file",
                                "name": "helpers.py",
                                "content": "def helper_function():\n    pass"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "directory",
                "name": "tests",
                "children": [
                    {
                        "type": "file",
                        "name": "test_main.py",
                        "content": "def test_main():\n    assert True"
                    }
                ]
            }
        ]
    }
