def linear_search(arr: list, target) -> int:
    """
    Perform linear search to find target element in array.
    
    Args:
        arr: List of elements to search through
        target: Element to find in the array
    
    Returns:
        Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
