# 🐍 Seaborn Pair Plot Example
# ============================

# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn এর penguins ডেটাসেট লোড
penguins = sns.load_dataset("penguins")

# ডেটাসেট দেখা
print(penguins.head())

# 🎨 Pair Plot আঁকা
sns.pairplot(data=penguins, hue="species", corner=True,diag_kind="hist", palette="Set2")

# চার্ট টাইটেল
plt.suptitle("🐧 Penguins Dataset - Pair Plot", fontsize=14, y=1.02)

# চার্ট দেখানো
plt.show()


# 📘 কোড ব্যাখ্যা (বাংলায়):

# sns.pairplot() → ডেটাসেটের প্রতিটি numeric ফিচারকে অন্যগুলোর সঙ্গে তুলনা করে scatterplot আকারে দেখায়।

# hue="species" → এখানে বিভিন্ন প্রজাতি অনুযায়ী (Adelie, Gentoo, Chinstrap) রঙ আলাদা করা হয়েছে।

# corner=True → শুধুমাত্র নিচের দিকের প্লটগুলো দেখায় (অর্ধেক প্লট), যাতে চার্টটি ক্লিন ও সুন্দর হয়।

# plt.suptitle() → পুরো figure এর উপরে টাইটেল সেট করে।

# 🎯 Pair Plot কী কাজে লাগে?

# Pair Plot মূলত Feature Relationship Visualization এর জন্য ব্যবহৃত হয়।

# এটি বোঝায় কোন কোন ফিচার (যেমন bill_length, flipper_length, body_mass) একে অপরের সাথে কীভাবে সম্পর্কিত।

# একই সাথে Distribution (Diagonal এ) এবং Scatter Relation দুটোই দেখা যায়।

 #Extra Example (Pair Plot with selected columns):
sns.pairplot(
    data=penguins,
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    hue="species",
    palette="coolwarm"
)
plt.suptitle("🐧 Selected Features - Pair Plot", fontsize=14, y=1.02)
plt.show()
