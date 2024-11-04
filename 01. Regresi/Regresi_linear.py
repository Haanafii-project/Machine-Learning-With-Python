import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data harga rumah
data = pd.read_csv('DATARUMAH2.csv')

# Fitur-Fitur yang akan digunakan untuk prediksi
X = data[['LB', 'KM']]
y = data ['HARGA']

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

#Visualisai Hasil Prediksi
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_test['LB'], y=y_test, label = 'Data Asli')
sns.lineplot( x=X_test['LB'], y=y_pred, color = 'red', label='prediksi')
plt.xlabel('Luas Rumah')
plt.ylabel('Harga Rumah')
plt.title('Prediksi Harga Rumah dengan Regresi Linear')
plt.legend()
plt.show()

# print(data)