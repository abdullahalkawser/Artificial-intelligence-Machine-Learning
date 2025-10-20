import numpy as np
import matplotlib.pyplot as plt

# # Random data generate
# t = np.random.randn(10)

# # Figure size (ঐচ্ছিকভাবে বড়/স্পষ্ট গ্রাফের জন্য)
# plt.figure(figsize=(6,4))

# # Scatter plot
# plt.scatter(t, t*2, marker='*', color='r')

# # Labels
# plt.xlabel("X axis label")
# plt.ylabel("Y axis label (t * 2)")

# # Title
# plt.title("Random Scatter Plot Example")

# # Grid যোগ করলে বুঝতে সহজ হয়
# plt.grid(True)

# # Show the plot
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# ১. 500টি এলোমেলো (random) x এবং y মান তৈরি করা
# np.random.randn() → Normal distribution থেকে ডেটা নেয় (mean=0, std=1)
# *10 করার ফলে ডেটা একটু বড় রেঞ্জে ছড়িয়ে পড়ে
x = np.random.randn(500) * 10
y = np.random.randn(500) * 10

# ২. Scatter plot আঁকা
plt.scatter(
    x,                # X-axis এর মান
    y,                # Y-axis এর মান
    marker='D',       # পয়েন্টের আকৃতি Diamond (D)
    color='black',    # পয়েন্টের ভিতরের রঙ কালো
    linewidths=7,     # পয়েন্টের বর্ডার লাইন পুরুত্ব
    edgecolors='red', # বর্ডারের রঙ লাল
    alpha=0.1,        # স্বচ্ছতা (10% opacity)
    s=0.5,            # পয়েন্টের আকার (খুবই ছোট - সাধারণত 50 বা 100 ব্যবহার হয়)
    label='Data points'  # লেজেন্ডে দেখানোর নাম
)

# ৩. প্লটে Grid লাইন দেখানো (x-y axis অনুযায়ী ব্যাকগ্রাউন্ড লাইন)
plt.grid(True)

# ৪. লেজেন্ড (label) উপরের বাঁ দিকে দেখানো
plt.legend(loc='upper left')

# ৫. চূড়ান্ত প্লট স্ক্রিনে দেখানো
plt.show()
