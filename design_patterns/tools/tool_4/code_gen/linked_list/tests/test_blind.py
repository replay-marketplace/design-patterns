import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """Test cases for LinkedList class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.ll = LinkedList()
    
    def test_create_empty_linked_list(self):
        """Test creating a new empty linked list."""
        ll = LinkedList()
        self.assertEqual(ll.size(), 0)
        self.assertEqual(ll.to_list(), [])
    
    def test_insert_at_end_default(self):
        """Test inserting values at the end (default behavior)."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
        self.assertEqual(self.ll.size(), 3)
    
    def test_insert_at_position(self):
        """Test inserting values at specific positions."""
        self.ll.insert(1)
        self.ll.insert(3)
        self.ll.insert(2, 1)  # Insert 2 at position 1
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
    
    def test_insert_at_beginning(self):
        """Test inserting at position 0."""
        self.ll.insert(2)
        self.ll.insert(3)
        self.ll.insert(1, 0)  # Insert 1 at position 0
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
    
    def test_insert_at_end_with_position(self):
        """Test inserting at the end using position."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3, 2)  # Insert at position 2 (end)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
    
    def test_delete_existing_value(self):
        """Test deleting an existing value."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        result = self.ll.delete(2)
        self.assertTrue(result)
        self.assertEqual(self.ll.to_list(), [1, 3])
        self.assertEqual(self.ll.size(), 2)
    
    def test_delete_non_existing_value(self):
        """Test deleting a non-existing value."""
        self.ll.insert(1)
        self.ll.insert(2)
        result = self.ll.delete(5)
        self.assertFalse(result)
        self.assertEqual(self.ll.to_list(), [1, 2])
    
    def test_delete_first_occurrence(self):
        """Test that delete removes only the first occurrence."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(2)
        self.ll.insert(3)
        result = self.ll.delete(2)
        self.assertTrue(result)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
    
    def test_delete_from_empty_list(self):
        """Test deleting from an empty list."""
        result = self.ll.delete(1)
        self.assertFalse(result)
    
    def test_delete_head(self):
        """Test deleting the head element."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        result = self.ll.delete(1)
        self.assertTrue(result)
        self.assertEqual(self.ll.to_list(), [2, 3])
    
    def test_search_existing_value(self):
        """Test searching for an existing value."""
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        self.assertEqual(self.ll.search(10), 0)
        self.assertEqual(self.ll.search(20), 1)
        self.assertEqual(self.ll.search(30), 2)
    
    def test_search_non_existing_value(self):
        """Test searching for a non-existing value."""
        self.ll.insert(1)
        self.ll.insert(2)
        result = self.ll.search(5)
        self.assertEqual(result, -1)
    
    def test_search_empty_list(self):
        """Test searching in an empty list."""
        result = self.ll.search(1)
        self.assertEqual(result, -1)
    
    def test_get_valid_position(self):
        """Test getting value at valid positions."""
        self.ll.insert('a')
        self.ll.insert('b')
        self.ll.insert('c')
        self.assertEqual(self.ll.get(0), 'a')
        self.assertEqual(self.ll.get(1), 'b')
        self.assertEqual(self.ll.get(2), 'c')
    
    def test_size_empty_list(self):
        """Test size of empty list."""
        self.assertEqual(self.ll.size(), 0)
    
    def test_size_after_operations(self):
        """Test size after various operations."""
        self.ll.insert(1)
        self.assertEqual(self.ll.size(), 1)
        self.ll.insert(2)
        self.assertEqual(self.ll.size(), 2)
        self.ll.delete(1)
        self.assertEqual(self.ll.size(), 1)
    
    def test_to_list_empty(self):
        """Test to_list on empty linked list."""
        self.assertEqual(self.ll.to_list(), [])
    
    def test_to_list_with_elements(self):
        """Test to_list with elements."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
    
    def test_insert_various_types(self):
        """Test inserting various data types."""
        self.ll.insert(1)
        self.ll.insert('string')
        self.ll.insert([1, 2, 3])
        self.ll.insert({'key': 'value'})
        self.assertEqual(self.ll.size(), 4)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 'string')
        self.assertEqual(self.ll.get(2), [1, 2, 3])
        self.assertEqual(self.ll.get(3), {'key': 'value'})


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs('../replay', exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLinkedList)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
