import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr)
print(arr[3])  # Accessing the first element
print(arr[-1])  # (শেষ element)
print(arr[-3])   # শেষ থেকে 3rd element → 8
print(arr[0:5])  # প্রথম 5 element [1 2 3 4 5]
print(arr[::2])  # প্রতি 2nd element [1 3 5 7 9]

# 2D array indexing

arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d[0, 1])  # Accessing element at row 0, column 1 → 2
print(arr2d[1, 2])  # Accessing element at row 1, column 2 → 6
print(arr2d[0])    # Accessing the first row → [1 2 3]
print(arr2d[:, 1])  # Accessing the second column → [2