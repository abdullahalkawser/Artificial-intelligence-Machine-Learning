# English: NumPy arrays have a specific data type (dtype) which determines the type of elements stored.
# বাংলা: NumPy array-তে প্রতিটি element-এর ডেটা টাইপ থাকে, যা নির্ধারণ করে কোন ধরনের মান রাখা হবে।

# Common dtypes:

# Data Type	NumPy dtype	Example	ব্যাখ্যা
# Integer	int32 / int64	1, 100	পূর্ণসংখ্যা
# Float	float32 / float64	1.5, 3.14	ভগ্নাংশ সংখ্যা
# Complex	complex64 / complex128	1+2j	জটিল সংখ্যা
# Boolean	bool	True, False	True/False মান
# String	str_	'Hello'	স্ট্রিং


# ডিফল্ট ডেটাটাইপ দেখা

import numpy as np

a = np.array([1, 2, 3])
b = np.array([1.5, 2.5, 3.5])

print("Array a:", a, "dtype:", a.dtype)
print("Array b:", b, "dtype:", b.dtype)

# a → integer array → dtype int64

# b → float array → dtype float64

# Datatype নির্ধারণ করা (Specify dtype)


c = np.array([1, 2, 3], dtype=float)
d = np.array([1.5, 2.5, 3.5], dtype=int)

print("Array c:", c, "dtype:", c.dtype)
print("Array d:", d, "dtype:", d.dtype)

# dtype=float → integer values float এ convert হয়ে যায়।

# dtype=int → float values truncate হয়ে integer হয়।


# c → float array → dtype float64
# d → integer array → dtype int64   


# Type Conversion (astype) astype() দিয়ে array কে সহজে অন্য dtype-এ convert করা যায়।

a = np.array([1, 2, 3])
b = a.astype(float)  # int → float
c = b.astype(int)    # float → int

print("Original a:", a, a.dtype)
print("b after astype(float):", b, b.dtype)
print("c after astype(int):", c, c.dtype)


#5️⃣ Common Tips

# Memory optimization: ছোট dtype ব্যবহার করা যায় (int8, float32) → memory কম লাগে।

# Arithmetic বা scientific computation-এ float ব্যবহার বেশি common।

# Boolean array → True/False মানের জন্য।

# 💡 Tip:

# array.dtype → current dtype দেখার জন্য

# astype() → datatype পরিবর্তন করার জন্য