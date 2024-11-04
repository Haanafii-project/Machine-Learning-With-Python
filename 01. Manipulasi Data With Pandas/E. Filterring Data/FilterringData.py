import pandas as pd

data = {'Kategori': ['A', 'B', 'C'],
        'Nilai': [10, 15, 20]}

# Membuat DataFrame dari Dictionary
df = pd.DataFrame(data)

# Mengambil kolom tertentu
selected_columns = df[['Kategori', 'Nilai']]

# Menfilter data berdasarkan kondisi
filtered_data = df[df['Nilai'] > 16]

# Mengubah nilai
df['Nilai'] = df['Nilai'] * 2

print(selected_columns)
print(filtered_data)
print(df)