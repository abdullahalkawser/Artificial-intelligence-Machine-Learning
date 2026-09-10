import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Available datasets
sns.get_dataset_names()

# Load dataset
penguins = sns.load_dataset('penguins')

# First 5 rows
penguins.head()

# Species count
penguins['species'].value_counts()

# Scatter plot
sns.scatterplot(
    data=penguins,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species',
    style='species'
)

sns.set_context("talk") # seaborn chart-এর context নির্ধারণ করা যায়। যেমন: paper, notebook, talk, poster
sns.set_context("poster", font_scale=1.5,) # seaborn chart-এর context নির্ধারণ করা যায়। যেমন: paper, notebook, talk, poster
sns.set_style("whitegrid") # seaborn chart-এর background style নির্ধারণ করা যায়। যেমন: darkgrid, whitegrid, dark, white, ticks
sns.color_palette("pastel") # seaborn chart-এর color palette নির্ধারণ করা যায়। যেমন: deep, muted, bright, pastel, dark, colorblind

plt.title("Penguins: Bill Length vs Bill Depth")
sns.despine() #দিয়ে chart-এর চারপাশের top/right/bottom/left spines (border lines) remove করা যায়।
plt.show()