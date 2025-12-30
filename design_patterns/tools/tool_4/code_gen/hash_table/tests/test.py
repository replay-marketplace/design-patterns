import unittest
import os

from src.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    """Test cases for HashTable data structure."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.ht = HashTable()
    
    def test_put_and_get_single_item(self):
        """Test inserting and retrieving a single item."""
        self.ht.put("key1", "value1")
        self.assertEqual(self.ht.get("key1"), "value1")
    
    def test_put_and_get_multiple_items(self):
        """Test inserting and retrieving multiple items."""
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.put("c", 3)
        self.assertEqual(self.ht.get("a"), 1)
        self.assertEqual(self.ht.get("b"), 2)
        self.assertEqual(self.ht.get("c"), 3)
    
    def test_put_update_existing_key(self):
        """Test updating an existing key."""
        self.ht.put("key", "old_value")
        self.ht.put("key", "new_value")
        self.assertEqual(self.ht.get("key"), "new_value")
        self.assertEqual(len(self.ht), 1)
    
    def test_get_nonexistent_key_raises_error(self):
        """Test that getting a nonexistent key raises KeyError."""
        with self.assertRaises(KeyError):
            self.ht.get("nonexistent")
    
    def test_delete_existing_key(self):
        """Test deleting an existing key."""
        self.ht.put("key", "value")
        self.ht.delete("key")
        self.assertFalse(self.ht.contains("key"))
        self.assertEqual(len(self.ht), 0)
    
    def test_delete_nonexistent_key_raises_error(self):
        """Test that deleting a nonexistent key raises KeyError."""
        with self.assertRaises(KeyError):
            self.ht.delete("nonexistent")
    
    def test_contains_existing_key(self):
        """Test contains returns True for existing key."""
        self.ht.put("key", "value")
        self.assertTrue(self.ht.contains("key"))
    
    def test_contains_nonexistent_key(self):
        """Test contains returns False for nonexistent key."""
        self.assertFalse(self.ht.contains("nonexistent"))
    
    def test_in_operator(self):
        """Test the 'in' operator works correctly."""
        self.ht.put("key", "value")
        self.assertTrue("key" in self.ht)
        self.assertFalse("other" in self.ht)
    
    def test_len_empty_table(self):
        """Test length of empty hash table."""
        self.assertEqual(len(self.ht), 0)
    
    def test_len_after_operations(self):
        """Test length after various operations."""
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.assertEqual(len(self.ht), 2)
        self.ht.delete("a")
        self.assertEqual(len(self.ht), 1)
    
    def test_keys(self):
        """Test keys method returns all keys."""
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.put("c", 3)
        keys = self.ht.keys()
        self.assertEqual(set(keys), {"a", "b", "c"})
    
    def test_values(self):
        """Test values method returns all values."""
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.put("c", 3)
        values = self.ht.values()
        self.assertEqual(set(values), {1, 2, 3})
    
    def test_integer_keys(self):
        """Test hash table works with integer keys."""
        self.ht.put(1, "one")
        self.ht.put(2, "two")
        self.assertEqual(self.ht.get(1), "one")
        self.assertEqual(self.ht.get(2), "two")
    
    def test_collision_handling(self):
        """Test that collisions are handled correctly."""
        ht = HashTable(size=2)  # Small size to force collisions
        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)
        ht.put("d", 4)
        self.assertEqual(ht.get("a"), 1)
        self.assertEqual(ht.get("b"), 2)
        self.assertEqual(ht.get("c"), 3)
        self.assertEqual(ht.get("d"), 4)
    
    def test_resize_on_load_factor(self):
        """Test that hash table resizes when load factor is exceeded."""
        ht = HashTable(size=4)
        for i in range(10):
            ht.put(f"key{i}", i)
        for i in range(10):
            self.assertEqual(ht.get(f"key{i}"), i)
    
    def test_delete_and_reinsert(self):
        """Test deleting and reinserting the same key."""
        self.ht.put("key", "value1")
        self.ht.delete("key")
        self.ht.put("key", "value2")
        self.assertEqual(self.ht.get("key"), "value2")
    
    def test_none_as_value(self):
        """Test that None can be stored as a value."""
        self.ht.put("key", None)
        self.assertIsNone(self.ht.get("key"))
        self.assertTrue(self.ht.contains("key"))


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs('../replay', exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHashTable)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')