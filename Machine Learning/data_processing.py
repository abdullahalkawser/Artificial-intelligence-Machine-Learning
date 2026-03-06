import pandas as pd

daata = pd.read_csv("data.csv")




df = pd.DataFrame(daata)

print(df.isnull().sum())

# print(df.dropna())
# print(df)



# print("Original Dataframe")
# # print(df)
# print(df.isnull().sum())

# df_drop = df.dropna() 
# # //1️⃣ df.dropna() এর মানে

# # dropna() মানে হলো যেসব row-তে empty / missing value (NaN) আছে সেগুলো delete করে দেওয়া।

# # df = তোমার DataFrame

# # dropna() = NaN থাকা row বাদ দেওয়া

# print(df_drop)

# # print(df.isnull().mean() * 100)  //প্রতিটি column-এ কত % missing value (NaN) আছে তা বের করে।


# # df['Age'] = df['Age'].fillna(df['Age'].mean())
# # df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# print(df)

# # df['Age'] = df['Age'].fillna(df['Age'].mean())

# # এর মানে:

# # df['Age'] → DataFrame এর Age column

# # mean() → Age column এর average (গড়) বের করা

# # fillna() → যেখানে NaN আছে সেখানে সেই average বসানো

# # df['Age'] = → নতুন value আবার Age column এ বসানো

# # Age column এ যেসব জায়গায় Age নেই (NaN), সেখানে Age এর average বসানো হচ্ছে।

# # 2️⃣ df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# # এখানে একই কাজ হচ্ছে কিন্তু Salary column এ।

# # 📌 মানে:

# # Salary না থাকলে Salary এর average দিয়ে পূরণ করা হচ্ছে।

# # 3️⃣ print(df)
# # print(df)

# # এটা final DataFrame output দেখাবে।