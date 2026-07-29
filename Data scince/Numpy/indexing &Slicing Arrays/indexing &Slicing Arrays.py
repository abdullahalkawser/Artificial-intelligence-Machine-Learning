# Indexing in numpy 

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr)

print(arr[3])
print(arr[0])

#Negative Indexing Negative Index মানে শেষ থেকে গণনা করা।

print(arr[-1])
print(arr[-3])



# 2d array indexing


arry = np.array([[1,2,3,4,5,6],
                 [7,8,9,10,11,12]

                 ])

# print('2d array porint',arry)
# arr[row,column]

print("2d array pinting and indexing ",arry[0][1])

print("2d array pinting and indexing ",arry[1][3])



# Slicing numpy python Slicing array[start:stop]

arrs=np.array([10,20,30,40,50])
# Value : 10   20   30   40   50   60
# Index :  0    1    2    3    4    5
#                ↑───────↑
#              শুরু      থামবে (4 নেবে না)

# নেওয়া হবে → 20 30 40

# সহজে মনে রাখার ট্রিক 🎯

# Start = নেবে (Included) ✅

# Stop = নেবে না (Excluded) ❌

print(arrs[1:5])

print(arrs[3:5])






