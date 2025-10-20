# প্রয়োজনীয় লাইব্রেরি
import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset লোড
penguins = sns.load_dataset('penguins')

# যদি 'species' বা 'flipper_length_mm' বা 'body_mass_g' এ NaN থাকে, drop করা
penguins = penguins.dropna(subset=['species','flipper_length_mm','body_mass_g'])

# Joint Plot (scatter) তৈরি
sns.jointplot(
    data=penguins,
    x='flipper_length_mm',  # x-axis: flipper length
    y='body_mass_g',        # y-axis: body mass
    kind= 'kde',        # scatter plot
    hue='species',          # species অনুযায়ী রঙ আলাদা
    height=7                # plot size
    # marginal_kws=dict(bins=15)  # optional, fill=True বাদ দিলাম
)

# শিরোনাম
plt.suptitle('Penguins Dataset - Joint Plot of Flipper Length vs Body Mass', fontsize=16, y=1.02)

# গ্রাফ দেখানো
plt.show()
