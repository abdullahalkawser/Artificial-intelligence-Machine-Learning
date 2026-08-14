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

print("Number of Students:", df["Name"].count())

print("Standard Deviation of Cgpa:", df["CGPA"].std())

# এটা statistical analysis-এ অনেক গুরুত্বপূর্ণ।

# Simple idea:

# Low std → values কাছাকাছি

# High std → values বেশি spread out

# ML/Data Science-এ std() খুব useful।

print("Variance of Cgpa:", df["CGPA"].var()) #variance বের করে 

# 12. একসাথে Multiple Aggregation

# একই column-এর উপর অনেকগুলো aggregation একসাথে করা যায়।


result = df["Age"].agg(["min", "max", "mean"])
print(df[["Age", "CGPA"]].agg(["mean", "min", "max"]))

print(result)

# 15. Different Column-এ Different Aggregation

# এটা খুব important concept।

result = df.agg({
    "Age": ["mean", "max"],
    "CGPA": ["mean", "min", "max"]
})


print(result)


# groupby() + Aggregation 🔥

# এটাই Pandas aggregation-এর সবচেয়ে important অংশগুলোর একটি।


datas = {
    "Name": ["Rahim", "Karim", "Sakib", "Nabil", "Hasan", "Rafi"],
    "Department": ["CSE", "CSE", "EEE", "EEE", "CSE", "CSE"],
    "CGPA": [3.50, 3.80, 3.20, 3.60, 3.90, 3.70]
}

dfs = pd.DataFrame(datas)

result = dfs.groupby("Department")["CGPA"].mean()

print(result)


# 17. groupby() + Multiple Aggregation


result = df.groupby("Department")["CGPA"].agg(
    ["mean", "min", "max"]
)

print(result)



# 18. GroupBy + Different Columns

# আরও powerful example:

# result = df.groupby("Department").agg({
#     "CGPA": ["mean", "max"],
#     "Name": "count"
# })


# print(result)
