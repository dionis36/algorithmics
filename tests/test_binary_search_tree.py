import unittest
import sys
import os

# The master test runner will handle the path.
# Add the parent directory of the current file to the system path to resolve the 'binary_search_tree' import.
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

from binary_search_tree import BinarySearchTree, Node

class TestBinarySearchTree(unittest.TestCase):
    """
    A unit test suite for the BinarySearchTree implementation.
    """
    def setUp(self):
        """Set up a new, empty tree for each test."""
        self.bst = BinarySearchTree()

    def test_insert_and_search(self):
        """Test basic insertion and search functionality."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        
        self.assertIsNotNone(self.bst.search(50))
        self.assertIsNotNone(self.bst.search(30))
        self.assertIsNotNone(self.bst.search(70))
        self.assertIsNone(self.bst.search(99))

    def test_in_order_traversal(self):
        """Test in-order traversal, which should return a sorted list."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.assertEqual(self.bst.in_order_traversal(), [20, 30, 40, 50, 70])
        
    def test_pre_order_traversal(self):
        """Test pre-order traversal (root, left, right)."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.assertEqual(self.bst.pre_order_traversal(), [50, 30, 20, 40, 70])

    def test_post_order_traversal(self):
        """Test post-order traversal (left, right, root)."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.assertEqual(self.bst.post_order_traversal(), [20, 40, 30, 70, 50])

    def test_delete_leaf_node(self):
        """Test deleting a node with no children."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.delete(30)
        self.assertIsNone(self.bst.search(30))
        self.assertEqual(self.bst.in_order_traversal(), [50, 70])
        
    def test_delete_node_with_one_child(self):
        """Test deleting a node with one child."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.delete(30)
        self.assertIsNone(self.bst.search(30))
        self.assertEqual(self.bst.in_order_traversal(), [20, 50, 70])

    def test_delete_node_with_two_children(self):
        """Test deleting a node with two children."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)
        self.bst.delete(70)
        self.assertIsNone(self.bst.search(70))
        self.assertEqual(self.bst.in_order_traversal(), [20, 30, 40, 50, 60, 80])

    def test_delete_root_node(self):
        """Test deleting the root node with a two-child case."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)
        self.bst.delete(50)
        self.assertIsNone(self.bst.search(50))
        # The new root should be the in-order successor (60)
        self.assertEqual(self.bst.root.data, 60)
        self.assertEqual(self.bst.in_order_traversal(), [20, 30, 40, 60, 70, 80])

    def test_delete_non_existent_value(self):
        """Test that deleting a non-existent value does not change the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.delete(99)
        self.assertEqual(len(self.bst.in_order_traversal()), 2)
