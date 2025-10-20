# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# উদাহরণ ডেটাসেট লোড করা
tips = sns.load_dataset('tips')

# Histogram তৈরি করা
plt.figure(figsize=(10,6))  # গ্রাফের আকার

sns.histplot(
    data=tips,          # ডেটাসেট
    x='total_bill',     # কোন numerical column দেখানো হবে
    bins=15,            # কতগুলো bin হবে
    kde=True,           # Kernel Density Estimate curve দেখাবে
    color='skyblue',    # histogram-এর রঙ
    edgecolor='black',   # bin-এর সীমানার রঙ
    multiple='stack'    # যদি hue ব্যবহার করা হয় তাহলে stacked histogram দেখাবে
)

# শিরোনাম ও লেবেল
plt.title('Tips Dataset - Histogram of Total Bill', fontsize=16)
plt.xlabel('Total Bill', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# গ্রাফ দেখানো
plt.show()


# কমেন্টস (বাংলা):

# bins দিয়ে নির্ধারণ করা হয় কত ভাগে data ভাগ হবে।

# kde=True দিলে smooth density curve দেখায়।

# color দিয়ে histogram-এর রঙ পরিবর্তন করা যায়।

# edgecolor দিয়ে bin-এর সীমানা আলাদা করা যায়।

# নোট:

# Histogram হলো numerical data distribution দেখার সবচেয়ে সহজ উপায়।

# KDE curve ব্যবহার করলে data-এর probability distribution আরও পরিষ্কার বোঝা যায়।

# বড় dataset-এ histogram analysis করে data-এর skewness, outliers, central tendency সহজে বোঝা যায়।