import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
tips = sns.load_dataset("tips")

# Style & Palette
sns.set_style("whitegrid")
sns.set_palette("pastel")   # pastel color palette



custom_colors = ["#FF5733", "#33FF57", "#3357FF", "#F0FF33"]  # নিজের রঙের list
sns.set_palette(sns.color_palette(custom_colors))
# Scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips, s=100, alpha=0.7)
plt.title("Scatter Plot with Pastel Palette")
plt.show()











# Seaborn Built-in Palettes
# 1️⃣ Categorical / Qualitative Palettes

# "deep", "muted", "pastel", "bright", "dark", "colorblind"

# 2️⃣ Sequential Palettes (continuous data)

# "Blues", "BuGn", "BuPu", "Oranges", "Purples"

# 3️⃣ Diverging Palettes (positive-negative)

# "coolwarm", "RdBu", "BrBG", "PiYG", "Spectral"

# 4️⃣ Custom Palette

# sns.color_palette(["red","green","blue"]) → নিজের রঙ define করা use case parours  best use for  table akare dew  