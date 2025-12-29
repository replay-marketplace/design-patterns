def matrix_multiply(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """
    Multiply two matrices and return the result.
    
    Args:
        matrix_a: First matrix (m x n)
        matrix_b: Second matrix (n x p)
    
    Returns:
        Resulting matrix (m x p)
    
    Raises:
        ValueError: If matrices have incompatible dimensions or are empty
    """
    if not matrix_a or not matrix_b:
        raise ValueError("Matrices cannot be empty")
    
    if not matrix_a[0] or not matrix_b[0]:
        raise ValueError("Matrices cannot have empty rows")
    
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    # Validate all rows have same length
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
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Perform multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result
