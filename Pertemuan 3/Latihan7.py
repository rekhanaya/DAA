# Nama file: Latihan7.py
# Pembuat: Rekha Inaya Putri (2022071044)
# Tanggal: 13 September 2023
# Deskripsi: Cetak isi list “Mahasiswa”, tambahkan kata “UPJ” di depan!

from datetime import date

x = date.today()
tanggal = x.strftime("%d %B %Y")
mahasiswa = ["Rekha Inaya Putri", str(2022071044), "Informatika", "Design dan Analisis Algoritma", str(tanggal), "Universitas Pembangunan Jaya"]
for i in mahasiswa:
     print("UPJ " + i)