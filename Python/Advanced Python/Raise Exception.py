age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative!")
else:
    print("Your age is:", age)


# Raising a Custom Exception    

# 4



class Accident(Exception):  # Custom Exception
    def __init__(self, msg):
        self.msg = msg        # Store message
    
    def abdullah(self):       # Custom method
        print('user define')
#Optional Improvements:

raise Accident("Be careful on the road!")


# Outside the class
# try:
#     raise Accident('car is crashed')
# except Accident as e:
#     print("Caught an accident:", e.msg)
#     e.abdullah()



#  Most Common Built-in Exceptions in Python    
# MemoryError,ValueError	Raised when a function receives a valid type but invalid value.
# TypeError	Raised when an operation is applied to an object of inappropriate type.
# NameError	Raised when a variable is not defined.
# IndexError	Raised when a list/tuple index is out of range.
# KeyError	Raised when a dictionary key is not found.
# ZeroDivisionError	Raised when dividing a number by zero.
# ImportError	Raised when an import fails.
# AttributeError	Raised when an attribute reference or assignment fails.
# FileNotFoundError	Raised when a file or directory is requested but doesn’t exist.
# RuntimeError	Raised when an error is detected that doesn’t fall in other categories.
# StopIteration	Raised by next() when there are no more items.
# IndentationError	Raised when indentation is not correct.
# SyntaxError	Raised when the parser finds a syntax error.
# MemoryError	Raised when an operation runs out of memory.
# FloatingPointError	Raised when a floating point operation fails.
# OverflowError






