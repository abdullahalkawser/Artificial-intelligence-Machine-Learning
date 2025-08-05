import numpy as np

A = np.array([2, 3])
B = np.array([4, 5])

result = np.dot(A, B)
print("Dot Product:", result)
print("A:", A)
print("B:", B)
print("Shape of A:", A.shape)
print("Shape of B:", B.shape)


#  2D Dot Product Example (Matrix form):

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = np.dot(A, B)
print(result)
