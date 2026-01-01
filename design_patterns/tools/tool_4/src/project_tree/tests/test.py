"""Tests for project_tree module."""

from project_tree import ProjectTree, ProjectNode
from dir_tree.dir_tree import DirTree


def test_project_tree_init():
    """Test initializing ProjectTree."""
    print("\n" + "="*60)
    print("TEST: test_project_tree_init")
    print("="*60)
    
    tree = ProjectTree(
        name="MyProject",
        prompt="Test prompt",
        functions=["func1", "func2"]
    )
    
    assert tree.name == "MyProject"
    assert tree.prompt == "Test prompt"
    assert tree.functions == ["func1", "func2"]
    assert isinstance(tree.dir_tree, DirTree)
    
    print("✓ ProjectTree initialized correctly")
    print(f"  Name: {tree.name}")
    print(f"  Prompt: {tree.prompt}")
    print(f"  Functions: {tree.functions}")
    print("\n✓ All assertions passed!")


def test_add_node():
    """Test adding nodes to the tree."""
    print("\n" + "="*60)
    print("TEST: test_add_node")
    print("="*60)
    
    tree = ProjectTree(name="TestTree")
    
    # Add a node without dependencies
    node1 = tree.add_node("project1")
    assert node1.name == "project1"
    assert len(node1.dependencies) == 0
    print("✓ Added node 'project1' without dependencies")
    
    # Add another node without dependencies
    node2 = tree.add_node("project2")
    assert node2.name == "project2"
    print("✓ Added node 'project2' without dependencies")
    
    # Add a node with dependencies
    node3 = tree.add_node("project3", dependencies=["project1", "project2"])
    assert node3.name == "project3"
    assert len(node3.dependencies) == 2
    assert node3.dependencies[0].name == "project1"
    assert node3.dependencies[1].name == "project2"
    print("✓ Added node 'project3' with dependencies on 'project1' and 'project2'")
    
    # Test that duplicate names raise error
    try:
        tree.add_node("project1")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"✓ Correctly raised ValueError for duplicate name: {e}")
    
    # Test that non-existent dependency raises error
    try:
        tree.add_node("project4", dependencies=["nonexistent"])
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"✓ Correctly raised ValueError for non-existent dependency: {e}")
    
    print("\n✓ All assertions passed!")


def test_get_dependencies():
    """Test getting dependencies of a node."""
    print("\n" + "="*60)
    print("TEST: test_get_dependencies")
    print("="*60)
    
    tree = ProjectTree(name="TestTree")
    
    tree.add_node("base")
    tree.add_node("middle", dependencies=["base"])
    tree.add_node("top", dependencies=["middle", "base"])
    
    # Get dependencies
    deps = tree.get_dependencies("top")
    assert len(deps) == 2
    assert deps[0].name == "middle"
    assert deps[1].name == "base"
    print("✓ Retrieved dependencies for 'top'")
    print(f"  Dependencies: {[d.name for d in deps]}")
    
    # Get dependencies for node without dependencies
    deps_empty = tree.get_dependencies("base")
    assert len(deps_empty) == 0
    print("✓ Retrieved empty dependencies for 'base'")
    
    # Test that non-existent node raises error
    try:
        tree.get_dependencies("nonexistent")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"✓ Correctly raised ValueError for non-existent node: {e}")
    
    print("\n✓ All assertions passed!")


def test_get_node():
    """Test getting a node by name."""
    print("\n" + "="*60)
    print("TEST: test_get_node")
    print("="*60)
    
    tree = ProjectTree(name="TestTree")
    
    node1 = tree.add_node("project1")
    node2 = tree.add_node("project2", dependencies=["project1"])
    
    retrieved = tree.get_node("project1")
    assert retrieved is not None
    assert retrieved.name == "project1"
    assert retrieved is node1
    print("✓ Retrieved node 'project1'")
    
    retrieved = tree.get_node("nonexistent")
    assert retrieved is None
    print("✓ Correctly returned None for non-existent node")
    
    print("\n✓ All assertions passed!")


