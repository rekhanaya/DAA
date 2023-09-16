# Nama file: Latihan1.py
# Pembuat: Rekha Inaya Putri (2022071044)
# Tanggal: 13 September 2023
# Deskripsi :Buatlah list dengan nama "Mahasiswa" yang berisi Nama, NIM, Prodi, mata kuliah, tanggal hari ini, nama universitas

from datetime import date

x = date.today()
tanggal = x.strftime("%d %B %Y")

mahasiswa = ["Rekha Inaya Putri", "2022071044", "Informatika", "Design dan Analisis Algoritma", tanggal, "Universitas Pembangunan Jaya"]

print("Mahasiswa = ", mahasiswa)

# Iterasi
print("# Iterasi")
for x in mahasiswa:
  print("UPJ " + x)


