# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  

# penguins dataset লোড করা
penguins = sns.load_dataset('penguins')

# Bar Plot তৈরি করা
plt.figure(figsize=(8,5))

sns.barplot(
    data=penguins,
    x='species',        # X-axis: Species (categorical)
    y='body_mass_g',    # Y-axis: Mean of body mass (numerical)
    hue= 'sex',          # hue দিয়ে লিঙ্গ অনুযায়ী আলাদা বার দেখাবে
    palette='pastel', # রঙের প্যালেট
    ci='sd',            # error bar = standard deviation
    capsize=0.2 ,       # error bar-এর মাথা ছোট করে দেয়
    estimator=np.var
)

# শিরোনাম ও লেবেল
plt.title('Average Body Mass by Species (Penguins)', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Average Body Mass (g)', fontsize=12)

plt.show()






# barplot স্বয়ংক্রিয়ভাবে mean value হিসাব করে দেখায়।

# ci='sd' দিলে standard deviation error bar দেখায়।

# capsize দিয়ে error bar-এর মাথা ছোট বা বড় করা যায়।

# ✅ নোট:

# Bar Plot সাধারণত categorical → numerical summary দেখাতে ব্যবহার হয়।

# Error bar data-এর variation বা uncertainty বোঝায়।

# চাইলে estimator=np.median দিয়ে mean-এর বদলে median ও দেখানো যায়।