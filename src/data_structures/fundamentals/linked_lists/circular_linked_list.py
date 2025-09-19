"""
This module contains the implementation of a Circular Linked List, a variation of a
singly linked list. This version adheres to professional standards, including
robust error handling, standard data structure methods, and type hints.

A Circular Linked List is a linear data structure where the last node points back
to the first node, forming a circle. This unique structure allows for seamless
traversal without a defined end, making it useful for applications like round-robin
scheduling, music playlists, or continuous data streams.
"""

# src\data_structures\fundamentals\linked_lists\circular_linked_list.py

from typing import Any, Iterable, Optional

class Node:
    """
    A node in a circular linked list.

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

class CircularLinkedList:
    """
    A circular linked list implementation with a complete set of standard data
    structure methods.

    Attributes:
        head: The head node of the list.
        size: The number of elements in the list.
    """
    def __init__(self) -> None:
        """Initializes a new, empty circular linked list."""
        self.head: Optional[Node] = None
        self.size: int = 0

    def __len__(self) -> int:
        """
        Returns the number of elements in the list.

        Time Complexity: O(1)
        """
        return self.size

    def __contains__(self, value: Any) -> bool:
        """
        Checks if the list contains a given value.

        Time Complexity: O(n)

        Args:
            value: The value to search for.

        Returns:
            bool: True if the value is in the list, False otherwise.
        """
        if self.is_empty():
            return False

        current = self.head
        while True:
            if current.data == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def __repr__(self) -> str:
        """
        Provides a clear string representation of the list for debugging.

        Returns:
            str: A string showing the list's contents.
        """
        if self.is_empty():
            return "CircularLinkedList()"

        nodes = []
        current = self.head
        while True:
            nodes.append(repr(current.data))
            current = current.next
            if current == self.head:
                break
        return "CircularLinkedList(" + " -> ".join(nodes) + " -> ...)"

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.

        Time Complexity: O(1)

        Returns:
            bool: True if the list has no elements, False otherwise.
        """
        return self.size == 0

    def append(self, value: Any) -> None:
        """
        Adds a new node to the end of the list.

        Time Complexity: O(n) to find the tail.

        Args:
            value: The value to add.
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1

    def prepend(self, value: Any) -> None:
        """
        Adds a new node to the beginning of the list.

        Time Complexity: O(n) to find the tail.

        Args:
            value: The value to add.
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def find(self, value: Any) -> Optional[Node]:
        """
        Finds and returns the first node containing the specified value.

        Time Complexity: O(n)

        Args:
            value: The value to search for.

        Returns:
            Node: The first node containing the value, or None if not found.
        """
        if self.is_empty():
            return None

        current = self.head
        while True:
            if current.data == value:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def delete(self, value: Any) -> Optional[Node]:
        """
        Deletes the first occurrence of a node with the specified value.

        Time Complexity: O(n)

        Args:
            value: The value of the node to delete.

        Returns:
            Node: The deleted node, or None if not found.
        """
        if self.is_empty():
            return None

        # Case 1: Deleting the head node
        if self.head.data == value:
            # Find the tail node
            if self.size == 1:
                deleted_node = self.head
                self.head = None
                self.size = 0
                return deleted_node
            
            current = self.head
            while current.next != self.head:
                current = current.next
            
            deleted_node = self.head
            current.next = self.head.next
            self.head = self.head.next
            self.size -= 1
            return deleted_node

        # Case 2: Deleting a node from the middle or tail
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == value:
                prev.next = current.next
                self.size -= 1
                return current
        return None

    def __iter__(self) -> Iterable[Node]:
        """
        Allows the list to be iterated over in a for loop.
        """
        if self.is_empty():
            return
        
        current = self.head
        while True:
            yield current
            current = current.next
            if current == self.head:
                break
