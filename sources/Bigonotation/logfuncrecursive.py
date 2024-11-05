def logfuncrecursive(n):
    if n <= 0:  # Base case to stop recursion
        return
    n //= 2  # Halve n
    print(f'value of n = {n}')
    return logfuncrecursive(n)  # Recursive call


if __name__ == "__main__":
    val = 4
    logfuncrecursive(val)