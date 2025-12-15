"""
Function 2: Number manipulation utility.
"""


def function_two(numbers: list[int | float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: A list of integers or floats.

    Returns:
        The average of the numbers.

    Raises:
        ValueError: If the list is empty.

    Example:
        >>> function_two([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)

