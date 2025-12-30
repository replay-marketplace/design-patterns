def bubble_sort(arr: list[int]) -> list[int]:
    """Sort an array of integers using bubble sort algorithm.
    
    Args:
        arr: List of integers to sort.
        
    Returns:
        A new list with elements sorted in ascending order.
    """
    # Create a copy to avoid modifying the original array
    result = arr.copy()
    n = len(result)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize if no swaps occur
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if current element is greater than next
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return result
