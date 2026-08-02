#Array Modification বলতে বোঝায়, একটি NumPy array তৈরি হওয়ার পর তার value পরিবর্তন করা, নতুন value যোগ করা, value মুছে ফেলা, replace করা বা update করা। array[index] = new_value

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print('original array:', a)

a[0] = 10 #index 0 er value 10  diye relace koira holo


print('array after modification:', a)




b = np.array([[1, 2, 3],
              [4, 5, 6]])

b[1, 1] = 6 #index (0,1) er value 10  diye relace koira holo Row 0, Column 1-এর value 2 ছিল।
# এখন 50 হয়েছে।

print('2D array after modification:', b)
