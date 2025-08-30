import sys
import os
import unittest

# Get the absolute path of the current directory (the project root)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Add the 'src' directory to the Python path
# This allows tests to import modules from src/
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))

def run_all_tests():
    """
    Discovers and runs all tests within the 'tests' directory.
    """
    print("Running all tests...")
    
    # Define the directory where tests are located
    test_dir = os.path.join(PROJECT_ROOT, 'tests')
    
    # Use unittest's TestLoader to discover all test files
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=test_dir, pattern='test_*.py')
    
    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed.")
        sys.exit(1)

if __name__ == '__main__':
    run_all_tests()
