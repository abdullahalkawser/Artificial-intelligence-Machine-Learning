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
print('2d array ',arr)

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


# 5. resize() Array-এর Size পরিবর্তন।

d=np.array([1,2,3,4])

d.resize((2,2))

print("change array size",d)

# 6. concatenate()

# দুইটি Array যুক্ত করা।


array1 = np.array([1,2,3,4,5,6,7,8,9,10])
array2 = np.array([11,12,13,14,15,16,17,18,19,20])

concatenated = np.concatenate((array1, array2))
print("concatenated array", concatenated)

# 7. vstack() Vertical Stack এটি একাধিক array-কে উপর-নিচ (row-wise) করে যুক্ত করতে ব্যবহার করা হয়।

a=np.array([1,2,3])

b=np.array([4,5,6])

print(np.vstack((a,b)))
Rahim = np.array([80, 75, 90])
Karim = np.array([70, 85, 88])

students = np.vstack((Rahim, Karim))

print(students)

# np.hstack() (Horizontal Stack)

# hstack এর পূর্ণরূপ হলো Horizontal Stack।

# এটি একাধিক array-কে পাশাপাশি (column-wise) যুক্ত করতে ব্যবহার করা হয়।





f = np.array([1, 2, 3])
g = np.array([4, 5, 6])

print('add to array  useing hstack:', np.hstack((f, g)))

# 9. split()  Array ভাগ করা।

ab = np.array([1, 2, 3, 4, 5, 6])
print('original array:', ab)
print('split array into 3 parts:', np.split(ab, 3))


