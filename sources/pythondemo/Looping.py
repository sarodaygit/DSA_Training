# basic_loops.py

# 1. For Loop: Iterating Over a List
fruits = ['apple', 'banana', 'cherry']
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)
print()

# 2. For Loop with Range: Using range()
print("Numbers from 0 to 4:")
for i in range(5):
    print(i)
print()

# 3. While Loop: Basic
count = 0
print("Counting from 0 to 4 using while loop:")
while count < 5:
    print(count)
    count += 1  # Increment count by 1
print()

# 4. Nested Loops: Nested For Loop
print("Nested For Loop:")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer: {i}, Inner: {j}")
print()

# 5. Loop Control Statements: Using break and continue
print("Using break and continue:")
for i in range(5):
    if i == 2:
        print("Skipping 2")
        continue  # Skip the current iteration
    if i == 4:
        print("Breaking the loop")
        break  # Exit the loop
    print(i)
print()

# 6. Looping Through a Dictionary: Iterating Over a Dictionary
student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
print("Student Scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")
