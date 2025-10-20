# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset লোড করা
penguins = sns.load_dataset('penguins')

# Count Plot তৈরি করা
plt.figure(figsize=(8,5))

sns.countplot(
    data=penguins,
    x='species',       # X-axis: species (categorical)
    hue='sex',         # পুরুষ ও নারীর সংখ্যা আলাদা রঙে দেখাবে
    palette='Set2',    # সুন্দর রঙের সেট
    dodge=True         # hue অনুযায়ী বারগুলো আলাদা করবে
)

# শিরোনাম ও লেবেল
plt.title('Count of Penguins by Species and Sex', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Sex')

# গ্রাফ দেখানো
plt.show()




# countplot categorical data-এর frequency (সংখ্যা) দেখায়।

# hue দিলে একটি দ্বিতীয় categorical variable অনুযায়ী ভাগ করে দেখানো যায় (যেমন male/female)।

# palette দিয়ে রঙের স্কিম পরিবর্তন করা যায়।

# dodge=True দিলে hue অনুযায়ী বারগুলো আলাদা আলাদা পাশে দেখায়।

# ✅ নোট:

# Count Plot হলো Bar Plot-এর একটি বিশেষ রূপ, যেখানে Seaborn নিজে count হিসাব করে।

# এটি dataset-এর class imbalance, distribution, বা category proportion বুঝতে খুব সহায়ক।

# চাইলে orient='h' দিয়ে horizontal count plot-ও বানানো যায়।
