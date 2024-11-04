import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [4, 3, 5, 2]

# Radar Chart dengan Matplotlib
# plt.figure(figsize=(8,6))
# ax = plt.subplot(111, polar=True)
# ax.fill_between(np.deg2rad(np.arange(0, 360, 90)),
#                 values + [values[0]], alpha=0.2)
# ax.set_xticks(np.deg2rad(np.arange(0, 360, 90)))
# ax.set_xticklabels(categories)
# plt.title('Radar Chart (Matplotlib)')

# Radar Chart dengan Seaborn
plt.figure(figsize=(8,6))
sns.set(style='whitegrid')
ax = sns.lineplot(x=categories + [categories[0]],
                  y=values + [values[0]], sort=False)
ax.fill_between(x=categories, y1=values, alpha=0.2)
plt.title('Radar Chart (Seaborn)')


plt.show()