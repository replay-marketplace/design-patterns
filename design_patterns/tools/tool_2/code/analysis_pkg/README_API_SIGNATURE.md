# Analysis Package

## API Signatures

### Basic: Dir/File counter mechanics

- `count_loc(dir: str) -> int` - Returns total lines of text in directory
- `count_words(dir: str, text: str = None) -> int` - Returns total words in dir (if text is None) or occurrences of text pattern
- `count_files(dir: str) -> int` - Returns the number of files in dir
- `count_file_types(dir: str) -> List[Tuple[str, int]]` - Returns a list of tuples, with file type (ex. "*.py") and corresponding count
- `count_function_defs(dir: str) -> int` - Returns the LoC in requirements.txt
- `get_path_to_file(dir: str, filename: str) -> str` - searches all files in the given dir for the given filename and returns the path to it

### Python Code Analysis

- `count_python_imports(dir: str) -> Tuple[int, List[str]]` - Use ast python lib to make a list of all imported functions, code, libraries, local or remote, all types. Returns the total number of imports and the list of all imports.
- `count_python_functions(dir: str) -> Tuple[int, List[str]]` - Use ast python lib to make a list of all functions defined in given dir. Returns the function count and all function names.

