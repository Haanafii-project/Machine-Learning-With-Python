import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.random.randn(40)
y = np.random.randn(40)
z = np.random.randn(40)
colors = np.random.randn(40)

plt.scatter(x, y, s=z*1000, c=colors)
plt.show()