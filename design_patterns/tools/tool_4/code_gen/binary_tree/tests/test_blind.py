import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the classes from the main module
from binary_tree import BinaryTree, TreeNode


class TestTreeNode(unittest.TestCase):
    """Test cases for TreeNode class."""
    
    def test_create_node(self):
        """Test creating a TreeNode with a value."""
        node = TreeNode(5)
        self.assertEqual(node.value, 5)
    
    def test_node_has_left_right_attributes(self):
        """Test that TreeNode has left and right attributes."""
        node = TreeNode(10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


class TestBinaryTree(unittest.TestCase):
    """Test cases for BinaryTree class."""
    
    def test_create_empty_tree(self):
        """Test creating an empty binary tree."""
        tree = BinaryTree()
        self.assertIsNotNone(tree)
    
    def test_insert_single_value(self):
        """Test inserting a single value into the tree."""
        tree = BinaryTree()
        tree.insert(5)
        self.assertTrue(tree.search(5))
    
    def test_insert_multiple_values(self):
        """Test inserting multiple values into the tree."""
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(3))
        self.assertTrue(tree.search(7))
    
    def test_search_existing_value(self):
        """Test searching for an existing value returns True."""
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(15))
    
    def test_search_non_existing_value(self):
        """Test searching for a non-existing value returns False."""
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        self.assertFalse(tree.search(100))
        self.assertFalse(tree.search(1))
    
    def test_search_empty_tree(self):
        """Test searching in an empty tree returns False."""
        tree = BinaryTree()
        self.assertFalse(tree.search(5))
    
    def test_inorder_traversal(self):
        """Test inorder traversal returns values in left, root, right order."""
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(1)
        tree.insert(4)
        result = tree.inorder_traversal()
        self.assertEqual(result, [1, 3, 4, 5, 7])
    
    def test_inorder_traversal_empty_tree(self):
        """Test inorder traversal on empty tree returns empty list."""
        tree = BinaryTree()
        result = tree.inorder_traversal()
        self.assertEqual(result, [])
    
    def test_preorder_traversal(self):
        """Test preorder traversal returns values in root, left, right order."""
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(1)
        tree.insert(4)
        result = tree.preorder_traversal()
        self.assertEqual(result, [5, 3, 1, 4, 7])
    
    def test_preorder_traversal_empty_tree(self):
        """Test preorder traversal on empty tree returns empty list."""
        tree = BinaryTree()
        result = tree.preorder_traversal()
        self.assertEqual(result, [])
    
    def test_postorder_traversal(self):
        """Test postorder traversal returns values in left, right, root order."""
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(1)
        tree.insert(4)
        result = tree.postorder_traversal()
        self.assertEqual(result, [1, 4, 3, 7, 5])
    
    def test_postorder_traversal_empty_tree(self):
        """Test postorder traversal on empty tree returns empty list."""
        tree = BinaryTree()
        result = tree.postorder_traversal()
        self.assertEqual(result, [])
    
    def test_insert_returns_none(self):
        """Test that insert method returns None."""
        tree = BinaryTree()
        result = tree.insert(5)
        self.assertIsNone(result)
    
    def test_traversal_returns_list_of_int(self):
        """Test that traversal methods return list of integers."""
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        
        inorder = tree.inorder_traversal()
        preorder = tree.preorder_traversal()
        postorder = tree.postorder_traversal()
        
        self.assertIsInstance(inorder, list)
        self.assertIsInstance(preorder, list)
        self.assertIsInstance(postorder, list)
        
        for val in inorder:
            self.assertIsInstance(val, int)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestTreeNode))
    suite.addTests(loader.loadTestsFromTestCase(TestBinaryTree))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Ensure replay directory exists
    os.makedirs('../replay', exist_ok=True)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
