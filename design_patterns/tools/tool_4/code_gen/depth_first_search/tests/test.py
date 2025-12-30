import unittest
import os
import sys

from src.dfs import dfs, dfs_iterative


class TestDFS(unittest.TestCase):
    """Test cases for Depth-First Search algorithm."""
    
    def setUp(self):
        """Set up test graphs."""
        # Simple linear graph
        self.linear_graph = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        
        # Tree-like graph
        self.tree_graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        
        # Graph with cycle
        self.cyclic_graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C']
        }
        
        # Single node graph
        self.single_node = {
            'A': []
        }
        
        # Disconnected graph (only reachable nodes from start)
        self.disconnected_graph = {
            'A': ['B'],
            'B': [],
            'C': ['D'],
            'D': []
        }
    
    def test_linear_graph(self):
        """Test DFS on a linear graph."""
        result = dfs(self.linear_graph, 'A')
        self.assertEqual(result, ['A', 'B', 'C'])
    
    def test_tree_graph(self):
        """Test DFS on a tree-like graph."""
        result = dfs(self.tree_graph, 'A')
        # Should visit A first, then go deep into B's subtree
        self.assertEqual(result[0], 'A')
        self.assertIn('B', result)
        self.assertIn('C', result)
        self.assertEqual(len(result), 6)
    
    def test_cyclic_graph(self):
        """Test DFS handles cycles correctly without infinite loop."""
        result = dfs(self.cyclic_graph, 'A')
        # Should visit all nodes exactly once
        self.assertEqual(len(result), 4)
        self.assertEqual(len(set(result)), 4)  # All unique
        self.assertEqual(result[0], 'A')
    
    def test_single_node(self):
        """Test DFS on a single node graph."""
        result = dfs(self.single_node, 'A')
        self.assertEqual(result, ['A'])
    
    def test_disconnected_graph(self):
        """Test DFS only visits reachable nodes."""
        result = dfs(self.disconnected_graph, 'A')
        self.assertEqual(result, ['A', 'B'])
        self.assertNotIn('C', result)
        self.assertNotIn('D', result)
    
    def test_invalid_start_node(self):
        """Test DFS raises error for invalid start node."""
        with self.assertRaises(KeyError):
            dfs(self.tree_graph, 'Z')
    
    def test_iterative_linear_graph(self):
        """Test iterative DFS on a linear graph."""
        result = dfs_iterative(self.linear_graph, 'A')
        self.assertEqual(result, ['A', 'B', 'C'])
    
    def test_iterative_cyclic_graph(self):
        """Test iterative DFS handles cycles correctly."""
        result = dfs_iterative(self.cyclic_graph, 'A')
        self.assertEqual(len(result), 4)
        self.assertEqual(len(set(result)), 4)
        self.assertEqual(result[0], 'A')
    
    def test_iterative_invalid_start(self):
        """Test iterative DFS raises error for invalid start node."""
        with self.assertRaises(KeyError):
            dfs_iterative(self.tree_graph, 'Z')
    
    def test_numeric_nodes(self):
        """Test DFS works with numeric node identifiers."""
        numeric_graph = {
            1: [2, 3],
            2: [4],
            3: [],
            4: []
        }
        result = dfs(numeric_graph, 1)
        self.assertEqual(result[0], 1)
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs('../replay', exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDFS)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
