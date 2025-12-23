def greet(name):
    """
    A simple greeting function.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int/float): First number.
        b (int/float): Second number.
    
    Returns:
        int/float: The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    # Example usage
    print(greet("World"))
    print(f"Sum: {add_numbers(5, 3)}")