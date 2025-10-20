# 🐍 Seaborn Rug Plot Example
# ============================

# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট করা
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn এর বিল্ট-ইন penguins ডেটাসেট লোড করা
penguins = sns.load_dataset("penguins")

# ডেটাসেটের প্রথম কয়েকটা সারি দেখা
print(penguins.head())

# 🎨 Rug Plot আঁকা
# এখানে 'bill_length_mm' কলামটি ব্যবহার করা হচ্ছে
sns.rugplot(data=penguins, x="bill_length_mm", height=0.1, color="darkblue")

# চার্টের টাইটেল যোগ করা
plt.title("🐧 Penguin Bill Length - Rug Plot", fontsize=14)

# চার্ট দেখানো
plt.show()


#🎯 Rug Plot কী কাজে লাগে?

# Rug Plot হলো একটি ডিস্ট্রিবিউশন visualization টুল।

# এটি data points কোথায় বেশি ঘনভাবে আছে তা বুঝতে সাহায্য করে।

# সাধারণত KDE Plot বা Histogram এর সাথে ব্যবহার করা হয়।


sns.kdeplot(data=penguins, x="bill_length_mm", fill=True, color="skyblue")
sns.rugplot(data=penguins, x="bill_length_mm", color="black")
plt.title("🐧 Penguin Bill Length: KDE + Rug Plot", fontsize=14)
plt.show()


# নোটস (Notes):

# Rug Plot একা সাধারণত কমন visualization না,
# বরং KDE বা Histogram এর supplementary layer হিসেবে ব্যবহার হয়।

# এটি ছোট কিন্তু খুব information-rich টুল, বিশেষ করে data density বোঝার জন্য।