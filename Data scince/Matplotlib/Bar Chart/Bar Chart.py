import matplotlib.pyplot as plt

subjects = ["Python", "Pandas", "NumPy", "ML"]
hours = [10, 8, 6, 4]
colors = ["red", "blue", "green", "orange"]

plt.bar(subjects, hours, color=colors)

plt.title("Learning Hours")
plt.xlabel("Subjects")
plt.ylabel("Hours")

plt.show()