# API Signature

## LinkedList Class

`LinkedList()` - Creates a new empty linked list

### Methods

`insert(value: any, position: int = None) -> None` - Inserts a value at the specified position (or at the end if position is None)

`delete(value: any) -> bool` - Deletes the first occurrence of the value, returns True if found and deleted, False otherwise

`search(value: any) -> int` - Searches for a value and returns its index (0-based), returns -1 if not found

`get(position: int) -> any` - Returns the value at the specified position

`size() -> int` - Returns the number of elements in the list

`to_list() -> list` - Returns the linked list as a Python list
