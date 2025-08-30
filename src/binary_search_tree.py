"""
This module contains the implementation of a Binary Search Tree (BST).

A BST is a tree-based data structure where each node holds a value, and its
left and right children satisfy the BST property: all values in the left
subtree are less than the node's value, and all values in the right subtree
are greater. This allows for efficient search, insertion, and deletion operations,
with a time complexity of O(log n) on average.
"""
from typing import Any, Optional

class Node:
    """
    A node in a Binary Search Tree.

    Attributes:
        data: The value stored in the node.
        left: A pointer to the left child node.
        right: A pointer to the right child node.
    """
    def __init__(self, data: Any):
        """Initializes a new node."""
        self.data: Any = data
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def __repr__(self) -> str:
        """Provides a string representation for debugging."""
        return f"Node({self.data})"

class BinarySearchTree:
    """
    A Binary Search Tree implementation with common operations.

    Attributes:
        root: The root node of the tree.
    """
    def __init__(self):
        """Initializes an empty BST."""
        self.root: Optional[Node] = None

    def insert(self, data: Any) -> None:
        """
        Inserts a new node with the given data into the tree.

        Time Complexity: O(log n) on average, O(n) in the worst case (unbalanced tree).
        Args:
            data: The value to be inserted.
        """
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: Optional[Node], data: Any) -> Node:
        """Recursive helper function for insertion."""
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # If data is equal, do nothing (duplicates are not allowed in this implementation)
        
        return node

    def search(self, data: Any) -> Optional[Node]:
        """
        Searches for a node with the given data.

        Time Complexity: O(log n) on average, O(n) in the worst case.
        Args:
            data: The value to search for.
        Returns:
            The node if found, otherwise None.
        """
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node: Optional[Node], data: Any) -> Optional[Node]:
        """Recursive helper function for search."""
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self, data: Any) -> None:
        """
        Deletes a node with the given data from the tree.

        Time Complexity: O(log n) on average, O(n) in the worst case.
        Args:
            data: The value to be deleted.
        """
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node: Optional[Node], data: Any) -> Optional[Node]:
        """Recursive helper function for deletion."""
        if node is None:
            return node
        
        # Traverse the tree to find the node to delete
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else: # Found the node to delete
            # Case 1: Node with no children or only one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 2: Node with two children. Find the inorder successor
            # (the smallest node in the right subtree)
            temp = self._find_min_node(node.right)
            # Copy the inorder successor's data to this node
            node.data = temp.data
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, temp.data)
        
        return node

    def _find_min_node(self, node: Node) -> Node:
        """Helper to find the smallest node in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self) -> list:
        """
        Performs an in-order traversal (left, root, right) of the tree.

        Returns:
            A list of nodes' data in sorted order.
        """
        result = []
        self._in_order_recursive(self.root, result)
        return result
    
    def _in_order_recursive(self, node: Optional[Node], result: list) -> None:
        """Recursive helper for in-order traversal."""
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.data)
            self._in_order_recursive(node.right, result)

    def pre_order_traversal(self) -> list:
        """
        Performs a pre-order traversal (root, left, right) of the tree.

        Returns:
            A list of nodes' data in pre-order.
        """
        result = []
        self._pre_order_recursive(self.root, result)
        return result
    
    def _pre_order_recursive(self, node: Optional[Node], result: list) -> None:
        """Recursive helper for pre-order traversal."""
        if node:
            result.append(node.data)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order_traversal(self) -> list:
        """
        Performs a post-order traversal (left, right, root) of the tree.

        Returns:
            A list of nodes' data in post-order.
        """
        result = []
        self._post_order_recursive(self.root, result)
        return result
    
    def _post_order_recursive(self, node: Optional[Node], result: list) -> None:
        """Recursive helper for post-order traversal."""
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.data)

    def __len__(self) -> int:
        """Returns the number of nodes in the tree."""
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node: Optional[Node]) -> int:
        """Recursive helper to count nodes."""
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
