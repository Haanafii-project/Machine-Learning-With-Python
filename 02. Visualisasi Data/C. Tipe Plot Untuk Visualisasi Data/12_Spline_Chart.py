import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Spline Chart (Matplotlib)')

plt.show()