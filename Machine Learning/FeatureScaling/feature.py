import pandas as pd
# sklearn থেকে StandardScaler import করা হয়েছে (data scale করার জন্য)
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split


# একটি dictionary তৈরি করা হয়েছে যেখানে study_hours এবং scores আছে
data = {
    "study_hours": [2, 3, 4, 5, 6],
    "scores": [50, 60, 70, 80, 90]
}

# dictionary থেকে pandas DataFrame তৈরি করা হয়েছে
df = pd.DataFrame(data)

# StandardScaler object তৈরি করা হয়েছে
# এটি data কে standard scale করবে (mean = 0, std = 1)
standred_scaler = StandardScaler()

# fit_transform() দিয়ে দুইটা কাজ হয়
# 1. data এর mean ও standard deviation শিখে নেয় (fit)
# 2. data কে scale করে (transform)
scaled_data = standred_scaler.fit_transform(df)

# # একটি message print করা হচ্ছে
# print("Standard Scaled Data:")

# # scaled numpy array print করা হচ্ছে
# print(scaled_data, "\n")






# # scaled numpy array কে আবার DataFrame এ convert করা হয়েছে
# df_scaled = pd.DataFrame(scaled_data, columns=["study_hours", "scores"])

# # final scaled dataframe print করা হচ্ছে
# print(df_scaled)





# 3. Min-Max Scaling
# -----------------------------

# # MinMaxScaler object তৈরি
# minmax_scaler = MinMaxScaler()

# # Data কে 0 থেকে 1 এর মধ্যে scale করা
# minmax_scaled_data = minmax_scaler.fit_transform(df)

# print("Min-Max Scaled Data (0-1 range):\n")

# # Scaled array কে আবার DataFrame বানানো
# df_minmax_scaled = pd.DataFrame(minmax_scaled_data, columns=["study_hours", "scores"])

# print(df_minmax_scaled)




# -----------------------------
# 2. Features (X) এবং Target (y) আলাদা করা
# -----------------------------
# এখানে study_hours হলো input (feature) এবং scores হলো output (target)
X = df[["study_hours"]]
y = df["scores"]

# -----------------------------
# 3. Data কে train এবং test এ ভাগ করা
# -----------------------------
# test_size=0.2 মানে 20% test, 80% train
# random_state=42 মানে split reproducible হবে
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Features (X_train):\n", X_train, "\n")
print("Testing Features (X_test):\n", X_test, "\n")
print("Training Target (y_train):\n", y_train, "\n")
print("Testing Target (y_test):\n", y_test, "\n")

