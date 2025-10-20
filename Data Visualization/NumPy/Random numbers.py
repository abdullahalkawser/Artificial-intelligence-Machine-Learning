# 1. np.random.rand() → Random float numbers (0 to 1 range)

# 👉 Uniform distribution এ 0 থেকে 1 এর মধ্যে random float generate করে।

import numpy as np

arr = np.random.rand(2, 3)  # 2 rows, 3 columns
print(arr)


# 2. np.random.randn() → Random numbers (Normal distribution)

# 👉 Mean = 0, Standard Deviation = 1, অর্থাৎ Gaussian distribution।
arr = np.random.randn(3, 3)  # 3x3 matrix
print(arr)
# 👉 এলোমেলো সংখ্যা generate করার জন্য। Dimension নির্দিষ্ট করতে হয় ।    


# 3. np.random.randint() → Random integers

# 👉 নির্দিষ্ট range এর মধ্যে random integer generate করে।
# Syntax → np.random.randint(low, high, size)

arr = np.random.randint(10, 50, (2, 4))  # 10 থেকে 49 এর মধ্যে random int # 2x4 array
print(arr)


# 4. np.random.random() → Random float numbers (0 to 1)

# 👉 একক float বা array আকারে generate করা যায়।

x = np.random.random()     # single random float
arr = np.random.random((2,2))  # 2x2 array
print(x)
print(arr)



# 5. np.random.choice() → Randomly pick from given list/array

# 👉 কোনো list/array থেকে এলোমেলোভাবে element বেছে নেয়।

arr = np.array([10, 20, 30, 40, 50])

choice1 = np.random.choice(arr)        # single random element
choice2 = np.random.choice(arr, 3)     # 3 random elements
print(choice1)
print(choice2)

# 6. np.random.seed() → Fixed random values (for reproducibility)

# 👉 প্রতিবার একই random number পেতে চাইলে seed সেট করতে হয়।

np.random.seed(42)
print(np.random.randint(1, 100, 5))


✅ Summary Table
Function	কাজ	Example
np.random.rand()	0–1 range random float	np.random.rand(2,3)
np.random.randn()	Normal distribution (mean=0, std=1)	np.random.randn(3,3)
np.random.randint()	Random integers	np.random.randint(10,50,(2,4))
np.random.random()	0–1 float (single/array)	np.random.random((2,2))
np.random.choice()	Randomly pick values	np.random.choice(arr,3)
np.random.seed()	Fixed reproducible random	np.random.seed(42)
