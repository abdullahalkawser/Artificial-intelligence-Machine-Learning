import pandas as pd 


data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Salary": [70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)