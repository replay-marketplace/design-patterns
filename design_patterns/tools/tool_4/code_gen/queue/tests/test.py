import unittest
import os

from src.queue import Queue


class TestQueue(unittest.TestCase):
    """Test cases for Queue data structure."""
    
    def setUp(self):
        """Set up a fresh queue for each test."""
        self.queue = Queue()
    
    def test_new_queue_is_empty(self):
        """Test that a new queue is empty."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
    
    def test_enqueue_single_item(self):
        """Test enqueuing a single item."""
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)
    
    def test_enqueue_multiple_items(self):
        """Test enqueuing multiple items."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)
    
    def test_dequeue_returns_first_item(self):
        """Test that dequeue returns the first item added (FIFO)."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
    
    def test_dequeue_empty_queue_raises_error(self):
        """Test that dequeue on empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()
    
    def test_front_returns_first_item_without_removing(self):
        """Test that front returns first item without removing it."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.front(), 1)
    
    def test_front_empty_queue_raises_error(self):
        """Test that front on empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.front()
    
    def test_size_after_operations(self):
        """Test size is correct after various operations."""
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)
    
    def test_len_method(self):
        """Test __len__ method works correctly."""
        self.assertEqual(len(self.queue), 0)
        self.queue.enqueue(1)
        self.assertEqual(len(self.queue), 1)
    
    def test_enqueue_different_types(self):
        """Test enqueuing different data types."""
        self.queue.enqueue(1)
        self.queue.enqueue("string")
        self.queue.enqueue([1, 2, 3])
        self.queue.enqueue({"key": "value"})
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), "string")
        self.assertEqual(self.queue.dequeue(), [1, 2, 3])
        self.assertEqual(self.queue.dequeue(), {"key": "value"})


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs('../replay', exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestQueue)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')