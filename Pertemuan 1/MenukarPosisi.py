# Nama file: MenukarPosisi.py
# Pembuat: Rekha Inaya Putri
# Tanggal: 3 September 2023
# Deskripsi : menukar posisi dua variabel x dan y, dengan kasus :
# Ada 2 buah: manggis dan pisang. Manggis di piring 1, Pisang di piring 2. Piring 3 kosong.

# Inisialisasi variabel
manggis = "Manggis di piring 1"
pisang = "Pisang di piring 2"

# Tampilkan posisi awal
print("Posisi Awal:")
print("Piring 1:", manggis)
print("Piring 2:", pisang)
print("Piring 3: Kosong\n")

# Menukar posisi
temp = manggis
manggis = pisang
pisang = temp

# Tampilkan posisi setelah pertukaran
print("Posisi Setelah Pertukaran:")
print("Piring 1:", manggis)
print("Piring 2:", pisang)
print("Piring 3: Kosong")
