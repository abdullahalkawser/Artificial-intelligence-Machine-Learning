# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset লোড করা
penguins = sns.load_dataset('penguins')

# Line Plot তৈরি করা
plt.figure(figsize=(10,6))

# আমরা species অনুযায়ী flipper_length_mm এর mean body_mass_g দেখব
sns.lineplot(
    x='flipper_length_mm',   # x-axis: flipper length
    y='body_mass_g',         # y-axis: body mass
    hue='species',           # species অনুযায়ী ভিন্ন লাইন
     style= 'island',
    data=penguins,           
    marker='o',              # marker ব্যবহার
    linewidth=2              # লাইন thickness
)

# শিরোনাম ও লেবেল
plt.title('Penguins Dataset - Line Plot of Body Mass vs Flipper Length', fontsize=16)
plt.xlabel('Flipper Length (mm)', fontsize=12)
plt.ylabel('Body Mass (g)', fontsize=12)
plt.legend(title='Species')

# গ্রাফ দেখানো
plt.show()



# কমেন্টস (বাংলা):
# lineplot সাধারণত sequential/numerical data দেখানোর জন্য ব্যবহৃত হয়।

# hue='species' দিলে বিভিন্ন species অনুযায়ী ভিন্ন লাইন তৈরি হয়।

# marker দিয়ে লাইন পয়েন্টগুলো হাইলাইট করা যায়।

# linewidth দিয়ে লাইন-এর ঘনত্ব নিয়ন্ত্রণ করা যায়।

# নোট:
# Line Plot দিয়ে trend, growth, change over a variable সহজে দেখা যায়।

# Large dataset-এ aggregation (mean, median) দিয়ে Line Plot তৈরি করলে trend পরিষ্কার হয়।

# style, dashes, markers parameter দিয়ে লাইন কাস্টমাইজ করা যায়।