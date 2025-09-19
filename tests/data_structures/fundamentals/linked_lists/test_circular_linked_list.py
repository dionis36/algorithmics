# tests\data_structures\fundamentals\linked_lists\test_circular_linked_list.py

"""
To test run the below on the root directory
pytest tests/data_structures/fundamentals/linked_lists/test_circular_linked_list.py
"""

import unittest
import sys
import os
import time

from src.data_structures.fundamentals.linked_lists.circular_linked_list import CircularLinkedList, Node

class TestCircularLinkedList(unittest.TestCase):
    
    def setUp(self):
        """Set up a new, empty list for each test."""
        self.cll = CircularLinkedList()
        self.output = []

    def test_len(self):
        """Test the __len__ method. 📏"""
        self.assertEqual(len(self.cll), 0)
        self.cll.append(1)
        self.assertEqual(len(self.cll), 1)
        self.cll.append(2)
        self.assertEqual(len(self.cll), 2)
        self.cll.delete(1)
        self.assertEqual(len(self.cll), 1)

    def test_is_empty(self):
        """Test the is_empty method. 🔍"""
        self.assertTrue(self.cll.is_empty())
        self.cll.append(1)
        self.assertFalse(self.cll.is_empty())

    def test_append(self):
        """Test the append method. ➕"""
        self.cll.append(1)
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.head.next.data, 1) # Points back to self
        self.cll.append(2)
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.head.next.data, 2)
        self.assertEqual(self.cll.head.next.next.data, 1) # 2's next points to head
        self.assertEqual(len(self.cll), 2)

    def test_prepend(self):
        """Test the prepend method. ➕"""
        self.cll.prepend(1)
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.head.next.data, 1) # Points back to self
        self.cll.prepend(2)
        self.assertEqual(self.cll.head.data, 2)
        self.assertEqual(self.cll.head.next.data, 1)
        self.assertEqual(self.cll.head.next.next.data, 2) # 1's next points to new head 2
        self.assertEqual(len(self.cll), 2)

    def test_delete_head_and_single_node(self):
        """Test deletion of the head node and a single node list. ✂️"""
        self.cll.append(1)
        self.cll.delete(1)
        self.assertTrue(self.cll.is_empty())
        
        self.cll.append(1)
        self.cll.append(2)
        self.cll.delete(1)
        self.assertEqual(self.cll.head.data, 2)
        self.assertEqual(self.cll.head.next.data, 2) # Points back to self

    def test_delete_middle_node(self):
        """Test deletion of a node from the middle of the list. ✂️"""
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        self.cll.delete(2)
        self.assertEqual(len(self.cll), 2)
        
        # Verify that the list is now 1 -> 3 -> 1
        current = self.cll.head
        self.assertEqual(current.data, 1)
        current = current.next
        self.assertEqual(current.data, 3)
        current = current.next
        self.assertEqual(current.data, 1)

    def test_delete_tail_node(self):
        """Test deletion of the tail node. ✂️"""
        self.cll.append(1)
        self.cll.append(2)
        self.cll.delete(2)
        self.assertEqual(len(self.cll), 1)
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.head.next.data, 1) # Last node now points to self

    def test_delete_non_existent(self):
        """Test deletion of a value not in the list. ❌"""
        self.cll.append(1)
        deleted = self.cll.delete(99)
        self.assertIsNone(deleted)
        self.assertEqual(len(self.cll), 1)

    def test_find(self):
        """Test the find method. 🔍"""
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        found_node = self.cll.find(2)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 2)
        self.assertIsNone(self.cll.find(99))

    def test_repr(self):
        """Test the __repr__ method. 📝"""
        self.assertEqual(repr(self.cll), "CircularLinkedList()")
        self.cll.append(1)
        self.cll.append(2)
        self.assertEqual(repr(self.cll), "CircularLinkedList(1 -> 2 -> ...)")

    def test_iteration(self):
        """Test list iteration using a for loop. 🔄"""
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        
        values = [node.data for node in self.cll]
        self.assertEqual(values, [1, 2, 3])

class TestRunner:
    """A custom test runner for a more visual and structured output."""
    def run_tests_with_visuals(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCircularLinkedList)
        total_tests = suite.countTestCases()
        passed_tests = 0
        
        print("===========================================")
        print("         Circular Linked List Test Suite")
        print("===========================================\n")
        
        for test in suite:
            test_name = test.id().split('.')[-1]
            doc_string = getattr(test, test_name).__doc__.strip() if getattr(test, test_name).__doc__ else "No description"
            
            print(f"🔬 Running test: {doc_string}")
            time.sleep(.5) # Add a small delay for a better visual experience
            
            try:
                result = unittest.TestResult()
                test.run(result)
                if result.wasSuccessful():
                    print(f"    - Status: ✅ PASSED")
                    passed_tests += 1
                else:
                    print(f"    - Status: ❌ FAILED")
                    for failure in result.failures:
                        print(f"      - Failure Details: {failure[1]}")
            except Exception as e:
                print(f"    - Status: ❌ FAILED with an exception: {e}")

        print("\n===========================================")
        print("✅ Test Suite Completed! ✅")
        print(f"Summary: {passed_tests} out of {total_tests} tests passed.")
        if passed_tests == total_tests:
            print("🎉 All tests passed successfully! The CircularLinkedList implementation is robust.")
        else:
            print("⚠️ Some tests failed. Please review the implementation.")

if __name__ == '__main__':
    # Use the custom TestRunner for a more visual experience
    runner = TestRunner()
    runner.run_tests_with_visuals()
