"""
Get JSON directory example.
"""


def get_json_dir_example() -> dict:
    """
    Returns an example of the json_dir file structure.
    
    Returns:
        dict: Example directory structure in JSON format
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
                "type": "directory",
                "name": "src",
                "children": [
                    {
                        "type": "file",
                        "name": "main.py",
                        "content": "def main():\n    print('Hello, World!')\n\nif __name__ == '__main__':\n    main()\n"
                    },
                    {
                        "type": "file",
                        "name": "__init__.py",
                        "content": ""
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
                        "content": "import unittest\n\nclass TestMain(unittest.TestCase):\n    def test_example(self):\n        self.assertTrue(True)\n"
                    }
                ]
            }
        ]
    }
