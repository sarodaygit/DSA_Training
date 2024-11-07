# Importing the array module for working with fixed-type arrays
import array

# Example 1: Creating an array with specific data type
# An integer array with elements
numbers = array.array('i', [10, 20, 30, 40, 50])
print("Initial array:", numbers)

# Accessing elements
print("\nAccessing elements:")
print("First element:", numbers[0])  # Expected output: 10
print("Last element:", numbers[-1])  # Expected output: 50

# Modifying elements
print("\nModifying elements:")
numbers[1] = 25
print("Modified array:", numbers)
ddd
# Error Scenario 1: Adding elements of the wrong type
try:
    print("\nAdding an element of the wrong type:")
    numbers.append(3.5)  # Trying to add a float to an integer array
except TypeError as e:
    print("Error:", e)

# Drawback: Fixed data type – arrays do not support mixed types

# Error Scenario 2: Accessing an index that’s out of range
try:
    print("\nAccessing an out-of-range index:")
    print(numbers[10])  # Accessing an invalid index
except IndexError as e:
    print("Error:", e)

# Drawback: Arrays don’t automatically handle invalid indices; manual checks are necessary

# Example 2: Inserting and removing elements
print("\nInserting and removing elements:")
numbers.insert(2, 15)  # Insert 15 at index 2
print("Array after insertion:", numbers)

numbers.pop(3)  # Remove element at index 3
print("Array after removal:", numbers)

# Limitation: Fixed Size (in some languages) and inefficient resizing
# In many languages (like C or Java), arrays are fixed size, and resizing is complex and costly.

# Example 3: Searching for an element
print("\nSearching for an element:")
if 25 in numbers:
    print("25 found in the array.")
else:
    print("25 not found in the array.")

# Drawback: Linear search time complexity (O(n))
# Arrays do not support fast search for unsorted elements.

# Error Scenario 3: Memory constraints when using large arrays
try:
    print("\nCreating a very large array (may cause MemoryError):")
    large_array = array.array('i', range(10**8))  # Trying to create a massive array
except MemoryError as e:
    print("Error:", e)

# Drawback: Arrays occupy contiguous memory, which can lead to memory issues with large sizes.

# Example 4: Deleting elements is inefficient
# Deleting an element in an array requires shifting all subsequent elements, which is costly in large arrays.
print("\nDeleting an element:")
del numbers[2]  # Delete the element at index 2
print("Array after deletion:", numbers)

# Drawback: Removing elements requires shifting, leading to O(n) time complexity for deletion.
# This can be slow for large arrays.

# Example 5: Arrays are static in size in low-level languages
# (For Python lists, which are dynamic arrays, this isn't a limitation, but in languages like C, arrays are static).
