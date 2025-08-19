import numpy as np

# CSV লোড করা (mixed types)
data = np.genfromtxt(
    "C:/Users/abdul/Desktop/Ai/Machine-Learning-Data-Science/NumPy/Cvs/sample_data.csv",
    delimiter=",",
    dtype=None,   # mixed type
    names=True,   # header row use করবে
    encoding="utf-8"
)

# Table style print
headers = data.dtype.names  # column names
print("{:<5} {:<10} {:<5} {:<7}".format(*headers))  # header print

for row in data:
    print("{:<5} {:<10} {:<5} {:<7}".format(row['id'], row['name'], row['age'], row['salary']))
