import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 30, 25]
y2 = [5, 15, 25, 20, 35]

# Figure 1
plt.figure()
plt.plot(x, y1, 'b^--')
plt.plot(x,y2, 'r*--')
plt.title("Student 1")
plt.xlabel("Exam")
plt.ylabel("Marks")

# Figure 2
plt.figure()
plt.plot(x, y2, 'ro-')
plt.title("Student 2")
plt.xlabel("Exam")
plt.ylabel("Marks")

plt.show()


# plt.figure() কী?

# plt.figure() দিয়ে Matplotlib-কে বলা হয়:

# "একটা নতুন আলাদা drawing area/canvas তৈরি করো।"

# যেমন খাতায় নতুন পৃষ্ঠা খুললে নতুন করে graph আঁকতে পারো।