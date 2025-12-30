"""Quick Sort implementation using partitioning and recursion."""
from typing import List


def partition(arr: List, low: int, high: int) -> int:
    """Partition the array around a pivot element.
    
    Uses the last element as pivot and places it in its correct
    sorted position. All smaller elements go to the left,
    all greater elements go to the right.
    
    Args:
        arr: The array to partition
        low: Starting index of the partition
        high: Ending index of the partition (pivot position)
    
    Returns:
        The final position of the pivot element
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_inplace(arr: List, low: int = None, high: int = None) -> None:
    """Sort an array in-place using quick sort algorithm.
    
    Args:
        arr: The array to sort
        low: Starting index (default: 0)
        high: Ending index (default: len(arr) - 1)
    """
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)


def quick_sort(arr: List) -> List:
    """Sort an array using quick sort algorithm.
    
    Creates a copy of the array and sorts it, leaving the original unchanged.
    
    Args:
        arr: The array to sort
    
    Returns:
        A new sorted list
    """
    if len(arr) <= 1:
        return arr.copy() if isinstance(arr, list) else list(arr)
    
    result = arr.copy()
    quick_sort_inplace(result, 0, len(result) - 1)
    return result
