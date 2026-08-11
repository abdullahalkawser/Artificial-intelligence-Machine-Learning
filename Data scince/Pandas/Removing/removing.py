import pandas as pd

data = {
    "Name": ["Kawser", "Rahim", "Sakib", "Nabil"],
    "Department": ["CSE", "CSE", "EEE", "CSE"],
    "CGPA": [3.75, 3.20, 3.90, 3.50],
    "Age": [22, 23, 22, 24]
}

df = pd.DataFrame(data)

print("Before:")
print(df)

# Remove Age column

df.drop("CGPA",inplace=True,axis=1)

print("After removing Age column:")
print(df)

# Remove multiple columns

df.drop(["Department","Name"],inplace=True,axis=1)
print("After removing multiple columns:")
print(df)



# drop() → Remove rows or columns
# axis=0 → Work with rows
# axis=1 → Work with columns
# drop_duplicates() → Remove duplicate rows
# dropna() → Remove rows containing missing values
# inplace=True → Modify the original DataFrame
# df[condition] → Filter data based on a condition
# 🔥 সবচেয়ে গুরুত্বপূর্ণ ৫টা মনে রাখো
# df.drop("Age", axis=1)

# df.drop(2, axis=0)

# df.drop(["Age", "City"], axis=1)

# df.drop_duplicates()

# df.dropna()

# Short formula:
# axis=0 → Row
# axis=1 → Column
# drop() → Remove
# drop_duplicates() → Duplicate Remove
# dropna() → Missing Data Removeew