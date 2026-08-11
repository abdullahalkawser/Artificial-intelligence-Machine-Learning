import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nabil", "Hasan"],
    "Age": [20, None, 22, 21, None],
    "CGPA": [3.50, 3.80, None, 3.20, 3.70],
    "City": ["Dhaka", "Chittagong", None, "Dhaka", "Khulna"]
}

df = pd.DataFrame(data)

print(df.isnull())  # Display the   DataFrame with True for missing values and False for non-missing values

# print(df.isna().sum()  )  # Check for missing values in issing Data খুঁজে বের করা — isna() the DataFrame

# টি প্রতিটি cell check করবে।

# Missing হলে → True
# Value থাকলে → False


#spacfic column missing value check
print(df['Age'].isna().sum())  # Check for missing values in the 'Age' column

