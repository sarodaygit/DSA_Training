def linearfunc(numlist):
    i=0
    for num in numlist:   
        product = 100 * 1000
        print(f'i =  {i} array value = {num} and product = {product}')
        i+= 1


if __name__ == "__main__":
    numlist = [2,3,6,4,5,7]
    linearfunc(numlist)
















# def linearfunc(numlist):   # O(1) - Function definition has no complexity impact
#     i = 0                  # O(1) - Initializing a variable is constant time
#     for num in numlist:    # O(n) - Loop iterates over each element in numlist, where n is the length of numlist
#         product = 100 * 1000  # O(1) - Constant time operation (simple multiplication)
#         print(f'i = {i} array value = {num} and {product}')  # O(1) - Printing is considered a constant time operation
#         i += 1             # O(1) - Incrementing a variable is constant time

# if __name__ == "__main__":  # O(1) - Constant time for checking a condition
#     numlist = [2, 3, 6, 4, 5, 7]  # O(1) - Initializing a list is constant time
#     linearfunc(numlist)      # O(n) - Function call has a complexity of O(n), derived from the loop inside linearfunc
