import os
import importlib.util

# Load the add function from module_01 without modifying sys.path
module_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
add_module_path = os.path.join(os.path.dirname(module_dir), 'module_01', 'src', 'add.py')
spec = importlib.util.spec_from_file_location("add", add_module_path)
add_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(add_module)
add = add_module.add


def calculate(a: int, b: int, compute_type: str) -> int:
    if compute_type == 'add':
        return add(a, b)
    elif compute_type == 'mult':
        return a * b
    else:
        raise ValueError("compute_type must be 'add' or 'mult'")
