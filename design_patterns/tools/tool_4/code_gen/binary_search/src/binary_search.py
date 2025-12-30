def binary_search(arr: list, target: int) -> int:
    """Search for target element in a sorted array using binary search.
    
    Args:
        arr: A sorted list of integers
        target: The integer value to search for
        
    Returns:
        The index of target if found, otherwise -1
    """
    if not arr:
        return -1
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
