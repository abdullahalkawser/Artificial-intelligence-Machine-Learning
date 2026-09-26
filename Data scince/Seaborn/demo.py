import seaborn as sns
import matplotlib.pyplot as plt

sns.set_context('paper')
sns.set_palette('pastel')

sns.scatterplot(
    data=fmri,
    x='subject',
    y='region',
    hue='timepoint'
)

sns.despine(left=True, right=True, offset=10)

plt.show()
