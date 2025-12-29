def calculator(num1: float, num2: float, operation: str) -> float:
    """
    Perform arithmetic operation on two numbers.
    
    Args:
        num1: First number.
        num2: Second number.
        operation: Operation string: 'add', 'sub', 'mult', 'div'.
    
    Returns:
        Result of the operation as float.
    
    Raises:
        ValueError: If operation is invalid or division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mult':
        return num1 * num2
    elif operation == 'div':
        if num2 == 0:
            raise ValueError('Division by zero')
        return num1 / num2
    else:
        raise ValueError('Invalid operation')
