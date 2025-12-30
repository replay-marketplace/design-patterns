import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.stack import Stack


class TestStack(unittest.TestCase):
    """Test cases for Stack data structure implementation."""
    
    def setUp(self):
        """Set up a fresh stack for each test."""
        self.stack = Stack()
    
    def test_new_stack_is_empty(self):
        """Test that a newly created stack is empty."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
    
    def test_push_single_item(self):
        """Test pushing a single item onto the stack."""
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)
    
    def test_push_multiple_items(self):
        """Test pushing multiple items onto the stack."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
    
    def test_pop_returns_last_pushed_item(self):
        """Test that pop returns the last pushed item (LIFO)."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
    
    def test_pop_reduces_size(self):
        """Test that pop reduces the stack size."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)
    
    def test_pop_empty_stack_raises_error(self):
        """Test that popping from empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.pop()
    
    def test_peek_returns_top_without_removing(self):
        """Test that peek returns top item without removing it."""
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.peek(), 2)
    
    def test_peek_empty_stack_raises_error(self):
        """Test that peeking at empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.peek()
    
    def test_is_empty_after_push_and_pop(self):
        """Test is_empty after pushing and popping all items."""
        self.stack.push(1)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
    
    def test_push_different_types(self):
        """Test pushing different data types onto the stack."""
        self.stack.push(1)
        self.stack.push("hello")
        self.stack.push([1, 2, 3])
        self.stack.push({"key": "value"})
        self.assertEqual(self.stack.pop(), {"key": "value"})
        self.assertEqual(self.stack.pop(), [1, 2, 3])
        self.assertEqual(self.stack.pop(), "hello")
        self.assertEqual(self.stack.pop(), 1)
    
    def test_len_method(self):
        """Test the __len__ method."""
        self.assertEqual(len(self.stack), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 2)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestStack)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')