# Nama file: Soal8.py
# Pembuat: Rekha Inaya Putri
# Tanggal: 6 September 2023
# Deskripsi: getSum adalah perintah untuk mendapatkan hasil jumlah seluruh angka. Bagaimana jika kita membutuhkan fungsi getBagi untuk membagikan seluruh angka?

def getBagi(myList):
  bagi = 0
  for item in myList:
    bagi = bagi/item
  return bagi
getBagi([-2, 4, 5, -7, 9, 4, 5])