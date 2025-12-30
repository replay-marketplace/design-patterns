def selection_sort(arr: list[int]) -> list[int]:
    """
    Sort an array of integers using selection sort algorithm.
    
    Selection sort works by repeatedly finding the minimum element
    from the unsorted portion and putting it at the beginning.
    
    Args:
        arr: List of integers to sort
        
    Returns:
        The sorted list in ascending order
    """
    # Create a copy to avoid modifying the original array
    result = arr.copy()
    n = len(result)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        result[i], result[min_idx] = result[min_idx], result[i]
    
    return result
