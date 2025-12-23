"""
greet function.
"""

def greet(name="World"):
    """
    Prints a greeting message.
    
    Args:
        name (str, optional): The name to greet. Defaults to "World".
    
    Returns:
        str: The greeting message
    """
    message = f"Hello, {name}!"
    print(message)
    return message
