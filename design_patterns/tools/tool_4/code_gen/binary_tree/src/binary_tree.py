class TreeNode:
    """A node in a binary tree."""
    
    def __init__(self, value: int):
        """Initialize a tree node with a value."""
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Binary Search Tree implementation with insert, search, and traversal operations."""
    
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None
    
    def insert(self, value: int) -> None:
        """Insert a value into the binary tree."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        """Recursively insert a value into the tree."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value: int) -> bool:
        """Search for a value in the tree."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: TreeNode, value: int) -> bool:
        """Recursively search for a value in the tree."""
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self) -> list:
        """Return list of values in inorder (left, root, right)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: TreeNode, result: list) -> None:
        """Recursively perform inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> list:
        """Return list of values in preorder (root, left, right)."""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: TreeNode, result: list) -> None:
        """Recursively perform preorder traversal."""
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> list:
        """Return list of values in postorder (left, right, root)."""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: TreeNode, result: list) -> None:
        """Recursively perform postorder traversal."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
