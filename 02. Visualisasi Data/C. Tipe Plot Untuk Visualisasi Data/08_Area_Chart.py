import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

data = {'period': [1, 2, 3, 4, 5, 6, 7, 8],
        'team_B': [15, 17, 17, 19, 22, 19, 19, 14],
        'team_C': [21, 18, 20, 16, 16, 15, 19, 22]}

df = pd.DataFrame(data)
color_map = ['orange', 'pink']

plt.stackplot(df.period, df.team_B, df.team_C, labels=['Team B', 'Team C'], colors=color_map
)

plt.show()