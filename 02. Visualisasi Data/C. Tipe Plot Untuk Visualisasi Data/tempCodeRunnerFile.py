import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('tips')
data_pivot = data.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(data_pivot, cmap='Y1Gnbu')

plt.show()