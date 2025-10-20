import pandas as pd

data = {
    "Name": ["Anis", "Rahim", "Karim"],
    "Age": [23, 25, 21],
    "CGPA": [3.5, 3.8, 3.2]
}

df = pd.DataFrame(data) # Create DataFrame without custom index

# Single column
print(df["Name"])

# Multiple columns
print(df[["Name", "CGPA"]])








    # 2. Shorthand Access (Attribute style)

    # ✅ Example:

print(df.Age)


    # English: Columns can also be accessed like an attribute: df.Age.

    # বাংলা: Column নাম attribute-এর মত ব্যবহার করা যায় → df.Age।






# Column Access করার বিভিন্ন উপায় — (Normal, Shorthand, Dot Notation)। আমি বাংলা + English এ Example সহ দেখাচ্ছি।

# 📘 Accessing Columns in Pandas
# 1. Normal Access (Dictionary style)

# English: Use column name inside square brackets [].

# বাংলা: Column-এর নাম dictionary key এর মত করে ব্যবহার করতে হয়।


# 3. Dot Notation (Shortcut for Shorthand)

# English: Same as shorthand, often called "dot notation".

# বাংলা: Shorthand style-কে অনেকসময় Dot Notation বলা হয়, যেমন df.Name, df.Age।

# ✅ Example:

print(df.CGPA)


# Output:

# 0    3.5
# 1    3.8
# 2    3.2
# Name: CGPA, dtype: float64

# 📝 Notes

# Normal access (df["col"]) → Safe, always works.

# Shorthand (df.col) → Faster, but only works if column name is valid.

# Dot notation = shorthand access style.

# 👉 এখন তোমার কাছে তিনটা technique হলো:

# df["Name"] → Dictionary style (সবচেয়ে recommended ✅)

# df[["Name","Age"]] → একসাথে একাধিক column

# df.Name / df.Age → Shorthand / Dot notation
