# methods_and_functions.py

# Function Definition
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

# Calling the Function
print(greet("Alice"))
print(greet("Bob"))
print()

# String Methods
message = "  Hello, World!  "
print("Original message:", message)

# Using the strip() method to remove whitespace
cleaned_message = message.strip()
print("Cleaned message:", cleaned_message)

# Using the upper() method to convert to uppercase
upper_message = cleaned_message.upper()
print("Uppercase message:", upper_message)
print()

# List Methods
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

# Using append() method to add an element
numbers.append(6)
print("List after appending 6:", numbers)

# Using remove() method to remove an element
numbers.remove(3)
print("List after removing 3:", numbers)
print()

# Dictionary Methods
student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
print("Original dictionary:", student_scores)

# Using keys() method to get all keys
print("Student Names:", student_scores.keys())

# Using values() method to get all values
print("Scores:", student_scores.values())

# Using get() method to access a value safely
alice_score = student_scores.get('Alice', 'Not found')
print("Alice's Score:", alice_score)


def decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()