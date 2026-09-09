import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 30, 25]
y2 = [5, 15, 25, 20, 35]

# figure() creates a new graph window.
# figure() নতুন আলাদা graph window বা canvas তৈরি করে।
plt.figure()

# plot(x, y, style) draws data as a line graph.
# plot(x, y, style) x এবং y-এর data দিয়ে line graph আঁকে।
# b^-- = blue triangle markers with a dashed line.
# r*-- = red star markers with a dashed line.

plt.plot(x, y1, "b^--", label="Student 1")
plt.plot(x, y2, "r*--", label="Student 2")

# title() adds a title above the graph.
# title() graph-এর উপরে একটি title বা শিরোনাম বসায়।
plt.title("Student Marks")

# xlabel() names the horizontal (x) axis.
# xlabel() horizontal বা x-axis-এর নাম বসায়।
plt.xlabel("Exam")

# ylabel() names the vertical (y) axis.
# ylabel() vertical বা y-axis-এর নাম বসায়।
plt.ylabel("Marks")

# legend() displays the labels given to each plot.
# legend() প্রতিটি line-এর নাম বা পরিচয় দেখায়।
plt.legend('upper left')

# grid() adds guide lines, making values easier to read.
# grid() graph-এ guide line যোগ করে, ফলে value পড়া সহজ হয়।
plt.grid( color='gray', linestyle='--', linewidth=0.5)

# Create a second independent figure.
# দ্বিতীয় একটি আলাদা figure তৈরি করা হচ্ছে।
plt.figure()

# Here, ro- means red circle markers with a solid line.
# এখানে ro- মানে red circle marker এবং solid line।
plt.plot(x, y2, "ro-", label="Student 2")
plt.title("Student 2")
plt.xlabel("Exam")
plt.ylabel("Marks")




plt.xticks([1, 2, 3, 4, 5], ["Exam 1", "Exam 2", "Exam 3", "Exam 4", "Exam 5"])
plt.yticks([5, 10, 15, 20, 25, 30, 35], ["5", "10", "15", "20", "25", "30", "35"])
plt.legend()
plt.legend(["x", "y"], loc="upper left")

# show() opens all created figures on the screen.
# show() তৈরি করা সব graph screen-এ দেখায়।

plt.show()