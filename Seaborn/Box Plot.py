# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset লোড করা
penguins = sns.load_dataset('penguins')

# Box Plot তৈরি করা
plt.figure(figsize=(8,6))

sns.boxplot(
    data=penguins,
    x='species',          # X-axis: categorical variable
    y='body_mass_g',      # Y-axis: numerical variable
    hue='sex',            # লিঙ্গ অনুযায়ী আলাদা বক্স
    palette='Set3',       # সুন্দর রঙের স্কিম
    dodge=True,           # hue অনুযায়ী বক্স আলাদা করা
    linewidth=2           # বক্সের রেখার পুরুত্ব
)

# শিরোনাম ও লেবেল
plt.title('Penguins Dataset - Body Mass Distribution by Species and Sex', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Body Mass (g)', fontsize=12)
plt.legend(title='Sex')

# গ্রাফ দেখানো
plt.show()




# boxplot data-এর minimum, Q1, median, Q3, maximum এবং outliers দেখায়।

# hue দিয়ে দ্বিতীয় categorical variable অনুযায়ী বক্স আলাদা করা যায়।

# palette দিয়ে রঙের সেট পরিবর্তন করা যায়।

# dodge=True দিলে ভিন্ন hue অনুযায়ী বক্সগুলো আলাদা হয়ে যায়।

# linewidth বক্সের বর্ডার স্পষ্ট করে।

# ✅ নোট:

# Box Plot হলো data distribution-এর summary view, যা এক নজরে spread ও outliers দেখায়।

# এটি numerical data-এর variability, skewness, এবং outlier detection এ সাহায্য করে।

# চাইলে orient='h' দিয়ে horizontal box plot বানানো যায়।

# বড় dataset-এর ক্ষেত্রে এটি swarmplot/stripplot-এর সাথে overlay করে আরও স্পষ্টভাবে visual করা যায়।
