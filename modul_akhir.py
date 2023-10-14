# Lab Analisis Data 1 MATH2301 Semester Ganjil 2020 

# Nama : Elicia Gloria Tirtajaya Budiawan 
# NIM : 232202718
# Prodi : CFP 

import numpy as np 
from tabulate import tabulate

Latihan_Soal = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20LS.csv", delimiter=",", dtype = "str") # untuk memuat file nilai akhir latihan soal dalam bentuk .csv ke dalam python
Kuis         = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Kuis.csv", delimiter=",", dtype = "str") # untuk memuat file nilai akhir kuis dalam bentuk .csv ke dalam python
Lab          = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Lab.csv", delimiter=",", dtype = "str") # untuk memuat file nilai akhir lab dalam bentuk .csv ke dalam python 
Proyek       = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Proyek.csv", delimiter=",", dtype = "str") # untuk memuat file nilai akhir proyek dalam bentuk .csv ke dalam python 
Jurnal       = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Jurnal.csv", delimiter=",", dtype = "str") # untuk memuat file nilai akhir jurnal dalam bentuk .csv ke dalam python 
Ujian        = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Ujian.csv", delimiter=",", dtype = "str") # untuk memuat file nilai akhri ujian dalam bentuk .csv ke dalam python 

nilai_latihan_soal = Latihan_Soal[1:,1:].astype(float) # untuk memperoleh nilai akhir latihan soal dan mengembalikannya ke bentuk (float) 
nilai_kuis         = Kuis[1:,1:].astype(float) # untuk memperoleh nilai akhir kuis dan mengembalikannya ke bentuk (float) 
nilai_lab          = Lab[1:,1:].astype(float) # untuk memperoleh nilai akhir lab dan mengembalikannya ke bentuk (float) 
nilai_proyek       = Proyek[1:,1:].astype(float) # untuk memperoleh nilai akhir proyek dan mengembalikannya ke bentuk (float) 
nilai_jurnal       = Jurnal[1:,1:].astype(float) # untuk memperoleh nilai akhir jurnal dan mengembalikannya ke bentuk (float) 
nilai_ujian        = Ujian[1:,1:].astype(float) # untuk memperoleh nilai kahir ujian dan mengembalikannya ke bentuk (float) 

bobot_latihan_soal = 1/100
bobot_kuis         = 2/100
bobot_lab          = 4/100
bobot_proyek       = 7.5/100
bobot_jurnal       = 3/100
bobot_ujian        = 25/100 

total_latihan_soal = np.sum(nilai_latihan_soal, axis=1) # total nilai latihan soal setiap mahasiswa
total_kuis         = np.sum(nilai_kuis,         axis=1) # total nilai kuis setiap mahasiswa
total_lab          = np.sum(nilai_lab,          axis=1) # total nilai lab setiap mahasiswa 
total_proyek       = np.sum(nilai_proyek,       axis=1) # total nilai proyek setiap mahasiswa
total_jurnal       = np.sum(nilai_jurnal,       axis=1) # total nilai jurnal setiap mahasiswa 
total_ujian        = np.sum(nilai_ujian,        axis=1) # total nilai ujian setiap mahasiswa 

total_bobot_latihan_soal = total_latihan_soal * bobot_latihan_soal # total nilai latihan soal 1 mahasiswa dikali bobot 
total_bobot_kuis         = total_kuis         * bobot_kuis         # total nilai kuis 1 mahasiswa dikali bobot
total_bobot_lab          = total_lab          * bobot_lab          # total nilai lab 1 mahasiswa dikali bobot
total_bobot_proyek       = total_proyek       * bobot_proyek       # total nilai proyek 1 mahasiswa dikali bobot
total_bobot_jurnal       = total_jurnal       * bobot_jurnal       # total nilai jurnal 1 mahasiswa dikali bobot
total_bobot_ujian        = total_ujian        * bobot_ujian        # total nilai ujian 1 mahasiswa dikali bobot


