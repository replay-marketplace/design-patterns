'''
Make a simple program that receives a path to a directory, and then uses ast lib to analize the code in the directory.
It should return a list of all the functions in the code.
It should return a list of all the classes in the code.
It should return a list of all the imports in the code.
'''

import ast
from pathlib import Path
from typing import List, Dict, Union


def get_imports(file_path: Path) -> List[str]:
    """Get imports from a single file without following them."""
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=str(file_path))
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
    except SyntaxError as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    except Exception as e:
        print(f"Warning: Error processing {file_path}: {e}")
    return imports


def get_functions(file_path: Path) -> List[Dict]:
    """Get functions from a single file."""
    functions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=str(file_path))
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    'name': node.name,
                    'file': str(file_path),
                    'line': node.lineno,
                    'args': [arg.arg for arg in node.args.args]
                })
    except SyntaxError as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    except Exception as e:
        print(f"Warning: Error processing {file_path}: {e}")
    return functions


def get_classes(file_path: Path) -> List[Dict]:
    """Get classes from a single file."""
    classes = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=str(file_path))
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                classes.append({
                    'name': node.name,
                    'file': str(file_path),
                    'line': node.lineno,
                    'methods': methods
                })
    except SyntaxError as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    except Exception as e:
        print(f"Warning: Error processing {file_path}: {e}")
    return classes


def get_files_to_analyze(paths: List[str]) -> List[Path]:
    """
    Get list of Python files to analyze from given paths.
    If a path is a directory, recursively find all .py files in it.
    If a path is a file, add it to the list.
    """
    files_to_analyze = []
    for path_str in paths:
        path = Path(path_str)
        if not path.exists():
            print(f"Warning: Path does not exist: {path}")
            continue
        
        if path.is_dir():
            # Find all Python files in directory
            files_to_analyze.extend(path.rglob("*.py"))
        elif path.is_file() and path.suffix == '.py':
            files_to_analyze.append(path)
        else:
            print(f"Warning: Not a Python file or directory: {path}")
    
    return files_to_analyze


def analyze_files(file_paths: List[Union[str, Path]]) -> Dict[str, List]:
    """
    Analyze explicitly passed files and return all functions, classes, and imports.
    Does not follow/resolve imports - only analyzes the files themselves.
    
    Args:
        file_paths: List of file paths or directory paths to analyze
        
    Returns:
        Dictionary with 'functions', 'classes', and 'imports' lists
    """
    # Convert to Path objects and get all files to analyze
    paths = [str(p) for p in file_paths]
    python_files = get_files_to_analyze(paths)
    
    all_functions = []
    all_classes = []
    all_imports = []
    
    for file_path in python_files:
        all_functions.extend(get_functions(file_path))
        all_classes.extend(get_classes(file_path))
        all_imports.extend(get_imports(file_path))
    
    return {
        'functions': all_functions,
        'classes': all_classes,
        'imports': all_imports
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python ast_analyzer.py <file_or_directory_path> [<file_or_directory_path> ...]")
        sys.exit(1)
    
    # Get all paths from command line arguments
    paths = sys.argv[1:]
    results = analyze_files(paths)
    
    print(f"\n=== Analysis Results ===")
    print(f"\nTotal number of functions: {len(results['functions'])}")
    if results['functions']:
        print("Functions:")
        for func in results['functions']:
            args_str = ', '.join(func['args'])
            print(f"  - {func['name']}({args_str}) in {func['file']}:{func['line']}")
    
    print(f"\nTotal number of classes: {len(results['classes'])}")
    if results['classes']:
        print("Classes:")
        for cls in results['classes']:
            methods_str = ', '.join(cls['methods']) if cls['methods'] else 'no methods'
            print(f"  - {cls['name']} in {cls['file']}:{cls['line']} (methods: {methods_str})")
    
    print(f"\nTotal number of imports: {len(results['imports'])}")
    if results['imports']:
        print("Imports:")
        for imp in results['imports']:
            print(f"  - {imp}")

