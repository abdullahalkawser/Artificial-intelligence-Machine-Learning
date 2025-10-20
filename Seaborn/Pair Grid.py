# 🐍 Seaborn PairGrid Example
# ===========================

# প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট করা
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn এর penguins ডেটাসেট লোড করা
penguins = sns.load_dataset("penguins")

# 🧹 Missing values বাদ দেয়া (PairGrid এ error এড়াতে)
penguins = penguins.dropna()

# 🎨 PairGrid তৈরি করা
g = sns.PairGrid(
    data=penguins,
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    hue="species"
)

# নিচের অংশে scatterplot দেখানো
g.map_lower(sns.scatterplot)

# উপরের অংশে KDE (density) দেখানো
g.map_upper(sns.kdeplot, fill=True)

# ডায়াগোনালে histogram দেখানো
g.map_diag(sns.histplot, kde=True)

# লেজেন্ড যোগ করা
g.add_legend()

# টাইটেল যোগ করা
plt.suptitle("🐧 Penguins Dataset - PairGrid Visualization", fontsize=14, y=1.02)

# চার্ট দেখানো
plt.show()



# sns.PairGrid() → PairPlot-এর মতো, তবে তুমি চাইলে প্রতিটি অংশে (উপর, নিচ, ডায়াগোনাল) আলাদা প্লট দিতে পারো।

# map_lower() → নিচের অংশে কোন প্লট দেখাবে তা নির্ধারণ করে।

# map_upper() → উপরের অংশে কোন প্লট দেখাবে।

# map_diag() → ডায়াগোনাল (নিজের সাথে সম্পর্ক) অংশে কোন প্লট দেখাবে।

# add_legend() → প্রজাতি অনুযায়ী (species) লেজেন্ড যোগ করে।


# 🧩 নোটস (Notes):

# PairGrid হল PairPlot-এর বেসিক ফ্রেমওয়ার্ক।

# তুমি চাইলে বিভিন্ন visualization একসাথে combine করতে পারো (scatter, kde, hist, reg ইত্যাদি)।

# EDA (Exploratory Data Analysis) তে এটা খুব কাজে লাগে —
# কারণ এতে ডেটার সম্পর্ক, distribution, ও clustering একসাথে বোঝা যায়।