import pandas as pd

# Membaca Data dari file CSV
data = pd.read_csv('DataSetHanafi.csv')

# Informasi tentang struktur data
print(data.info())

# Statistik deskriptif data
print(data.describe())

# Menyimpan data ke file CSV baru
data.to_csv('NewDataSetHanafi.csv', index=False)