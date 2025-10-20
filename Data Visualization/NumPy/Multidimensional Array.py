import numpy as np

# 1D Array Example:

arr1 = np.array([1, 2, 3, 4])
print(arr1)
print(arr1.shape)


# // 2D Array Example:
arr2 = np.array([[1,2,3,4,5,6,7,8,9,10],[10,11,12,13,14,15,16,17,18,19]])
print(arr2)
# print(arr2.shape)// Output: (2, 10)

# //3D Array:

# Structure:

# 2 blocks (layers)

# Each block has 2 rows × 2 columns

arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(arr3)
print(arr3.shape)  # Output: (2, 2, 3)
print(arr2.ndim)   # 2 → 2D array
