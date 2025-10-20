# # 🔹 What is Filtering Data?

# English:
# Filtering means selecting only those rows from a DataFrame that match a condition.

# বাংলায়:
# Filtering মানে হলো DataFrame থেকে নির্দিষ্ট শর্ত অনুযায়ী কিছু row বেছে নেওয়া।

import pandas as pd

# -----------------------------
# Sample DataFrame বানানো
# -----------------------------
data = {
    "Name": ["Anu", "Rahim", "Karim", "Sonia", "Rafi"],
    "Age": [20, 25, 19, 30, 22],
    "Score": [85, 70, 90, 60, 75]
}

df = pd.DataFrame(data)  # dictionary থেকে DataFrame বানানো হলো
print("Original DataFrame:\n", df, "\n")

# Filter: Age greater than 21

# শর্ত: Age > 21
result = df[df["Age"] > 21]
print("Age > 21:\n", result, "\n")
# Filter: Score less than or equal to 75
# শর্ত: Score <= 75
result = df[df["Score"] <= 75]
print("Score <= 75:\n", result, "\n")
# Filter: Name is 'Karim'

#3️⃣ Multiple Conditions (AND → &)
# শর্ত: Age > 20 AND Score > 70
result = df[(df["Age"] > 20) & (df["Score"] > 70)]
print("Age > 20 AND Score > 70:\n", result, "\n")
# Filter: Age less than 25 OR Score greater than 80

## শর্ত: Age > 20 AND Score > 70
result = df[(df["Age"] > 20) & (df["Score"] > 70)]
print("Age > 20 AND Score > 70:\n", result, "\n")

# 4️⃣ Multiple Conditions (OR → |)
# শর্ত: Age < 25 OR Score > 80
result = df[(df["Age"] < 25) | (df["Score"] > 80)]
print("Age < 25 OR Score > 80:\n", result, "\n")

# 5️⃣ Using isin() Method
# শর্ত: Name in ['Anu', 'Sonia']
result = df[df["Name"].isin(["Anu", "Sonia"])]
print("Name in ['Anu', 'Sonia']:\n", result, "\n")

# 5️⃣ Filter by String Value

# শর্ত: Name == "Anu"
result = df[df["Name"] == "Anu"]
print("Name == 'Anu':\n", result, "\n")
# শর্ত: Name != "Anu"
result = df[df["Name"] != "Anu"]    

# Important Notes (খুব জরুরি বিষয়)

# df[condition] → এইভাবে ফিল্টার করতে হয়।

# Multiple conditions → বন্ধনীর মধ্যে রাখতে হবে।

# Logical operators:

# & → AND

# | → OR

# তুলনা করার জন্য:

# == → সমান

# > → বেশি

# < → কম

# >= → সমান বা বেশি

# <= → সমান বা কম
