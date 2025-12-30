def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    """Merge two sorted arrays into a single sorted array.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        
    Returns:
        A new sorted array containing all elements from both input arrays
    """
    if not arr1:
        return arr2[:] if arr2 else []
    if not arr2:
        return arr1[:]
    
    result = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Append remaining elements
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result
