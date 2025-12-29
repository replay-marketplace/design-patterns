# API Signature

## Function: calculate

- **Description**: Performs addition or multiplication on two integers based on compute_type.
- **Parameters**:
  - `a` (int): First integer.
  - `b` (int): Second integer.
  - `compute_type` (str): Operation type, either 'add' or 'mult'.
- **Returns**: int - The result of the operation.
- **Example**:
  ```python
  result = calculate(3, 4, 'add')
  print(result)  # Output: 7
  ```