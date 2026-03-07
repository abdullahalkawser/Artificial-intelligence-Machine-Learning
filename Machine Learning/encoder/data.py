import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ১. ডাটা লোড করা
df = pd.read_csv("new.csv")
df_label = df.copy()
le = LabelEncoder()

# ২. প্রত্যেকটি কলাম আলাদাভাবে এনকোড করা (নিশ্চিত করুন এই লাইনগুলো আছে)
df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])

df_label['Passed_Encoded'] = le.fit_transform(df_label['Passed'])

# ৩. কলামগুলো প্রিন্ট করা
# এখানে নিশ্চিত করুন যে নামগুলো হুবহু উপরের তৈরি করা নামের সাথে মিলছে
cols_to_show = ['Name', 'Gender', 'City', 'Passed', 'Gender_Encoded','Passed_Encoded']
# print(df_label[cols_to_show].head())






# Pandas ব্যবহার করে City column এর One Hot Encoding করা হচ্ছে
df_encoded = pd.get_dummies(df, columns=['City'],dtype=int)

# # নতুন লাইনে একটি message print করা হচ্ছে
# print('\n One Hot Encoded DataFrame (City): \n')

# True/False কে 1/0 এ convert করা হচ্ছে (Binary format)
# df_encoded = df_encoded.astype(int)

# Message print করা
print('\n Binary Encoded DataFrame (City):\n')

# Final DataFrame দেখানো
print(df_encoded)

print('\n Binary Encoded DataFrame (City): \n')

# Encoding করার পর যে নতুন DataFrame তৈরি হয়েছে তা print করা হচ্ছে
print(df_encoded)



