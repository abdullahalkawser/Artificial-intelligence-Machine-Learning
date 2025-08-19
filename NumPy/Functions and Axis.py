import numpy as np

a = np.array([1, 2, 3, 4, 5])

# np.sum() → যোগফল

# np.mean() → গড়

# np.min() / np.max() → সর্বনিম্ন / সর্বোচ্চ

# np.std() → Standard deviation

# np.var() → Variance
print("Array:", a)
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))



#2D Array + axis

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# Column-wise sum (axis=0)
col_sum = np.sum(a, axis=0)

# Row-wise sum (axis=1)
row_sum = np.sum(a, axis=1)

print("Array:\n", a)
print("Column-wise sum (axis=0):", col_sum)
print("Row-wise sum (axis=1):", row_sum)


# Mean along axis
print("Mean along columns:", np.mean(a, axis=0))
print("Mean along rows:", np.mean(a, axis=1))

# Max along axis
print("Max along columns:", np.max(a, axis=0))
print("Max along rows:", np.max(a, axis=1))

# Min along axis
print("Min along columns:", np.min(a, axis=0))  
print("Min along rows:", np.min(a, axis=1))

# Standard deviation along axis
print("Standard deviation along columns:", np.std(a, axis=0))
print("Standard deviation along rows:", np.std(a, axis=1))
# Variance along axis
print("Variance along columns:", np.var(a, axis=0))
print("Variance along rows:", np.var(a, axis=1))    

