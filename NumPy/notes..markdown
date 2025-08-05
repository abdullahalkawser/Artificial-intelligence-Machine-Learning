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