"""Fibonacci number generator."""

def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(n: int) -> list:
    """Generate a list of the first n Fibonacci numbers.
    
    Args:
        n: The number of Fibonacci numbers to generate
    
    Returns:
        A list of the first n Fibonacci numbers
    """
    if n <= 0:
        return []
    return [fibonacci(i) for i in range(n)]
