import seaborn as sns
import matplotlib.pyplot as plt

data  = sns.load_dataset('flights')
data_pivot = data.pivot_table(index='month', columns='year', values='passenger')

sns.set_theme(style='darkgrid')
sns.lineplot(data=data_pivot)

plt.show()