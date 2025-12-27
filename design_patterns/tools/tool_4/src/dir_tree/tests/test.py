"""Tests for dir_tree module."""

from dir_tree import DirTree, Node_Dir, File, State


def test_json_to_tree():
    """Test creating a tree from JSON."""
    print("\n" + "="*60)
    print("TEST: test_json_to_tree")
    print("="*60)
    
    files = [
        {"path": "src/main.py", "contents": "print('hello')"},
        {"path": "src/utils.py", "contents": "def helper(): pass"},
        {"path": "README.md", "contents": "# Project"},
    ]
    
    print("\nInput files:")
    for f in files:
        print(f"  - {f['path']}: {f['contents'][:30]}...")
    
    tree = DirTree()
    root = tree.json_to_tree(files)
    
    print("\n✓ Root node created")
    assert root is not None
    
    print(f"\nRoot directory structure:")
    print(f"  - Directories: {list(root.children.keys())}")
    print(f"  - Files: {list(root.files.keys())}")
    
    assert "src" in root.children
    assert "README.md" in root.files
    assert root.files["README.md"].content == "# Project"
    
    print(f"\n✓ Root contains 'src' directory")
    print(f"✓ Root contains 'README.md' file")
    print(f"  README.md content: {root.files['README.md'].content}")
    
    src_dir = root.children["src"]
    print(f"\n'src' directory structure:")
    print(f"  - Files: {list(src_dir.files.keys())}")
    
    assert "main.py" in src_dir.files
    assert "utils.py" in src_dir.files
    assert src_dir.files["main.py"].content == "print('hello')"
    
    print(f"\n✓ 'src' contains 'main.py'")
    print(f"  main.py content: {src_dir.files['main.py'].content}")
    print(f"✓ 'src' contains 'utils.py'")
    print(f"  utils.py content: {src_dir.files['utils.py'].content}")
    
    print("\n✓ test_json_to_tree PASSED")


def test_dir_exists():
    """Test dir_exists method."""
    print("\n" + "="*60)
    print("TEST: test_dir_exists")
    print("="*60)
    
    files = [
        {"path": "src/main.py", "contents": "print('hello')"},
        {"path": "src/utils.py", "contents": "def helper(): pass"},
        {"path": "docs/readme.md", "contents": "# Docs"},
    ]
    
    print("\nInput files:")
    for f in files:
        print(f"  - {f['path']}")
    
    tree = DirTree()
    tree.json_to_tree(files)
    
    print("\nTesting dir_exists() method:")
    
    test_paths = [
        ("src", True),
        ("docs", True),
        ("nonexistent", False),
        ("src/nested", False),
    ]
    
    for path, expected in test_paths:
        result = tree.dir_exists(path)
        status = "✓" if result == expected else "✗"
        print(f"  {status} dir_exists('{path}') = {result} (expected: {expected})")
        assert result == expected
    
    print("\n✓ test_dir_exists PASSED")


def test_file_attributes():
    """Test File dataclass attributes."""
    print("\n" + "="*60)
    print("TEST: test_file_attributes")
    print("="*60)
    
    print("\nCreating File instance:")
    file = File(
        path="src/test.py",
        content="test content",
        state=State.READONLY
    )
    
    print(f"  File object created: {file}")
    print(f"\nTesting attributes:")
    print(f"  - path: {file.path}")
    print(f"  - content: {file.content}")
    print(f"  - state: {file.state}")
    
    assert file.path == "src/test.py"
    print("  ✓ path == 'src/test.py'")
    
    assert file.content == "test content"
    print("  ✓ content == 'test content'")
    
    assert file.state == State.READONLY
    print("  ✓ state == State.READONLY")
    
    print("\n✓ test_file_attributes PASSED")


def test_node_dir_attributes():
    """Test Node_Dir dataclass attributes."""
    print("\n" + "="*60)
    print("TEST: test_node_dir_attributes")
    print("="*60)
    
    print("\nCreating Node_Dir instance:")
    node = Node_Dir(
        path="src",
        state=State.VISIBLE
    )
    
    print(f"  Node_Dir object created: {node}")
    print(f"\nTesting attributes:")
    print(f"  - path: {node.path}")
    print(f"  - state: {node.state}")
    print(f"  - children type: {type(node.children)}")
    print(f"  - files type: {type(node.files)}")
    print(f"  - children: {node.children}")
    print(f"  - files: {node.files}")
    
    assert node.path == "src"
    print("  ✓ path == 'src'")
    
    assert node.state == State.VISIBLE
    print("  ✓ state == State.VISIBLE")
    
    assert isinstance(node.children, dict)
    print("  ✓ children is a dict")
    
    assert isinstance(node.files, dict)
    print("  ✓ files is a dict")
    
    print("\n✓ test_node_dir_attributes PASSED")


