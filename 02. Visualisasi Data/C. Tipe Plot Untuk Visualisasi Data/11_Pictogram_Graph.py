import seaborn as sns
import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [4, 3, 5, 2]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=['red', 'green', 'blue', 'yellow'])
plt.title('Pictogram Graph (Matplotlib)')

plt.show()