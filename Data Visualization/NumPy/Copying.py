import numpy as np


# English: Copying means creating a new array from an existing array.
# বাংলা: Copying হলো একটি নতুন array তৈরি করা যা মূল array-এর সাথে সম্পর্কিত বা সম্পর্কহীন হতে পারে।

# NumPy-তে মূলত তিন ধরনের copying থাকে:

# View (Shallow Copy)

# Copy (Deep Copy)

# Assignment (Reference)



a = np.array([1, 2, 3])
b = a  # Assignment

b[0] = 100

print("Array a:", a)
print("Array b:", b)

# b = a → মূল array a পরিবর্তিত হলে b ও পরিবর্তিত হয়।

# View (Shallow Copy)

a = np.array([1, 2, 3])
b = a.view()  # Shallow copy

b[0] = 100

print("Array a:", a)
print("Array b:", b)
# View → নতুন array object, কিন্তু data একই জায়গায় থাকে।

# Array shape বা metadata independent, কিন্তু data shared।



# Copy (Deep Copy)

a = np.array([1, 2, 3])
b = a.copy()  # Deep copy

b[0] = 100

print("Array a:", a)
print("Array b:", b)


# b = a.copy() → মূল array পরিবর্তিত হলেও copy পরিবর্তিত হয় না।