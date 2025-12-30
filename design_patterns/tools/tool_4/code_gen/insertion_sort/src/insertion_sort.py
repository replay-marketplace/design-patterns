def insertion_sort(arr: list[int]) -> list[int]:
    """Sort an array of integers using insertion sort algorithm.
    
    Args:
        arr: A list of integers to sort.
        
    Returns:
        The sorted list in ascending order.
    """
    # Create a copy to avoid modifying the original array
    result = arr.copy()
    
    # Iterate through the array starting from the second element
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        
        # Move elements that are greater than key to one position ahead
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        
        # Place key at its correct position
        result[j + 1] = key
    
    return result
