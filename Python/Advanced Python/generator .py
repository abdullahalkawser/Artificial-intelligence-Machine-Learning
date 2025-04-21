def newa():
    print('1st')
    yield 10 #yield একটার পর একটা মান দেয় এবং function এর "pause state" মনে রাখে।
    print('1st')
    yield 12
    print('1st')
    yield 15
    print('1st')
    yield 15

z = newa()
print(next(z))  
print(next(z))    
print(next(z))      
print(next(z))    

#Generator to Yield Squares of Numbers


def square_numbers(n):
    for i in range(n):
        yield i * i

# Using the generator
for num in square_numbers(5):
    print(num)


# Define a generator function to generate Fibonacci numbers up to a limit
def fibonacci_generator(limit):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    count = 0    # Counter to keep track of how many numbers have been generated

    # Loop until we've generated the desired number of Fibonacci numbers
    while count < limit:
        yield a  # Yield the current value of 'a' (this pauses the function)
        a, b = b, a + b  # Move to the next two numbers in the sequence
        count += 1  # Increment the counter

# Using the generator in a for loop
for num in fibonacci_generator(10):
    print(num)  # Prints each Fibonacci number yielded by the generator
