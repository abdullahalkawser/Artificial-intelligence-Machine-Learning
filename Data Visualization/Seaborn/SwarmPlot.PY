# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# উদাহরণ ডেটাসেট লোড করা
tips = sns.load_dataset('tips')

# Swarm Plot তৈরি করা
plt.figure(figsize=(10,6))  # গ্রাফের আকার

sns.swarmplot(
    x='day',        # x-axis: সপ্তাহের দিন
    y='total_bill', # y-axis: বিলের মান
    data=tips,      # ডেটাসেট
    hue='sex',      # লিঙ্গ অনুযায়ী রঙ আলাদা হবে
    dodge=True,     # লিঙ্গ অনুযায়ী আলাদা কলামে দেখাবে
    size=80       # মার্কারের আকার
)

# শিরোনাম ও লেবেল
plt.title('Tips Dataset - Swarm Plot', fontsize=16)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Total Bill', fontsize=12)
plt.legend(title='Sex')  # লেজেন্ড যোগ করা

# গ্রাফ দেখানো
plt.show()


# নোট:

# Swarm Plot Strip Plot-এর উন্নত রূপ, যেখানে data distribution পরিষ্কারভাবে দেখা যায়।

# বড় dataset-এ Swarm Plot ধীরগতিতে render হতে পারে। সেই ক্ষেত্রে violinplot + swarmplot overlay ব্যবহার করা হয়।

# এটা মূলত categorical vs numerical data visualization-এর জন্য খুবই উপযোগী।
