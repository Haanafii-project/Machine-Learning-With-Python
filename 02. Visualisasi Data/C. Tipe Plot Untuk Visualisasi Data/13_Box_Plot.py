import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.rand(100)

# Box Plot dengan Matplotlib
# plt.figure(figsize=(8, 6))
# plt.boxplot(data, vert=False)
# plt.title('Box Plot (Matplotlib)')

# Box Plot dengan Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(data, orient='v')
plt.title('Box Plot (Seaborn)')


plt.show()