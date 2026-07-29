
#array creation python numpy

import numpy as np



array = np.array([1,2,3,4,5,6,6,6,6,7,8,9,10])

print('Manual creation of array:', array)


# Creating an array using np.zeros() function

array2 =np.zeros((2,4))
print('Creating an array using np.zeros() function:', array2)


# Creating an array using np.ones() function

array3 = np.ones((3,5))
print('Creating an array using np.ones() function:', array3)

# Creating an array using np.arange() function

array4 = np.arange(5,100,5)

#ধরো, তুমি 0 থেকে 100 পর্যন্ত প্রতি 5 ইউনিট পরপর Data Point চাও।
print('Creating an array using np.arange() function:', array4)


# Creating an array using np.linspace() function

array5 = np.linspace(0,100,10)
#ধরো, তুমি 0 থেকে 100 পর্যন্ত 10টি Data Point চাও 
print('Creating an array using np.linspace() function:', array5)


# Creating an array using np.eye() function
#identity matrix তৈরি করতে np.eye() ব্যবহার করা হয়। np.eye(n) n x n identity matrix return করে।

array6 = np.eye(3)
print('Creating an array using np.eye() function:', array6)




array7 = np.full((2,3),7)
print('Creating an array using np.full() function:', array7)




#📌 Quick Revision Table
# Function	কী কাজ করে	Real-Life Example
# np.array()	List → Array	Student Marks
# np.zeros()	সব 0	Blank Image / Empty Matrix
# np.ones()	সব 1	Default Flag
# np.empty()	খালি Memory	পরে Data Fill করবে
# np.full()	একই Value	সব Student-এর Initial Score = 50
# np.eye()	Identity Matrix	Linear Algebra
# np.arange()	Step অনুযায়ী সংখ্যা	Even Number, Index
# np.linspace()	Equal Interval	Graph X-axis
# np.random.rand()	Random Float	AI Testing
# np.random.randint()	Random Integer	Dice, Random Data
# 🎯 AI/ML-এ সবচেয়ে বেশি ব্যবহৃত
# ⭐ np.array()
# ⭐ np.zeros()
# ⭐ np.ones()
# ⭐ np.arange()
# ⭐ np.linspace()
# ⭐ np.random.rand()
# ⭐ np.random.randint()
# ⭐ np.eye()





array= np
