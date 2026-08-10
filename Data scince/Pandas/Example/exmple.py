import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nusrat", "Jannat", "Hasan", "Arif", "Mim"],
    "Age": [21, 24, 19, 22, 25, 20, 23, 18],
    "Department": ["BBA", "CSE", "BBA", "EEE", "CSE", "BBA", "EEE", "CSE"],
    "City": ["Dhaka", "Chittagong", "Dhaka", "Sylhet", "Dhaka", "Rajshahi", "Dhaka", "Khulna"],
    "CGPA": [3.50, 3.80, 3.20, 3.90, 3.60, 3.10, 3.75, 3.40],
    "Salary": [25000, 35000, 22000, 40000, 32000, 20000, 38000, 28000]
}

df = pd.DataFrame(data)

# selecting a single column
n = df["Department"]
print(n)

#selecting multiple columns
c = df[["Name", "Age", "CGPA"]]


print(c)



# single condition row selection
s= df[df["Age"] > 22]
print("Rows where Age is greater than 22:")
print(s)


# multiple condition row selection
m= df[(df["Age"] > 22) & (df["CGPA"] > 3.5)]

h = df[(df["Age"] > 22) | (df["CGPA"] > 3.5)]
print("Rows where Age is greater than 22 or CGPA is greater than 3.5:")
print(h)