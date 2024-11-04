import seaborn as sns
import matplotlib.pyplot as plt

data = [44, 45, 40, 41, 39]
keys = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5']

palette_color = sns.color_palette('bright')
plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')

plt.show()