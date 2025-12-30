class Node:
    """A node in the linked list."""
    
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A singly linked list implementation with insert, delete, and search operations."""
    
    def __init__(self):
        self.head = None
        self._size = 0
    
    def insert(self, value, position=None):
        """Insert a value at the specified position (or at the end if position is None)."""
        new_node = Node(value)
        
        if position is None:
            position = self._size
        
        if position < 0 or position > self._size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self._size}")
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        self._size += 1
    
    def delete(self, value):
        """Delete the first occurrence of the value. Returns True if found and deleted."""
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, value):
        """Search for a value and return its index (0-based). Returns -1 if not found."""
        current = self.head
        index = 0
        
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, position):
        """Return the value at the specified position."""
        if position < 0 or position >= self._size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self._size}")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.value
    
    def size(self):
        """Return the number of elements in the list."""
        return self._size
    
    def to_list(self):
        """Return the linked list as a Python list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"LinkedList({self.to_list()})"
