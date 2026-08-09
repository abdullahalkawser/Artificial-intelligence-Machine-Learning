# Broadcasting হলো NumPy-এর এমন একটি feature, যার মাধ্যমে ভিন্ন shape-এর array-এর মধ্যে arithmetic operation করা যায়—সবসময় manually reshape বা loop লিখতে হয় না।


import numpy as np

# arr = np.array([10,20,30,40])
# print("array before Broadcasting:",arr)

# print("array after Broadcasting:",arr+10)

d = np.array([10,23,45,67])
c = 10

print("array before Broadcasting:", d)
print("array after Broadcasting:", d + c) # Scalar 10 automatically [10,10,10,10] হয়ে গিয়েছে। প্রতিটি element এর সাথে যোগ হয়েছে।


# 2 daimentional array
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])




print("Multiple array after Broadcasting:", a + b)