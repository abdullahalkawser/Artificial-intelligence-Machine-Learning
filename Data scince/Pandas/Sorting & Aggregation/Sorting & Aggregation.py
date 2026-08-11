# 1️⃣ Sorting কী?

# Sorting = Data-কে নির্দিষ্ট order-এ সাজানো।

# যেমন:

# Age ছোট → বড়
# Salary বড় → ছোট
# CGPA high → low
# Date পুরোনো → নতুন

# Pandas-এ মূলত দুইটি method বেশি ব্যবহার হয়:

# sort_values()
# sort_index()



import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nabil", "Hasan"],
    "Age": [22, 20, 25, 21, 23],
    "CGPA": [3.50, 3.80, 3.20, 3.90, 3.60],
    "Salary": [30000, 45000, 25000, 50000, 40000]
}

df = pd.DataFrame(data)

print("Original DataFramewithout sorting:")

print(df)

print("\nDataFrame sorted by Age (ascending):")


# 🔹 Ascending Sorting ছোট থেকে বড়
# মনে রাখবে:
# ascending=True

# Default হচ্ছে True.

# df_sorted_age = df.sort_values("Age")
# print(df_sorted_age)




# 3️⃣ Descending Sorting

# বড় থেকে ছোট:


# ascending=False

# after sorting, original DataFrame-এ কোন পরিবর্তন হবে না। যদি original DataFrame-এ পরিবর্তন করতে চাও, তাহলে inplace=True দিতে হবে।
Age = df.sort_values("Age", ascending=False)
print(Age)


# 4️⃣ Multiple Column Sorting

# একাধিক column দিয়েও sort করা যায়।


df_sorted_multiple = df.sort_values(["Age","Salary"],ascending=[True,False]) 
print("\nDataFrame sorted by Age (ascending) and Salary (descending):")
print(df_sorted_multiple)


# এর অর্থ:

# আগে Age → ছোট থেকে বড়
# একই Age হলে CGPA → বড় থেকে ছোট

# এটা real-world dataset-এ অনেক useful।



