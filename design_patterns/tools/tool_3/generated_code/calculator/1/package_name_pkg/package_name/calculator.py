def calculator(num1: float, num2: float, operation: str) -> float:
    """
    Perform arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): Operation to perform. Must be one of: 'add', 'sub', 'mult', 'div'.
    
    Returns:
        float: Result of the operation.
    
    Raises:
        ValueError: If operation is invalid or division by zero is attempted.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mult':
        return num1 * num2
    elif operation == 'div':
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Use 'add', 'sub', 'mult', or 'div'.")
