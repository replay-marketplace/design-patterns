from module1 import add, sub


def calculate(a: int, b: int, type: str) -> int:
    """Calculate based on type using add or sub from module1."""
    if type == "add":
        return add(a, b)
    elif type == "sub":
        return sub(a, b)
    else:
        raise ValueError(f"Unknown type: {type}. Must be 'add' or 'sub'")

