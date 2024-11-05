# This Fibonacci function uses a technique known as dynamic programming with memoization (or caching) to efficiently calculate the Fibonacci sequence. Let’s break down how it applies memoization:

# Caching Results:
# The cache list stores previously computed Fibonacci numbers to avoid redundant calculations. Specifically, cache[i] represents the Fibonacci number at position i.
# By storing these values in the cache, the function avoids recalculating Fibonacci numbers for the same input multiple times, which would be inefficient.
# Iterative Calculation:
# The code uses an iterative approach to populate the cache, filling in each Fibonacci number from 2 up to n using the relation:
# cache[i]=cache[i−1]+cache[i−2]
# This avoids the exponential time complexity of a recursive solution without caching and reduces it to linear time complexity, 𝑂(𝑛).
# Memoization Effect:
# By storing previously computed values in cache, the function essentially memorizes the results of subproblems, allowing it to access them in constant time, 𝑂(1).This is often referred to as tabulation (a form of bottom-up dynamic programming), where the table of results is filled in progressively.





def fibonacci(n):
    # Edge case: if n is 0 or 1, return n as the Fibonacci number
    if n <= 1:
        return n
    
    # Initialize a list for caching results of Fibonacci subproblems
    cache = [0] * (n + 1)
    # Base cases
    cache[0] = 0
    cache[1] = 1
    
    # Fill the cache list iteratively
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    
    # Return the nth Fibonacci number
    return cache[n]

def fibonacci_wo(n):
    # Base cases
    if n <= 1:
        return n
    
    # Recursive calculation without memoization
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    val = 4
    # Example usage
    print(fibonacci(10))  # Output: 55
    # Example usage without memoization
    print(fibonacci_wo(10))  # Output: 55