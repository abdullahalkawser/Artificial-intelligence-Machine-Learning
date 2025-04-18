marks = [48,5895,589,494,49489,393,349];

student = ['abdullah', 34.4,'software Engnineer']



student[0]= 'kawser'
print(student)
print(type(marks))
print(len(marks))


mark = [24,33,34,36,37,39]
print(mark[1:5])

print(mark[-3:-1])

'''listing method'''

num =[2,4,7,9,4,6,9,0]
print(num.append(100))
print(num)
print(num.sort())
print(num)
print(num.sort(reverse=True))
print(num)
print(num.reverse())
print(num)

print(num.insert(3,200))
print(num)

print(num.remove(7))
print(num)

print(num.pop(4))
print(num)

'''Tuples vs Lists: Lists are mutable, meaning you can change, add, or remove elements after creation. Tuples are immutable, making them a better choice for data that should not be changed.'''

'''Tuple Example'''

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[1:4])  # Output: (2, 3, 4)

# You can also have tuples with different data types
mixed_tuple = (1, "hello", 3.14, True)

# Print the entire tuple
print(mixed_tuple)  # Output: (1, 'hello', 3.14, True)


# Nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))

# You cannot change a tuple's elements, so the following will raise an error:
# my_tuple[1] = 10  # This will throw a TypeError

# However, you can concatenate tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)
