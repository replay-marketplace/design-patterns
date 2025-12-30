def matrix_multiply(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """
    Multiply two matrices and return the result.
    
    Args:
        matrix_a: First matrix (m x n)
        matrix_b: Second matrix (n x p)
    
    Returns:
        Result matrix (m x p)
    
    Raises:
        ValueError: If matrices have incompatible dimensions or are empty
    """
    if not matrix_a or not matrix_a[0]:
        raise ValueError("Matrix A cannot be empty")
    if not matrix_b or not matrix_b[0]:
        raise ValueError("Matrix B cannot be empty")
    
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    # Check that all rows have consistent length
    for row in matrix_a:
        if len(row) != cols_a:
            raise ValueError("Matrix A has inconsistent row lengths")
    for row in matrix_b:
        if len(row) != cols_b:
            raise ValueError("Matrix B has inconsistent row lengths")
    
    # Check dimension compatibility
    if cols_a != rows_b:
        raise ValueError(f"Cannot multiply matrices: A has {cols_a} columns but B has {rows_b} rows")
    
    # Initialize result matrix with zeros
    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Perform multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result
