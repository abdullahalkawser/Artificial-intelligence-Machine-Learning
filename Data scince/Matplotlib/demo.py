# 1. Matplotlib কী?

# Matplotlib = Python দিয়ে data-এর graph/chart তৈরি করার library।

# 🧠 Shortcut:

# Data → Matplotlib → Visualization

# ML-এ data বুঝতে, pattern দেখতে, trend দেখতে Matplotlib ব্যবহার হয়।


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks of a student scored in the exam")
plt.grid() # Add grid for better readability
plt.plot(x, y, marker="*", linestyle="dashed") # Add markers to the data points


plt.show()


# সবচেয়ে গুরুত্বপূর্ণ Shortcuts
# plt.plot()

# ➡️ Line graph

# plt.title()

# ➡️ Graph-এর নাম

# plt.xlabel()

# ➡️ X-axis-এর নাম

# plt.ylabel()

# ➡️ Y-axis-এর নাম

# plt.grid()

# ➡️ Grid দেখাও

# plt.show()

# ➡️ Graph দেখাও

# marker="o"

# ➡️ Data point দেখাও