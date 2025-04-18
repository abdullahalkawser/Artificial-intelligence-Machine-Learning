import math


#Primitive Data Types in Python

print(10 + 3)  # Addition: 10 + 3 = 13
print(10 - 3)  # Subtraction: 10 - 3 = 7
print(10 * 3)  # Multiplication: 10 * 3 = 30
print(10 / 3)  # Division (float result): 10 / 3 = 3.3333...
print(10 % 3)  # Modulus (remainder of division): 10 % 3 = 1
print(10 // 3)  # Floor division (quotient of division): 10 // 3 = 3
print(10 ** 3)  # Exponentiation: 10 ^ 3 = 1000


# . Using Built-in Functions with Numbers



print(abs(-10))  # Output: 10 abs() - Absolute Value

print(round(3.14159, 2))  # Output: 3.14 round() - Rounding Numbers



print(pow(2, 3))  # Output: 8 pow(x, y) - Exponentiation (x ** y)


print(max(5, 10, 2))  # Output: 10 max() and min() - Finding Maximum and Minimum
print(min(5, 10, 2))  # Output: 2


#Common math Functions

print(math.sqrt(25))    # Output: 5.0
print(math.factorial(5))  # Output: 120
print(math.ceil(4.3))    # Output: 5 ceil() - Rounding Up
print(math.floor(4.7))   # Output: 4 floor() - Rounding Down
print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045 math.e and math.pi - Constants

import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.random())  # Random float between 0 and 1
print(random.uniform(1, 10))  # Random float between 1 and 10

choices = ["apple", "banana", "cherry"]
print(random.choice(choices))  # Randomly picks one item from the list

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: Shuffled list of numbers




#Type Conversion in Python




x = 10   # Integer
y = 2.5  # Float

result = x + y  # Python converts 'x' to float automatically

print(result)   # Output: 12.5
print(type(result))  # Output: <class 'float'>

#Integer Conversion (int())



a = 10.9
b = "15"

print(int(a))  # Output: 10 (removes decimal part)
print(int(b))  # Output: 15 (converts string to int)


#Float Conversion (float())


a = 10
b = "3.14"

print(float(a))  # Output: 10.0
print(float(b))  # Output: 3.14


#Complex Number Conversion (complex())


a = 5
b = 3.2

print(complex(a))  # Output: (5+0j)
print(complex(b))  # Output: (3.2+0j)
print(complex(a, b))  # Output: (5+3.2j)

#String Conversion (str())


a = 100
b = 3.14

print(str(a))  # Output: "100"
print(str(b))  # Output: "3.14"



#Boolean Conversion (bool())
print(bool(0))  # Output: False
print(bool(10))  # Output: True
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
print(bool([]))  # Output: False
print(bool([1, 2, 3]))  # Output: True

#Example: Converting Data Types

a = "10"
b = "20"

# Convert strings to integers and add
sum_value = int(a) + int(b)

print(sum_value)  # Output: 30
print(type(sum_value))  # Output: <class 'int'>





# Augmented Assignment Operator:

x = 10;
x += 3  # x = x + 3

x += 3	
x = x + 3
x = 10;
x += 3 # 13
x = x - 3
x -= 3

x = 10; 
x -= 3 # 7
x *= 3	
x = x * 3
x = 10;
x *= 3 # 30
x /= 3	
x = x / 3
x = 10;
x /= 3 # 3.3333
x //= 3
x = x // 3
x = 10; 
x //= 3 # 3
x %= 3
x = x % 3
x = 10;
x %= 3 # 1
x **= 3	
x = x ** 3
x = 2; 
x **= 3 # 8