# 🧮 Koleksi Tugas Metode Numerik

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Array-013243?style=for-the-badge&logo=numpy)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv)

Repository ini berisi implementasi program untuk memenuhi **Tugas Besar Mata Kuliah Metode Numerik**. Terdiri dari dua topik utama: **Regresi Linear** dan **Turunan Numerik**.

**👨‍🎓 Identitas Mahasiswa**
* **Nama:** [Nama Lengkap Kamu]
* **NIM:** [NIM Kamu]
* **Kelas:** [Kelas Kamu]

---

## 📂 Daftar Proyek

### 1. Prediksi Penjualan (Regresi Linear)
Menerapkan metode **Least Squares (Kuadrat Terkecil)** untuk memprediksi total penjualan berdasarkan data historis biaya iklan.

* **Metode:** Regresi Linear Sederhana ($y = mx + c$)
* **File:** `regresi_linear.py`
* **Algoritma Utama:**
    ```python
    # Menghitung Slope (m) dan Intercept (c) secara manual
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
    c = (sum_y - m * sum_x) / n
    ```

**📸 Hasil Visualisasi:**
> *Garis merah menunjukkan tren prediksi yang membelah data aktual (titik biru).*

<img width="1618" height="910" alt="Screenshot 2025-12-26 234242" src="https://github.com/user-attachments/assets/e5f3a578-c220-4bd3-b333-9b2a534f5bf9" />

---

### 2. Deteksi Tepi Citra (Turunan Numerik)
Menerapkan **Turunan Numerik (Numerical Differentiation)** menggunakan **Operator Sobel** untuk mendeteksi tepi (*edge detection*) pada citra digital.

* **Metode:** Diferensiasi Numerik (Finite Difference)
* **File:** `deteksi_tepi.py`
* **Input:** `foto.jpg`
* **Algoritma Utama:**
    ```python
    # Menghitung Gradien (Turunan) arah X dan Y
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    # Menghitung Magnitude (Kekuatan Tepi)
    gradient = np.sqrt(sobelx**2 + sobely**2)
    ```

**📸 Hasil Demonstrasi:**
> *Gambar kiri adalah input asli, gambar kanan adalah hasil kalkulasi turunan numerik (tepi).*

<img width="1633" height="919" alt="Screenshot 2025-12-27 003253" src="https://github.com/user-attachments/assets/3d13cab5-b73e-4580-b57c-32e08a81c014" />
---

## 🚀 Cara Menjalankan Program

Pastikan Python sudah terinstall, lalu install library yang dibutuhkan:

```bash
pip install numpy matplotlib opencv-python
```
Menjalankan Regresi:
```bash
python regresi_linear.py
```
Menjalankan Deteksi Tepi: Pastikan ada file foto.jpg di folder yang sama, lalu run:
```bash
python deteksi_tepi.py
```
Copyright © 2025 - Muhammad Ilham
