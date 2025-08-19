import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Concatenating arrays along the first axis (default)
c = np.concatenate((a, b))
print("Concatenated array:", c)

# 2D Arrays (দুই-মাত্রিক অ্যারে)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
d = np.concatenate((a, b), axis=0)  # # Row-wise concatenation (axis=0)
e = np.concatenate((a, b), axis=1)  # Column-wise concatenation (axis=1)
print("Concatenated along columns:\n", e)
print("Concatenated along rows:\n", d)

#hstack ও vstack
ra = np.array([[1, 2], [3, 4]])
rb = np.array([[5, 6], [7, 8]])
cr = np.hstack((ra, rb))  # Horizontal stack
cv = np.vstack((ra, rb))  # Vertical stack 
print("Horizontal stack:\n", cr)
print("Vertical stack:\n", cv)