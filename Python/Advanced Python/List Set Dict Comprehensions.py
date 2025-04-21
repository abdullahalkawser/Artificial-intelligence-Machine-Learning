# Syntax: [expression for item in iterable if condition]
#1. List Comprehension


# Example: Square of numbers from 0 to 4
squares = [x*x for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# With condition (only even squares)
even_squares = [x*x for x in range(5) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16]

#Set Comprehension

# Syntax: {expression for item in iterable if condition}

# Example: Unique squares from a list (no duplicates)
nums = [1, 2, 2, 3, 4]
unique_squares = {x*x for x in nums}
print(unique_squares)  # Output: {16, 1, 4, 9}


#Dictionary Comprehension
# Syntax: {key_expr: value_expr for item in iterable if condition}

# Example: Number and its square as key:value
square_dict = {x: x*x for x in range(5)}
print(square_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition (only even keys)
even_square_dict = {x: x*x for x in range(5) if x % 2 == 0}
print(even_square_dict)  # Output: {0: 0, 2: 4, 4: 16}



#Nested List Comprehension
# 2D List Flatten
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
