"""
This module contains the implementation of a Doubly Linked List, a foundational
data structure. This version is designed to meet professional standards,
including robust error handling, standard data structure methods, and type hints.

A Doubly Linked List is a linear data structure where each element, called a node,
contains a value, a pointer to the next node, and a pointer to the previous node.
This structure allows for efficient O(1) time complexity for insertions and deletions
at both the head and tail.
"""

# src\data_structures\fundamentals\linked_lists\doubly_linked_list.py

from typing import Any, Iterable, Optional

class Node:
    """
    A node in a doubly linked list.

    Attributes:
        data: The value stored in the node. Can be any data type.
        next: A pointer to the next node in the list. Defaults to None.
        prev: A pointer to the previous node in the list. Defaults to None.
    """
    def __init__(self, data: Any) -> None:
        """
        Initializes a new node with the given data.

        Args:
            data: The value to be stored in the node.
        """
        self.data: Any = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class DoublyLinkedList:
    """
    A doubly linked list implementation with a complete set of standard data
    structure methods.

    Attributes:
        head: The head node of the list.
        tail: The tail node of the list.
    """
    def __init__(self) -> None:
        """
        Initializes an empty doubly linked list.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __len__(self) -> int:
        """
        Returns the number of nodes in the list.

        Time Complexity: O(n)
        Note: For O(1) time complexity, a 'size' counter could be maintained.

        Returns:
            int: The number of nodes.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

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

        Time Complexity: O(1)

        Args:
            data: The data for the new node.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

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
            self.head.prev = new_node
            self.head = new_node

    def delete(self, value: Any) -> None:
        """
        Deletes the first occurrence of a node with the given value.

        Time Complexity: O(n) in the worst case.

        Args:
            value: The data value of the node to delete.
        """
        if self.is_empty():
            return

        current = self.head
        while current:
            if current.data == value:
                # Case 1: Deleting the head node
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:  # The list becomes empty
                        self.tail = None
                # Case 2: Deleting the tail node
                elif current.next is None:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                # Case 3: Deleting a middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_after(self, node: Node, value: Any) -> None:
        """
        Inserts a new node with the given value after a specified existing node.

        This operation has a time complexity of O(1) if the node reference is
        already available.

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
        new_node.prev = node
        
        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node
            
        node.next = new_node

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

    def reverse(self) -> None:
        """
        Reverses the list in-place by swapping the next and prev pointers for each node.

        Time Complexity: O(n), as it requires visiting every node.
        """
        if self.is_empty():
            return
            
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp

    def __iter__(self) -> Iterable[Node]:
        """
        Allows the list to be iterated over in a for loop from head to tail.
        """
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        """
        Provides a clear string representation of the list for debugging and printing.
        """
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return " <-> ".join(nodes)
