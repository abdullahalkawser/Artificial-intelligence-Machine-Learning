# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset লোড করা
penguins = sns.load_dataset('penguins')

# Regression Plot species অনুযায়ী
sns.lmplot(
    x='flipper_length_mm',   # independent variable
    y='body_mass_g',         # dependent variable
    hue='species',           # species অনুযায়ী রঙ আলাদা হবে
    data=penguins,           # dataset
    markers=['o', 's', 'D'], # species অনুযায়ী marker আলাদা
    height=6,                # plot height
    aspect=1.2,              # plot width/height অনুপাত
    scatter_kws={'s':50, 'alpha':0.7}, # scatter point customization
    line_kws={'linewidth':2}           # regression line customization
)

# শিরোনাম ও লেবেল
plt.title('Penguins Dataset - Flipper Length vs Body Mass by Species', fontsize=16)
plt.xlabel('Flipper Length (mm)', fontsize=12)
plt.ylabel('Body Mass (g)', fontsize=12)

# গ্রাফ দেখানো
plt.show()



# hue='species' দিলে তিনটি species অনুযায়ী রঙিন regression line এবং scatter points দেখায়।

# markers parameter দিয়ে species অনুযায়ী আলাদা মার্কার ব্যবহার করা যায়।

# scatter_kws দিয়ে পয়েন্টের আকার ও transparency নিয়ন্ত্রণ করা যায়।

# line_kws দিয়ে regression line-এর thickness পরিবর্তন করা যায়।

# নোট:

# lmplot হলো categorical hue + regression visualization-এর জন্য ideal।

# এটি একই graph-এ multiple species বা group-এর trend বোঝার জন্য খুব উপযোগী।
