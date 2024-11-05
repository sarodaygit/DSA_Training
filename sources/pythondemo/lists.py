# Example 1: Basic List Creation and Indexing
my_list = [10, 20, 30, 40, 50]
print("Initial list:", my_list)

# Accessing elements by positive and negative indexing
print("\nAccessing elements by indexing:")
print("First element (positive index):", my_list[0])  # Expected output: 10
print("Last element (negative index):", my_list[-1])  # Expected output: 50

# Error Scenario 1: Index out of range
try:
    print("Accessing out-of-range index:", my_list[10])  # Raises IndexError
except IndexError as e:
    print("Error:", e)

# Example 2: Slicing Lists
print("\nList slicing examples:")
print("First three elements:", my_list[:3])  # Expected output: [10, 20, 30]
print("Elements from index 1 to 3:", my_list[1:4])  # Expected output: [20, 30, 40]
print("Elements from index 2 to the end:", my_list[2:])  # Expected output: [30, 40, 50]
print("Copy of the list:", my_list[:])  # Copy of entire list
print("Reverse list with slicing:", my_list[::-1])  # Expected output: [50, 40, 30, 20, 10]

# Limitation: Slicing creates a shallow copy and can consume additional memory if done on large lists

# Example 3: Modifying Lists
print("\nModifying list elements:")
my_list[2] = 99
print("Modified list:", my_list)  # Expected output: [10, 20, 99, 40, 50]

# Example 4: Adding Elements
print("\nAdding elements:")
my_list.append(60)  # Adds to the end
print("List after append:", my_list)

my_list.insert(1, 15)  # Inserts at index 1
print("List after insert:", my_list)

# Limitation: Inserting elements in the middle or beginning requires shifting, which is slower for large lists

# Example 5: Removing Elements
print("\nRemoving elements:")
my_list.remove(99)  # Removes first occurrence of 99
print("List after remove:", my_list)

my_list.pop()  # Removes last element
print("List after pop:", my_list)

# Error Scenario 2: Removing an element not in the list
try:
    my_list.remove(999)  # Element not in list
except ValueError as e:
    print("Error:", e)

# Limitation: Removal by value raises an error if the value is not found

# Example 6: Searching and Counting
print("\nSearching and counting elements:")
print("Index of 40:", my_list.index(40))  # Expected output: index of 40
print("Count of 20:", my_list.count(20))  # Expected output: count of 20 in list

# Limitation: Linear time complexity for search, which can be slow for large lists

# Example 7: List Length and Memory
print("\nList length and memory usage:")
print("Length of list:", len(my_list))

# Example 8: Copying Lists (Shallow and Deep Copies)
import copy

original_list = [1, [2, 3], 4]
shallow_copy = original_list.copy()       # Shallow copy
deep_copy = copy.deepcopy(original_list)  # Deep copy

original_list[1][0] = "changed"
print("\nShallow copy after modifying original:", shallow_copy)  # Inner lists are affected
print("Deep copy after modifying original:", deep_copy)          # Inner lists are unaffected

# Limitation: Shallow copies keep references to inner lists, while deep copies are independent

# Example 9: Performance with Large Lists
import time

print("\nPerformance example with large list:")
large_list = list(range(1000000))

# Accessing an element (fast, O(1))
start_time = time.time()
_ = large_list[500000]
print("Access time:", time.time() - start_time, "seconds")

# Slicing a large list (creates a new list, O(k))
start_time = time.time()
sliced_large_list = large_list[:1000]
print("Slicing time for first 1000 elements:", time.time() - start_time, "seconds")

# Inserting an element at the beginning (slow, O(n))
start_time = time.time()
large_list.insert(0, -1)
print("Insertion time at beginning:", time.time() - start_time, "seconds")

# Removing an element from the beginning (slow, O(n))
start_time = time.time()
large_list.pop(0)
print("Deletion time at beginning:", time.time() - start_time, "seconds")

# Example 10: Limitations with Lists (Homogeneity and Performance)
mixed_list = [1, "text", 3.14, True]
print("\nMixed data type list:", mixed_list)

# While Python lists support mixed data types, certain operations (e.g., mathematical operations) are limited.
try:
    result = mixed_list[0] + mixed_list[1]  # Attempting to add an int and a str
except TypeError as e:
    print("Error with mixed types:", e)

# Limitation: Mixed data types in lists can lead to unexpected TypeErrors in operations

# Example 11: Multi-dimensional Lists (Nested Lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMulti-dimensional list (2D matrix):", matrix)
print("Accessing an element in 2D list:", matrix[1][1])  # Expected output: 5

# Limitation: Multi-dimensional lists increase complexity for access, modification, and copy operations

# Example 12: Summary of Drawbacks and Limitations
print("\nSummary of List Drawbacks and Limitations:")
print("- Lists consume more memory when resized dynamically.")
print("- Slicing, shallow copying, and nested lists increase memory usage and complexity.")
print("- Insertions and deletions at the start or middle are slower (O(n)).")
print("- Lists with mixed data types may lead to TypeErrors during operations.")
print("- Linear search times (O(n)) for unsorted lists can be inefficient.")
