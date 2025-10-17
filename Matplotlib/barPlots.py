import matplotlib.pyplot as plt



# ) Basic Bar Plot (Matplotlib ব্যবহার করে)

import matplotlib.pyplot as plt

# ডেটা
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 9]

# বার চার্ট
plt.bar(categories, values)

plt.title('Basic Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()


# ) Horizontal Bar Plot (Matplotlib ব্যবহার করে)
import matplotlib.pyplot as plt
# ডেটা
categories = ['A', 'B', 'C', 'D', 'E']      
values = [10, 15, 7, 12, 9]
# Horizontal বার চার্ট
plt.barh(categories, values, color='skyblue')
plt.title('Horizontal Bar Plot')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()

# বার প্লটে মান (value) দেখানো

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 9]

plt.bar(categories, values, color='lightgreen')

# প্রতিটি বারের উপরে মান লেখা
for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.title('Bar Plot with Values')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()


# Grouped Bar Plot (একাধিক ডেটা compare)

import numpy as np
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
set1 = [10, 20, 15, 25]
set2 = [12, 18, 17, 22]

x = np.arange(len(categories))   # [0,1,2,3]
width = 0.4                      # প্রতিটি বারের প্রস্ত

plt.bar(x - width/2, set1, width, label='Set 1')
plt.bar(x + width/2, set2, width, label='Set 2')

plt.xticks(x, categories)
plt.title('Grouped Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()
