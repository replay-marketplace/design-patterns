"""Merge Sort implementation using divide and conquer approach."""


def merge(left: list, right: list) -> list:
    """Merge two sorted lists into a single sorted list.
    
    Args:
        left: First sorted list
        right: Second sorted list
    
    Returns:
        A new sorted list containing all elements from both input lists
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort(arr: list) -> list:
    """Sort an array using merge sort algorithm (divide and conquer).
    
    Args:
        arr: The list to be sorted
    
    Returns:
        A new sorted list
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr.copy() if arr else []
    
    # Divide: split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Conquer: recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Combine: merge the sorted halves
    return merge(sorted_left, sorted_right)
