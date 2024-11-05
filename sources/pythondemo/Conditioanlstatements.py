# 1. Simple If Statement
print("Simple If Statement:")
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print()

# 2. If-Elif-Else Statement
print("If-Elif-Else Statement:")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")
print()

# 3. Nested If Statement
print("Nested If Statement:")
num = 15
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("It is also even.")
    else:
        print("It is odd.")
else:
    print("The number is not positive.")
print()

# 4. Using Logical Operators
print("Using Logical Operators:")
temperature = 30
is_raining = False
if temperature > 25 and not is_raining:
    print("It's a nice day for a picnic.")
else:
    print("Better stay indoors.")
print()

# 5. Using the Ternary Operator
print("Using the Ternary Operator:")
x = 5
y = 10
max_value = x if x > y else y
print(f"The maximum value is: {max_value}")
print()



# 7. Input Based Conditional OR Case Statements
print("Input Based Conditional:")
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    if number > 0:
        print("You entered a positive number.")
    elif number < 0:
        print("You entered a negative number.")
    else:
        print("You entered zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
