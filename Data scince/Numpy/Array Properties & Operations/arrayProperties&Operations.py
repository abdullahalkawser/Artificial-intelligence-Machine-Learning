

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



#astype()  Array কে অন্য Data Type এ Convert করতে ব্যবহার হয়।
array = array.astype('float64')
relst = array.astype('int32')



print("Array Properties & Operations", relst)




#mathamatical Operations Numpy 


arr = np.array([10,20,30,40,50,60])
print( arr + 10) #add 10 to each element
print( arr - 10) #sub 10 to each element
print( arr * 10) #multiply 10 to each element
print( arr / 10) #divide 10 to each element
print( arr ** 2) #power of 2 to each element
print( arr % 10) #modulus 10 to each element
print( arr // 10) #floor division 10 to each element




#aggegate functions  mean, median, sum, min, max, std, var
arr = np.array([10,20,30,40,50,60])
arr = np.sum(arr)   

arr = np.mean(arr)
arr = np.median(arr)
arr = np.min(arr)
arr = np.max(arr)
arr = np.std(arr)
arr = np.var(arr)


print ("Array Properties & Operations aggeate oapretion ", arr)





