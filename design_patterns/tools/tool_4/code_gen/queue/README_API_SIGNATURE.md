# API Signature

`Queue()` - Creates a new empty queue instance

`enqueue(item: any) -> None` - Adds an item to the back of the queue

`dequeue() -> any` - Removes and returns the item from the front of the queue. Raises IndexError if queue is empty.

`front() -> any` - Returns the item at the front of the queue without removing it. Raises IndexError if queue is empty.

`is_empty() -> bool` - Returns True if the queue is empty, False otherwise

`size() -> int` - Returns the number of items in the queue
