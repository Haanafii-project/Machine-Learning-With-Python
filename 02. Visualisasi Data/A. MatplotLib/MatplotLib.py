import matplotlib.pyplot as plt

# Contoh data baru
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

# Membuat plot garis
plt.plot(x, y, label="Data")

# Menambahkan label dan judul
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Contoh Plot Matplotlib")

# Menampilkan plot legenda
plt.legend()

# Menampilkan plot
plt.show()
