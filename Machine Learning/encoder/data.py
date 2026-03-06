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
print(df_label[cols_to_show].head())