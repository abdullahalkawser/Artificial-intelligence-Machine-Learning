import time

# ✅ Decorator definition
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()                # Start timer
        result = func(*args, **kwargs)          # Call the original function
        end_time = time.time()                  # End timer
        print("Function '{}' took {:.6f} seconds".format(func.__name__, end_time - start_time))
        return result                           # Return original function's result
    return wrapper                              # Return the wrapper function

# ✅ Square calculator using the decorator
@time_it
def calculator(numbr):
    result = []
    for i in range(1, numbr + 1):
        result.append(i * i)  # Square of i
    return result

# ✅ Cube calculator using the same decorator
@time_it
def calculators(numbr):
    result = []
    for i in range(1, numbr + 1):
        result.append(i ** 3)  # Cube of i
    return result

# ✅ Function calls
print(calculator(5))   # Should print squares and execution time
print(calculators(5))  # Should print cubes and execution time
