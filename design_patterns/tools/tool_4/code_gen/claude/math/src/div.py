def div(a: int, b: int) -> int:
    """Divide a by b and return the integer result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b
