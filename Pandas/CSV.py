# 🔹 What is CSV?

# English:
# CSV (Comma-Separated Values) is a plain text file where each row represents a record and values are separated by commas.

# Bangla:
# CSV হলো একটি সাধারণ টেক্সট ফাইল যেখানে প্রতিটি row একটি record এবং comma (,) দিয়ে আলাদা করা থাকে।


# pd.read_csv("file.csv") → CSV ফাইল পড়ার জন্য।

# Parameters:

# sep=";" → separator change

# names=[...] → custom column names

# index_col=0 → কোন কলামকে index বানাতে হবে

# skiprows=n → n সংখ্যক row skip

# nrows=n → নির্দিষ্ট সংখ্যক row পড়তে

# na_values=["NA"] → missing value handle

# encoding="utf-8" → encoding problem solve

# Functions after reading:

# df.head() → প্রথম 5 row

# df.tail() → শেষের 5 row

# df.info() → ডেটা টাইপ ও summary

# df.describe() → সংখ্যাগত কলামের statistics


import pandas as pd

df = pd.read_csv(r"C:\Users\abdul\Desktop\Ai\Machine-Learning-Data-Science\Pandas\data.csv")

# print(df)   # First 5 rows

# e =df.loc[0:10,["Name","Age","CGPA"]] # Select specific columns and rows

e = df.loc[0:10, 'Name' : 'CGPA']  # Select specific columns and rows using range
print(e)

# e =df.loc[[1,4,7],["Name","Age","CGPA"]] # Select specific rows by index  
# print(e) 



# Common Parameters
# ✅ Change Separator
# df = pd.read_csv("data.csv", sep=";")


# 👉 যদি ডেটা ; দিয়ে separate থাকে।

# ✅ Custom Column Names
# df = pd.read_csv("data.csv", names=['Name','Age','CGPA'], header=None)

# ✅ Index Column
# df = pd.read_csv("data.csv", index_col=0)


# 👉 প্রথম কলামকে index বানানো হবে।

# ✅ Handle Missing Values
# df = pd.read_csv("data.csv", na_values=["NA", "Missing"])

# ✅ Skip Rows
# df = pd.read_csv("data.csv", skiprows=2)


# 👉 প্রথম 2 লাইন বাদ যাবে।

# ✅ Read Only Some Rows
# df = pd.read_csv("data.csv", nrows=5)


# 👉 শুধু প্রথম 5 row পড়বে।

# ✅ Encoding Problem Fix
# df = pd.read_csv("data.csv", encoding="utf-8")

# 🔹 Example CSV File (data.csv)
# Name,Age,CGPA
# Anu,20,3.5
# Rahman,22,3.8
# Abdullah,21,3.9

# # 🔹 Example Code
# import pandas as pd

# df = pd.read_csv("data.csv")

# print(df.head())        # প্রথম 5 row
# print(df.columns)       # কলামের নাম
# print(df.info())        # summary
# print(df.describe())    # statistics
# print(df.columns())     


# df.sample() হলো Pandas DataFrame এর একটি ফাংশন যা randomly row(s) select করে।

# 🔹 Example with your Sample Data
# import pandas as pd

# # Read the sample CSV
# df = pd.read_csv("/mnt/data/sample_data.csv")

# # Randomly select one row
# random_row = df.sample()
# print(random_row)


# Output (example, random every time):

#       Name  Age  CGPA Dept
# 2  Abdullah   21   3.9  CSE

# 🔹 Select Multiple Random Rows
# df.sample(n=2)   # randomly 2 rows

# 🔹 Random Rows with Fraction
# df.sample(frac=0.4)  # 40% rows randomly

# 🔹 Reset Random Seed
# df.sample(n=2, random_state=42)  # deterministic random selection


# Bangla Summary:

# df.sample() → এক বা একাধিক row randomly select করে।

# n → number of rows

# frac → fraction of rows

# random_state → নির্দিষ্ট seed দিয়ে same rows বের করা



Access Data with loc & iloc
1. loc (Label-based access)

English: Access rows/columns using labels (names).

বাংলা: Row বা column নামের মাধ্যমে data access করতে ব্যবহার হয়।

✅ Example:

import pandas as pd

data = {
    "Name": ["Anis", "Rahim", "Karim"],
    "Age": [23, 25, 21],
    "CGPA": [3.5, 3.8, 3.2]
}

df = pd.DataFrame(data, index=["s1", "s2", "s3"])

# Single row by label
print(df.loc["s1"])

# Multiple rows by label
print(df.loc[["s1", "s3"]])

# Specific row & column
print(df.loc["s2", "CGPA"])

# Slice rows with labels
print(df.loc["s1":"s2"])  


Output:

Name     Anis
Age        23
CGPA      3.5
Name: s1, dtype: object

    Name  Age  CGPA
s1  Anis   23   3.5
s3  Karim  21   3.2

3.8

    Name  Age  CGPA
s1  Anis   23   3.5
s2  Rahim  25   3.8

2. iloc (Integer-location based access)

English: Access rows/columns using integer positions (index numbers).

বাংলা: Row বা column serial index number (0,1,2...) দিয়ে data access করা হয়।

✅ Example:

# Single row by index number
print(df.iloc[0])

# Multiple rows by index number
print(df.iloc[[0, 2]])

# Specific row & column by position
print(df.iloc[1, 2])

# Slice rows with index numbers
print(df.iloc[0:2])


Output:

Name     Anis
Age        23
CGPA      3.5
Name: s1, dtype: object

    Name  Age  CGPA
s1  Anis   23   3.5
s3  Karim  21   3.2

3.8

    Name  Age  CGPA
s1  Anis   23   3.5
s2  Rahim  25   3.8

📝 Notes

loc → label দিয়ে data access

Row/Column name ব্যবহার করতে হয়।

Example: df.loc["s2", "CGPA"]

iloc → index number দিয়ে data access

Row/Column-এর position (0,1,2…) ব্যবহার হয়।

Example: df.iloc[1, 2]

Key Difference:

loc["s1"] → Label "s1" দিয়ে access।

iloc[0] → প্রথম row (index=0) access।