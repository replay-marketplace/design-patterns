import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from solution import dfs


class TestDFS(unittest.TestCase):
    """Test cases for DFS (Depth-First Search) traversal function."""
    
    def test_example_from_readme(self):
        """Test the example provided in the API signature documentation."""
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        result = dfs(graph, 'A')
        self.assertEqual(result, ['A', 'B', 'D', 'E', 'F', 'C'])
    
    def test_single_node_graph(self):
        """Test DFS on a graph with a single node."""
        graph = {'A': []}
        result = dfs(graph, 'A')
        self.assertEqual(result, ['A'])
    
    def test_linear_graph(self):
        """Test DFS on a linear graph (chain)."""
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['D'],
            'D': []
        }
        result = dfs(graph, 'A')
        self.assertEqual(result, ['A', 'B', 'C', 'D'])
    
    def test_disconnected_start(self):
        """Test DFS starting from a node with no neighbors."""
        graph = {
            'A': [],
            'B': ['C'],
            'C': []
        }
        result = dfs(graph, 'A')
        self.assertEqual(result, ['A'])
    
    def test_numeric_nodes(self):
        """Test DFS with numeric node identifiers."""
        graph = {
            1: [2, 3],
            2: [4],
            3: [],
            4: []
        }
        result = dfs(graph, 1)
        self.assertEqual(result, [1, 2, 4, 3])
    
    def test_graph_with_cycle(self):
        """Test DFS on a graph with cycles (should not revisit nodes)."""
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']  # Cycle back to A
        }
        result = dfs(graph, 'A')
        self.assertEqual(result, ['A', 'B', 'C'])
    
    def test_fully_connected_graph(self):
        """Test DFS on a fully connected graph."""
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B']
        }
        result = dfs(graph, 'A')
        # Should visit all nodes exactly once
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], 'A')
        self.assertIn('B', result)
        self.assertIn('C', result)
    
    def test_returns_list(self):
        """Test that DFS returns a list type."""
        graph = {'A': ['B'], 'B': []}
        result = dfs(graph, 'A')
        self.assertIsInstance(result, list)
    
    def test_with_provided_visited_set(self):
        """Test DFS with a pre-populated visited set."""
        graph = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': [],
            'D': []
        }
        visited = {'B'}  # B is already visited
        result = dfs(graph, 'A', visited)
        # Should skip B and its subtree
        self.assertIn('A', result)
        self.assertNotIn('B', result)
        self.assertNotIn('D', result)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDFS)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Ensure replay directory exists
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'replay')
    os.makedirs(replay_dir, exist_ok=True)
    
    # Write test result to file
    with open(os.path.join(replay_dir, 'test_blind_bool.txt'), 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
