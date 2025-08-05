# Python Data Structures: List vs Array vs NumPy Array

## ১. Python List (Mixed Data Types Possible)
- List-এ বিভিন্ন ধরনের মান রাখা যায় — যেমন integer, string, float, boolean একসাথে।
- ছোট থেকে মাঝারি ডেটার জন্য উপযুক্ত।
- ডেটার টাইপ একই হতে হবে এমন বাধ্যবাধকতা নেই।

```python
my_list = [1, "hello", 3.14, True]

print(my_list)
# Output: [1, 'hello', 3.14, True]
২. Python Array (array module) (Same Type Only)
array মডিউল থেকে তৈরি করা Array শুধুমাত্র একই ধরনের ডেটা রাখতে পারে।

সংখ্যাসূচক ডেটার জন্য দ্রুত এবং memory efficient।

টাইপ কোড 'i' দ্বারা integer array তৈরি করা হয়।

python
Copy
Edit
import array

# 'i' means integer type
my_array = array.array('i', [1, 2, 3, 4])

print(my_array)       # Output: array('i', [1, 2, 3, 4])
print(my_array[2])    # Output: 3
৩. NumPy Array (Numerical Computing এর জন্য)
বড় ডেটাসেট ও গাণিতিক কাজের জন্য বেশি উপযোগী।

Scientific computing এ ব্যাপক ব্যবহৃত।

দ্রুত এবং বেশি ফাংশনালিটি থাকে।

python
Copy
Edit
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
# Output: [1 2 3 4]

সংক্ষেপে:

List সহজে ব্যবহারযোগ্য, যেখানে ডেটা মিক্সড টাইপ হতে পারে।

array.array একই ধরনের সংখ্যাসূচক ডেটার জন্য ভালো এবং মেমোরি কম ব্যবহার করে।

NumPy Array বড় আকারের গাণিতিক কাজের জন্য সবচেয়ে বেশি ব্যবহৃত এবং দ্রুত।





# 🔢 Dot Product in Python (with NumPy)

**Dot Product** হলো দুটি ভেক্টরের মধ্যে একটি scalar মানের গাণিতিক গুণফল।  
Formula: a · b = a₁×b₁ + a₂×b₂ + ... + aₙ×bₙ

import numpy as np

# Define two 1D vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Method 1: Using np.dot()
dot_product = np.dot(a, b)
print(dot_product)  # Output: 32

# Method 2: Using @ operator (Python 3.5+)
print(a @ b)        # Output: 32

 Explanation: (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32




 For 2D Arrays (Matrix Dot Product)

 A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication (dot product)
result = np.dot(A, B)
print(result)

Calculation:
[1×5 + 2×7, 1×6 + 2×8] => [19, 22]
[3×5 + 4×7, 3×6 + 4×8] => [43, 50]

