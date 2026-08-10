# 1. describe() কী?

# Pandas-এর describe() হলো এমন একটি function, যেটা DataFrame-এর গুরুত্বপূর্ণ statistical summary একসাথে বের করে দেয়।

# সহজ ভাষায়:

# অনেকগুলো data দেখে manually হিসাব না করে, describe() আমাদের data-এর একটা quick report দেয়।

# এটা Data Analysis / EDA করার সময় খুব বেশি ব্যবহার হয়।

import pandas as pd

data = {
    "Name": ["Kawser", "Rahim", "Sakib", "Nabil",
             "Hasan", "Rafi", "Tanvir", "Fahim"],

    "Age": [21, 22, 21, 23, 22, 21, 24, 22],

    "CGPA": [3.75, 3.20, 3.90, 3.50, 3.60, 3.10, 3.85, 3.40],

    "Credits": [120, 110, 130, 115, 125, 105, 128, 118]
}

df = pd.DataFrame(data)

print(df)

print("\nStatistical Summary of the DataFrame:\n")

# print(df.describe())
print(df.columns)

print(f"Data Types of the DataFrame:\n{df.dtypes}\n")
print(f"shape of the DataFrame:\n{df.shape}\n")