def linear_search(arr, target):
    """
    Perform a linear search on the list.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, else -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
if __name__ == "__main__":
    my_list = [4, 2, 7, 1, 9]
    target_value = 1
    result = linear_search(my_list, target_value)

    if result != -1:
        print(f"Target {target_value} found at index {result}.")
    else:
        print(f"Target {target_value} not found in the list.")
