def two_sum(nums: list, target: int) -> list:
    """
    Find two numbers in the array that add up to the target value.
    
    Args:
        nums: A list of integers to search through
        target: The target sum to find
    
    Returns:
        A list containing the two indices of numbers that add up to the target,
        or an empty list if no solution is found.
    """
    # Use a hash map to store seen numbers and their indices
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []
