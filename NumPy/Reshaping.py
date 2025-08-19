import numpy as np

a = np.arange(1,13)  # 1 থেকে 12 পর্যন্ত সংখ্যা তৈরি করে।
# arange(start, stop) ফাংশন start থেকে শুরু করে stop-1 পর্যন্ত সংখ্যা তৈরি করে।
print("Original array:",a)
print("Shape of original array:", a.shape)
b = a.reshape((3,4))
print("Reshaped array:\n", b)
print("Reshaped array:\n", b.shape)

# np.newaxis দিয়ে array এর dimension এক ধাপ বাড়ানো যায়। সাধারণত 1D → 2D বা extra dimension যুক্ত করার জন্য ব্যবহার হয়।

#Example 1: 1D → 2D Row Vector

c = a[:,np.newaxis]  # 1D array কে 2D array তে রূপান্তর করা হচ্ছে।
print("Array after adding new axis:\n", c)

#arr[:, np.newaxis] → 1D → 2D column vector
c = a[np.newaxis,:]  # 1D array কে 2D array তে রূপান্তর করা হচ্ছে।
print("Array after adding new axis:\n", c)




arr = np.arange(1, 13)  # 1 থেকে 12 পর্যন্ত সংখ্যা তৈরি করে।


#✨ Example 3: Using None (equivalent to np.newaxis)
row_vec2 = arr[None, :]    # same as np.newaxis
col_vec2 = arr[:, None]    # same as np.newaxis

print(row_vec2.shape, col_vec2.shape)