
# NumPy Reshaping, Newaxis & Flatten Notes

এই নোটে আমরা NumPy-এর array reshaping, `np.newaxis` এবং `flatten()` ব্যবহার সম্পর্কে দেখব.

---

## 1️⃣ NumPy Array Reshaping

```python
import numpy as np

# 1 থেকে 12 পর্যন্ত সংখ্যা তৈরি
a = np.arange(1, 13)
print("Original array:", a)
print("Shape of original array:", a.shape)

# 1D → 2D reshaping
b = a.reshape((3, 4))
print("Reshaped array:\n", b)
print("Shape of reshaped array:", b.shape)
```

**ব্যাখ্যা:**  
- `arange(start, stop)` → start থেকে stop-1 পর্যন্ত সংখ্যা তৈরি করে।  
- `reshape((rows, cols))` → array কে নতুন dimension এ রূপান্তর করে।  

---

## 2️⃣ Adding a New Axis (`np.newaxis`)

```python
# 1D → 2D Row Vector
c_row = a[np.newaxis, :]    # Row vector
print("Row vector:\n", c_row)

# 1D → 2D Column Vector
c_col = a[:, np.newaxis]    # Column vector
print("Column vector:\n", c_col)

# Using None (equivalent to np.newaxis)
row_vec2 = a[None, :]
col_vec2 = a[:, None]
print("Shapes:", row_vec2.shape, col_vec2.shape)
```

**ব্যাখ্যা:**  
- `np.newaxis` বা `None` ব্যবহার করে array এর dimension 1 ধাপ বাড়ানো যায়।  
- সাধারণত 1D → 2D বা extra dimension যুক্ত করার জন্য ব্যবহার হয়।  

---

## 3️⃣ Flatten Multi-dimensional Array

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Original array:\n", arr)

flat_arr = arr.flatten()
print("Flattened array:\n", flat_arr)
```

**ব্যাখ্যা:**  
- `flatten()` → multi-dimensional array কে 1D array এ রূপান্তর করে।  
- মূল array অপরিবর্তিত থাকে।  
- সাধারণত সব element এক জায়গায় নিয়ে কাজ করার জন্য ব্যবহার করা হয়।  

---

✅ **Summary:**  
- `reshape()` → shape পরিবর্তন  
- `np.newaxis` বা `None` → extra dimension যোগ  
- `flatten()` → 1D array তৈরি
