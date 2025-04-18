# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#2. while loop
    # Print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1

#3. Nested loops
# Nested loop: printing a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # New line after each row

#4. Loop Control Statements

# Looping until a condition is met, then breaking
for i in range(10):
    if i == 5:
        break  # Exits the loop when i equals 5
    print(i)

# Skipping even numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skips the current iteration if i is even
    print(i)

# Using the else statement with loops
for i in range(5):
    print(i)                    
