# tests\data_structures\fundamentals\linked_lists\test_doubly_linked_list.py

"""
to test run the below on the root dir
pytest tests/data_structures/fundamentals/linked_lists/test_singly_doubly_list.py
"""

import unittest
import sys
import os
import time

# # Add the parent directory to the system path to resolve the 'dsa' import
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_structures.fundamentals.linked_lists.doubly_linked_list import DoublyLinkedList, Node

class TestDoublyLinkedList(unittest.TestCase):
    
    def setUp(self):
        """Set up a new, empty list for each test."""
        self.dll = DoublyLinkedList()
        self.output = []

    def _log_status(self, test_name, status):
        """Helper to log test status."""
        self.output.append(f"    - {test_name}: {status}")

    def test_len(self):
        """Test the __len__ method. 📏"""
        self.assertEqual(len(self.dll), 0)
        self.dll.append(1)
        self.assertEqual(len(self.dll), 1)
        self.dll.append(2)
        self.assertEqual(len(self.dll), 2)
        self.dll.delete(1)
        self.assertEqual(len(self.dll), 1)
        self.dll.prepend(0)
        self.assertEqual(len(self.dll), 2)
        self._log_status("Test Length", "✅ PASSED")

    def test_contains(self):
        """Test the __contains__ method. 🔍"""
        self.dll.append(1)
        self.dll.append(2)
        self.assertTrue(1 in self.dll)
        self.assertTrue(2 in self.dll)
        self.assertFalse(3 in self.dll)
        self.dll.delete(1)
        self.assertFalse(1 in self.dll)
        self._log_status("Test Contains", "✅ PASSED")

    def test_find(self):
        """Test the find method. 🔎"""
        self.dll.append(1)
        self.dll.append(2)
        found_node = self.dll.find(1)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.data, 1)
        self.assertIsNone(self.dll.find(99))
        self._log_status("Test Find", "✅ PASSED")

    def test_is_empty(self):
        """Test the is_empty method. 🗑️"""
        self.assertTrue(self.dll.is_empty())
        self.dll.append(1)
        self.assertFalse(self.dll.is_empty())
        self.dll.delete(1)
        self.assertTrue(self.dll.is_empty())
        self._log_status("Test Is Empty", "✅ PASSED")

    def test_append_on_empty_list(self):
        """Test appending the first element to an empty list. ➕"""
        self.dll.append(1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertIsNone(self.dll.head.prev)
        self.assertIsNone(self.dll.head.next)
        self.assertFalse(self.dll.is_empty())
        self._log_status("Test Append on Empty List", "✅ PASSED")

    def test_append_on_non_empty_list(self):
        """Test appending to an existing list. ➕➕"""
        self.dll.append(1)
        self.dll.append(2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 2)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.prev.data, 1)
        self.assertIsNone(self.dll.head.prev)
        self.assertIsNone(self.dll.tail.next)
        self._log_status("Test Append on Non-Empty List", "✅ PASSED")

    def test_prepend(self):
        """Test prepending to a list. ➡️"""
        self.dll.append(1)
        self.dll.prepend(0)
        self.assertEqual(self.dll.head.data, 0)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertEqual(self.dll.head.next.data, 1)
        self.assertEqual(self.dll.tail.prev.data, 0)
        self._log_status("Test Prepend", "✅ PASSED")

    def test_delete_head(self):
        """Test deleting the head node. ✂️➡️"""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.delete(1)
        self.assertEqual(self.dll.head.data, 2)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(self.dll.tail.data, 2)
        self.assertEqual(len(self.dll), 1)
        self._log_status("Test Delete Head", "✅ PASSED")
        
    def test_delete_tail(self):
        """Test deleting the tail node. ⬅️✂️"""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.delete(2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertIsNone(self.dll.tail.next)
        self.assertEqual(len(self.dll), 1)
        self._log_status("Test Delete Tail", "✅ PASSED")
        
    def test_delete_middle_node(self):
        """Test deleting a node from the middle. ✂️"""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.delete(2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 3)
        self.assertEqual(self.dll.head.next.data, 3)
        self.assertEqual(self.dll.tail.prev.data, 1)
        self.assertEqual(len(self.dll), 2)
        self._log_status("Test Delete Middle Node", "✅ PASSED")

    def test_delete_non_existent_value(self):
        """Test deleting a value that is not in the list. 🚫"""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.delete(99)
        self.assertEqual(len(self.dll), 2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 2)
        self._log_status("Test Delete Non-existent Value", "✅ PASSED")

    def test_insert_after(self):
        """Test the insert_after method. 🩹"""
        self.dll.append(1)
        self.dll.append(3)
        node_to_insert_after = self.dll.head
        self.dll.insert_after(node_to_insert_after, 2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.head.next.next.data, 3)
        self.assertEqual(self.dll.tail.data, 3)
        self._log_status("Test Insert After", "✅ PASSED")
        
    def test_insert_after_raises_error(self):
        """Test that insert_after raises a ValueError for a None node. 🚨"""
        with self.assertRaises(ValueError):
            self.dll.insert_after(None, "invalid")
        self._log_status("Test Insert After with Error", "✅ PASSED")

    def test_reverse(self):
        """Test the reverse method on a list. 🔄"""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.reverse()
        self.assertEqual(self.dll.head.data, 3)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertEqual(self.dll.tail.prev.data, 2)
        self.assertEqual(list(node.data for node in self.dll), [3, 2, 1])
        self._log_status("Test Reverse", "✅ PASSED")

    def test_multiple_data_types(self):
        """Test the list with different data types. 🧪"""
        class CustomObject:
            def __init__(self, name):
                self.name = name
            def __eq__(self, other):
                return isinstance(other, CustomObject) and self.name == other.name
        
        # Test with integers
        self.dll.append(10)
        self.dll.append(20)
        self.assertEqual(self.dll.head.data, 10)
        self.dll.delete(20)
        self.assertEqual(self.dll.head.data, 10)

        # Test with strings
        self.dll.append("Hello")
        self.dll.append("World")
        self.assertEqual(self.dll.tail.data, "World")
        
        # Test with custom objects
        obj1 = CustomObject("A")
        obj2 = CustomObject("B")
        self.dll.append(obj1)
        self.dll.append(obj2)
        
        self.assertEqual(self.dll.tail.data, obj2)
        self.dll.delete(obj1)
        self.assertEqual(self.dll.tail.prev.data, "World")
        self._log_status("Test Multiple Data Types", "✅ PASSED")

class TestRunner:
    """A class to run tests with visual feedback and delays."""
    
    def run_tests_with_visuals(self, test_class):
        """
        Runs all test methods of a given class with simulated delays and visual logs.
        """
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
        
        print("🚀 Starting DoublyLinkedList Test Suite...")
        print("===========================================")
        time.sleep(.5)

        total_tests = suite.countTestCases()
        passed_tests = 0
        
        for test in suite:
            test_name = test.id().split('.')[-1]
            doc_string = getattr(test, test_name).__doc__.strip() if getattr(test, test_name).__doc__ else "No description"
            
            print(f"\n🔬 Running test: {doc_string}")
            time.sleep(.5)
            
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
            print("🎉 All tests passed successfully! The DoublyLinkedList implementation is robust.")
        else:
            print("⚠️ Some tests failed. Please review the implementation.")

if __name__ == '__main__':
    # Use the custom TestRunner for a more visual experience
    runner = TestRunner()
    runner.run_tests_with_visuals(TestDoublyLinkedList)
