# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset লোড করা
penguins = sns.load_dataset('penguins')

# KDE Plot তৈরি করা
plt.figure(figsize=(8,6))

sns.kdeplot(
    data=penguins,
    x='body_mass_g',     # কোন numerical column-এর distribution দেখাবে
    hue='species',       # species অনুযায়ী আলাদা curve
    fill=True,           # curve এর নিচে রঙ ভরবে
    common_norm=False,   # প্রত্যেক species আলাদাভাবে normalize হবে
    alpha=0.5,           # transparency
    linewidth=2          # curve এর রেখার পুরুত্ব
)

# শিরোনাম ও লেবেল
plt.title('Penguins Dataset - Body Mass Distribution by Species (KDE Plot)', fontsize=16)
plt.xlabel('Body Mass (g)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(title='Species')

# গ্রাফ দেখানো
plt.show()




# ✅ বাংলা কমেন্টস:
# kdeplot data distribution-কে smooth curve আকারে দেখায় (histogram-এর মতো, কিন্তু continuous)।

# hue ব্যবহার করলে ভিন্ন গ্রুপ অনুযায়ী আলাদা রঙে curve দেখায়।

# fill=True দিলে curve এর নিচে রঙ ভরে।

# common_norm=False দিলে প্রতিটি group আলাদা করে normalize হয়।

# alpha transparency নিয়ন্ত্রণ করে।

# ✅ নোট:
# KDE Plot হলো histogram-এর smooth সংস্করণ।

# এটি data-এর shape, peak, skewness, spread সহজে বোঝায়।

# বড় dataset-এ KDE plot noise কমিয়ে clear trend দেখাতে সাহায্য করে।

# একাধিক group তুলনা করতে এটি অত্যন্ত উপযোগী (যেমন বিভিন্ন species-এর body mass distribution)।