"""
Project: Python List vs NumPy Array Comparison
Author: Pramod Wickramanayake
Description: Demonstrating why NumPy is essential for AI and Mathematical operations.
"""

import numpy as np

def compare_list_and_array():
    # 1. Standard Python List
    python_list = [1, 2, 3, 4, 5]
    
    # 2. NumPy Array (Optimized for Data Science)
    numpy_array = np.array([1, 2, 3, 4, 5])

    print("--- Comparison Results ---")

    # In Python Lists, '*' operator duplicates the list
    print(f"Python List * 2 (Duplicates items): {python_list * 2}")

    # In NumPy, '*' operator performs element-wise multiplication
    print(f"NumPy Array * 2 (Mathematical multiplication): {numpy_array * 2}")

if __name__ == "__main__":
    compare_list_and_array()