def binary_search_recursive(arr, target, lowindex, highindex):

    if lowindex > highindex:
        return -1
    isascending = arr[lowindex] < arr[highindex]
    midindex = (lowindex + highindex)//2
    guess =  arr[midindex]
    if guess == target:
        return midindex
    
    if isascending:
        if guess < target:
            return binary_search_recursive(arr, target, midindex + 1, highindex)
        elif guess > target:
            return binary_search_recursive(arr, target, lowindex, midindex - 1)
    else:
        if guess < target:
            return binary_search_recursive(arr, target, lowindex, midindex -1)
        elif guess > target:
            return binary_search_recursive(arr, target, midindex + 1, highindex )
   


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr = [9, 7, 5, 3, 1] 
target = 7

result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")