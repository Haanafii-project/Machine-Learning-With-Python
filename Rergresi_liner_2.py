import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data harga rumah
data = pd.read_csv('data_pendapatan.csv')

# Fitur-Fitur yang akan digunakan untuk prediksi
X = data[['Pengalaman Kerja (tahun)']]
y = data ['Pendapatan (ribu Rupiah)']

# Membagi data menjadi data pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membangun model linear regresi
model = LinearRegression()
model.fit(X_train, y_train)

# Membuat Prediksi
y_pred = model.predict(X_test)

# Evaluasi Model
mse = mean_squared_error (y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(X_test, X_train, y_test,y_train, y_pred)

#Visualisai Hasil Prediksi
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_test['Pengalaman Kerja (tahun)'], y=y_test, label = 'Data Asli')
sns.lineplot( x=X_test['Pengalaman Kerja (tahun)'], y=y_pred, color = 'red', label='prediksi')
plt.xlabel('Pengalaman Kerja (tahun)')
plt.ylabel('Pendapatan')
plt.title('Prediksi Pendapatan dengan Regresi Linear')
plt.legend()
plt.show()
