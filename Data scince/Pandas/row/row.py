import pandas as pd

data = {
    "Student_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115,
        116, 117, 118, 119, 120
    ],

    "Name": [
        "Kawser", "Rahim", "Sakib", "Nabil", "Hasan",
        "Fahim", "Tanvir", "Rafi", "Siam", "Adnan",
        "Shakil", "Imran", "Rakib", "Mehedi", "Arif",
        "Jahid", "Nayeem", "Sabbir", "Arafat", "Munna"
    ],

    "Department": [
        "CSE", "CSE", "EEE", "CSE", "BBA",
        "CSE", "EEE", "CSE", "BBA", "CSE",
        "EEE", "CSE", "CSE", "BBA", "EEE",
        "CSE", "BBA", "CSE", "EEE", "CSE"
    ],

    "CGPA": [
        3.75, 3.20, 3.90, 3.50, 3.45,
        3.80, 3.10, 3.65, 3.30, 3.95,
        3.25, 3.70, 3.55, 3.40, 3.85,
        3.60, 3.15, 3.78, 3.35, 3.88
    ]
}

df = pd.DataFrame(data)

# print(df)


# print(df.loc[2])  #accessing a row by index


print ("first  5 rows of the DataFrame:")
print ("..................................................:")
print(df.head())  #accessing first 5 rows
print ("last  5 rows of the DataFrame:")
print(df.tail())  #accessing last 5 rows


# কাজ	Code
# প্রথম Row	df.iloc[0]
# দ্বিতীয় Row	df.iloc[1]
# প্রথম 5 Row	df.head()
# শেষ 5 Row	df.tail()
# নির্দিষ্ট Row	df.loc[2]
# একাধিক Row	df.iloc[[0,2]]
# Row filter	df[df["Age"] > 20]
# Row delete	df.drop(index=2)
# Row update	df.loc[2,"Age"] = 25
# নতুন Row	df.loc[len(df)] = data
