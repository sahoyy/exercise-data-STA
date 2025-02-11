  
import streamlit as st
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Diketahui
mean = 10  # Rata-rata diameter (cm)
std_dev = 0.5  # Standar deviasi (cm)
lower_limit = 9.5  # Batas bawah (cm)
upper_limit = 10.5  # Batas atas (cm)

# Menghitung Z-score
z_lower = (lower_limit - mean) / std_dev
z_upper = (upper_limit - mean) / std_dev

# Menghitung probabilitas bohlam cacat
p_lower = stats.norm.cdf(z_lower)  # P(X < 9.5)
p_upper = 1 - stats.norm.cdf(z_upper)  # P(X > 10.5)

defective_proportion = p_lower + p_upper

# Menampilkan perhitungan
print("Perhitungan Z-score:")
print(f"Z_lower = (9.5 - 10) / 0.5 = {z_lower:.2f}")
print(f"Z_upper = (10.5 - 10) / 0.5 = {z_upper:.2f}")

print("
Perhitungan Probabilitas:")
print(f"P(X < 9.5) = P(Z < {z_lower:.2f}) = {p_lower:.4f}")
print(f"P(X > 10.5) = P(Z > {z_upper:.2f}) = {p_upper:.4f}")
print(f"Total proporsi bohlam cacat = {p_lower:.4f} + {p_upper:.4f} = {defective_proportion:.4f} ({defective_proportion*100:.2f}%)")

# Membuat Tabel Distribusi Normal
z_values = [-1, 1]
p_values = [p_lower, p_upper]
data = {"Z-score": z_values, "Probabilitas": p_values}
df = pd.DataFrame(data)
print("
Tabel Distribusi Normal Standar:")
print(df)

# Visualisasi Distribusi Normal
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)
y = stats.norm.pdf(x, mean, std_dev)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Distribusi Normal")
plt.fill_between(x, y, where=(x < lower_limit), color='red', alpha=0.5, label="Bohlam Cacat (<9.5 cm)")
plt.fill_between(x, y, where=(x > upper_limit), color='red', alpha=0.5, label="Bohlam Cacat (>10.5 cm)")
plt.axvline(mean, color='blue', linestyle='dashed', label="Mean = 10 cm")
plt.axvline(lower_limit, color='black', linestyle='dashed', label="Batas Bawah = 9.5 cm")
plt.axvline(upper_limit, color='black', linestyle='dashed', label="Batas Atas = 10.5 cm")

plt.title("Distribusi Diameter Bohlam Lampu")
plt.xlabel("Diameter (cm)")
plt.ylabel("Probabilitas Kepadatan")
plt.legend()
plt.show()
