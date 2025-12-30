# API Signature

`Stack()` - Creates a new empty stack instance

`push(item: any) -> None` - Pushes an item onto the top of the stack

`pop() -> any` - Removes and returns the top item from the stack. Raises IndexError if stack is empty.

`peek() -> any` - Returns the top item without removing it. Raises IndexError if stack is empty.

`is_empty() -> bool` - Returns True if the stack is empty, False otherwise.

`size() -> int` - Returns the number of items in the stack.
