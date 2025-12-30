"""Depth-First Search implementation for graph traversal."""


def dfs(graph: dict, start, visited: set = None) -> list:
    """
    Perform depth-first search traversal on a graph (recursive implementation).
    
    Args:
        graph: A dictionary representing an adjacency list where keys are nodes
               and values are lists of adjacent nodes.
        start: The starting node for the traversal.
        visited: Optional set to track visited nodes (used internally).
    
    Returns:
        A list of nodes in the order they were visited during DFS traversal.
    
    Raises:
        KeyError: If the start node is not in the graph.
    """
    if start not in graph:
        raise KeyError(f"Start node '{start}' not found in graph")
    
    if visited is None:
        visited = set()
    
    result = []
    
    if start not in visited:
        visited.add(start)
        result.append(start)
        
        for neighbor in graph[start]:
            if neighbor not in visited:
                result.extend(dfs(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph: dict, start) -> list:
    """
    Perform depth-first search traversal on a graph (iterative implementation).
    
    Args:
        graph: A dictionary representing an adjacency list where keys are nodes
               and values are lists of adjacent nodes.
        start: The starting node for the traversal.
    
    Returns:
        A list of nodes in the order they were visited during DFS traversal.
    
    Raises:
        KeyError: If the start node is not in the graph.
    """
    if start not in graph:
        raise KeyError(f"Start node '{start}' not found in graph")
    
    visited = set()
    result = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
