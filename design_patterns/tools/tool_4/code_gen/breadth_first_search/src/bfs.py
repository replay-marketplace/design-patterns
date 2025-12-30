"""Breadth-First Search implementation for graph traversal."""

from collections import deque
from typing import Any, Dict, List, Optional


def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform breadth-first search traversal on a graph.
    
    Args:
        graph: Adjacency list representation of the graph.
                Keys are nodes, values are lists of neighboring nodes.
        start: The starting node for traversal.
    
    Returns:
        List of nodes in BFS traversal order.
    
    Raises:
        ValueError: If start node is not in the graph.
    """
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")
    
    visited = set()
    result = []
    queue = deque([start])
    
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_path(graph: Dict[Any, List[Any]], start: Any, end: Any) -> List[Any]:
    """
    Find the shortest path between two nodes using BFS.
    
    Args:
        graph: Adjacency list representation of the graph.
        start: The starting node.
        end: The target node.
    
    Returns:
        List representing the shortest path from start to end.
        Returns empty list if no path exists.
    
    Raises:
        ValueError: If start or end node is not in the graph.
    """
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")
    if end not in graph:
        raise ValueError(f"End node '{end}' not found in graph")
    
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                
                if neighbor == end:
                    return new_path
                
                visited.add(neighbor)
                queue.append((neighbor, new_path))
    
    return []
