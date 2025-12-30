class HashTable:
    """A hash table implementation using separate chaining for collision resolution."""
    
    def __init__(self, size: int = 16):
        """Initialize the hash table with the given size.
        
        Args:
            size: Initial number of buckets (default 16)
        """
        self._size = size
        self._buckets = [[] for _ in range(size)]
        self._count = 0
        self._load_factor_threshold = 0.75
    
    def _hash(self, key) -> int:
        """Compute the hash index for a given key.
        
        Args:
            key: The key to hash
            
        Returns:
            The bucket index for this key
        """
        return hash(key) % self._size
    
    def _resize(self):
        """Resize the hash table when load factor exceeds threshold."""
        old_buckets = self._buckets
        self._size *= 2
        self._buckets = [[] for _ in range(self._size)]
        self._count = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def put(self, key, value) -> None:
        """Insert or update a key-value pair.
        
        Args:
            key: The key to insert/update
            value: The value to associate with the key
        """
        if self._count / self._size >= self._load_factor_threshold:
            self._resize()
        
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self._count += 1
    
    def get(self, key):
        """Retrieve the value for a given key.
        
        Args:
            key: The key to look up
            
        Returns:
            The value associated with the key
            
        Raises:
            KeyError: If the key is not found
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key not found: {key}")
    
    def delete(self, key) -> None:
        """Remove a key-value pair from the hash table.
        
        Args:
            key: The key to remove
            
        Raises:
            KeyError: If the key is not found
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return
        
        raise KeyError(f"Key not found: {key}")
    
    def contains(self, key) -> bool:
        """Check if a key exists in the hash table.
        
        Args:
            key: The key to check
            
        Returns:
            True if the key exists, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def __len__(self) -> int:
        """Return the number of key-value pairs."""
        return self._count
    
    def __contains__(self, key) -> bool:
        """Support 'in' operator."""
        return self.contains(key)
    
    def keys(self) -> list:
        """Return a list of all keys."""
        result = []
        for bucket in self._buckets:
            for k, v in bucket:
                result.append(k)
        return result
    
    def values(self) -> list:
        """Return a list of all values."""
        result = []
        for bucket in self._buckets:
            for k, v in bucket:
                result.append(v)
        return result
    
    def items(self) -> list:
        """Return a list of all key-value pairs."""
        result = []
        for bucket in self._buckets:
            for k, v in bucket:
                result.append((k, v))
        return result
    
    def __repr__(self) -> str:
        """Return string representation of the hash table."""
        items = [f"{k!r}: {v!r}" for k, v in self.items()]
        return "HashTable({" + ", ".join(items) + "})"
