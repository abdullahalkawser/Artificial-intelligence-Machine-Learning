# 🔹 What is a DataFrame?

# English:
# A DataFrame is a 2-dimensional labeled data structure in Pandas. It looks like a table (rows and columns), similar to an Excel spreadsheet or SQL table.

# Bangla:
# একটি DataFrame হলো দুই-মাত্রিক (2D) ডেটা স্ট্রাকচার যেখানে row এবং column থাকে। এটিকে এক্সেল শিট বা SQL টেবিলের মতো ভাবা যায়।


# Summary Notes (Bangla + English)

# DataFrame = 2D labeled data structure (rows + columns)
# DataFrame হলো দুই-মাত্রিক টেবিল ডেটা।

# Create from:

# Dictionary

# List of dictionaries

# Numpy array

# CSV / Excel file

# Access data:

# Columns → df['col']

# Rows → df.loc[] (label), df.iloc[] (index)

# Modify:

# Add new column → df['new'] = ...

# Drop column/row → df.drop()

# Summary & Stats:

# df.head(), df.tail(), df.info(), df.describe()

# Missing Data Handling:

# isnull(), fillna(), dropna()


import pandas as pd
# একটি সিম্পল ডেটা তৈরি করি
data = {
    'name':['abdullah','sabiirlli','sabiir'],
    'age':[22,34,45],
    'city':['Dhaka','Chittagong','Khulna'],
    'salary':[1000,2000,3000],
    'is_married':[True,False,True],
    'height':[5.5,6.0,5.8],
    'weight':[70,80,75],
    'birth_date':['2001-01-01','1990-05-15','1985-10-20'],
    'is_active':[True,False,True],
}
# DataFrame তৈরি
df =pd.DataFrame(data)

# পুরো DataFrame দেখাও
print("Complete DataFrame:")
print(df)


# ✅ From List of Dictionaries
data = [
    {'Name': 'Anu', 'Age': 20, 'CGPA': 3.5},
    {'Name': 'Rahman', 'Age': 22, 'CGPA': 3.8},
    {'Name': 'Abdullah', 'Age': 21, 'CGPA': 3.9}
]

df = pd.DataFrame(data)
print(df)

# ✅ Custom Index
# df = pd.DataFrame(data, index=['a', 'b', 'c'])
# print(df)


