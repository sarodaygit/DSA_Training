# Binary Search Algorithm for both ascending and descending arrays
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Check if the array is sorted in ascending or descending order
    is_ascending = arr[low] < arr[high]

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        guess = arr[mid]

        if guess == target:
            return mid  # Target found, return the index

        if is_ascending:
            if guess < target:
                low = mid + 1  # Search the right half
            elif guess > target:
                high = mid - 1  # Search the left half
        else:  # For descending order
            if guess > target:
                low = mid + 1  # Search the right half
            elif guess < target:
                high = mid - 1  # Search the left half

    return -1  # Target not found

# Example usage:
arr = [9, 7, 5, 3, 1]  # Descending order array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 1

result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")
