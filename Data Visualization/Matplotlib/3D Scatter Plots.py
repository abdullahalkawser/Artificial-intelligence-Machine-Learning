from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# ১. ৩টি ডাইমেনশনের ডেটা তৈরি করা
x = np.random.randn(100) * 10   # X-axis data
y = np.random.randn(100) * 5    # Y-axis data
z = np.random.randn(100) * 20   # Z-axis data

# ২. Figure তৈরি এবং 3D subplot যোগ করা
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# ৩. 3D scatter আঁকা
ax.scatter(
    x, y, z,
    c='blue',          # পয়েন্টের রঙ
    marker='o',        # পয়েন্টের আকার
    s=40,              # পয়েন্টের size
    alpha=0.7          # transparency
)

# ৪. অক্ষগুলোর নাম দেওয়া (optional but useful)
ax.set_title("3D Scatter Plot Example")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

# ৫. গ্রাফ দেখানো
plt.show()







# 3D Curve Plots


# প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করি
import numpy as np           # সংখ্যা ও গণনার জন্য
import matplotlib.pyplot as plt   # প্লট করার জন্য
from mpl_toolkits.mplot3d import Axes3D  # 3D প্লটের জন্য

# t এর মান নির্ধারণ (0 থেকে 10π পর্যন্ত 1000টি পয়েন্ট)
t = np.linspace(0, 10 * np.pi, 1000)

# হেলিক্স সমীকরণ
x = np.cos(t)   # x = cos(t)
y = np.sin(t)   # y = sin(t)
z = t           # z = t  (ধীরে ধীরে উপরে উঠবে)

# 3D ফিগার তৈরি করি
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# লাইন (কার্ভ) আঁকি
ax.plot(x, y, z)

# টাইটেল ও লেবেল যোগ করি
ax.set_title("3D Helix (স্পাইরাল কার্ভ)")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# প্লট দেখাই
plt.show()




# 3D Bar Plots


# প্রয়োজনীয় লাইব্রেরি ইমপোর্ট
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D plot করার জন্য

# ডাটা তৈরি (উদাহরণ হিসাবে ছোট সংখ্যা ব্যবহার)
x = [1, 2, 3, 4, 5]       # X-axis এর মান
y = [2, 3, 4, 5, 6]       # Y-axis এর মান
z = np.zeros(5)           # সববার মাটি থেকে শুরু হবে (0 height থেকে)

# প্রতিটি বার-এর উচ্চতা (Z direction)
height = [5, 2, 7, 1, 6]  # বার কতটা উপরে উঠবে

# বার-এর প্রস্থ নির্ধারণ
dx = np.ones(5) * 0.5     # X-axis এ বার-এর প্রস্থ
dy = np.ones(5) * 0.5     # Y-axis এ বার-এর প্রস্থ
dz = height               # Z-axis এ উচ্চতা

# 3D প্লট তৈরি
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3D বার আঁকা
ax.bar3d(x, y, z, dx, dy, dz)

# শিরোনাম ও লেবেল যোগ করা
ax.set_title("3D Bar Plot (৩ডি বার প্লট উদাহরণ)")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Height (Z)")

# প্লট দেখানো
plt.show()