# Tugas 1 
print("Tugas 1")
print()

nilai_akhir_awal = total_bobot_latihan_soal + total_bobot_kuis + total_bobot_lab + total_bobot_proyek + total_bobot_jurnal + total_bobot_ujian
nilai_akhir      = nilai_akhir_awal[:,np.newaxis] # untuk menambahkan dimensi array 1 menjadi array column
print("Nilai Akhir masing-masing siswa :\n", nilai_akhir)
print()

skala_penilaian = [
    (nilai_akhir >= 91) & (nilai_akhir < 101), # A
    (nilai_akhir >= 86) & (nilai_akhir < 91),  # A-
    (nilai_akhir >= 81) & (nilai_akhir < 86),  # B+
    (nilai_akhir >= 76) & (nilai_akhir < 81),  # B
    (nilai_akhir >= 71) & (nilai_akhir < 76),  # B-
    (nilai_akhir >= 61) & (nilai_akhir < 71),  # C+
    (nilai_akhir >= 51) & (nilai_akhir < 61),  # C
    (nilai_akhir >= 46) & (nilai_akhir < 51),  # C-
    (nilai_akhir >= 41) & (nilai_akhir < 46),  # D
    (nilai_akhir >= 0)  & (nilai_akhir < 41),  # F
]

# indeks prestasi sesuai dengan rentang 
categories = ['A','A-','B+','B','B-','C+','C','C-','D','F']

indeks_prestasi = np.select(skala_penilaian, categories) # indeks prestasi dari nilai akhir 
print("Indeks Prestasi Mahasiswa :\n", indeks_prestasi)
print()

NIM = Latihan_Soal[1:,0:1].astype(str) # untuk mencetak NIM mahasiswa
print("NIM Mahasiswa :\n", NIM)
print()

math_2031_angkatan_20XX = np.block([NIM, nilai_akhir, indeks_prestasi]) # menggabungkan NIM, nilai akhir, dan indeks prestasi menjadi satu array 
header = ['NIM', 'nilai akhir', 'indeks prestasi']

table = tabulate (math_2031_angkatan_20XX, header, tablefmt="fancy_grid") # mengubah tampilan dari array menjadi tabel 
print("Tabel Informasi NIM, Nilai Akhir, dan Indeks Prestasi Mahasiswa :\n")
print(table)
print()

# Tugas 2
print("Tugas 2")
print()

# untuk mengetahui rata-rata nilai yang paling tinggi
print("Mean Nilai Latihan Soal =") 
print(np.mean(nilai_latihan_soal, axis=0))
print("Mean Nilai Kuis =")
print(np.mean(nilai_kuis, axis=0))
print("Mean Nilai Lab =")
print(np.mean(nilai_lab, axis=0))
print("Mean Nilai Proyek =")
print(np.mean(nilai_proyek, axis=0))
print("Mean Nilai Jurnal =")
print(np.mean(nilai_jurnal, axis=0))
print("Mean Nilai Ujian =")
print(np.mean(nilai_ujian, axis=0))
print()

# Menetapkan bobot baru 
# Nilai UTS dan UAS tidak boleh < 15%, namun nilai UTS dan UAS adalah yang terendah, sehingga:
# UTS = 15%
# UAS = 15% 
# Nilai dengan rata rata tertinggi adalah Jurnal, maka 
# Jurnal = 26% 

# Bobot baru agar rata-rata naik 
bobot_latihan_soal_baru = 1/100
bobot_kuis_baru         = 1/100
bobot_lab_baru          = 1/100
bobot_proyek_baru       = 1/100
bobot_jurnal_baru       = 26/100
bobot_ujian_baru        = 15/100

nilai_jurnal = Jurnal[1:,1:].astype(float) # untuk memperoleh nilai akhir jurnal baru dan mengembalikannya ke bentuk (float)

jurnal = np.sum(nilai_jurnal, axis=1) 

