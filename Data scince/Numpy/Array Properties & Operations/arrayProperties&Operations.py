

#Array Properties & Operations python numpy

import numpy as np

array = np.array([10,20,30,40,50,60])
print("Array 1  Dimension( :", array.ndim)
array = np.array([[10,20,30,40,50,60],
                  [1,2,3,4,5,6]])



# 3 d array = np.array([[[10,20,30,40,50,60],
#                  [1,2,3,4,5,6]],
#                  [[10,20,30,40,50,60],
#                  [1,2,3,4,5,6]]])



print("Array Properties & Operations", array)
print("Array Shape:", array.shape)
print("Array Dimension( :", array.ndim)
print("Array Size:", array.size)
print("Array Data Type:", array.dtype)


#5. itemsize  একটি Element কত Byte Memory নিচ্ছে।

print("Array Item Size:", array.itemsize)

#nbytes  পুরো Array কত Byte Memory ব্যবহার করছে।

print("Array Total Bytes:", array.nbytes)
print ("Array Type:", type(array))