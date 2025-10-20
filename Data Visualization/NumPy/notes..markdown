# Python Data Structures: List vs Array vs NumPy Array

## ১. Python List (Mixed Data Types Possible)
- List-এ বিভিন্ন ধরনের মান রাখা যায় — যেমন integer, string, float, boolean একসাথে।
- ছোট থেকে মাঝারি ডেটার জন্য উপযুক্ত।
- ডেটার টাইপ একই হতে হবে এমন বাধ্যবাধকতা নেই।

```python
my_list = [1, "hello", 3.14, True]

print(my_list)
# Output: [1, 'hello', 3.14, True]
২. Python Array (array module) (Same Type Only)
array মডিউল থেকে তৈরি করা Array শুধুমাত্র একই ধরনের ডেটা রাখতে পারে।

সংখ্যাসূচক ডেটার জন্য দ্রুত এবং memory efficient।

টাইপ কোড 'i' দ্বারা integer array তৈরি করা হয়।

python
Copy
Edit
import array

# 'i' means integer type
my_array = array.array('i', [1, 2, 3, 4])

print(my_array)       # Output: array('i', [1, 2, 3, 4])
print(my_array[2])    # Output: 3
৩. NumPy Array (Numerical Computing এর জন্য)
বড় ডেটাসেট ও গাণিতিক কাজের জন্য বেশি উপযোগী।

Scientific computing এ ব্যাপক ব্যবহৃত।

দ্রুত এবং বেশি ফাংশনালিটি থাকে।

python
Copy
Edit
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
# Output: [1 2 3 4]

সংক্ষেপে:

List সহজে ব্যবহারযোগ্য, যেখানে ডেটা মিক্সড টাইপ হতে পারে।

array.array একই ধরনের সংখ্যাসূচক ডেটার জন্য ভালো এবং মেমোরি কম ব্যবহার করে।

NumPy Array বড় আকারের গাণিতিক কাজের জন্য সবচেয়ে বেশি ব্যবহৃত এবং দ্রুত।





# 🔢 Dot Product in Python (with NumPy)

**Dot Product** হলো দুটি ভেক্টরের মধ্যে একটি scalar মানের গাণিতিক গুণফল।  
Formula: a · b = a₁×b₁ + a₂×b₂ + ... + aₙ×bₙ

import numpy as np

# Define two 1D vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Method 1: Using np.dot()
dot_product = np.dot(a, b)
print(dot_product)  # Output: 32

# Method 2: Using @ operator (Python 3.5+)
print(a @ b)        # Output: 32

 Explanation: (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32




 For 2D Arrays (Matrix Dot Product)

 A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication (dot product)
result = np.dot(A, B)
print(result)

Calculation:
[1×5 + 2×7, 1×6 + 2×8] => [19, 22]
[3×5 + 4×7, 3×6 + 4×8] => [43, 50]









# 📘 NumPy Multidimensional Arrays (ndarray) – বাংলা-ইংলিশ নোট

NumPy-র সবচেয়ে important feature হলো এর **ndarray (N-dimensional array)**। এটা এক ধরণের array object যেটা multiple dimensions handle করতে পারে – 1D, 2D, 3D বা তার চেয়েও বেশি।

---

## 🧠 What is an ndarray?

NumPy-এর `ndarray` হচ্ছে multi-dimensional array যার মধ্যে সব elements একি data type-এর হয়।

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)
```

🔹 Output:
```
[1 2 3]
```

এখানে `arr` হলো 1-Dimensional array।

---

## 🌀 Dimensions Explained

### ✅ 1-D Array

একটা সাধারণ লিস্টের মত।

```python
arr1d = np.array([10, 20, 30])
print(arr1d)
```

🔹 Shape: `(3,)` → 3 items, 1 dimension

---

### ✅ 2-D Array (Matrix)

Matrix-এর মতো Row এবং Column থাকে।

```python
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arr2d)
```

🔹 Shape: `(2, 3)` → 2 rows, 3 columns

---

### ✅ 3-D Array (Tensor)

Multiple 2D arrays এর collection

```python
arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr3d)
```

🔹 Shape: `(2, 2, 2)` → 2 matrices, each 2x2

---

## 🔍 Important Attributes

| Attribute        | Description                           | উদাহরণ |
|------------------|---------------------------------------|--------|
| `ndim`           | Dimension count                       | `arr.ndim` |
| `shape`          | Tuple of dimensions (rows, cols, etc) | `arr.shape` |
| `size`           | Total number of elements               | `arr.size` |
| `dtype`          | Data type of elements                 | `arr.dtype` |

---

### 🧪 Example:

```python
arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Dimension:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
```

🔹 Output:
```
Dimension: 2
Shape: (2, 3)
Size: 6
Data Type: int64
```

---

## 🛠 Creating Arrays with Functions

| Function        | Description                         |
|------------------|-------------------------------------|
| `np.zeros()`     | All zeros                          |
| `np.ones()`      | All ones                           |
| `np.eye()`       | Identity matrix                    |
| `np.arange()`    | Range array                        |
| `np.reshape()`   | Reshape the array                  |

```python
z = np.zeros((2, 3))
print(z)
```

🔹 Output:
```
[[0. 0. 0.]
 [0. 0. 0.]]
```

---

## 🔄 Reshaping Arrays

```python
a = np.array([1, 2, 3, 4, 5, 6])
reshaped = a.reshape(2, 3)
print(reshaped)
```

🔹 Output:
```
[[1 2 3]
 [4 5 6]]
```

---

## 🔚 Summary (সারাংশ)

- NumPy arrays can be 1D, 2D, 3D বা তারও বেশি dimension এর।
- সব elements এর same data type থাকতে হয়।
- Useful attributes: `ndim`, `shape`, `size`, `dtype`
- You can create arrays using `array()`, `zeros()`, `ones()`, `arange()`, `reshape()` etc.
