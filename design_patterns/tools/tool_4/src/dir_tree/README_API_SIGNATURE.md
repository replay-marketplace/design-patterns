# DirTree API Signature

## Classes

### DirTree
- `__init__(root: Optional[Node_Dir] = None) -> None` - Initialize DirTree with optional root node
- `add_file(filepath: str, content: str = "", state: State = State.VISIBLE) -> None` - Add a file to the tree at the given path
- `add_dir(dirpath: str, state: State = State.VISIBLE) -> None` - Add a directory to the tree at the given path
- `print_dir_tree() -> None` - Print the directory tree with tree structure using ├──, │, └──
- `json_to_tree(files: List[Dict[str, str]]) -> Node_Dir` - Create tree from JSON and return root node
- `dir_exists(dirpath: str) -> bool` - Check if directory exists
- `set_dir_to_invisible(dirpath: str) -> None` - Set a directory to invisible (HIDDEN state)
- `generate_file_dict() -> Dict[str, str]` - Generate a dictionary with files. Does not include files set to HIDDEN, or anything within a dir that's set to HIDDEN

### Node_Dir
- `path: str` - Path of the directory
- `state: State` - State of the directory (VISIBLE, READONLY, HIDDEN)
- `children: Dict[str, Node_Dir]` - Child directories
- `files: Dict[str, File]` - Files in this directory

### File
- `path: str` - Path of the file
- `content: str` - Content of the file
- `state: State` - State of the file (VISIBLE, READONLY, HIDDEN)

### State (Enum)
- `VISIBLE` - Visible state
- `READONLY` - Read-only state
- `HIDDEN` - Hidden state

