# API Signature

`two_sum(nums: list[int], target: int) -> list[int]` - Finds two numbers in the array that add up to the target value and returns their indices.

## Parameters
- `nums`: A list of integers to search through
- `target`: The target sum to find

## Returns
- A list containing the two indices of numbers that add up to the target
- Returns an empty list if no solution is found

## Example
```python
two_sum([2, 7, 11, 15], 9)  # Returns [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
```
