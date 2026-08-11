import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nabil", "Hasan"],
    "Age": [20, None, 22, 21, None],
    "CGPA": [3.50, 3.80, None, 3.20, 3.70],
    "City": ["Dhaka", "Chittagong", None, "Dhaka", "Khulna"]
}

df = pd.DataFrame(data)

# print(df.isnull())  # Display the   DataFrame with True for missing values and False for non-missing values

# print(df.isna().sum()  )  # Check for missing values in issing Data খুঁজে বের করা — isna() the DataFrame

# টি প্রতিটি cell check করবে।

# Missing হলে → True
# Value থাকলে → False



#spacfic column missing value check
# print(df['Age'].isna().sum())  # Check for missing values in the 'Age' column

# 3️⃣ Missing Data বাদ দেওয়া — dropna()

# যদি missing data থাকা পুরো row বাদ দিতে চাও:

# axis=0 → row Missing থাকা row remove
# axis=1 → column Missing থাকা column remove
 
# new_df = df.dropna(axis= 0,inplace= True)  # Drop rows with any missing values inparams=True will modify the original DataFrame in place and return None, so new_df will be None.
# print('  after dropping rows with missing values:', new_df)  # Display the DataFrame after dropping rows with missing values

# print(new_df)  # Display the DataFrame after dropping rows with missing values

# print(df)  # Display the original DataFrame after dropping rows with missing values




# 5️⃣ Missing Data Replace করা — fillna()

# অনেক সময় data delete করতে চাই না। তখন missing value-এর জায়গায় নতুন value বসাই।


print("Before filling missing values:")

print(df)  


# print("\nAfter filling missing values:")

# df ['Age'] = df["Age"].fillna(23000000)  # Fill missing values in the 'Age' column with the mean of the column

# print(df)  # Display the DataFrame after filling missing values

# Missing Age-এর জায়গায় 21 বসেছে।

# কখন ব্যবহার করবে?

# যখন তুমি জানো missing value-এর জায়গায় একটি reasonable value দেওয়া যায়।



# Mean দিয়ে Missing Value Fill Avage mean

# Numerical data-এর ক্ষেত্রে খুব common technique।

mean_age = df["Age"].mean()  # Calculate the mean of the 'Age' column
df["Age"] = df["Age"].fillna(mean_age)
print("\nAfter filling missing values with mean:")

print(df)


# কখন Mean ব্যবহার করবে?

# যখন:

# Numerical data
# Data খুব বেশি skewed না
# Average

# Median দিয়ে Missing Value Fill
median_age = df["Age"].median()

df["Age"] = df["Age"].fillna(median_age)

print("\nAfter filling missing values with median:")
print(df)


# Mean vs Median

# ধরো salary:

# 20,000
# 22,000
# 25,000
# 30,000
# 5,00,000

# এখানে 5,00,000 অনেক বড় value।

# Mean অনেক বেশি হয়ে যাবে।

# তাই salary-এর মতো data-তে অনেক সময়:

# median()

# better choice।

# সহজে মনে রাখো:

# Mean → Normal/less skewed data

# Median → Outlier থাকলে ভালো


8️⃣ Mode দিয়ে Missing Value Fill

Categorical data-এর জন্য mode() বেশি useful।

ধরো:

City
Dhaka
Dhaka
NaN
Khulna
Dhaka

এখানে সবচেয়ে বেশি আসা value হলো:

Dhaka

তাই:

df["City"] = df["City"].fillna(df["City"].mode()[0])

Output:

City
Dhaka
Dhaka
Dhaka
Khulna
Dhaka
কেন mode()[0]?

mode() একটি Series return করে।

df["City"].mode()

তাই প্রথম mode value নিতে:

.mode()[0]
9️⃣ ffill() — Forward Fill

আগের value দিয়ে missing value পূরণ করে।

df["City"] = df["City"].ffill()

Example:

Dhaka
NaN
Khulna
NaN

হবে:

Dhaka
Dhaka
Khulna
Khulna
কখন ব্যবহার করবে?

যখন data sequence/order অনুযায়ী চলে।

যেমন:

Time-series data
Daily temperature
Stock data
Sensor data
🔟 bfill() — Backward Fill

পরের value দিয়ে missing value পূরণ করে।

df["City"] = df["City"].bfill()

Example:

Dhaka
NaN
Khulna
NaN

হবে:

Dhaka
Khulna
Khulna
NaN

শেষের NaN থাকবে কারণ তার পরে কোনো value নেই।

🧠 Real-Life Example — Student Dataset

ধরো university-তে student data:

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nabil"],
    "Age": [20, None, 22, None],
    "CGPA": [3.50, 3.80, None, 3.20],
    "Department": ["CSE", "CSE", None, "EEE"]
}

df = pd.DataFrame(data)

print(df)
Step 1 — Missing data check
print(df.isna().sum())
Step 2 — Age → Median
df["Age"] = df["Age"].fillna(df["Age"].median())
Step 3 — CGPA → Mean
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].mean())
Step 4 — Department → Mode
df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)

এখন dataset অনেক cleaner।

🔥 কোনটা কখন ব্যবহার করবে?
Method	কী করে	কখন ব্যবহার করবে
isna()	Missing খুঁজে	Missing check
isnull()	Missing খুঁজে	isna()-এর alternative
dropna()	Missing row/column delete	Missing খুব কম হলে
fillna()	Missing replace	Data রাখতে চাইলে
mean()	Average দিয়ে fill	Numerical data
median()	Middle value দিয়ে fill	Outlier থাকলে
mode()	Most frequent value	Categorical data
ffill()	আগের value নেয়	Time-series/sequence
bfill()	পরের value নেয়	Time-series/sequence
📌 Final Revision Notes
Missing Data কী?

Dataset-এর কোনো value না থাকলে তাকে Missing Data বলে।

Common forms:

NaN
None
NaT
🔎 Missing Check
df.isna()

মোট missing:

df.isna().sum()
🗑️ Missing Remove

Row remove:

df.dropna()

Column remove:

df.dropna(axis=1)
🔄 Missing Replace
df.fillna(value)

Specific column:

df["Age"] = df["Age"].fillna(21)
📊 Numerical Data

Mean:

df["Age"].fillna(df["Age"].mean())

Median:

df["Age"].fillna(df["Age"].median())

Outlier থাকলে → Median generally safer.

🏷️ Categorical Data

Mode:

df["City"].fillna(df["City"].mode()[0])
⏩ Sequence / Time-Series

Forward:

df.ffill()

Backward:

df.bfill()
⭐ এক লাইনের Cheat Sheet
Check       → isna()
Remove      → dropna()
Replace     → fillna()
Average     → mean()
Middle      → median()
Most common → mode()
Previous    → ffill()
Next        → bfill()

ML/Data Science-এ সবচেয়ে important idea: Missing value দেখেই সবসময় dropna() করবে না। আগে বুঝবে কেন missing, data type কী, missing কত শতাংশ, এবং সেই value replace করা logically valid কিনা।