# 🔹 What is a Series?

# English:
# A Series is a one-dimensional array-like object in Pandas that can hold any data type (integers, floats, strings, objects, etc.). It is similar to a column in Excel or SQL table.

# Bangla:
# একটি Series হলো এক-মাত্রিক (1D) ডেটা স্ট্রাকচার যা Pandas এ থাকে। এতে integer, float, string, object যেকোনো ধরনের ডেটা রাখা যায়। একে এক্সেলের এক কলাম বা SQL টেবিলের কলামের মতো ভাবা যায়।

import pandas as pd
 
data =[10, 20, 30, 40]

# Series তৈরি
s = pd.Series(data)
# Series এর তথ্য দেখাও
print("Series:",s)

# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64 #👉 এখানে left side এ index এবং right side এ values।

# ✅ Custom Index
s = pd.Series(data,index=['a', 'b', 'c', 'd'])
print("Custom Index Series:",s)
print(s)

# ✅ From Dictionary

data = {'a': 100, 'b': 200, 'c': 300}
s = pd.Series(data)
print(s)

# Output:

# a    100
# b    200
# c    300
# dtype: int64




# Summary Notes (Bangla + English)

# Series = One-dimensional labeled array
# সিরিজ হলো এক-মাত্রিক লেবেলযুক্ত ডেটা অ্যারে।

# Index + Values থাকে
# বাম দিকে index, ডান দিকে values।

# Create Series from:

# List

# Dictionary

# Numpy array

# Access by:

# Position (s[0])

# Label (s['a'])

# Useful Functions:

# s.values, s.index, s.dtype, s.shape

# s.mean(), s.max(), s.min(), s.sum()

# NaN Handling:

# isnull(), notnull(), fillna(value)