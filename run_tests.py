#!/usr/bin/env python3
"""
Master Test Runner for the Algorithmics library.
This CLI tool allows you to run all tests or selectively run tests for specific components.
"""

import unittest
import argparse
import os
import sys
import glob

def discover_and_run_tests(test_pattern="test_*.py", specific_dir=None):
    """
    Discovers and runs tests based on a pattern and optional directory.
    
    Args:
        test_pattern (str): The pattern to match test files.
        specific_dir (str): The specific directory to look in (relative to 'tests/'). 
                            If None, runs all tests.
    """
    
    # Start in the project root directory
    start_dir = os.path.join(os.path.dirname(__file__), 'tests')
    
    # If a specific directory is provided, adjust the start directory
    if specific_dir:
        start_dir = os.path.join(start_dir, specific_dir)
        if not os.path.exists(start_dir):
            print(f"Error: The directory '{specific_dir}' does not exist in 'tests/'.")
            return False
    
    print(f"Discovering tests in: {start_dir}")
    print(f"Using pattern: {test_pattern}")
    print("-" * 50)
    
    # Discover and run the tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir, pattern=test_pattern)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return success status (useful for CI/CD pipelines)
    return result.wasSuccessful()

def list_available_test_modules():
    """Lists all available test modules in the tests directory."""
    print("Available test modules:\n")
    
    test_files = glob.glob('tests/**/test_*.py', recursive=True)
    
    if not test_files:
        print("No test files found. Looking for files matching 'test_*.py'.")
        return
    
    # Create a mapping of simple names to full paths
    module_map = {}
    for file_path in test_files:
        # Convert file path to a simpler identifier
        # e.g., 'tests/data_structures/test_linked_list.py' -> 'data_structures.linked_list'
        simple_name = file_path.replace('tests/', '').replace('/', '.').replace('test_', '').replace('.py', '')
        module_map[simple_name] = file_path
    
    # Print the available options in a nice format
    for i, (name, path) in enumerate(module_map.items(), 1):
        print(f"{i:2d}. {name:40s} ({path})")
    
    return module_map

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Run tests for the Algorithmics library.")
    parser.add_argument(
        '--module', '-m', 
        type=str,
        help="Run tests for a specific module (e.g., 'data_structures.linked_list')"
    )
    parser.add_argument(
        '--list', '-l', 
        action='store_true',
        help="List all available test modules without running them"
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_available_test_modules()
        sys.exit(0)
    
    # Run the tests based on the user's choice
    if args.module:
        print(f"Running tests for module: {args.module}")
        success = discover_and_run_tests(specific_dir=args.module)
    else:
        print("Running ALL tests...")
        success = discover_and_run_tests()
    
    # Exit with a proper status code (0 for success, 1 for failure)
    # This is important for CI/CD systems like GitHub Actions.
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
"""
How to Use Your New CLI Test Runner:
List all available tests:

bash
python run_tests.py --list
# or
python run_tests.py -l
Output:

Available test modules:

1. data_structures.linked_list          (tests/data_structures/test_linked_list.py)
2. algorithms.sorting                   (tests/algorithms/test_sorting.py)
Run all tests:

bash
python run_tests.py
Run tests for a specific module (using the simple name from the list):

bash
python run_tests.py --module data_structures.linked_list
# or
python run_tests.py -m algorithms.sorting
Key Features of This Runner:
Clean CLI Interface: Uses argparse, the standard Python library for CLIs.

Flexible Discovery: Can run all tests or just a specific subset.

Helpful Listing: The --list flag shows you exactly what you can run.

CI/CD Ready: Returns proper exit codes (0 for success, 1 for failure), which is crucial for automation on GitHub.

Professional: This isn't a simple script; it's a robust tool that mirrors testing utilities in large frameworks.

This setup completes your professional project structure. You now have:

Automatic package discovery for easy development.

A powerful, flexible test runner that adds real utility.

A codebase that is organized, scalable, and meets the highest standards.


"""