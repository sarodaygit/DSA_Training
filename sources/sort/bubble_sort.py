def bubble_sort(list_a):
    n = len(list_a)  # Length of the list
    sorted = False   # Variable to track if the list is sorted
    pass_num = 1     # Counter to track the number of passes

    # Repeat until no swaps are made (indicating the list is sorted)
    while not sorted:
        print(f"\n--- Pass {pass_num} ---")
        sorted = True  # Assume the list is sorted at the beginning of each pass
        # Traverse the list up to the second last unsorted element
        print(f'Checking for the range {range(n-1)}')
        for i in range(0, n - 1):  # Iterate over the list up to the last unsorted element
            # If the current element is greater than the next, swap them
            if list_a[i] > list_a[i + 1]:
                sorted = False  # Since a swap is made, the list wasn't sorted
                # Swap the elements and print the action
                print(f"Swapping {list_a[i]} and {list_a[i + 1]}")
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                # Print the list after each swap
                print("Current list:", list_a)
            else:
                print(f'Not swapping {list_a[i]} and {list_a[i + 1]}; continuing with {list_a[i + 1]}')

        # Reduce `n` by 1, as the largest element of this pass is now in place
        n -= 1
        print(f"End of Pass {pass_num}: {list_a}")
        pass_num += 1  # Increment the pass counter

    print("\nFinal sorted list:", list_a)
    return list_a


# Test the function
original_list = [3,2,4,1]
print(original_list)
sorted_list = bubble_sort(original_list)
print(sorted_list)
# bubble_sort([7, 8, 5, 4, 9, 2])
