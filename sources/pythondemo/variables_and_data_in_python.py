
# Variables and Data in Python

# 1. What is a Variable?
# A variable is a symbolic name associated with a value and can be used to refer to that value in your code.
# In Python, you do not need to declare a variable before using it. You can simply assign a value to a variable.

# Example:
x = 10          # Integer
y = 3.14       # Float
name = "Alice"  # String

print(x)       # Output: 10
print(y)       # Output: 3.14
print(name)    # Output: Alice

# 2. Data Types
# Python has various built-in data types that you can use:

# Integers: Whole numbers, both positive and negative.
# Floats: Numbers with decimal points.
# Strings: Sequence of characters enclosed in quotes.
# Booleans: Represents True or False.

# Example:
age = 25                   # Integer
height = 5.9               # Float
greeting = "Hello, World!" # String
is_student = True          # Boolean

print(type(age))          # Output: <class 'int'>
print(type(height))       # Output: <class 'float'>
print(type(greeting))     # Output: <class 'str'>
print(type(is_student))   # Output: <class 'bool'>

# 3. Variable Naming Conventions
# Variable names should be descriptive and follow certain rules:
# Must start with a letter or underscore (_).
# Can contain letters, numbers, and underscores.
# Cannot contain spaces or special characters (except for underscores).
# Case-sensitive.

# Example:
first_name = "John"
_lastName = "Doe"
age_23 = 23

# Invalid variable names (will raise SyntaxError)
# 1st_name = "Jane"  # Cannot start with a number
# my-name = "Smith"   # Hyphen is not allowed

# 4. Multiple Assignment
# You can assign multiple variables in a single line.

# Example:
a, b, c = 1, 2.5, "Python"
print(a)  # Output: 1
print(b)  # Output: 2.5
print(c)  # Output: Python

# 5. Constants
# In Python, there are no constant types, but by convention, you can use uppercase variable names to indicate that a variable should not change.

# Example:
PI = 3.14159
MAX_USERS = 100

print(PI)        # Output: 3.14159
print(MAX_USERS) # Output: 100

# 6. Type Conversion
# You can convert between different data types using built-in functions.

# Example:
num_str = "100"            # String
num_int = int(num_str)     # Convert to Integer
num_float = float(num_str)  # Convert to Float

print(num_int)   # Output: 100
print(num_float) # Output: 100.0

# 7. Dynamic Typing
# Python is dynamically typed, meaning you do not need to declare the data type of a variable explicitly. The interpreter infers the type based on the value assigned.

# Example:
var = 5          # Initially an Integer
print(type(var)) # Output: <class 'int'>

var = "Now I'm a string!"  # Changes to String
print(type(var)) # Output: <class 'str'>

# Error Conditions and Limitations

# 1. Type Errors
# Type errors occur when an operation is performed on incompatible data types. 

# Example:
num = 5
text = "Hello"

# This will raise a TypeError
try:
    result = num + text
except TypeError as e:
    print(f"Type Error: {e}")  # Output: Type Error: unsupported operand type(s) for +: 'int' and 'str'

# 2. Name Errors
# Name errors occur when you try to use a variable that has not been defined.

# Example:
try:
    print(undefined_var)  # Raises NameError
except NameError as e:
    print(f"Name Error: {e}")  # Output: Name Error: name 'undefined_var' is not defined

# 3. Index Errors
# Index errors happen when you try to access an index that is out of the range of a list or other indexable data types.

# Example:
my_list = [1, 2, 3]

try:
    print(my_list[5])  # Raises IndexError
except IndexError as e:
    print(f"Index Error: {e}")  # Output: Index Error: list index out of range

# 4. Key Errors
# Key errors occur when you try to access a dictionary with a key that does not exist.

# Example:
my_dict = {"name": "Alice", "age": 30}

try:
    print(my_dict["gender"])  # Raises KeyError
except KeyError as e:
    print(f"Key Error: {e}")  # Output: Key Error: 'gender'

# 5. Attribute Errors
# Attribute errors arise when you try to access an attribute or method that does not exist for a particular data type.

# Example:
num = 10

try:
    num.append(5)  # Raises AttributeError
except AttributeError as e:
    print(f"Attribute Error: {e}")  # Output: Attribute Error: 'int' object has no attribute 'append'

# 6. Value Errors
# Value errors occur when a built-in operation or function receives an argument that has the right type but an inappropriate value.

# Example:
try:
    num = int("abc")  # Raises ValueError
except ValueError as e:
    print(f"Value Error: {e}")  # Output: Value Error: invalid literal for int() with base 10: 'abc'

# 7. Limitations of Basic Data Types
# Single Data Storage: Primitive data types store single pieces of data, which limits scalability.
# Examples: Why lists, tuples, or dictionaries might be better choices than just using multiple variables.

# Example:
# Using individual variables for multiple values
student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"
# This becomes cumbersome as the number of students grows

# Immutability: Certain data types, like strings and tuples, are immutable, meaning their content cannot be changed after creation.

# Example:
# Attempting to modify a string
name = "Alice"
try:
    name[0] = "E"  # Raises TypeError
except TypeError as e:
    print(f"Type Error: {e}")  # Output: Type Error: 'str' object does not support item assignment
