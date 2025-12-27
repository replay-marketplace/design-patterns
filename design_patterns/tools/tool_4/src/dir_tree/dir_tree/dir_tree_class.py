"""Directory tree implementation with File and Node_Dir classes."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional, List


class State(Enum):
    """State enum for files and directories."""
    VISIBLE = "visible"
    READONLY = "readonly"
    HIDDEN = "hidden"


@dataclass
class File:
    """File node in the directory tree."""
    path: str
    content: str
    state: State = State.VISIBLE


@dataclass
class Node_Dir:
    """Directory node in the directory tree."""
    path: str
    state: State = State.VISIBLE
    children: Dict[str, 'Node_Dir'] = field(default_factory=dict)
    files: Dict[str, File] = field(default_factory=dict)


class DirTree:
    """Directory tree class that holds all nodes."""
    
    def __init__(self, root: Optional[Node_Dir] = None):
        """Initialize DirTree with optional root node."""
        if root is None:
            self.root = Node_Dir(path="", state=State.VISIBLE)
        else:
            self.root = root
    
    def add_file(self, filepath: str, content: str = "", state: State = State.VISIBLE) -> None:
        """Add a file to the tree at the given path."""
        parts = filepath.split('/')
        filename = parts[-1]
        dir_parts = parts[:-1] if len(parts) > 1 else []
        
        # Navigate to or create the directory
        current = self.root
        for dir_name in dir_parts:
            if dir_name == "":
                continue
            if dir_name not in current.children:
                dir_path = '/'.join([current.path, dir_name]).lstrip('/')
                current.children[dir_name] = Node_Dir(path=dir_path, state=State.VISIBLE)
            current = current.children[dir_name]
        
        # Add the file
        current.files[filename] = File(path=filepath, content=content, state=state)
    
    def add_dir(self, dirpath: str, state: State = State.VISIBLE) -> None:
        """Add a directory to the tree at the given path."""
        parts = [p for p in dirpath.split('/') if p != ""]
        
        current = self.root
        for dir_name in parts:
            if dir_name not in current.children:
                dir_path = '/'.join([current.path, dir_name]).lstrip('/')
                current.children[dir_name] = Node_Dir(path=dir_path, state=state)
            current = current.children[dir_name]
    
    def _print_node(self, node: Node_Dir, prefix: str = "", is_last: bool = True) -> None:
        """Recursively print a node and its children."""
        # Print current directory (skip root if path is empty)
        if node.path != "":
            connector = "└── " if is_last else "├── "
            dir_name = node.path.split('/')[-1] if node.path else '.'
            print(f"{prefix}{connector}{dir_name}/")
            prefix_update = "    " if is_last else "│   "
        else:
            # Root node - don't print it, but use empty prefix for children
            prefix_update = ""
        
        # Collect all items (files and directories)
        file_items = sorted(node.files.items())
        dir_items = sorted(node.children.items())
        
        all_items = []
        for name, file_obj in file_items:
            all_items.append(('file', name, file_obj))
        for name, dir_obj in dir_items:
            all_items.append(('dir', name, dir_obj))
        
        # Print all items
        for i, (item_type, name, obj) in enumerate(all_items):
            is_last_item = (i == len(all_items) - 1)
            if item_type == 'file':
                connector = "└── " if is_last_item else "├── "
                print(f"{prefix}{prefix_update}{connector}{name}")
            else:
                # Directory - recurse
                new_prefix = prefix + prefix_update
                self._print_node(obj, new_prefix, is_last_item)
    
    def print_dir_tree(self) -> None:
        """Print the directory tree with tree structure using ├──, │, └──."""
        if self.root.path == "" and not self.root.children and not self.root.files:
            print("(empty tree)")
            return
        
        self._print_node(self.root, "", True)
    
    def json_to_tree(self, files: List[Dict[str, str]]) -> Node_Dir:
        """Create tree from JSON list of files and return root node."""
        self.root = Node_Dir(path="", state=State.VISIBLE)
        
        for file_dict in files:
            filepath = file_dict.get("path", "")
            content = file_dict.get("contents", file_dict.get("content", ""))
            self.add_file(filepath, content)
        
        return self.root
    
    def dir_exists(self, dirpath: str) -> bool:
        """Check if a directory exists in the tree."""
        parts = [p for p in dirpath.split('/') if p != ""]
        
        current = self.root
        for dir_name in parts:
            if dir_name not in current.children:
                return False
            current = current.children[dir_name]
        return True
    
    def set_dir_to_invisible(self, dirpath: str) -> None:
        """Set a directory to invisible (HIDDEN state)."""
        parts = [p for p in dirpath.split('/') if p != ""]
        
        # If empty path, set root to invisible
        if not parts:
            self.root.state = State.HIDDEN
            return
        
        current = self.root
        for dir_name in parts:
            if dir_name not in current.children:
                # Directory doesn't exist, create it as invisible
                dir_path = '/'.join([current.path, dir_name]).lstrip('/')
                current.children[dir_name] = Node_Dir(path=dir_path, state=State.HIDDEN)
                return
            current = current.children[dir_name]
        
        # Directory exists, set it to invisible
        current.state = State.HIDDEN
    
    def _generate_file_dict_recursive(self, node: Node_Dir, file_dict: Dict[str, str]) -> None:
        """Recursively collect files from visible directories."""
        # Skip if directory is hidden
        if node.state == State.HIDDEN:
            return
        
        # Add visible files from this directory
        for filename, file_obj in node.files.items():
            if file_obj.state != State.HIDDEN:
                file_dict[file_obj.path] = file_obj.content
        
        # Recursively process child directories
        for child_dir in node.children.values():
            self._generate_file_dict_recursive(child_dir, file_dict)
    
    def generate_file_dict(self) -> Dict[str, str]:
        """Generate a dictionary with files. Does not include files set to HIDDEN, 
        or anything within a dir that's set to HIDDEN."""
        file_dict = {}
        self._generate_file_dict_recursive(self.root, file_dict)
        return file_dict

