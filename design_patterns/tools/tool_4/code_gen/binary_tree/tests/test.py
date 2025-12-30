import unittest
import os

from src.binary_tree import BinaryTree, TreeNode


class TestBinaryTree(unittest.TestCase):
    """Test cases for BinaryTree data structure."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.tree = BinaryTree()
    
    def test_empty_tree(self):
        """Test that a new tree is empty."""
        self.assertIsNone(self.tree.root)
        self.assertEqual(self.tree.inorder_traversal(), [])
    
    def test_insert_single(self):
        """Test inserting a single value."""
        self.tree.insert(10)
        self.assertIsNotNone(self.tree.root)
        self.assertEqual(self.tree.root.value, 10)
    
    def test_insert_multiple(self):
        """Test inserting multiple values."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.tree.insert(v)
        self.assertEqual(self.tree.root.value, 50)
        self.assertEqual(self.tree.root.left.value, 30)
        self.assertEqual(self.tree.root.right.value, 70)
    
    def test_search_existing(self):
        """Test searching for existing values."""
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.tree.insert(v)
        for v in values:
            self.assertTrue(self.tree.search(v))
    
    def test_search_nonexisting(self):
        """Test searching for non-existing values."""
        values = [50, 30, 70]
        for v in values:
            self.tree.insert(v)
        self.assertFalse(self.tree.search(100))
        self.assertFalse(self.tree.search(25))
    
    def test_search_empty_tree(self):
        """Test searching in an empty tree."""
        self.assertFalse(self.tree.search(10))
    
    def test_inorder_traversal(self):
        """Test inorder traversal returns sorted values."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.tree.insert(v)
        expected = [20, 30, 40, 50, 60, 70, 80]
        self.assertEqual(self.tree.inorder_traversal(), expected)
    
    def test_preorder_traversal(self):
        """Test preorder traversal."""
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.tree.insert(v)
        expected = [50, 30, 20, 40, 70]
        self.assertEqual(self.tree.preorder_traversal(), expected)
    
    def test_postorder_traversal(self):
        """Test postorder traversal."""
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.tree.insert(v)
        expected = [20, 40, 30, 70, 50]
        self.assertEqual(self.tree.postorder_traversal(), expected)
    
    def test_tree_node_creation(self):
        """Test TreeNode creation."""
        node = TreeNode(42)
        self.assertEqual(node.value, 42)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBinaryTree)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')