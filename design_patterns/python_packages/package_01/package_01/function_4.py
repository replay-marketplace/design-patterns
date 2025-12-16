"""
Function 4: List manipulation utility.
"""


def function_four(items: list, reverse: bool = False) -> list:
    """
    Remove duplicates from a list while preserving order.

    Args:
        items: The list to process.
        reverse: If True, reverse the order after removing duplicates.

    Returns:
        A new list with duplicates removed.

    Example:
        >>> function_four([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
        >>> function_four([1, 2, 2, 3, 1, 4], reverse=True)
        [4, 3, 2, 1]
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    if reverse:
        result.reverse()
    
    return result


