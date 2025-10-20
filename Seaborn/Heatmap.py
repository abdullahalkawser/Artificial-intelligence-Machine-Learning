# 🐧 Seaborn দিয়ে Heatmap তৈরি করা
# ==================================

# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn এর বিল্ট-ইন penguins dataset লোড
penguins = sns.load_dataset("penguins")

# ডেটাসেটের প্রথম কয়েকটা সারি দেখা
print(penguins.head())

# শুধুমাত্র সংখ্যাসূচক (numeric) কলামগুলো নিতে হবে correlation এর জন্য
numeric_data = penguins.select_dtypes(include=['float64', 'int64'])

# কলামগুলোর মধ্যে correlation বের করা
corr = numeric_data.corr()

# 🎨 Heatmap আঁকা
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)

# টাইটেল যোগ করা
plt.title("🐧 Penguin Dataset Correlation Heatmap", fontsize=14)

# চার্ট দেখানো
plt.show()


#buji nai akhno amke abar dekhte hbe 




















# কোড ব্যাখ্যা (বাংলায়):

# sns.load_dataset("penguins") → Seaborn এর বিল্ট-ইন penguins ডেটা লোড করে।

# select_dtypes() → শুধুমাত্র সংখ্যাসূচক ডেটা বেছে নেয় (যাতে correlation করা যায়)।

# corr() → Numeric কলামগুলোর মধ্যে সম্পর্ক (correlation coefficient) বের করে।

# sns.heatmap() → correlation ম্যাট্রিক্সকে রঙে প্রকাশ করে, যেখানে:

# annot=True → প্রতিটি বক্সে correlation মান দেখায়।

# cmap="coolwarm" → রঙের থিম নির্ধারণ করে।

# linewidths=0.5 → বক্সগুলোর মধ্যে লাইন যোগ করে সুন্দরভাবে আলাদা করে।

# 🧩 নোটস (Notes):

# Heatmap মূলত দেখায় কোন কোন ফিচার একে অপরের সাথে সম্পর্কিত।

# Correlation মান:

# +1 → একদম সরাসরি সম্পর্ক (positive correlation)

# -1 → উল্টো সম্পর্ক (negative correlation)

# 0 → কোনো সম্পর্ক নেই

# Machine Learning বা Data Analysis এ এটা Feature Selection এর জন্য খুব গুরুত্বপূর্ণ।
