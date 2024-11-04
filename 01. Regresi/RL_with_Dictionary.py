import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data harga rumah dalam bentuk dictionary
data = {'Luas Rumah': [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700],
        'Jumlah Kamar': [3, 3, 2, 4, 2, 3, 4, 3, 2, 3],
        'Harga': [245000, 312000, 279000, 388000, 199000, 219000, 405000, 324000, 319000, 255000]}

# Membuat DataFrame dari dictionary
df = pd.DataFrame(data)

# Fitur-fitur yang akan digunakan untuk prediksi
X = df[['Luas Rumah', 'Jumlah Kamar']]
y = df['Harga']

#Membagi data menjadi data pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Membuat model regresi Linear
model = LinearRegression() 
model.fit(X_train, y_train)

#Membuat prediksi
y_pred = model.predict(X_test)

#Evaluasi model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

print(X_test, X_train, y_test,y_train, y_pred)

#Visualisasi hasil prediksi
plt.figure(figsize=(10, 6))
plt.scatter(X_test['Luas Rumah'], y_test, label = 'Data Asli')
plt.plot(X_test['Luas Rumah'], y_pred, color='red', label='Prediksi')
plt.xlabel('Luas Rumah')
plt.ylabel('Harga Rumah')
plt.title('Prediksi Harga Rumah dengan Regresi Linear')
plt.legend()
plt.show()
