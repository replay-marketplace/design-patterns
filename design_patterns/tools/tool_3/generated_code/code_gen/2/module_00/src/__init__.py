"""Module for basic calculations."""

def calculate(a: int, b: int, compute_type: str) -> int:
    """Return the result of addition or multiplication.

    Args:
        a (int): First integer.
        b (int): Second integer.
        compute_type (str): 'add' for addition, 'mult' for multiplication.

    Returns:
        int: The result of the operation.

    Raises:
        ValueError: If compute_type is not 'add' or 'mult'.
    """
    if compute_type == 'add':
        return a + b
    elif compute_type == 'mult':
        return a * b
    else:
        raise ValueError("compute_type must be 'add' or 'mult'")

__all__ = ['calculate']