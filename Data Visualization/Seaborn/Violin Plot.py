# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset লোড করা
penguins = sns.load_dataset('penguins')

# Violin Plot তৈরি করা
plt.figure(figsize=(8,6))

sns.violinplot(
    data=penguins,
    x='species',          # X-axis: categorical variable
    y='body_mass_g',      # Y-axis: numerical variable
    hue='sex',            # লিঙ্গ অনুযায়ী ভিন্ন রঙ
    split=True,           # পুরুষ ও নারীকে একই violin-এ দুই পাশে ভাগ করে দেখায়
    palette='Set2',       # সুন্দর রঙের সেট
    inner='quartile',     # median + quartile line দেখাবে
    linewidth=1.5
)

# শিরোনাম ও লেবেল
plt.title('Penguins Dataset - Body Mass Distribution by Species and Sex (Violin Plot)', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Body Mass (g)', fontsize=12)
plt.legend(title='Sex')

# গ্রাফ দেখানো
plt.show()





# বাংলা কমেন্টস:

# violinplot একসাথে data distribution (density) এবং summary statistics দেখায়।

# split=True দিলে একই violin-এর দুই পাশে দুটি hue group দেখায় (যেমন male vs female)।

# inner='quartile' দিলে median এবং quartile লাইন যোগ হয়।

# palette রঙ পরিবর্তনের জন্য ব্যবহৃত হয়।

# linewidth বর্ডার স্পষ্ট করে।

# ✅ নোট:

# Violin Plot হলো Box Plot-এর উন্নত রূপ, যেখানে data-এর shape দেখা যায়।

# এটি distribution comparison-এর জন্য খুবই শক্তিশালী visualization tool।

# বড় dataset-এ pattern, symmetry বা outliers বোঝা অনেক সহজ হয়।

# চাইলে sns.violinplot-এর উপর sns.swarmplot বা sns.stripplot overlay করে data points-ও দেখানো যায়।