"""Directory tree implementation with File and Node_Dir classes."""

import os
import stat
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional, List, Union


class State(Enum):
    """State enum for files and directories."""
    VISIBLE = "visible"
    HIDDEN = "hidden"
    VISIBLE_PATH = "visible_path"


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
    
    def add_dir(self, name: str, state: State = State.VISIBLE) -> None:
        """Add an empty directory to the tree.
        
        Args:
            name: Directory name (if it contains '/', it's treated as a path)
            state: State of the directory (default: VISIBLE)
        """
        parts = [p for p in name.split('/') if p != ""]
        
        current = self.root
        for dir_name in parts:
            if dir_name not in current.children:
                dir_path = '/'.join([current.path, dir_name]).lstrip('/')
                current.children[dir_name] = Node_Dir(path=dir_path, state=state)
            current = current.children[dir_name]
    
    def _count_words_in_file(self, file: File) -> int:
        """Count words in a file's content.
        
        Args:
            file: File object to count words in
            
        Returns:
            Number of words in the file content
        """
        if not file.content:
            return 0
        # Split by whitespace and count non-empty strings
        words = file.content.split()
        return len(words)
    
    def _count_words_in_dir(self, node: Node_Dir) -> int:
        """Recursively count words in all files within a directory.
        
        Args:
            node: Directory node to count words in
            
        Returns:
            Total word count of all files in the directory and subdirectories
        """
        total_words = 0
        
        # Count words in files in this directory
        for file_obj in node.files.values():
            total_words += self._count_words_in_file(file_obj)
        
        # Recursively count words in subdirectories
        for child_dir in node.children.values():
            total_words += self._count_words_in_dir(child_dir)
        
        return total_words
    
    def _get_state_abbreviation(self, state: State) -> str:
        """Get state abbreviation for printing.
        
        Args:
            state: State enum value
            
        Returns:
            Single letter abbreviation: V for visible, H for hidden, P for visible_path
        """
        if state == State.VISIBLE:
            return "V"
        elif state == State.HIDDEN:
            return "H"
        elif state == State.VISIBLE_PATH:
            return "P"
        else:
            return "?"
    
    def _print_node(self, node: Node_Dir, prefix: str = "", is_last: bool = True, 
                   words: bool = False, contents: bool = False, state: bool = False) -> None:
        """Recursively print a node and its children.
        
        Args:
            node: Directory node to print
            prefix: Prefix string for tree structure
            is_last: Whether this is the last item in its parent
            words: If True, print word count before file/directory names
            contents: If True, print file contents after file names
            state: If True, print state abbreviation before file/directory names
        """
        # Print current directory (skip root if path is empty)
        if node.path != "":
            connector = "└── " if is_last else "├── "
            dir_name = node.path.split('/')[-1] if node.path else '.'
            
            # Build prefix components
            prefix_parts = []
            
            # Add state if requested
            if state:
                state_abbr = self._get_state_abbreviation(node.state)
                prefix_parts.append(f"({state_abbr})")
            
            # Add word count if requested
            if words:
                word_count = self._count_words_in_dir(node)
                prefix_parts.append(f"({word_count})")
            
            # Combine prefix parts
            item_prefix = " ".join(prefix_parts) + " " if prefix_parts else ""
            
            print(f"{prefix}{connector}{item_prefix}{dir_name}/")
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
                
                # Build prefix components
                prefix_parts = []
                
                # Add state if requested
                if state:
                    state_abbr = self._get_state_abbreviation(obj.state)
                    prefix_parts.append(f"({state_abbr})")
                
                # Add word count if requested
                if words:
                    word_count = self._count_words_in_file(obj)
                    prefix_parts.append(f"({word_count})")
                
                # Combine prefix parts
                item_prefix = " ".join(prefix_parts) + " " if prefix_parts else ""
                
                # Add content if requested
                content_suffix = ""
                if contents:
                    content_suffix = f', content="{obj.content}"'
                
                print(f"{prefix}{prefix_update}{connector}{item_prefix}{name}{content_suffix}")
            else:
                # Directory - recurse
                new_prefix = prefix + prefix_update
                self._print_node(obj, new_prefix, is_last_item, words, contents, state)
    
    def print_dir_tree(self, words: bool = False, contents: bool = False, state: bool = False) -> None:
        """Print the directory tree with tree structure using ├──, │, └──.
        
        Args:
            words: If True, print word count before file/directory names (default: False)
            contents: If True, print file contents after file names (default: False)
            state: If True, print state abbreviation before file/directory names (default: False)
                   V = visible, H = hidden
        """
        print()
        if self.root.path == "" and not self.root.children and not self.root.files:
            print("(empty tree)")
            return
        
        self._print_node(self.root, "", True, words, contents, state)
    
    def json_to_tree(self, files: Union[List[Dict[str, str]], Dict[str, str]]) -> Node_Dir:
        """Create tree from JSON list of files or dictionary of files and return root node.
        
        Args:
            files: Either:
                - List[Dict[str, str]]: List of dicts with "path" and "contents"/"content" keys
                - Dict[str, str]: Dictionary mapping file paths to file contents
        """
        self.root = Node_Dir(path="", state=State.VISIBLE)
        
        # Handle dictionary format (path -> content)
        if isinstance(files, dict):
            for filepath, content in files.items():
                self.add_file(filepath, content)
        # Handle list format (list of dicts with "path" and "contents"/"content")
        elif isinstance(files, list):
            for file_dict in files:
                if isinstance(file_dict, dict):
                    filepath = file_dict.get("path", "")
                    content = file_dict.get("contents", file_dict.get("content", ""))
                    self.add_file(filepath, content)
                else:
                    raise ValueError(f"Expected dict in list, got {type(file_dict)}")
        else:
            raise ValueError(f"Expected list or dict, got {type(files)}")
        
        return self.root
    
    def add_files_to_dir_tree(self, files: Union[List[Dict[str, str]], Dict[str, str]]) -> Node_Dir:
        """Add files to an existing tree without resetting it.
        
        Args:
            files: Either:
                - List[Dict[str, str]]: List of dicts with "path" and "contents"/"content" keys
                - Dict[str, str]: Dictionary mapping file paths to file contents
                
        Returns:
            The root Node_Dir of the tree
        """
        # Handle dictionary format (path -> content)
        if isinstance(files, dict):
            for filepath, content in files.items():
                self.add_file(filepath, content)
        # Handle list format (list of dicts with "path" and "contents"/"content")
        elif isinstance(files, list):
            for file_dict in files:
                if isinstance(file_dict, dict):
                    filepath = file_dict.get("path", "")
                    content = file_dict.get("contents", file_dict.get("content", ""))
                    self.add_file(filepath, content)
                else:
                    raise ValueError(f"Expected dict in list, got {type(file_dict)}")
        else:
            raise ValueError(f"Expected list or dict, got {type(files)}")
        
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
                # If file has VISIBLE_PATH state, use placeholder content
                if file_obj.state == State.VISIBLE_PATH:
                    file_dict[file_obj.path] = "[HIDDEN FILE CONTENTS, DO NOT EDIT]"
                else:
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
    
    def _print_simple_recursive(self, node: Node_Dir) -> None:
        """Recursively print attributes of all nodes.
        
        Args:
            node: Directory node to print attributes for
        """
        # Print directory node attributes
        print(f"Node_Dir: path='{node.path}', state={node.state.value}, "
              f"num_children={len(node.children)}, num_files={len(node.files)}")
        
        # Print file attributes
        for filename, file_obj in sorted(node.files.items()):
            print(f"  File: path='{file_obj.path}', state={file_obj.state.value}, "
                  f"content_length={len(file_obj.content)}")
        
        # Recursively print child directories
        for child_dir in sorted(node.children.values(), key=lambda x: x.path):
            self._print_simple_recursive(child_dir)
    
    def print_simple(self) -> None:
        """Print the attributes of each node in the tree."""
        if self.root.path == "" and not self.root.children and not self.root.files:
            print("(empty tree)")
            return
        
        self._print_simple_recursive(self.root)
    
    def change_dir_tree_state(self, state: State) -> int:
        """Change the state of the entire dir_tree and all its subdirectories and files.
        
        This function changes the state of the entire dir_tree (starting from root).
        Then it recursively goes and changes the state of all sub dirs and their files.
        
        Args:
            state: New state to set for the entire tree
            
        Returns:
            Total number of states updated (for both files and dirs)
        """
        return self._change_dir_state_recursive(self.root, state)
    
    def _change_dir_state_recursive(self, node: Node_Dir, state: State) -> int:
        """Recursively change the state of a directory and all its subdirectories and files.
        
        When the state is VISIBLE_PATH, all files in the directory and subdirectories
        will also be set to VISIBLE_PATH state.
        
        Args:
            node: Directory node to change state for
            state: New state to set (including VISIBLE_PATH which propagates to all files)
            
        Returns:
            Total number of states updated (directory + all subdirectories + all files)
        """
        count = 0
        
        # Change the state of this directory
        node.state = state
        count += 1
        
        # Change the state of all files in this directory
        for file_obj in node.files.values():
            file_obj.state = state
            count += 1
        
        # Recursively change the state of all subdirectories
        for child_dir in node.children.values():
            count += self._change_dir_state_recursive(child_dir, state)
        
        return count
    
    def change_dir_state(self, path: str, state: State) -> int:
        """Find a directory by exact path and change its state, recursively updating all subdirectories and files.
        
        When setting a directory to VISIBLE_PATH state, the state propagates to all files
        within that directory and its subdirectories as well.
        
        Args:
            path: Exact path to the directory (must match exactly)
            state: New state to set for the directory and all its contents
            
        Returns:
            Total number of states updated (directory + all subdirectories + all files)
            
        Raises:
            ValueError: If the directory path does not exist
        """
        parts = [p for p in path.split('/') if p != ""]
        
        # If empty path, change root state
        if not parts:
            return self._change_dir_state_recursive(self.root, state)
        
        # Navigate to the target directory
        current = self.root
        for dir_name in parts:
            if dir_name not in current.children:
                raise ValueError(f"Directory path '{path}' does not exist")
            current = current.children[dir_name]
        
        # Verify the path matches exactly
        if current.path != path:
            raise ValueError(f"Directory path '{path}' does not match exactly. Found path: '{current.path}'")
        
        # Change state recursively
        return self._change_dir_state_recursive(current, state)
    
    def change_file_state(self, path: str, state: State) -> int:
        """Find a file by exact path and change its state, then update parent directories.
        
        Args:
            path: Exact path to the file (must match exactly)
            state: New state to set for the file
            
        Returns:
            Number of states updated (file + parent directories, only counting actual changes)
            
        Raises:
            ValueError: If the file path does not exist
        """
        parts = path.split('/')
        filename = parts[-1]
        dir_parts = parts[:-1] if len(parts) > 1 else []
        
        # Navigate to the parent directory, keeping track of the path
        current = self.root
        parent_dirs = []  # Store parent directories in order (from root to parent of file)
        
        for dir_name in dir_parts:
            if dir_name == "":
                continue
            if dir_name not in current.children:
                raise ValueError(f"File path '{path}' does not exist: directory '{dir_name}' not found")
            parent_dirs.append(current)  # Store parent before moving down
            current = current.children[dir_name]
        
        # Find the file in the current directory
        if filename not in current.files:
            raise ValueError(f"File path '{path}' does not exist: file '{filename}' not found")
        
        file_obj = current.files[filename]
        
        # Verify the path matches exactly
        if file_obj.path != path:
            raise ValueError(f"File path '{path}' does not match exactly. Found path: '{file_obj.path}'")
        
        count = 0
        
        # Change the file's state only if it's different
        if file_obj.state != state:
            file_obj.state = state
            count += 1
        
        # Recursively go up the directories and change parent directory states
        # If file state is set to VISIBLE, all parent dirs need to be changed to VISIBLE if they were HIDDEN
        if state == State.VISIBLE:
            # Include the immediate parent directory (the one containing the file)
            parent_dirs.append(current)
            # Traverse up through parent directories (from immediate parent up to root)
            for parent_dir in reversed(parent_dirs):
                if parent_dir.state == State.HIDDEN:
                    parent_dir.state = State.VISIBLE
                    count += 1
        
        return count
    
    def _store_files_recursive(self, node: Node_Dir, output_dir: str) -> None:
        """Recursively store visible files from the tree to the filesystem.
        
        Args:
            node: Directory node to process
            output_dir: Base output directory path
        """
        # Skip if directory is hidden
        if node.state == State.HIDDEN:
            return
        
        # Create directory if it's not the root and doesn't exist
        if node.path != "":
            dir_path = os.path.join(output_dir, node.path)
            os.makedirs(dir_path, exist_ok=True)
        
        # Store visible files from this directory
        for filename, file_obj in node.files.items():
            if file_obj.state == State.VISIBLE:
                # Construct full file path
                if node.path != "":
                    file_path = os.path.join(output_dir, node.path, filename)
                else:
                    file_path = os.path.join(output_dir, filename)
                
                # Write file content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(file_obj.content)
                
                # Make .sh files executable
                if filename.endswith('.sh'):
                    os.chmod(file_path, os.stat(file_path).st_mode | stat.S_IEXEC)
        
        # Recursively process child directories
        for child_dir in node.children.values():
            self._store_files_recursive(child_dir, output_dir)
    
    def store_files(self, output_dir: str) -> str:
        """Store files and their contents into the provided output directory.
        
        Only visible files are stored. If a *.sh file is stored, it is made executable
        with chmod +x.
        
        Args:
            output_dir: Directory path where files should be stored
            
        Returns:
            The absolute path where files were stored
        """
        # Create output directory if it doesn't exist
        abs_output_dir = os.path.abspath(output_dir)
        os.makedirs(abs_output_dir, exist_ok=True)
        
        # Recursively store all visible files
        self._store_files_recursive(self.root, abs_output_dir)
        
        return abs_output_dir

