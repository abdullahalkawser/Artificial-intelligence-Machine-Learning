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



# 2. Modify Multiple Values

# একসাথে অনেকগুলো value পরিবর্তন করা যায়।



c = np.array([1, 2, 3, 4, 5])

c[1:4] = 10 #index 1 theke 3 porjonto value 10 diye relace koira holo

c[1:4]= [10,20,30] #index 1 theke 3 porjonto value 10,20,30 diye relace koira holo

print('array after modifying multiple values:', c)