def test_get_all_nodes():
    """Test getting all nodes."""
    print("\n" + "="*60)
    print("TEST: test_get_all_nodes")
    print("="*60)
    
    tree = ProjectTree(name="TestTree")
    
    tree.add_node("project1")
    tree.add_node("project2")
    tree.add_node("project3", dependencies=["project1"])
    
    all_nodes = tree.get_all_nodes()
    assert len(all_nodes) == 3
    assert "project1" in all_nodes
    assert "project2" in all_nodes
    assert "project3" in all_nodes
    print(f"✓ Retrieved all {len(all_nodes)} nodes")
    print(f"  Node names: {list(all_nodes.keys())}")
    
    print("\n✓ All assertions passed!")


def test_get_nodes():
    """Test getting a list of all nodes."""
    print("\n" + "="*60)
    print("TEST: test_get_nodes")
    print("="*60)
    
    tree = ProjectTree(name="TestTree")
    
    node1 = tree.add_node("project1")
    node2 = tree.add_node("project2")
    node3 = tree.add_node("project3", dependencies=["project1"])
    
    nodes_list = tree.get_nodes()
    assert len(nodes_list) == 3
    assert isinstance(nodes_list, list)
    
    # Verify all nodes are in the list
    node_names = [node.name for node in nodes_list]
    assert "project1" in node_names
    assert "project2" in node_names
    assert "project3" in node_names
    
    print(f"✓ Retrieved list of {len(nodes_list)} nodes")
    print(f"  Node names: {node_names}")
    
    # Test empty tree
    empty_tree = ProjectTree(name="EmptyTree")
    empty_list = empty_tree.get_nodes()
    assert len(empty_list) == 0
    assert isinstance(empty_list, list)
    print("✓ Empty tree returns empty list")
    
    print("\n✓ All assertions passed!")


def test_project_node_apis():
    """Test ProjectNode apis attribute."""
    print("\n" + "="*60)
    print("TEST: test_project_node_apis")
    print("="*60)
    
    tree = ProjectTree(name="TestTree")
    
    # Create a node and verify it has empty apis by default
    node1 = tree.add_node("project1")
    assert node1.apis == []
    print("✓ Node created with empty apis list by default")
    
    # Add APIs to the node
    node1.apis = [
        "add_node(name: str, dependencies: List[str] = None) -> ProjectNode",
        "get_dependencies(name: str) -> List[ProjectNode]"
    ]
    assert len(node1.apis) == 2
    assert "add_node" in node1.apis[0]
    print("✓ Added API signatures to node")
    print(f"  APIs: {node1.apis}")
    
    # Create another node with APIs
    node2 = tree.add_node("project2")
    node2.apis = ["test_function() -> None"]
    assert len(node2.apis) == 1
    print("✓ Created another node with API signature")
    
    print("\n✓ All assertions passed!")


def test_print_tree():
    """Test printing the project tree."""
    print("\n" + "="*60)
    print("TEST: test_print_tree")
    print("="*60)
    
    tree = ProjectTree(name="TestProjectTree")
    
    # Create a tree with dependencies
    tree.add_node("base")
    tree.add_node("middle", dependencies=["base"])
    tree.add_node("top", dependencies=["middle", "base"])
    tree.add_node("standalone")
    
    # Add some APIs
    top_node = tree.get_node("top")
    top_node.apis = ["process_data() -> None", "validate() -> bool"]
    
    print("\nPrinting tree (without APIs):")
    tree.print_tree(show_apis=False)
    
    print("\nPrinting tree (with APIs):")
    tree.print_tree(show_apis=True)
    
    # Test empty tree
    empty_tree = ProjectTree(name="EmptyTree")
    print("\nPrinting empty tree:")
    empty_tree.print_tree()
    
    print("\n✓ All print operations completed successfully!")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUNNING PROJECT_TREE TESTS")
    print("="*60)
    
    test_project_tree_init()
    test_add_node()
    test_get_dependencies()
    test_get_node()
    test_get_all_nodes()
    test_get_nodes()
    test_project_node_apis()
    test_print_tree()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("="*60 + "\n")
