# লাইব্রেরি ইমপোর্ট
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset লোড
tips = sns.load_dataset("tips")

# Style & Context
sns.set_style("whitegrid")      # Background + grid
sns.set_context("talk")         # Large labels for presentation
sns.set_palette("Set2")         # Color palette

# Scatter Plot তৈরি করা
sns.scatterplot(x="total_bill", y="tip", data=tips,hue= 'day')
# Set context to 'paper' (small fonts)
sns.set_context('paper')

sns.despine(top=True, right=True, left=False, bottom=False, offset=5)# হলো Seaborn-এর একটি ফাংশন যা প্লটের চারপাশের উপর এবং ডান দিকের axes (spines) সরিয়ে দেয়। এতে প্লটটা আরও “clean” এবং minimal দেখায়।

# Plot title এবং label
plt.title("Total Bill vs Tip Scatter Plot")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()



# Seaborn-এর চারটি built-in context আছে:

# Context	Description
# 'paper'	Smallest, journal paper বা ছোট figure-এর জন্য।
# 'notebook'	Default, Jupyter Notebook-এর জন্য।
# 'talk'	Medium, presentation talk-এর জন্য।
# 'poster'	Largest, poster বা big screen presentation-এর জন্য।