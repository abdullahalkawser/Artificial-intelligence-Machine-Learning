# import matplotlib.pyplot as plt

# hours = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

# marks = [35, 40, 45, 50, 55, 65, 70, 75, 85, 90]

# plt.scatter(hours, marks,s=100, label='Data Points', c='red', alpha=0.5, edgecolors='white', linewidth=1.5, marker='p')

# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.title("Study Hours vs Marks")
# plt.legend()
# plt.grid()
# plt.show()

# # plt.show()অবশ্যই 😄 তুমি সম্ভবত Scatter Plot (plt.scatter()) বলতে চাচ্ছো। এটা Matplotlib-এর খুব important plot—বিশেষ করে Data Science / ML / EDA-তে।

# # 🔵 Scatter Plot — একদম সহজভাবে
# # Scatter Plot কী?

# # Scatter Plot = দুইটা numerical variable-এর মধ্যে relationship দেখানো।

# # সহজ ভাষায়:

# # X-এর value পরিবর্তন হলে Y-এর value কীভাবে পরিবর্তন হচ্ছে—সেটা dots দিয়ে দেখায়।

# # যেমন:

# # একজন student কত ঘণ্টা পড়েছে → কত marks পেয়েছে
# # মানুষের Height → Weight
# # Product Price → Sales
# # Advertising Cost → Revenue


import matplotlib.pyplot as plt

# Class A
x1 = [1, 2, 3, 4, 5]
y1 = [35, 40, 45, 50, 55]

# Class B
x2 = [1, 2, 3, 4, 5]
y2 = [45, 50, 60, 65, 75]

plt.scatter(x1, y1, label="Class A", s=100)
plt.scatter(x2, y2, label="Class B", s=100)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Class A vs Class B")
plt.legend()
plt.grid(True)

plt.show()