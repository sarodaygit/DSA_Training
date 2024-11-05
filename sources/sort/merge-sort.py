def merge_sort(arr):
    # Recursive function to split the array
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        print(f'mid => {mid}')
        left_half = arr[:mid]  # Split the array into left half
        right_half = arr[mid:]  # Split the array into right half

        print(f"\nSplitting: {arr} -> Left: {left_half}, Right: {right_half}")

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        merge(arr, left_half, right_half)

        print(f"After merging: {arr}")  # Print the array after merge


def merge(sorted_arr, left_half, right_half):
    # Function to merge two sorted sorted_arrays into a single sorted sorted_array
    i = j = k = 0  # Initialize pointers for left_half, right_half, and sorted_arr

    print("\nMerging:", left_half, "and", right_half)
    
    # Merge the left_half and right_half into sorted_arr
    while i < len(left_half) and j < len(right_half):
        print(f"Comparing left_half[{i}] = {left_half[i]} with right_half[{j}] = {right_half[j]}")
        if left_half[i] < right_half[j]:
            sorted_arr[k] = left_half[i]
            print(f"sorted_arr[{k}] = left_half[{i}] -> {sorted_arr[k]}")
            i += 1
        else:
            sorted_arr[k] = right_half[j]
            print(f"sorted_arr[{k}] = right_half[{j}] -> {sorted_arr[k]}")
            j += 1
        k += 1
        print(f"Updated indices: i = {i}, j = {j}, k = {k}")

    # Copy the remaining elements of left_half, if any
    while i < len(left_half):
        sorted_arr[k] = left_half[i]
        print(f"sorted_arr[{k}] = left_half[{i}] -> {sorted_arr[k]} (Remaining element from left_half)")
        i += 1
        k += 1
        print(f"Updated indices after processing left_half: i = {i}, k = {k}")

    # Copy the remaining elements of right_half, if any
    while j < len(right_half):
        sorted_arr[k] = right_half[j]
        print(f"sorted_arr[{k}] = right_half[{j}] -> {sorted_arr[k]} (Remaining element from right_half)")
        j += 1
        k += 1
        print(f"Updated indices after processing right_half: j = {j}, k = {k}")

    # Print the sorted_array after every merge
    print(f"sorted_array after merging: {sorted_arr}")


# Example array to test the function
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("\nSorted array:", arr)


#                                    merge_sort([38, 27, 43, 3, 9, 82, 10])
#                                           /                              \
#                 merge_sort([38, 27, 43])                                       merge_sort([3, 9, 82, 10])
#                   /                \                                               /                     \
#  merge_sort([38])          merge_sort([27, 43])                          merge_sort([3, 9])             merge_sort([82, 10])
#                            /            \                                /        \                       /       \
#                   merge_sort([27])   merge_sort([43])            merge_sort([3])  merge_sort([9])   merge_sort([82])  merge_sort([10])
#                                \              /                           \          /                         \              /
#                              [27, 43] (merge)                               [3, 9] (merge)                  [82, 10] (merge)
#                                 \                                           /                                      \
#                              [27, 38, 43] (merge)                           [3, 9, 82, 10] (merge)
#                                             \                                    /
#                                      [3, 9, 10, 27, 38, 43, 82] (final merge)
