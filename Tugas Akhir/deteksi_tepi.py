import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- LANGKAH 1: BACA GAMBAR ---
# Pastikan ada file bernama 'foto.jpg' di folder yang sama dengan file kode ini!
nama_file = 'foto.jpg' 
img = cv2.imread(nama_file, 0) # Angka 0 artinya baca sebagai Grayscale (Hitam Putih)

# --- CEK APAKAH GAMBAR DITEMUKAN ---
if img is None:
    print(f"ERROR FATAL: File '{nama_file}' tidak ditemukan!")
    print("Solusi: Pastikan file gambar ada di folder yang sama dan namanya benar.")
else:
    print("Gambar ditemukan, memproses metode numerik...")

    # --- LANGKAH 2: METODE NUMERIK (SOBEL) ---
    # Hitung Gradien arah X (Vertikal) dan Y (Horizontal)
    # ksize=3 artinya kita pakai matriks kernel ukuran 3x3
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    # --- LANGKAH 3: HITUNG MAGNITUDE (KEKUATAN TEPI) ---
    # Rumus Pythagoras: akar(x^2 + y^2)
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
    
    # Konversi ke format gambar (integer 8-bit) agar bisa tampil
    gradient_magnitude = np.uint8(np.absolute(gradient_magnitude))

    # --- LANGKAH 4: TAMPILKAN HASIL ---
    plt.figure(figsize=(12, 6))

    # Plot Gambar Asli
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Gambar Asli (Grayscale)')
    plt.axis('off')

    # Plot Hasil Deteksi Tepi
    plt.subplot(1, 2, 2)
    plt.imshow(gradient_magnitude, cmap='gray')
    plt.title('Hasil Deteksi Tepi (Metode Sobel)')
    plt.axis('off')

    print("Berhasil! Menampilkan grafik...")
    plt.show()