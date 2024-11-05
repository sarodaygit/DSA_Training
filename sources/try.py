
# def insertion_sort(list_a):
#     indexing_length = range(1, len(list_a))
#     for i in indexing_length:
#         value_to_sort = list_a[i]
#         print(f'for the lenght of list {len(list_a)}  value_to_sort {value_to_sort} at position  i = {i}')

#         while list_a[i-1] > value_to_sort and i>0:
#         # while list_a[i-1] and i >0 :
#             list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
#             print(list_a)
#             i = i -1

#     return list_a


# A = [7, 8, 5, 4, 9, 2]
# print(f'Original list => {A}')
# B = insertion_sort(A)
# print(B)
# # print(insertion_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8]))


def insertion_sort(list_a):
    # Start at the second element (index 1) because the first element is trivially sorted
    for i in range(1, len(list_a)):
        # The value to be positioned in the sorted portion of the list
        value_to_sort = list_a[i]
        print(f"\nProcessing value {value_to_sort} at index {i} for list of length {len(list_a)}")

        # Create a variable to traverse the sorted portion
        sorted_index = i
        
        # Move elements of list_a[0...i-1] that are greater than value_to_sort one position ahead
        while sorted_index > 0 and list_a[sorted_index - 1] > value_to_sort:
            print(f"  Shifting {list_a[sorted_index - 1]} to the right")
            list_a[sorted_index] = list_a[sorted_index - 1]
            sorted_index -= 1  # Move to the next position to the left

        # Place the value_to_sort in the correct sorted position
        list_a[sorted_index] = value_to_sort
        print(f"  Inserted {value_to_sort} at index {sorted_index}: {list_a}")

    return list_a

# Example usage
A = [7, 8, 5, 4, 9, 2]
print(f"Original list => {A}")
B = insertion_sort(A)
print("Sorted list:", B)
