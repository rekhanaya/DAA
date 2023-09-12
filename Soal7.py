# Nama file: Soal7.py
# Pembuat: Rekha Inaya Putri
# Tanggal: 6 September 2023
# Deskripsi: getSum adalah perintah untuk mendapatkan hasil jumlah seluruh angka. Bagaimana jika kita membutuhkan fungsi getKali untuk mengalikan seluruh angka?

def getkali(myList):
    kali = 1
    for item in myList:
      kali = kali * item
    return kali
getkali([1,2,3])