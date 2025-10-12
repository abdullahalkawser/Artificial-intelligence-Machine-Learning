import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 50)
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.cos(x)

# Create 2 rows, 2 columns subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 6)) 

# ---------------- Subplot 1 ----------------
axes[0, 0].plot(x, y1, color='r', linestyle='--', marker='o') # red dashed line with circle markers
axes[0, 0].set_title("Linear (y = x)") # Title for the subplot  
axes[0, 0].set_xlabel("X-axis")
axes[0, 0].set_ylabel("Y-axis")

# ---------------- Subplot 2 ----------------
axes[0, 1].plot(x, y2, color='g', linestyle='-', marker='s')
axes[0, 1].set_title("Quadratic (y = x^2)")
axes[0, 1].set_xlabel("X-axis")
axes[0, 1].set_ylabel("Y-axis")

# ---------------- Subplot 3 ----------------
axes[1, 0].plot(x, y3, color='b', linestyle='-.', marker='^')
axes[1, 0].set_title("Sine Wave")
axes[1, 0].set_xlabel("X-axis")
axes[1, 0].set_ylabel("Y-axis")

# ---------------- Subplot 4 ----------------
axes[1, 1].plot(x, y4, color='m', linestyle=':', marker='*')
axes[1, 1].set_title("Cosine Wave")
axes[1, 1].set_xlabel("X-axis")
axes[1, 1].set_ylabel("Y-axis")

# Add main title for the full figure
fig.suptitle("Multiple Plots using Subplots", fontsize=16)

# Adjust spacing to prevent overlap
plt.tight_layout()

# Finally show the plots
plt.show()


# Important Notes (Very Useful)

# 🟢 1. fig, axes = plt.subplots(r, c) → always needed for multiple plots
# 🟢 2. For each subplot use → axes[row, col].plot(...)
# 🟢 3. Use set_title, set_xlabel, set_ylabel for subplot titles and labels
# 🟢 4. Use suptitle() for overall main title
# 🟢 5. plt.tight_layout() → সাইজ ঠিক করে দেয় (no overlap)
# 🟢 6. Styling = color + linestyle + marker
# 🟢 7. axes is an array → so use [row, col]
# 🟢 8. figsize=(width, height) → figure size in inches
# 🟢 9. plt.subplots(2, 2) → 2 rows and 2 columns (4 subplots)
# 🟢 10. plt.subplots(3, 1) → 3 rows and 1 column (3 subplots stacked vertically)