import numpy as np
import matplotlib.pyplot as plt

# 1. Inisialisasi Data (X: Biaya Iklan, Y: Penjualan)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([15, 25, 35, 40, 50, 65, 75, 80, 95, 105])

# 2. Perhitungan Metode Numerik (Least Squares) manual
n = len(X)
sum_x = np.sum(X)
sum_y = np.sum(Y)
sum_xx = np.sum(X**2)
sum_xy = np.sum(X*Y)

# Hitung m (slope) dan c (intercept) sesuai rumus numerik
m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
c = (sum_y - m * sum_x) / n

# 3. Prediksi dan Error
Y_pred = m * X + c
error = np.mean((Y - Y_pred)**2)

# Output Hasil
print(f"Model Regresi: y = {m:.4f}x + {c:.4f}")
print(f"Mean Squared Error: {error:.4f}")

# 4. Visualisasi
plt.scatter(X, Y, color='blue', label='Data Aktual')
plt.plot(X, Y_pred, color='red', label='Regresi Linear')
plt.title(f'Regresi Linear: y = {m:.2f}x + {c:.2f}')
plt.xlabel('Biaya Iklan'); plt.ylabel('Penjualan')
plt.legend(); plt.grid(True); plt.show()