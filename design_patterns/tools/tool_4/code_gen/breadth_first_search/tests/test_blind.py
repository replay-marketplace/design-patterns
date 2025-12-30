import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from bfs import bfs, bfs_path

class TestBFS(unittest.TestCase):
    """Test cases for BFS graph traversal functions."""
    
    def setUp(self):
        """Set up test graphs."""
        # Simple connected graph
        self.simple_graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        
        # Disconnected graph
        self.disconnected_graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }
        
        # Single node graph
        self.single_node_graph = {
            'A': []
        }
        
        # Linear graph
        self.linear_graph = {
            1: [2],
            2: [1, 3],
            3: [2, 4],
            4: [3]
        }
    
    # Tests for bfs function
    def test_bfs_simple_graph(self):
        """Test BFS traversal on a simple connected graph."""
        result = bfs(self.simple_graph, 'A')
        self.assertIsInstance(result, list)
        self.assertEqual(result[0], 'A')  # Start node should be first
        self.assertEqual(len(result), 6)  # All nodes should be visited
        self.assertEqual(set(result), {'A', 'B', 'C', 'D', 'E', 'F'})
    
    def test_bfs_single_node(self):
        """Test BFS on a single node graph."""
        result = bfs(self.single_node_graph, 'A')
        self.assertEqual(result, ['A'])
    
    def test_bfs_linear_graph(self):
        """Test BFS on a linear graph."""
        result = bfs(self.linear_graph, 1)
        self.assertEqual(result[0], 1)
        self.assertEqual(len(result), 4)
    
    def test_bfs_disconnected_graph(self):
        """Test BFS on disconnected graph only visits reachable nodes."""
        result = bfs(self.disconnected_graph, 'A')
        self.assertEqual(set(result), {'A', 'B'})
    
    def test_bfs_returns_list(self):
        """Test that BFS returns a list."""
        result = bfs(self.simple_graph, 'A')
        self.assertIsInstance(result, list)
    
    # Tests for bfs_path function
    def test_bfs_path_direct_connection(self):
        """Test BFS path finding with directly connected nodes."""
        result = bfs_path(self.simple_graph, 'A', 'B')
        self.assertEqual(result, ['A', 'B'])
    
    def test_bfs_path_same_node(self):
        """Test BFS path when start equals end."""
        result = bfs_path(self.simple_graph, 'A', 'A')
        self.assertEqual(result, ['A'])
    
    def test_bfs_path_shortest_path(self):
        """Test that BFS finds the shortest path."""
        result = bfs_path(self.simple_graph, 'A', 'F')
        self.assertIsInstance(result, list)
        self.assertEqual(result[0], 'A')
        self.assertEqual(result[-1], 'F')
        # Shortest path from A to F is A->C->F (length 3)
        self.assertEqual(len(result), 3)
    
    def test_bfs_path_no_path_exists(self):
        """Test BFS path returns empty list when no path exists."""
        result = bfs_path(self.disconnected_graph, 'A', 'C')
        self.assertEqual(result, [])
    
    def test_bfs_path_linear_graph(self):
        """Test BFS path on linear graph."""
        result = bfs_path(self.linear_graph, 1, 4)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_bfs_path_returns_list(self):
        """Test that BFS path returns a list."""
        result = bfs_path(self.simple_graph, 'A', 'F')
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBFS)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
