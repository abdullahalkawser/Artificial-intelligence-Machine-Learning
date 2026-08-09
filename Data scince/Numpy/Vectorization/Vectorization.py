# ⚡ NumPy Vectorization — সহজভাবে বুঝি

# Vectorization হলো এমন একটি technique যেখানে একটি array-এর অনেকগুলো value-এর উপর একসাথে operation করা হয়, Python for loop না লিখে।

# সহজ ভাষায়:

# Loop বাদ দিয়ে পুরো array-এর উপর একসাথে calculation করাই Vectorization।

# NumPy শেখার সময় Broadcasting + Vectorization দুটো খুব গুরুত্বপূর্ণ।

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

reeuslt = arr * 2  # Vectorized operation: Multiply each element by 2
new_arr = arr + 5  # Vectorized operation: Add 5 to each element
srr = arr ** 2  # Vectorized operation: Square each element
print("Original array:", arr)
print("After multiplying by 2:", reeuslt)
print("After adding 5:", new_arr)
print("After squaring:", srr)


A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A + B

print(C)


# একসাথে পুরো matrix-এর calculation হয়েছে।


# খুব সহজ Comparison
# বিষয়	Meaning
# for loop	এক এক করে কাজ
# Vectorization	একসাথে অনেক data-এর উপর কাজ
# Broadcasting	Different shape-এর data কীভাবে operation করবে
# NumPy	Efficient numerical calculation