def test_add_file():
    """Test add_file method."""
    print("\n" + "="*60)
    print("TEST: test_add_file")
    print("="*60)
    
    tree = DirTree()
    
    print("\nAdding files:")
    print("  - add_file('src/main.py', 'print(\\\"hello\\\")')")
    print("  - add_file('src/utils.py', 'def helper(): pass')")
    print("  - add_file('README.md', '# Project')")
    
    tree.add_file("src/main.py", "print(\"hello\")")
    tree.add_file("src/utils.py", "def helper(): pass")
    tree.add_file("README.md", "# Project")
    
    print("\n✓ Files added")
    
    # Check root files
    assert "README.md" in tree.root.files
    print(f"  ✓ Root contains 'README.md'")
    assert tree.root.files["README.md"].content == "# Project"
    print(f"  ✓ README.md content: {tree.root.files['README.md'].content}")
    
    # Check src directory
    assert "src" in tree.root.children
    print(f"  ✓ Root contains 'src' directory")
    
    src_dir = tree.root.children["src"]
    assert "main.py" in src_dir.files
    print(f"  ✓ 'src' contains 'main.py'")
    assert src_dir.files["main.py"].content == "print(\"hello\")"
    print(f"  ✓ main.py content: {src_dir.files['main.py'].content}")
    
    assert "utils.py" in src_dir.files
    print(f"  ✓ 'src' contains 'utils.py'")
    assert src_dir.files["utils.py"].content == "def helper(): pass"
    print(f"  ✓ utils.py content: {src_dir.files['utils.py'].content}")
    
    print("\n✓ test_add_file PASSED")


def test_add_dir():
    """Test add_dir method."""
    print("\n" + "="*60)
    print("TEST: test_add_dir")
    print("="*60)
    
    tree = DirTree()
    
    print("\nAdding directories:")
    print("  - add_dir('src')")
    print("  - add_dir('docs')")
    print("  - add_dir('src/components')")
    
    tree.add_dir("src")
    tree.add_dir("docs")
    tree.add_dir("src/components")
    
    print("\n✓ Directories added")
    
    # Check root directories
    assert "src" in tree.root.children
    print(f"  ✓ Root contains 'src' directory")
    assert "docs" in tree.root.children
    print(f"  ✓ Root contains 'docs' directory")
    
    # Check nested directory
    src_dir = tree.root.children["src"]
    assert "components" in src_dir.children
    print(f"  ✓ 'src' contains 'components' directory")
    
    print("\n✓ test_add_dir PASSED")


def test_print_dir_tree():
    """Test print_dir_tree method."""
    print("\n" + "="*60)
    print("TEST: test_print_dir_tree")
    print("="*60)
    
    tree = DirTree()
    
    print("\nBuilding tree structure:")
    tree.add_dir("src")
    tree.add_dir("docs")
    tree.add_dir("src/components")
    tree.add_file("src/main.py", "print('hello')")
    tree.add_file("src/utils.py", "def helper(): pass")
    tree.add_file("src/components/button.py", "class Button: pass")
    tree.add_file("README.md", "# Project")
    tree.add_file("docs/readme.md", "# Documentation")
    
    print("  - Created directories: src, docs, src/components")
    print("  - Created files: src/main.py, src/utils.py, src/components/button.py, README.md, docs/readme.md")
    
    print("\n" + "-"*60)
    print("Printing directory tree:")
    print("-"*60)
    tree.print_dir_tree()
    print("-"*60)
    
    print("\n✓ Directory tree printed successfully")
    print("\n✓ test_print_dir_tree PASSED")


