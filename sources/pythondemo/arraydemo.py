# Import the array module for array operations
import array

# ==========================
# 1. Creating an Array
# ==========================
# Using a list to create an array-like structure
arr_list = [1, 2, 3, 4, 5]
print("List:", arr_list)  # Output: [1, 2, 3, 4, 5]

# Using the array module to create an integer array
arr_array = array.array('i', [1, 2, 3, 4, 5])
print("Array:", arr_array)  # Output: array('i', [1, 2, 3, 4, 5])

float_array = array.array("f",[1.0, 2.5])
print(type(float_array[1]))
# ==========================
# 2. Accessing Elements (Indexing)
# ==========================
# Accessing a single element
print("Element at index 1:", arr_array[1])  # Output: 2

# Accessing the last element using negative indexing
print("Last element:", arr_array[-1])  # Output: 5


# ==========================
# 3. Slicing
# ==========================
# Slicing the array to get elements from index 1 to 3
print("Slice [1:4]:", arr_array[1:4])  # Output: array('i', [2, 3, 4])

# Slicing to get the first three elements
print("Slice [:3]:", arr_array[:3])  # Output: array('i', [1, 2, 3])

# Slicing with step to get every second element
print("Slice [::2]:", arr_array[::2])  # Output: array('i', [1, 3, 5])


# ==========================
# 4. Inserting Elements
# ==========================
# Inserting an element in the list at index 2
arr_list.insert(2, 10)  # Insert 10 at index 2
print("List after insert:", arr_list)  # Output: [1, 2, 10, 3, 4, 5]

# Inserting in an array
arr_array.insert(2, 10)  # Insert 10 at index 2
print("Array after insert:", arr_array)  # Output: array('i', [1, 2, 10, 3, 4, 5])


# ==========================
# 5. Appending Elements
# ==========================
# Appending to list
arr_list.append(6)
print("List after append:", arr_list)  # Output: [1, 2, 10, 3, 4, 5, 6]

# Appending to array
arr_array.append(6)
print("Array after append:", arr_array)  # Output: array('i', [1, 2, 10, 3, 4, 5, 6])


# ==========================
# 6. Deleting Elements
# ==========================
# Deleting an element by index using del in list
del arr_list[2]
print("List after deletion by index:", arr_list)  # Output: [1, 2, 3, 4, 5, 6]

# Removing an element by value
arr_list.remove(3)
print("List after deletion by value:", arr_list)  # Output: [1, 2, 4, 5, 6]


# ==========================
# 7. Finding Elements
# ==========================
# Finding index of an element
index_of_4 = arr_list.index(4)
print("Index of 4 in list:", index_of_4)  # Output: 2

# Counting occurrences of an element
count_of_5 = arr_list.count(5)
print("Count of 5 in list:", count_of_5)  # Output: 1


# ==========================
# 8. Sorting the Array
# ==========================
# Sorting the list
arr_list_unsorted = [5, 1, 3, 2, 4]
arr_list_unsorted.sort()
print("Sorted list:", arr_list_unsorted)  # Output: [1, 2, 3, 4, 5]


# ==========================
# 9. Reversing the Array
# ==========================
# Reversing the list
arr_list_unsorted.reverse()
print("Reversed list:", arr_list_unsorted)  # Output: [5, 4, 3, 2, 1]


# ==========================
# 10. Extending the Array
# ==========================
# Extending the list with multiple elements
arr_list.extend([7, 8, 9])
print("List after extend:", arr_list)  # Output: [1, 2, 4, 5, 6, 7, 8, 9]


# ==========================
# 11. Copying the Array
# ==========================
# Creating a copy of the list
arr_list_copy = arr_list.copy()
print("Copied list:", arr_list_copy)  # Output: [1, 2, 4, 5, 6, 7, 8, 9]


# ==========================
# 12. Clearing the Array
# ==========================
# Clearing all elements in the list
arr_list.clear()
print("List after clear:", arr_list)  # Output: []


numbers = array.array('i', [10, 20, 30, 40, 50])
print("Initial array:", numbers)

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
