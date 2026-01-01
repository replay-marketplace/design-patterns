# ProjectTree API Signature

## Classes

### ProjectTree
- `__init__(name: str = "", dir_tree: Optional[DirTree] = None, prompt: str = "", functions: List[str] = None) -> None` - Initialize ProjectTree with name, dir_tree, prompt, and functions
- `add_node(name: str, dependencies: List[str] = None) -> ProjectNode` - Add a new project node to the tree and return it
- `get_dependencies(name: str) -> List[ProjectNode]` - Get the dependencies of a project node by name
- `get_node(name: str) -> Optional[ProjectNode]` - Get a project node by name
- `get_all_nodes() -> Dict[str, ProjectNode]` - Get all nodes in the tree as a dictionary
- `get_nodes() -> List[ProjectNode]` - Get a list of all nodes in the tree
- `print_tree(show_apis: bool = False) -> None` - Print the project tree showing all nodes and their dependencies

### ProjectNode
- `name: str` - Name of the project
- `dependencies: List[ProjectNode]` - List of project nodes that this project depends on
- `apis: List[str]` - List of strings containing API signatures
