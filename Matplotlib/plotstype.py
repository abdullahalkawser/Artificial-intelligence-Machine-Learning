import numpy as np
import matplotlib.pyplot as plt

# Random data generate
t = np.random.randn(10)

# Figure size (ঐচ্ছিকভাবে বড়/স্পষ্ট গ্রাফের জন্য)
plt.figure(figsize=(6,4))

# Scatter plot
plt.scatter(t, t*2, marker='*', color='r')

# Labels
plt.xlabel("X axis label")
plt.ylabel("Y axis label (t * 2)")

# Title
plt.title("Random Scatter Plot Example")

# Grid যোগ করলে বুঝতে সহজ হয়
plt.grid(True)

# Show the plot
plt.show()
