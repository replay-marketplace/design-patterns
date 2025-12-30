import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.bfs import bfs, bfs_path


class TestBFS(unittest.TestCase):
    """Test cases for BFS graph traversal algorithm."""
    
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
        self.single_node = {
            'A': []
        }
        
        # Numeric nodes
        self.numeric_graph = {
            1: [2, 3],
            2: [1, 4],
            3: [1, 4],
            4: [2, 3]
        }
    
    def test_bfs_simple_graph(self):
        """Test BFS traversal on a simple connected graph."""
        result = bfs(self.simple_graph, 'A')
        self.assertEqual(result[0], 'A')
        self.assertEqual(len(result), 6)
        # B and C should come before D, E, F
        self.assertIn('B', result[1:3])
        self.assertIn('C', result[1:3])
    
    def test_bfs_visits_all_reachable(self):
        """Test that BFS visits all reachable nodes."""
        result = bfs(self.simple_graph, 'A')
        self.assertEqual(set(result), {'A', 'B', 'C', 'D', 'E', 'F'})
    
    def test_bfs_disconnected_graph(self):
        """Test BFS on disconnected graph only visits reachable nodes."""
        result = bfs(self.disconnected_graph, 'A')
        self.assertEqual(set(result), {'A', 'B'})
    
    def test_bfs_single_node(self):
        """Test BFS on single node graph."""
        result = bfs(self.single_node, 'A')
        self.assertEqual(result, ['A'])
    
    def test_bfs_numeric_nodes(self):
        """Test BFS with numeric node identifiers."""
        result = bfs(self.numeric_graph, 1)
        self.assertEqual(result[0], 1)
        self.assertEqual(len(result), 4)
    
    def test_bfs_invalid_start(self):
        """Test BFS raises error for invalid start node."""
        with self.assertRaises(ValueError):
            bfs(self.simple_graph, 'Z')
    
    def test_bfs_path_simple(self):
        """Test finding shortest path between two nodes."""
        path = bfs_path(self.simple_graph, 'A', 'F')
        self.assertEqual(path[0], 'A')
        self.assertEqual(path[-1], 'F')
        self.assertEqual(len(path), 3)  # A -> C -> F
    
    def test_bfs_path_same_node(self):
        """Test path when start equals end."""
        path = bfs_path(self.simple_graph, 'A', 'A')
        self.assertEqual(path, ['A'])
    
    def test_bfs_path_no_path(self):
        """Test path returns empty list when no path exists."""
        path = bfs_path(self.disconnected_graph, 'A', 'C')
        self.assertEqual(path, [])
    
    def test_bfs_path_direct_neighbor(self):
        """Test path to direct neighbor."""
        path = bfs_path(self.simple_graph, 'A', 'B')
        self.assertEqual(path, ['A', 'B'])
    
    def test_bfs_path_invalid_start(self):
        """Test path raises error for invalid start node."""
        with self.assertRaises(ValueError):
            bfs_path(self.simple_graph, 'Z', 'A')
    
    def test_bfs_path_invalid_end(self):
        """Test path raises error for invalid end node."""
        with self.assertRaises(ValueError):
            bfs_path(self.simple_graph, 'A', 'Z')


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBFS)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