def test_set_dir_to_invisible():
    """Test set_dir_to_invisible method."""
    print("\n" + "="*60)
    print("TEST: test_set_dir_to_invisible")
    print("="*60)
    
    tree = DirTree()
    
    print("\nBuilding tree structure:")
    tree.add_dir("src")
    tree.add_dir("docs")
    tree.add_dir("src/components")
    tree.add_file("src/main.py", "print('hello')")
    tree.add_file("src/utils.py", "def helper(): pass")
    tree.add_file("src/components/button.py", "class Button: pass")
    tree.add_file("README.md", "# Project")
    tree.add_file("docs/readme.md", "# Documentation")
    
    print("  - Created directories: src, docs, src/components")
    print("  - Created files: src/main.py, src/utils.py, src/components/button.py, README.md, docs/readme.md")
    
    print("\nInitial directory states:")
    print(f"  - src state: {tree.root.children['src'].state}")
    print(f"  - docs state: {tree.root.children['docs'].state}")
    print(f"  - src/components state: {tree.root.children['src'].children['components'].state}")
    
    # Set docs to invisible
    print("\nSetting 'docs' directory to invisible...")
    tree.set_dir_to_invisible("docs")
    
    print(f"  - docs state after set_dir_to_invisible: {tree.root.children['docs'].state}")
    assert tree.root.children['docs'].state == State.HIDDEN
    print("  ✓ docs directory is now HIDDEN")
    
    # Set src/components to invisible
    print("\nSetting 'src/components' directory to invisible...")
    tree.set_dir_to_invisible("src/components")
    
    print(f"  - src/components state after set_dir_to_invisible: {tree.root.children['src'].children['components'].state}")
    assert tree.root.children['src'].children['components'].state == State.HIDDEN
    print("  ✓ src/components directory is now HIDDEN")
    
    # Verify other directories are still visible
    print(f"\n  - src state: {tree.root.children['src'].state}")
    assert tree.root.children['src'].state == State.VISIBLE
    print("  ✓ src directory is still VISIBLE")
    
    # Print the directory tree to show hidden directories
    print("\n" + "-"*60)
    print("Directory tree (docs and src/components are HIDDEN):")
    print("-"*60)
    tree.print_dir_tree()
    print("-"*60)
    
    # Generate and print the dictionary to show what's included
    print("\nGenerating file dictionary...")
    file_dict = tree.generate_file_dict()
    print(f"\nGenerated Dict (contains {len(file_dict)} files):")
    print("{")
    for path, content in sorted(file_dict.items()):
        print(f"  '{path}': '{content}',")
    print("}")
    
    # Verify hidden directories' files are not in the dict
    assert "docs/readme.md" not in file_dict
    assert "src/components/button.py" not in file_dict
    print("\n✓ docs/readme.md NOT in dictionary (directory is HIDDEN)")
    print("✓ src/components/button.py NOT in dictionary (directory is HIDDEN)")
    
    # Verify visible files are in the dict
    assert "src/main.py" in file_dict
    assert "src/utils.py" in file_dict
    assert "README.md" in file_dict
    print("✓ Visible files ARE in dictionary")
    
    print("\n✓ test_set_dir_to_invisible PASSED")


