"""
This module contains the implementation of a Singly Linked List, a foundational
data structure. This version adheres to professional standards, including robust
error handling, standard data structure methods, and type hints.

A Singly Linked List is a linear data structure where each element, called a node,
contains a value and a pointer to the next node in the sequence. Unlike a doubly
linked list, it does not maintain a pointer to the previous node. This makes
some operations, like backward traversal, impossible but simplifies the
structure and reduces memory overhead.
"""
from typing import Any, Iterable, Optional

class Node:
    """
    A node in a singly linked list.

    Attributes:
        data: The value stored in the node. Can be any data type.
        next: A pointer to the next node in the list. Defaults to None.
    """
    def __init__(self, data: Any) -> None:
        """
        Initializes a new node with the given data.

        Args:
            data: The value to be stored in the node.
        """
        self.data: Any = data
        self.next: Optional[Node] = None

class SinglyLinkedList:
    """
    A singly linked list implementation with a complete set of standard data
    structure methods.

    Attributes:
        head: The head node of the list.
        tail: The tail node of the list. Maintaining a tail pointer allows for
              O(1) appends.
    """
    def __init__(self) -> None:
        """
        Initializes an empty singly linked list.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def __len__(self) -> int:
        """
        Returns the number of nodes in the list.

        Time Complexity: O(1) due to the maintained size counter.

        Returns:
            int: The number of nodes.
        """
        return self.size

    def __contains__(self, value: Any) -> bool:
        """
        Checks if a value is present in the list.

        Time Complexity: O(n)

        Args:
            value: The value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        return self.find(value) is not None

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None

    def append(self, data: Any) -> None:
        """
        Appends a new node with the given data to the end of the list.

        Time Complexity: O(1) due to the tail pointer.

        Args:
            data: The data for the new node.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data: Any) -> None:
        """
        Adds a new node with the given data to the beginning of the list.

        Time Complexity: O(1)

        Args:
            data: The data for the new node.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def delete(self, value: Any) -> None:
        """
        Deletes the first occurrence of a node with the given value.

        Time Complexity: O(n) in the worst case.

        Args:
            value: The data value of the node to delete.
        """
        if self.is_empty():
            return

        # Case 1: Deleting the head node
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:  # The list becomes empty
                self.tail = None
            self.size -= 1
            return

        # Case 2: Deleting a middle or tail node
        current = self.head
        while current.next:
            if current.next.data == value:
                # Update the tail if we are deleting the last node
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def insert_after(self, node: Node, value: Any) -> None:
        """
        Inserts a new node with the given value after a specified existing node.

        Time Complexity: O(1) if the node reference is already available.

        Args:
            node: The existing node after which to insert the new node.
            value: The data for the new node.

        Raises:
            ValueError: If the provided node is None.
        """
        if node is None:
            raise ValueError("Cannot insert after a None node.")
            
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        self.size += 1
        
        # If we inserted after the current tail, the new node becomes the tail
        if new_node.next is None:
            self.tail = new_node

    def find(self, value: Any) -> Optional[Node]:
        """
        Finds and returns the first node containing the specified value.

        Time Complexity: O(n)

        Args:
            value: The value to search for.

        Returns:
            Node: The first node containing the value, or None if not found.
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None
        
    def __iter__(self) -> Iterable[Node]:
        """
        Allows the list to be iterated over in a for loop.
        """
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        """
        Provides a clear string representation of the list for debugging.
        """
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return " -> ".join(nodes)