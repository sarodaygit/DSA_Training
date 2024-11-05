def selection_sort(list_a):
    n = len(list_a)
    
    # Iterate over the entire list
    for i in range(n - 1):  # No need to check the last element, as it will already be sorted
        min_index = i  # Assume the minimum is the first element of the unsorted part
        print(f"\n--- Pass {i + 1} ---")
        print(f"Initial minimum value at index {min_index}: {list_a[min_index]}")

        # Traverse the unsorted part of the list
        for j in range(i + 1, n):
            # If a smaller element is found, update the minimum index
            if list_a[j] < list_a[min_index]:
                min_index = j  # Update min_index to the index of the new minimum
                print(f"New minimum found at index {min_index}: {list_a[min_index]}")
            else:
                print(f"Element {list_a[j]} at index {j} is not smaller than {list_a[min_index]} (current minimum).")
            
            # Print the current minimum after each comparison
            print(f"Current minimum after comparing index {j}: {list_a[min_index]}")

        # If a new minimum was found, swap it with the first element of the unsorted part
        if min_index != i:
            print(f"Swapping {list_a[i]} with {list_a[min_index]}")
            list_a[min_index], list_a[i] = list_a[i], list_a[min_index]
            print("List after swap:", list_a)
        else:
            print(f"No swap needed for index {i}: {list_a[i]} is already the minimum.")

        # Print the current state of the list after each pass
        sorted_part = list_a[:i + 1]  # Elements sorted so far
        unsorted_part = list_a[i + 1:]  # Elements yet to be sorted
        print("Current sorted part:", sorted_part)
        print("Current unsorted part:", unsorted_part)

    return list_a

# Example usage
# original_list = [7,6,5,8] #Try this also
original_list = [1, 10, 23, -2]
sorted_list = selection_sort(original_list)
print("\nFinal sorted list:", sorted_list)
