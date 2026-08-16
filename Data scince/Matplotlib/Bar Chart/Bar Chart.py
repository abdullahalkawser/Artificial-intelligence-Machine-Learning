import matplotlib.pyplot as plt

subjects = ["Python", "Pandas", "NumPy", "ML"]
hours = [10, 8, 6, 4]
colors = ["red", "blue", "green", "orange"]

plt.bar(subjects, hours, color=colors)
# plt.barh(subjects, hours, color=colors) # horizontal bar chart

plt.xticks(rotation=45) #atribute use kore x-axis er value gulo ke rotate kora jay
plt.yticks(rotation=45) #atribute use kore y-axis er value gulo ke rotate kora jay

plt.title("Learning Hours")
plt.xlabel("Subjects")
plt.ylabel("Hours")

plt.show()

# যখন category compare করতে হবে। tkhn bar chat use korte hbe 

# Bar Chart খুব বেশি ব্যবহার করবে:

# 📊 Category comparison
# 📊 Feature importance
# 📊 Class distribution
# 📊 Sales comparison
# 📊 Student performance
# 📊 Product comparison
# 📊 Frequency/count