import pandas as pd

# Membaca Data dari file CSV
df = pd.read_csv('DataSetHanafi.csv')

# Mengurutkan data berdasarkan Populasi dan Area, secara ascending (paling kecil ke terbesar)
df_sorted = df.sort_values(by=['Populasi', 'Area'], ascending=True)

print(df)
print(df_sorted)