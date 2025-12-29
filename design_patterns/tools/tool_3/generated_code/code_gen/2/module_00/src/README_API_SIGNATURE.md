# API Signature

## Function: calculate

- **Parameters:**
  - `a` (int): First integer.
  - `b` (int): Second integer.
  - `compute_type` (str): Type of computation, either 'add' or 'mult'.
- **Returns:** int - The result of the computation.
- **Description:** Performs addition or multiplication based on compute_type.

## Example Usage
```python
from module_00 import calculate

result_add = calculate(5, 3, 'add')
print(result_add)  # Output: 8

result_mult = calculate(5, 3, 'mult')
print(result_mult)  # Output: 15
```