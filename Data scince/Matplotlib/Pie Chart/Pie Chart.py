import matplotlib.pyplot as plt



# Student transport data
transport = ["Bus", "Rickshaw", "Metro", "Walking"]
students = [40, 25, 20, 15]

plt.pie(students, labels=transport, colors=['blue', 'green', 'yellow', 'red'],autopct='%1.1f%%', startangle=90, shadow=True, explode=(0.1, 0, 0, 0), wedgeprops={'edgecolor': 'green'})

plt.legend()
plt.title("Transportation Used by 100 Students  for Daily Commute")
plt.show()