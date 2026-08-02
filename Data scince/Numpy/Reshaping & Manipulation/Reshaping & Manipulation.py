#Reshaping (Array-এর Shape পরিবর্তন)
#array.reshape(rows, columns)
import numpy as np

a = np.array([1,2,3,4,5,6])

print(a)

b = a.reshape(2,3)

print(b)


#2. Flatten() ২D কে ১D বানানো। নতুন Copy তৈরি করে


arr = np.array([[1,2,3,4,5,],
               [6,7,8,9,10]])
print('2d array ',arr);

print("convert 2d array to 1d array with copy ",arr.flatten())

#3. ravel() Flatten-এর মতো কিন্তু এটি সাধারণত view দেয় (নতুন কপি না বানিয়ে)।

aray2 = np.array([[10,20,30,40,50,],
                 [60,70,80,90,100]])

c= aray2.ravel()
print("ravel function call without copy",c)


# 4. transpose() Row কে Column বানায়।

arra3 = np.array([[1,2,3,4,5,6],
                  [7,8,9,10,11,12]])

print("raow version 2d array ",arra3)
print("row convert to column   2d array ",arra3.T)

