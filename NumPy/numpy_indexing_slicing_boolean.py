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


# //

# 2. Slicing (range নিয়ে কাজ করা)

arr = np.array([10,20,30,40,50,60])

print(arr[1:4])    # [20 30 40] → index 1 থেকে 3
print(arr[:3])     # [10 20 30] → প্রথম 3 টা element
print(arr[3:])     # [40 50 60] → index 3 থেকে শেষ পর্যন্ত
print(arr[::2])    # [10 30 50] → step 2


# 2D slicing
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[0:2, 1:3])  
# [[2 3]
#  [5 6]]

# Boolean Indexing (শর্ত দিয়ে ডেটা ফিল্টার করা)


arr = np.array([10, 20, 30, 40, 50])

print(arr > 25)        # [False False  True  True  True]
print(arr[arr > 25])   # [30 40 50]

print(arr % 20 == 0)   # [False  True False  True False]
print(arr[arr % 20 == 0]) # [20 40]
print(arr2d[arr2d > 5])  # [6 7 8 9] → 5 এর বেশি element গুলো
print(arr2d[arr2d % 2 == 0])  # [2  4 6 8] → even numbers