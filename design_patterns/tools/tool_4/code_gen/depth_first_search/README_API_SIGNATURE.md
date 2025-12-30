# API Signature

`dfs(graph: dict, start: any, visited: set = None) -> list` - Performs depth-first search traversal on a graph represented as an adjacency list. Returns a list of nodes in the order they were visited.

## Parameters
- `graph`: A dictionary where keys are node identifiers and values are lists of adjacent nodes
- `start`: The starting node for the traversal
- `visited`: Optional set to track visited nodes (used internally for recursion)

## Returns
- `list`: A list of nodes in DFS traversal order

## Example
```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
result = dfs(graph, 'A')  # Returns ['A', 'B', 'D', 'E', 'F', 'C']
```
