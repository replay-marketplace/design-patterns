# API Signature

## HashTable Class

`HashTable(size: int = 16) -> HashTable` - Creates a new hash table with the specified initial size.

### Methods

`put(key: any, value: any) -> None` - Inserts or updates a key-value pair in the hash table.

`get(key: any) -> any` - Retrieves the value associated with the given key. Raises KeyError if key not found.

`delete(key: any) -> None` - Removes the key-value pair from the hash table. Raises KeyError if key not found.

`contains(key: any) -> bool` - Returns True if the key exists in the hash table, False otherwise.

`__len__() -> int` - Returns the number of key-value pairs in the hash table.

`keys() -> list` - Returns a list of all keys in the hash table.

`values() -> list` - Returns a list of all values in the hash table.
