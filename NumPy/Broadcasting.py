import numpy as np

a = np.array([1, 2, 3, 4])
b = 10

# Scalar addition
c = a + b

print("Array a:", a)
print("Scalar b:", b)
print("Result:", c) #Scalar 10 automatically [10,10,10,10] হয়ে গিয়েছে। প্রতিটি element এর সাথে যোগ হয়েছে।



# 1D array + 1D array (different shapes)


a = np.array([[1], [2], [3]])  # shape (3,1)
b = np.array([10, 20, 30])     # shape (3,)

# Broadcasting
c = a + b

print("Array a:\n", a)
print("Array b:", b)
print("Result:\n", c) # a এর shape (3,1), b এর shape (3,) → NumPy automatically b কে (1,3) বানিয়ে broadcasting করেছে। ফলে সব element-wise যোগ হয়েছে।




#2D array + 1D array
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])

# Broadcasting along rows
c = a + b

print("Result:\n", c)
# a এর shape (2,3), b এর shape (3,) → NumPy automatically b কে (1,3) বানিয়ে broadcasting করেছে। ফলে সব element-wise যোগ হয়েছে। প্রতিটি row এ b যোগ হয়েছে।



# 6️⃣ Important Notes / টিপস

# Broadcasting memory efficient, কারণ actual copy হয় না।

# সব ধরনের arithmetic operation এ কাজ করে: +, -, *, /।

# Shape mismatch হলে ValueError আসে।

# 💡 Tip:

# Scalar + array → সব element এ apply

# Row/Column-wise addition → broadcasting ব্যবহার