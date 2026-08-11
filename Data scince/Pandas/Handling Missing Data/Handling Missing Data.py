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
