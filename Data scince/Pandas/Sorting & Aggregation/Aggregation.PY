# Aggregation কী?

# Aggregation মানে হলো অনেকগুলো data-কে একটা summary result-এ convert করা।

# সহজভাবে:

# Many values → One summarized value

# Example:


# aggregation function-গুলো হলো:


# এখন যদি আমরা জানতে চাই:

# Average CGPA কত?
# Maximum CGPA কত?
# Minimum CGPA কত?
# Total কত?
# কয়জন student আছে?

# এগুলো বের করাকে Aggregation বলা যায়।

# 2. Common Aggregation Functions

# Pandas-এ সবচেয়ে বেশি ব্যবহৃত aggregation methods:

# Method	কাজ
# sum()	Total বের করে
# mean()	Average বের করে
# median()	Middle value
# min()	Minimum value
# max()	Maximum value
# count()	Non-null value count
# std()	Standard deviation
# var()	Variance
# nunique()	Unique value count




import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nabil", "Hasan"],
    "Age": [20, 22, 21, 23, 24],
    "CGPA": [3.50, 3.80, 3.20, 3.90, 3.70]
}

df = pd.DataFrame(data)



print(df)

print("Average Cgpa:", df["CGPA"].mean())
print("Maximum Cgpa:", df["CGPA"].max())
print("Minimum Cgpa:", df["CGPA"].min())

print("Total Cgpa:", df["CGPA"].sum())








