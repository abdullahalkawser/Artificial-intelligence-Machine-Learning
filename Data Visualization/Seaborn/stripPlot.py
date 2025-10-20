# প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করা
import seaborn as sns
import matplotlib.pyplot as plt

# উদাহরণ ডেটাসেট লোড করা (Seaborn এর 'tips' dataset)
tips = sns.load_dataset('tips')

# Strip Plot তৈরি করা
plt.figure(figsize=(10,6))  # গ্রাফের আকার নির্ধারণ
sns.set_context('talk')  # কনটেক্সট সেট করা

sns.stripplot(
    x='day',        # x-axis এ দিনগুলি দেখাবে
    y='total_bill', # y-axis এ বিলের মান দেখাবে
    data=tips,      # ডেটাসেট
    jitter=True,    # পয়েন্টগুলো একটু ছড়ানো হবে যাতে একে অপরের উপর না পড়ে
    hue='sex',      # লিঙ্গ অনুযায়ী রঙ আলাদা হবে
    dodge=True,     # লিঙ্গ অনুযায়ী আলাদা আলাদা রেখা দেখাবে
    marker='o',     # মার্কারের ধরন
    size=8          # মার্কারের আকার
)
sns.despine()  # গ্রাফ থেকে স্পাইন সরিয়ে ফেলা

# গ্রাফের শিরোনাম ও লেবেল
plt.title('Tips Dataset - Strip Plot', fontsize=16)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Total Bill', fontsize=12)
plt.legend(title='Sex')  # লেজেন্ড যোগ করা

# গ্রাফ দেখানো
plt.show()


# নোট:

# Strip Plot মূলত categorical vs numerical ডেটা ভিজুয়ালাইজেশনের জন্য ব্যবহৃত হয়।

# ছোট dataset-এ খুব ভালো দেখায়, কিন্তু বড় dataset-এ swarmplot বা violinplot ভালো হতে পারে।

# যেকোনো categorical data-তে pattern বা distribution দেখতে Strip Plot খুবই সহজ এবং দ্রুত।
