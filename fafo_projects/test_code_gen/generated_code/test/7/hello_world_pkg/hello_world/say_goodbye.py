"""
say_goodbye function.
"""

def say_goodbye(name="World"):
    """
    Prints a goodbye message.
    
    Args:
        name (str, optional): The name to say goodbye to. Defaults to "World".
    
    Returns:
        str: The goodbye message
    """
    message = f"Goodbye, {name}!"
    print(message)
    return message
