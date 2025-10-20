import numpy as np
import matplotlib.pyplot as plt

# ১. এলোমেলো ডেটা তৈরি করা (Mean=0, Std=1)
data = np.random.randn(1000) * 10 + 50
# এখানে data-এর গড় হবে 50 এবং ডেটা আশেপাশে ছড়াবে

# ২. Histogram আঁকা
plt.hist(
    data,
    bins=5,           # কত ভাগে (রেঞ্জে) ভাগ করবে
    color='skyblue',   # বারগুলোর রঙ
    edgecolor='black', # বর্ডার রঙ
    alpha=0.7  ,        # স্বচ্ছতা
    orientation='horizontal' # বারগুলো অনুভূমিক
)

# ৩. গ্রাফের টাইটেল ও এক্সিস লেবেল
plt.title("Histogram of Random Data")
plt.xlabel("Value Range (Bins)")
plt.ylabel("Frequency (Count)")

# ৪. গ্রিড যোগ করতে চাইলে
plt.grid(axis='y', linestyle='--', alpha=0.5)

# ৫. গ্রাফ দেখানো
plt.show()


শেষের সংক্ষিপ্ত নোট (Quick Note)

✅ Histogram হল Numeric Data এর Frequency Distribution দেখানোর জন্য Bar-এর মতো চার্ট
✅ Horizontal axis = Value ranges (bins)
✅ Vertical axis = Frequency (কতবার এসেছে)
✅ plt.hist(data, bins=10) হল মূল ফাংশন
✅ Histogram দিয়ে ডেটার আচরণ (shape, spread, outlier) সহজে বোঝা যায়।
