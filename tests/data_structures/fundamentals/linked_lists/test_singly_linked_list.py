import unittest
import sys
import os
import time

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithmics.src.data_structures.fundamentals.linked_lists.singly_linked_list import SinglyLinkedList, Node

class TestSinglyLinkedList(unittest.TestCase):
    
    def setUp(self):
        """Set up a new, empty list for each test."""
        self.sll = SinglyLinkedList()

    def test_len(self):
        """Test the __len__ method. 📏"""
        self.assertEqual(len(self.sll), 0)
        self.sll.append(1)
        self.assertEqual(len(self.sll), 1)
        self.sll.prepend(0)
        self.assertEqual(len(self.sll), 2)
        self.sll.delete(0)
        self.assertEqual(len(self.sll), 1)

    def test_contains(self):
        """Test the __contains__ method. 🔍"""
        self.sll.append(1)
        self.sll.append(2)
        self.assertTrue(1 in self.sll)
        self.assertTrue(2 in self.sll)
        self.assertFalse(3 in self.sll)
        self.sll.delete(1)
        self.assertFalse(1 in self.sll)

    def test_find(self):
        """Test the find method. 🔎"""
        self.sll.append(1)
        self.sll.append(2)
        found_node = self.sll.find(1)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.data, 1)
        self.assertIsNone(self.sll.find(99))

    def test_is_empty(self):
        """Test the is_empty method. 🗑️"""
        self.assertTrue(self.sll.is_empty())
        self.sll.append(1)
        self.assertFalse(self.sll.is_empty())
        self.sll.delete(1)
        self.assertTrue(self.sll.is_empty())

    def test_append_on_empty_list(self):
        """Test appending the first element to an empty list. ➕"""
        self.sll.append(1)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.tail.data, 1)
        self.assertIsNone(self.sll.head.next)
        self.assertFalse(self.sll.is_empty())
        self.assertEqual(len(self.sll), 1)

    def test_append_on_non_empty_list(self):
        """Test appending to an existing list. ➕➕"""
        self.sll.append(1)
        self.sll.append(2)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.tail.data, 2)
        self.assertEqual(self.sll.head.next.data, 2)
        self.assertIsNone(self.sll.tail.next)
        self.assertEqual(len(self.sll), 2)
        
    def test_prepend(self):
        """Test prepending to a list. ➡️"""
        self.sll.append(1)
        self.sll.prepend(0)
        self.assertEqual(self.sll.head.data, 0)
        self.assertEqual(self.sll.tail.data, 1)
        self.assertEqual(self.sll.head.next.data, 1)
        self.assertEqual(len(self.sll), 2)

    def test_delete_head(self):
        """Test deleting the head node. ✂️➡️"""
        self.sll.append(1)
        self.sll.append(2)
        self.sll.delete(1)
        self.assertEqual(self.sll.head.data, 2)
        self.assertEqual(self.sll.tail.data, 2)
        self.assertEqual(len(self.sll), 1)

    def test_delete_tail(self):
        """Test deleting the tail node. ⬅️✂️"""
        self.sll.append(1)
        self.sll.append(2)
        self.sll.delete(2)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.tail.data, 1)
        self.assertIsNone(self.sll.tail.next)
        self.assertEqual(len(self.sll), 1)
        
    def test_delete_middle_node(self):
        """Test deleting a node from the middle. ✂️"""
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.sll.delete(2)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.tail.data, 3)
        self.assertEqual(self.sll.head.next.data, 3)
        self.assertEqual(len(self.sll), 2)

    def test_delete_non_existent_value(self):
        """Test deleting a value that is not in the list. 🚫"""
        self.sll.append(1)
        self.sll.append(2)
        self.sll.delete(99)
        self.assertEqual(len(self.sll), 2)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.tail.data, 2)

    def test_insert_after(self):
        """Test the insert_after method. 🩹"""
        self.sll.append(1)
        self.sll.append(3)
        node_to_insert_after = self.sll.head
        self.sll.insert_after(node_to_insert_after, 2)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.head.next.data, 2)
        self.assertEqual(self.sll.head.next.next.data, 3)
        self.assertEqual(self.sll.tail.data, 3)
        self.assertEqual(len(self.sll), 3)

    def test_insert_after_raises_error(self):
        """Test that insert_after raises a ValueError for a None node. 🚨"""
        with self.assertRaises(ValueError):
            self.sll.insert_after(None, "invalid")

    def test_multiple_data_types(self):
        """Test the list with different data types. 🧪"""
        class CustomObject:
            def __init__(self, name):
                self.name = name
            def __eq__(self, other):
                return isinstance(other, CustomObject) and self.name == other.name
        
        # Test with integers
        self.sll.append(10)
        self.sll.append(20)
        self.assertEqual(self.sll.head.data, 10)
        self.sll.delete(20)
        self.assertEqual(self.sll.head.data, 10)

        # Test with strings
        self.sll.append("Hello")
        self.sll.append("World")
        self.assertEqual(self.sll.tail.data, "World")
        
        # Test with custom objects
        obj1 = CustomObject("A")
        obj2 = CustomObject("B")
        self.sll.append(obj1)
        self.sll.append(obj2)
        
        self.assertEqual(self.sll.tail.data, obj2)
        self.sll.delete(obj1)
        self.assertEqual(self.sll.tail.data, obj2)

    def test_insert_after_tail(self):
        """Test inserting after the tail node. ➡️"""
        self.sll.append(1)
        self.sll.append(2)
        self.sll.insert_after(self.sll.tail, 3)
        self.assertEqual(self.sll.tail.data, 3)
        self.assertEqual(self.sll.head.next.next.data, 3)
        self.assertEqual(len(self.sll), 3)

    def test_delete_only_node(self):
        """Test deleting the only node in the list. 💥"""
        self.sll.append(1)
        self.sll.delete(1)
        self.assertTrue(self.sll.is_empty())
        self.assertIsNone(self.sll.head)
        self.assertIsNone(self.sll.tail)
        self.assertEqual(len(self.sll), 0)

# The following code is for running the tests with visual output.
class TestRunner:
    """A class to run tests with visual feedback and delays."""
    
    def run_tests_with_visuals(self, test_class):
        """
        Runs all test methods of a given class with simulated delays and visual logs.
        """
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        print("🚀 Starting SinglyLinkedList Test Suite...")
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
            print("🎉 All tests passed successfully! The SinglyLinkedList implementation is robust.")
        else:
            print("⚠️ Some tests failed. Please review the implementation.")

if __name__ == '__main__':
    # Use the custom TestRunner for a more visual experience
    runner = TestRunner()
    runner.run_tests_with_visuals(TestSinglyLinkedList)