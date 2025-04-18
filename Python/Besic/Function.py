#Syntax for Defining a Function:
def function_name(parameters):
    # Block of code
    return 

def greet():
    print("Hello, World!") # Function body

greet()  # Calling the function



# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Calling the function with an argument
greet("Bob")    # Calling with a different argument

#Function with a Return Value

def add(a, b):
    return a + b

result = add(3, 5)  # The function returns the sum
print(result)


#Function with Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Uses the default value "Guest"
greet("Alice")  # Passes "Alice" as an argument

#Functions with Multiple Return Values

def operations(x, y):
    sum_result = x + y
    diff_result = x - y
    return sum_result, diff_result  # Returns both results as a tuple

result_sum, result_diff = operations(10, 5)
print("Sum:", result_sum)
print("Difference:", result_diff)

#Lambda Functions (Anonymous Functions)

# A lambda function that adds two numbers
add = lambda x, y: x + y

print(add(3, 5))  # Output will be 8

#Recursion (A function calling itself)

def factorial(n):
    if n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output will be 120
#Function Scope

x = 10  # Global variable

def my_function():
    y = 20  # Local variable
    print(x)  # Accesses global variable
    print(y)  # Accesses local variable

my_function()
