

### Getters / Setters
- `get_json_dir_example() -> string` - Returns an example of the json_dir file
- `get_json_dir_schema() -> string` - Returns the schema of the json_dir file
- `generate_json_schema_from_json(input_json_file)` - Saves to the same location



===================================================================================================================
                                                   DIR TREE
===================================================================================================================

==== STEP 1 =====

Implement this in tool_4/src/

1. class dir_tree that holds all the nodes. 
Make a seperate class for nodes for: files and dir.
Use dataclass python lib. 

Node_Dir Attributes:
- path: string
- state: Enum: visible, readonly, hidden

File Attributes: 
- path: string
- content: str
- state: Enum: visible, readonly, hidden

Example dir structure
```
tool_4/src/
├── dir_tree/                        # module1     
│   ├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed APIs for dir_tree (`function_name(size: int, name: string) -> int` - <Description>)
│   ├── dir_tree/
│   │   ├── __init__.py
│   │   ├── dir_tree_class.py
│   └── tests/
│       ├── test.py                 
│       ├── run_tests.sh            # Test runner that sets PYTHONPATH and runs tests
│       ├── setup.sh                # Make python env, install requirements, set PYTHONPATH in venv activation
│       ├── requirements.txt
│       ├── README.md               # Absolute minimum possible readme, just one line how to run the test
│       └── venv/
```

## Import Strategy (Avoid sys.path.insert and pip install -e)

**PYTHONPATH in setup.sh **
- In `setup.sh`: After creating venv, add `export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"` to venv/bin/activate
- Or set it in a test runner script `run_tests.sh`: `PYTHONPATH="$(dirname "$0")/.." python test.py`
- Test files use clean imports: `from module1 import add, sub`


Methods:
`add_file`
`add_dir`
`print_dir_tree` - prints the tree, with dir and file names using ├──, │, └──


In src/dir_tree/tests/ edit the tests so that they print things to terminal when I run them, so I can inspect that this works. 







Create methods for:
1. json_to_tree(files: Dict) -> Node_Dir - Given a dict json, it creases the tree, and returns a pointer to the root node in the tree. 


# Clean imports: `from module1 import add, sub` (no sys.path manipulation)




Advanced
- How will agents specify edits? Full file replacement, diffs, or something like search/replace blocks?




Pruning for Coders
Add a field for "view": 

1. Fully excluded
- completly non existent

2. path included, contents excluded. 
- readonly=True. 
- existance of file is known, but its contents are hidden, but the file is functional and it's there

3. Path & contents included. readonly=True

4. Path & contents included. readonly=False



====== Advanced Class =======

1. class dir_tree that holds all the nodes. 
Make a seperate class for nodes for: files and dir.
Use dataclass python lib. 

Node_Dir Attributes:
- name: string
- path: string
- tokens: int
- tokens_dirty: bool
- type: Enum: "sw", "replay_infra"
- readonly: T/F

File Attributes: 
- name: string
- path: string
- content: str
- tokens: int
- tokens_dirty: bool
- type: Enum: "sw", "replay_infra"
- readonly: T/F
