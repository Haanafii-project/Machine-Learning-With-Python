import seaborn as sns
import matplotlib.pyplot as plt

# Membuat Data sederhana.
data = [10, 13, 15, 17, 20, 22, 25, 27, 30, 32]

# Membuat Histogram menggunakan Seaborn.
sns.histplot(data, bins=5, kde=True)

# Membuat Judul Pada Grafik.
plt.title('Contoh Histogram Seaborn')

# Memberi Label pada Sumbu X dan Y.
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

# Menampilkan hasil Grafik.
plt.show()