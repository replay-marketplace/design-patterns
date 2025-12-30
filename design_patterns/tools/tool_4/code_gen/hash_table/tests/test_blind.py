import unittest
import sys
import os

# Import the HashTable class from the parent directory
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    """Test cases for HashTable class based on API signature."""
    
    def test_create_hash_table_default_size(self):
        """Test creating a hash table with default size."""
        ht = HashTable()
        self.assertIsInstance(ht, HashTable)
        self.assertEqual(len(ht), 0)
    
    def test_create_hash_table_custom_size(self):
        """Test creating a hash table with custom size."""
        ht = HashTable(size=32)
        self.assertIsInstance(ht, HashTable)
        self.assertEqual(len(ht), 0)
    
    def test_put_and_get_single_item(self):
        """Test inserting and retrieving a single key-value pair."""
        ht = HashTable()
        ht.put("key1", "value1")
        self.assertEqual(ht.get("key1"), "value1")
    
    def test_put_and_get_multiple_items(self):
        """Test inserting and retrieving multiple key-value pairs."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.put("key2", "value2")
        ht.put("key3", "value3")
        self.assertEqual(ht.get("key1"), "value1")
        self.assertEqual(ht.get("key2"), "value2")
        self.assertEqual(ht.get("key3"), "value3")
    
    def test_put_update_existing_key(self):
        """Test updating an existing key's value."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.put("key1", "updated_value")
        self.assertEqual(ht.get("key1"), "updated_value")
    
    def test_get_nonexistent_key_raises_keyerror(self):
        """Test that getting a nonexistent key raises KeyError."""
        ht = HashTable()
        with self.assertRaises(KeyError):
            ht.get("nonexistent")
    
    def test_delete_existing_key(self):
        """Test deleting an existing key."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.delete("key1")
        self.assertFalse(ht.contains("key1"))
    
    def test_delete_nonexistent_key_raises_keyerror(self):
        """Test that deleting a nonexistent key raises KeyError."""
        ht = HashTable()
        with self.assertRaises(KeyError):
            ht.delete("nonexistent")
    
    def test_contains_existing_key(self):
        """Test contains returns True for existing key."""
        ht = HashTable()
        ht.put("key1", "value1")
        self.assertTrue(ht.contains("key1"))
    
    def test_contains_nonexistent_key(self):
        """Test contains returns False for nonexistent key."""
        ht = HashTable()
        self.assertFalse(ht.contains("nonexistent"))
    
    def test_len_empty_table(self):
        """Test length of empty hash table."""
        ht = HashTable()
        self.assertEqual(len(ht), 0)
    
    def test_len_after_insertions(self):
        """Test length after inserting items."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.put("key2", "value2")
        ht.put("key3", "value3")
        self.assertEqual(len(ht), 3)
    
    def test_len_after_deletion(self):
        """Test length after deleting an item."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.put("key2", "value2")
        ht.delete("key1")
        self.assertEqual(len(ht), 1)
    
    def test_len_after_update(self):
        """Test length doesn't change after updating existing key."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.put("key1", "updated_value")
        self.assertEqual(len(ht), 1)
    
    def test_keys_empty_table(self):
        """Test keys returns empty list for empty table."""
        ht = HashTable()
        self.assertEqual(ht.keys(), [])
    
    def test_keys_with_items(self):
        """Test keys returns all keys."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.put("key2", "value2")
        ht.put("key3", "value3")
        keys = ht.keys()
        self.assertEqual(len(keys), 3)
        self.assertIn("key1", keys)
        self.assertIn("key2", keys)
        self.assertIn("key3", keys)
    
    def test_values_empty_table(self):
        """Test values returns empty list for empty table."""
        ht = HashTable()
        self.assertEqual(ht.values(), [])
    
    def test_values_with_items(self):
        """Test values returns all values."""
        ht = HashTable()
        ht.put("key1", "value1")
        ht.put("key2", "value2")
        ht.put("key3", "value3")
        values = ht.values()
        self.assertEqual(len(values), 3)
        self.assertIn("value1", values)
        self.assertIn("value2", values)
        self.assertIn("value3", values)
    
    def test_different_key_types(self):
        """Test hash table works with different key types."""
        ht = HashTable()
        ht.put("string_key", "value1")
        ht.put(123, "value2")
        ht.put((1, 2), "value3")
        self.assertEqual(ht.get("string_key"), "value1")
        self.assertEqual(ht.get(123), "value2")
        self.assertEqual(ht.get((1, 2)), "value3")
    
    def test_different_value_types(self):
        """Test hash table works with different value types."""
        ht = HashTable()
        ht.put("key1", "string_value")
        ht.put("key2", 123)
        ht.put("key3", [1, 2, 3])
        ht.put("key4", {"nested": "dict"})
        self.assertEqual(ht.get("key1"), "string_value")
        self.assertEqual(ht.get("key2"), 123)
        self.assertEqual(ht.get("key3"), [1, 2, 3])
        self.assertEqual(ht.get("key4"), {"nested": "dict"})


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHashTable)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Ensure replay directory exists
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'replay')
    os.makedirs(replay_dir, exist_ok=True)
    
    # Write test result to file
    with open(os.path.join(replay_dir, 'test_blind_bool.txt'), 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
