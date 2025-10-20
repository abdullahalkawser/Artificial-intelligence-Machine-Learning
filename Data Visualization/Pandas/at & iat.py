# 📘 Pandas: at & iat (Single Value Access)
# 1. at (Label-based single value access)

# English: Used to get/set a single value in DataFrame using row label + column label.

# বাংলা: Row-এর নাম (label) আর Column-এর নাম দিয়ে একটা cell-এর data access করতে ব্যবহার হয়।

# ✅ Example:

import pandas as pd

data = {
    "Name": ["Anis", "Rahim", "Karim"],
    "Age": [23, 25, 21],
    "CGPA": [3.5, 3.8, 3.2]
}

df = pd.DataFrame(data, index=["s1", "s2", "s3"])

# # Single value access
# print(df.at["s2", "CGPA"])   # Row label = s2, Column label = CGPA

# # Update single value
# df.at["s3", "Age"] = 22
# print(df)

# 2. iat (Integer-location based single value access)

# English: Used to get/set a single value in DataFrame using row index + column index (numbers).

# বাংলা: Row-এর position number আর Column-এর position number দিয়ে একটা cell-এর data access করা হয়।

# Single value access
print(df.iat[2, 2])   # Row index = 1, Column index = 2

# # Update single value
df.iat[1, 1] = 24
print(df)


# Notes

# at → Label দিয়ে single value access

# Faster than loc when working with only one value.

# Example: df.at["s2", "CGPA"]

# iat → Index number দিয়ে single value access

# Faster than iloc for only one value.

# Example: df.iat[1, 2]

# Key Difference:

# at["s2", "CGPA"] → row label + column label দিয়ে access।

# iat[1, 2] → row index + column index দিয়ে access।