total_bobot_jurnal_baru = jurnal * bobot_jurnal_baru # nilai jurnal tiap mahasiswa dikali bobot baru 

total_bobot_latihan_soal_baru       = total_latihan_soal      * bobot_latihan_soal_baru # total nilai baru latihan soal per 1 mahasiswa dikali bobot 
total_bobot_kuis_baru               = total_kuis              * bobot_kuis_baru # total nilai baru kuis per 1 mahasiswa dikali bobot
total_bobot_lab_baru                = total_lab               * bobot_lab_baru # total nilai baru lab per 1 mahasiswa dikali bobot 
total_bobot_proyek_baru             = total_proyek            * bobot_proyek_baru # total nilai baru proyek per 1 mahasiswa dikali bobot 
total_bobot_jurnal_baru             = total_bobot_jurnal_baru * bobot_jurnal_baru # total nilai baru jurnal per 1 mahasiswa dikali bobot
total_bobot_ujian_baru              = total_ujian             * bobot_ujian_baru # total nilai baru ujian per 1 mahasiswa dikali bobot

nilai_akhir_awal_baru = (total_bobot_latihan_soal_baru + total_bobot_kuis_baru + total_bobot_lab_baru + total_bobot_proyek_baru + total_bobot_jurnal_baru + total_bobot_ujian_baru) 
nilai_akhir_baru      = nilai_akhir_awal_baru[:,np.newaxis] # untuk menambahkan dimensi array 1 menjadi array column
print("Nilai AKhir Baru :\n", nilai_akhir_baru)
print()

skala_nilai_baru = [
    (nilai_akhir_baru >= 91),                           # A 
    (nilai_akhir_baru >= 86) & (nilai_akhir_baru < 91), # A- 
    (nilai_akhir_baru >= 81) & (nilai_akhir_baru < 86), # B+
    (nilai_akhir_baru >= 76) & (nilai_akhir_baru < 81), # B
    (nilai_akhir_baru >= 71) & (nilai_akhir_baru < 76), # B-
    (nilai_akhir_baru >= 61) & (nilai_akhir_baru < 71), # C+
    (nilai_akhir_baru >= 51) & (nilai_akhir_baru < 61), # C
    (nilai_akhir_baru >= 46) & (nilai_akhir_baru < 51), # C-
    (nilai_akhir_baru >= 41) & (nilai_akhir_baru < 46), # D
    (nilai_akhir_baru >= 0)  & (nilai_akhir_baru < 41), # F
]

indeks_prestasi_baru = np.select(skala_nilai_baru, categories) # indeks prestasi dari nilai akhir 
print("Indeks Prestasi Mahasiswa Baru :\n", indeks_prestasi_baru)
print()

print("Rata rata nilai lama = ", np.mean(nilai_akhir)) # untuk menampilkan rata rata nilai lama
print("Rata rata Nilai Baru = ", np.mean(nilai_akhir_baru)) # untuk menampilkan rata rata nilai baru

indeks_yang_dicari = 'A'
indeks_lama = np.count_nonzero(indeks_prestasi == indeks_yang_dicari) # mencari jumlah nilai dengan skala 'A' pada array lama
indeks_baru = np.count_nonzero(indeks_prestasi_baru == indeks_yang_dicari) # mencari jumlah nilai dengan skala 'A' pada array baru

print("Jumlah Nilai 'A' lama = ", indeks_lama)
print("Jumlah Nilai 'A' baru = ", indeks_baru)
print()

math_2031_angkatan_20xx_baru = np.block([NIM, nilai_akhir_baru, indeks_prestasi_baru]) # menggabungkan NIM, nilai akhir baru, dan indeks prestasi baru menjadi satu array 
table_baru = tabulate (math_2031_angkatan_20xx_baru, header, tablefmt="fancy_grid") # mengubah tampilan dari array menjadi tabel
print("Tabel Baru :\n")
print(table_baru)
print()

