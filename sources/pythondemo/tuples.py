### 3. Tuples ###

# Creating a Tuple
tup = (100, 200, 300, 400, 500)
print("Tuple:", tup)

# Indexing in Tuple
print("Element at index 1:", tup[1])

# Slicing a Tuple
print("Tuple slice [1:4]:", tup[1:4])

# Length of Tuple
print("Length of tuple:", len(tup))

# Tuple Concatenation
tup2 = (600, 700, 800)
tup += tup2
print("Tuple after concatenation:", tup)

# Tuple Unpacking
a, b, c, *rest = tup
print("First element:", a)
print("Second element:", b)
print("Third element:", c)
print("Rest of the elements:", rest)

# Traversing the Tuple
print("Traversing the tuple:")
for element in tup:
    print(element, end=' ')
print("\n")

# Attempting to Modify a Tuple (This will raise an error, uncomment to see)
# tup[0] = 999  # Uncommenting this line will raise a TypeError