def test_generate_file_dict():
    """Test generate_file_dict method."""
    print("\n" + "="*60)
    print("TEST: test_generate_file_dict")
    print("="*60)
    
    tree = DirTree()
    
    print("\nBuilding tree structure:")
    tree.add_file("src/main.py", "print('hello')")
    tree.add_file("src/utils.py", "def helper(): pass")
    tree.add_file("src/components/button.py", "class Button: pass")
    tree.add_file("src/components/modal.py", "class Modal: pass")
    tree.add_file("README.md", "# Project")
    tree.add_file("docs/readme.md", "# Documentation")
    tree.add_file("docs/api.md", "# API Reference")
    
    print("  - Files created:")
    print("    - src/main.py")
    print("    - src/utils.py")
    print("    - src/components/button.py")
    print("    - src/components/modal.py")
    print("    - README.md")
    print("    - docs/readme.md")
    print("    - docs/api.md")
    
    # Generate file dict without any invisible directories
    print("\n" + "-"*60)
    print("Directory tree (all visible):")
    print("-"*60)
    tree.print_dir_tree()
    print("-"*60)
    
    print("\nGenerating file dictionary (all visible)...")
    file_dict = tree.generate_file_dict()
    
    print(f"\nGenerated Dict (contains {len(file_dict)} files):")
    print("{")
    for path, content in sorted(file_dict.items()):
        print(f"  '{path}': '{content}',")
    print("}")
    
    expected_files = {
        "src/main.py": "print('hello')",
        "src/utils.py": "def helper(): pass",
        "src/components/button.py": "class Button: pass",
        "src/components/modal.py": "class Modal: pass",
        "README.md": "# Project",
        "docs/readme.md": "# Documentation",
        "docs/api.md": "# API Reference"
    }
    
    assert len(file_dict) == len(expected_files)
    print(f"\n✓ Dictionary contains {len(expected_files)} files (expected)")
    
    for path, expected_content in expected_files.items():
        assert path in file_dict
        assert file_dict[path] == expected_content
        print(f"  ✓ {path} matches expected content")
    
    # Set docs directory to invisible
    print("\n" + "-"*60)
    print("Setting 'docs' directory to invisible...")
    tree.set_dir_to_invisible("docs")
    
    print("\nDirectory tree (docs is HIDDEN):")
    print("-"*60)
    tree.print_dir_tree()
    print("-"*60)
    
    print("\nGenerating file dictionary (docs is invisible)...")
    file_dict = tree.generate_file_dict()
    
    print(f"\nGenerated Dict (contains {len(file_dict)} files):")
    print("{")
    for path, content in sorted(file_dict.items()):
        print(f"  '{path}': '{content}',")
    print("}")
    
    # Should not include docs files
    assert "docs/readme.md" not in file_dict
    assert "docs/api.md" not in file_dict
    print("\n✓ docs/readme.md NOT in dictionary (directory is invisible)")
    print("✓ docs/api.md NOT in dictionary (directory is invisible)")
    
    # Should still include other files
    assert "src/main.py" in file_dict
    assert "src/utils.py" in file_dict
    assert "README.md" in file_dict
    print("✓ Other files ARE in dictionary")
    
    # Set src/components to invisible
    print("\n" + "-"*60)
    print("Setting 'src/components' directory to invisible...")
    tree.set_dir_to_invisible("src/components")
    
    print("\nDirectory tree (docs and src/components are HIDDEN):")
    print("-"*60)
    tree.print_dir_tree()
    print("-"*60)
    
    print("\nGenerating file dictionary (docs and src/components are invisible)...")
    file_dict = tree.generate_file_dict()
    
    print(f"\nGenerated Dict (contains {len(file_dict)} files):")
    print("{")
    for path, content in sorted(file_dict.items()):
        print(f"  '{path}': '{content}',")
    print("}")
    
    # Should not include components files
    assert "src/components/button.py" not in file_dict
    assert "src/components/modal.py" not in file_dict
    print("\n✓ src/components/button.py NOT in dictionary (directory is invisible)")
    print("✓ src/components/modal.py NOT in dictionary (directory is invisible)")
    
    # Should still include src files (not in components)
    assert "src/main.py" in file_dict
    assert "src/utils.py" in file_dict
    print("✓ src/main.py and src/utils.py ARE in dictionary")
    
    # Test with hidden file
    print("\n" + "-"*60)
    print("Setting 'src/utils.py' file to HIDDEN state...")
    tree.root.children['src'].files['utils.py'].state = State.HIDDEN
    
    print("\nDirectory tree (with hidden file src/utils.py):")
    print("-"*60)
    tree.print_dir_tree()
    print("-"*60)
    
    print("\nGenerating file dictionary (with hidden file)...")
    file_dict = tree.generate_file_dict()
    
    print(f"\nGenerated Dict (contains {len(file_dict)} files):")
    print("{")
    for path, content in sorted(file_dict.items()):
        print(f"  '{path}': '{content}',")
    print("}")
    
    # Should not include hidden file
    assert "src/utils.py" not in file_dict
    print("\n✓ src/utils.py NOT in dictionary (file is HIDDEN)")
    
    # Should still include visible files
    assert "src/main.py" in file_dict
    assert "README.md" in file_dict
    print("✓ Visible files ARE in dictionary")
    
    print("\n✓ test_generate_file_dict PASSED")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUNNING ALL TESTS")
    print("="*60)
    
    test_json_to_tree()
    test_dir_exists()
    test_file_attributes()
    test_node_dir_attributes()
    test_add_file()
    test_add_dir()
    test_print_dir_tree()
    test_set_dir_to_invisible()
    test_generate_file_dict()
    
    print("\n" + "="*60)
    print("ALL TESTS PASSED! ✓")
    print("="*60 + "\n")

