import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    """Test cases for Queue implementation."""
    
    def test_create_empty_queue(self):
        """Test creating a new empty queue."""
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)
    
    def test_enqueue_single_item(self):
        """Test enqueuing a single item."""
        q = Queue()
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 1)
    
    def test_enqueue_multiple_items(self):
        """Test enqueuing multiple items."""
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.size(), 3)
    
    def test_dequeue_single_item(self):
        """Test dequeuing a single item."""
        q = Queue()
        q.enqueue(42)
        result = q.dequeue()
        self.assertEqual(result, 42)
        self.assertTrue(q.is_empty())
    
    def test_dequeue_fifo_order(self):
        """Test that dequeue follows FIFO order."""
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
    
    def test_dequeue_empty_queue_raises_error(self):
        """Test that dequeue on empty queue raises IndexError."""
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()
    
    def test_front_returns_first_item(self):
        """Test that front returns the first item without removing it."""
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        result = q.front()
        self.assertEqual(result, 1)
        self.assertEqual(q.size(), 2)
    
    def test_front_empty_queue_raises_error(self):
        """Test that front on empty queue raises IndexError."""
        q = Queue()
        with self.assertRaises(IndexError):
            q.front()
    
    def test_is_empty_on_empty_queue(self):
        """Test is_empty returns True for empty queue."""
        q = Queue()
        self.assertTrue(q.is_empty())
    
    def test_is_empty_on_non_empty_queue(self):
        """Test is_empty returns False for non-empty queue."""
        q = Queue()
        q.enqueue(1)
        self.assertFalse(q.is_empty())
    
    def test_size_empty_queue(self):
        """Test size returns 0 for empty queue."""
        q = Queue()
        self.assertEqual(q.size(), 0)
    
    def test_size_after_operations(self):
        """Test size after various operations."""
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.enqueue(3)
        self.assertEqual(q.size(), 2)
    
    def test_enqueue_different_types(self):
        """Test enqueuing different types of items."""
        q = Queue()
        q.enqueue(1)
        q.enqueue("string")
        q.enqueue([1, 2, 3])
        q.enqueue({"key": "value"})
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), "string")
        self.assertEqual(q.dequeue(), [1, 2, 3])
        self.assertEqual(q.dequeue(), {"key": "value"})

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestQueue)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    import os
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
