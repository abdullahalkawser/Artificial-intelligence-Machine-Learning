#  1. np.array() – Manual values দিয়ে array বানানো

# 👉 Python list বা tuple কে NumPy array তে convert করে।

import numpy as np

# # 1D array
# arr1 = np.array([1, 2, 3, 4])
# print(arr1)

# # 2D array
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)
# # 3D array
# arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(arr3)


# 2. np.zeros() – All zeros array

# 👉 পুরো array শূন্য (0) দিয়ে ভরে যাবে। Dimension নির্দিষ্ট করতে হয়।

# 👉 পুরো array শূন্য (0) দিয়ে ভরে যাবে। Dimension নির্দিষ্ট করতে হয়।

# arr = np.zeros((2, 3))  # 2 rows, 3 columns
# print(arr) 


# 3. np.ones() – All ones array

# 👉 পুরো array 1 দিয়ে ভরে যাবে।

arr = np.ones((2, 3))  # 2 rows, 3 columns
print(arr)



# 4. np.full() – Custom value দিয়ে array

# 👉 নিজের পছন্দমত সংখ্যা দিয়ে array ভরা যায়।


arr = np.full((2, 4), 7)  # 2 row, 4 column, সব জায়গায় 7
print(arr)


# 5. np.arange() – Range দিয়ে array বানানো

# 👉 Python এর range() এর মত কাজ করে, কিন্তু NumPy array return করে।
# Syntax → np.arange(start, stop, step)

arr = np.arange(0, 10, 2)  # 0 থেকে 10 পর্যন্ত, step 2
print(arr)




# 6. np.linspace() – Evenly spaced values

# 👉 নির্দিষ্ট range এর মধ্যে সমান ভাগে সংখ্যা generate করবে।
# Syntax → np.linspace(start, stop, num)

arr = np.linspace(0, 1, 5)  # 0 থেকে 1 পর্যন্ত, মোট 5 ভাগে
print(arr)


# 7. np.eye() – Identity matrix


# 👉 Main diagonal এ 1 থাকবে, বাকি সব জায়গায় 0।
arr = np.eye(3)  # 3x3 identity matrix
print(arr)


# 8. np.random – Random numbers দিয়ে array

# 👉 এলোমেলো সংখ্যা generate করার জন্য।

arr = np.random.rand(2, 3)  # 2 rows, 3 columns, random floats between 0 and 1
print(arr)


## ✅ Summary Table

| Function       | কাজ | Example |
|----------------|--------------------|----------------|
| `np.array()`   | Manual values | `np.array([1,2,3])` |
| `np.zeros()`   | সব 0 দিয়ে ভরে | `np.zeros((2,3))` |
| `np.ones()`    | সব 1 দিয়ে ভরে | `np.ones((3,2))` |
| `np.full()`    | Custom value | `np.full((2,4), 7)` |
| `np.arange()`  | Range of values | `np.arange(1,10,2)` |
| `np.linspace()`| Even spacing | `np.linspace(0,1,5)` |
| `np.eye()`     | Identity matrix | `np.eye(3)` |
| `np.random`    | Random values | `np.random.randint(10,50,(3,3))` |