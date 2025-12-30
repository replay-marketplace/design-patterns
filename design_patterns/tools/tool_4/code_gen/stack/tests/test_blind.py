import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stack import Stack


class TestStack(unittest.TestCase):
    """Test cases for Stack class based on API signature."""
    
    def setUp(self):
        """Set up a fresh stack for each test."""
        self.stack = Stack()
    
    def test_create_empty_stack(self):
        """Test that a new stack is created empty."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
    
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
    
    def test_push_various_types(self):
        """Test pushing various types of items."""
        self.stack.push(42)
        self.stack.push("string")
        self.stack.push([1, 2, 3])
        self.stack.push({"key": "value"})
        self.stack.push(None)
        self.assertEqual(self.stack.size(), 5)
    
    def test_pop_returns_top_item(self):
        """Test that pop returns the top item."""
        self.stack.push(1)
        self.stack.push(2)
        result = self.stack.pop()
        self.assertEqual(result, 2)
    
    def test_pop_removes_item(self):
        """Test that pop removes the item from stack."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)
    
    def test_pop_empty_stack_raises_index_error(self):
        """Test that pop raises IndexError on empty stack."""
        with self.assertRaises(IndexError):
            self.stack.pop()
    
    def test_peek_returns_top_item(self):
        """Test that peek returns the top item."""
        self.stack.push(1)
        self.stack.push(2)
        result = self.stack.peek()
        self.assertEqual(result, 2)
    
    def test_peek_does_not_remove_item(self):
        """Test that peek does not remove the item."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.peek()
        self.assertEqual(self.stack.size(), 2)
    
    def test_peek_empty_stack_raises_index_error(self):
        """Test that peek raises IndexError on empty stack."""
        with self.assertRaises(IndexError):
            self.stack.peek()
    
    def test_is_empty_on_new_stack(self):
        """Test is_empty returns True for new stack."""
        self.assertTrue(self.stack.is_empty())
    
    def test_is_empty_after_push(self):
        """Test is_empty returns False after push."""
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
    
    def test_is_empty_after_push_and_pop(self):
        """Test is_empty returns True after pushing and popping all items."""
        self.stack.push(1)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
    
    def test_size_on_new_stack(self):
        """Test size returns 0 for new stack."""
        self.assertEqual(self.stack.size(), 0)
    
    def test_size_after_pushes(self):
        """Test size returns correct count after pushes."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
    
    def test_size_after_push_and_pop(self):
        """Test size returns correct count after push and pop."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)
    
    def test_lifo_order(self):
        """Test that stack follows LIFO order."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestStack)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
