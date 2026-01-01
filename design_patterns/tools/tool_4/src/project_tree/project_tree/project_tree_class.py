"""Project tree implementation with ProjectNode and ProjectTree classes."""

from dataclasses import dataclass, field
from typing import List, Optional, Dict

# Try importing DirTree with different paths to handle different execution contexts
try:
    from dir_tree.dir_tree import DirTree
except ImportError:
    from src.dir_tree.dir_tree import DirTree


@dataclass
class ProjectNode:
    """Node representing a project in the project tree."""
    name: str
    dir: str = ""
    dependencies: List['ProjectNode'] = field(default_factory=list)
    apis: List[str] = field(default_factory=list)
    prompt: str = ""


class ProjectTree:
    """Project tree class that holds a simple tree of projects with dependencies."""
    
    def __init__(self, name: str = "", dir_tree: Optional[DirTree] = None, 
                 prompt: str = "", functions: List[str] = None):
        """Initialize ProjectTree with name, dir_tree, prompt, and functions.
        
        Args:
            name: Name of the project tree
            dir_tree: DirTree instance (default: creates new DirTree)
            prompt: Prompt string
            functions: List of function names (default: empty list)
        """
        self.name = name
        self.dir_tree = dir_tree if dir_tree is not None else DirTree()
        self.prompt = prompt
        self.functions = functions if functions is not None else []
        
        # Dictionary to store nodes by name for quick lookup
        self._nodes: Dict[str, ProjectNode] = {}
    
    def add_node(self, name: str, dir: str = "", dependencies: List[str] = None, prompt: str = "", apis: List[str] = None) -> ProjectNode:
        """Add a new project node to the tree.
        
        Args:
            name: Name of the project node
            dir: Directory path for the project node (default: empty string)
            dependencies: List of project names that this node depends on
            prompt: Prompt string for the project node (default: empty string)
            apis: List of API signatures for the project node (default: empty list)
            
        Returns:
            The created ProjectNode
            
        Raises:
            ValueError: If a node with the same name already exists
            ValueError: If any dependency name doesn't exist in the tree
        """
        if name in self._nodes:
            raise ValueError(f"Node with name '{name}' already exists")
        
        # Create the new node
        node = ProjectNode(name=name, dir=dir, prompt=prompt, apis=apis if apis is not None else [])
        
        # Resolve dependencies if provided
        if dependencies:
            for dep_name in dependencies:
                if dep_name not in self._nodes:
                    raise ValueError(f"Dependency '{dep_name}' does not exist in the tree")
                node.dependencies.append(self._nodes[dep_name])
        
        # Store the node
        self._nodes[name] = node
        
        return node
    
    def get_dependencies(self, name: str) -> List[ProjectNode]:
        """Get the dependencies of a project node.
        
        Args:
            name: Name of the project node
            
        Returns:
            List of ProjectNode dependencies
            
        Raises:
            ValueError: If the node doesn't exist
        """
        if name not in self._nodes:
            raise ValueError(f"Node with name '{name}' does not exist")
        
        return self._nodes[name].dependencies
    
    def get_node(self, name: str) -> Optional[ProjectNode]:
        """Get a project node by name.
        
        Args:
            name: Name of the project node
            
        Returns:
            ProjectNode if found, None otherwise
        """
        return self._nodes.get(name)
    
    def get_all_nodes(self) -> Dict[str, ProjectNode]:
        """Get all nodes in the tree.
        
        Returns:
            Dictionary mapping node names to ProjectNode instances
        """
        return self._nodes.copy()
    
    def get_nodes(self) -> List[ProjectNode]:
        """Get a list of all nodes in the tree.
        
        Returns:
            List of ProjectNode instances
        """
        return list(self._nodes.values())
    
    def get_nodes_in_dependency_order(self) -> List[ProjectNode]:
        """Get nodes in dependency order, starting with leaves (nodes with no dependencies).
        
        This method performs a topological sort of the dependency graph, returning
        nodes such that all dependencies of a node appear before the node itself.
        Leaves (nodes with no dependencies) appear first, followed by nodes that
        depend on them, and so on.
        
        Returns:
            List of ProjectNode instances in dependency order (leaves first)
            
        Raises:
            ValueError: If a circular dependency is detected
        """
        if not self._nodes:
            return []
        
        # Track which nodes have been processed (by name)
        processed = set()
        result = []
        
        # Keep track of remaining node names
        remaining = set(self._nodes.keys())
        
        # Iterate until all nodes are processed
        while remaining:
            # Find nodes whose dependencies are all already processed (or have no dependencies)
            ready_nodes = []
            for node_name in remaining:
                node = self._nodes[node_name]
                if all(dep.name in processed for dep in node.dependencies):
                    ready_nodes.append(node)
            
            # If no nodes are ready, there's a circular dependency
            if not ready_nodes:
                raise ValueError(
                    f"Circular dependency detected. Remaining nodes: {', '.join(sorted(remaining))}"
                )
            
            # Add ready nodes to result and mark as processed
            for node in ready_nodes:
                result.append(node)
                processed.add(node.name)
                remaining.remove(node.name)
        
        return result
    
    def print_tree(self, show_apis: bool = False) -> None:
        """Print the project tree showing all nodes and their dependencies.
        
        Args:
            show_apis: If True, also print API signatures for each node (default: False)
        """
        print()
        if self.name:
            print(f"Project Tree: {self.name}")
        else:
            print("Project Tree")
        print("=" * 60)
        
        if not self._nodes:
            print("(empty tree)")
            return
        
        # Print each node with its dependencies
        for node_name, node in sorted(self._nodes.items()):
            print(f"\n{node_name}")
            
            # Print directory
            if node.dir:
                print(f"  Dir: {node.dir}")
            else:
                print("  Dir: (none)")
            
            # Print dependencies
            if node.dependencies:
                dep_names = [dep.name for dep in node.dependencies]
                print(f"  Dependencies: {', '.join(dep_names)}")
            else:
                print("  Dependencies: (none)")
            
            # Print prompt
            if node.prompt:
                print(f"  Prompt: {node.prompt}")
            else:
                print("  Prompt: (none)")
            
            # Print APIs if requested
            if show_apis and node.apis:
                print("  APIs:")
                for api in node.apis:
                    print(f"    - {api}")
        
        print("\n" + "=" * 60)
