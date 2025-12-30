import unittest
import os

from src.linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    """Test cases for LinkedList data structure."""
    
    def setUp(self):
        """Set up a fresh linked list for each test."""
        self.ll = LinkedList()
    
    def test_empty_list(self):
        """Test that a new list is empty."""
        self.assertEqual(self.ll.size(), 0)
        self.assertEqual(self.ll.to_list(), [])
    
    def test_insert_at_end(self):
        """Test inserting elements at the end."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
        self.assertEqual(self.ll.size(), 3)
    
    def test_insert_at_beginning(self):
        """Test inserting elements at the beginning."""
        self.ll.insert(1)
        self.ll.insert(2, 0)
        self.ll.insert(3, 0)
        self.assertEqual(self.ll.to_list(), [3, 2, 1])
    
    def test_insert_at_middle(self):
        """Test inserting elements in the middle."""
        self.ll.insert(1)
        self.ll.insert(3)
        self.ll.insert(2, 1)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
    
    def test_insert_invalid_position(self):
        """Test inserting at invalid position raises error."""
        with self.assertRaises(IndexError):
            self.ll.insert(1, 5)
        with self.assertRaises(IndexError):
            self.ll.insert(1, -1)
    
    def test_delete_from_beginning(self):
        """Test deleting from the beginning."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        result = self.ll.delete(1)
        self.assertTrue(result)
        self.assertEqual(self.ll.to_list(), [2, 3])
    
    def test_delete_from_middle(self):
        """Test deleting from the middle."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        result = self.ll.delete(2)
        self.assertTrue(result)
        self.assertEqual(self.ll.to_list(), [1, 3])
    
    def test_delete_from_end(self):
        """Test deleting from the end."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        result = self.ll.delete(3)
        self.assertTrue(result)
        self.assertEqual(self.ll.to_list(), [1, 2])
    
    def test_delete_nonexistent(self):
        """Test deleting a value that doesn't exist."""
        self.ll.insert(1)
        self.ll.insert(2)
        result = self.ll.delete(5)
        self.assertFalse(result)
        self.assertEqual(self.ll.to_list(), [1, 2])
    
    def test_delete_from_empty(self):
        """Test deleting from an empty list."""
        result = self.ll.delete(1)
        self.assertFalse(result)
    
    def test_search_found(self):
        """Test searching for existing values."""
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        self.assertEqual(self.ll.search(10), 0)
        self.assertEqual(self.ll.search(20), 1)
        self.assertEqual(self.ll.search(30), 2)
    
    def test_search_not_found(self):
        """Test searching for non-existing values."""
        self.ll.insert(1)
        self.ll.insert(2)
        self.assertEqual(self.ll.search(5), -1)
    
    def test_search_empty_list(self):
        """Test searching in an empty list."""
        self.assertEqual(self.ll.search(1), -1)
    
    def test_get_valid_position(self):
        """Test getting values at valid positions."""
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        self.assertEqual(self.ll.get(0), 10)
        self.assertEqual(self.ll.get(1), 20)
        self.assertEqual(self.ll.get(2), 30)
    
    def test_get_invalid_position(self):
        """Test getting values at invalid positions."""
        self.ll.insert(1)
        with self.assertRaises(IndexError):
            self.ll.get(5)
        with self.assertRaises(IndexError):
            self.ll.get(-1)
    
    def test_len_method(self):
        """Test the __len__ method."""
        self.assertEqual(len(self.ll), 0)
        self.ll.insert(1)
        self.assertEqual(len(self.ll), 1)
        self.ll.insert(2)
        self.assertEqual(len(self.ll), 2)
    
    def test_with_strings(self):
        """Test linked list with string values."""
        self.ll.insert("hello")
        self.ll.insert("world")
        self.assertEqual(self.ll.search("hello"), 0)
        self.assertEqual(self.ll.search("world"), 1)
        self.assertTrue(self.ll.delete("hello"))
        self.assertEqual(self.ll.to_list(), ["world"])


class TestNode(unittest.TestCase):
    """Test cases for Node class."""
    
    def test_node_creation(self):
        """Test creating a node."""
        node = Node(42)
        self.assertEqual(node.value, 42)
        self.assertIsNone(node.next)
    
    def test_node_linking(self):
        """Test linking nodes together."""
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        self.assertEqual(node1.next.value, 2)


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs('../replay', exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestLinkedList))
    suite.addTests(loader.loadTestsFromTestCase(TestNode))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')