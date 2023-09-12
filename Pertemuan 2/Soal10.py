# Nama file: Soal10.py
# Pembuat: Rekha Inaya Putri
# Tanggal: 6 September 2023
# Deskripsi: Buatlah suatu fungsi untuk :mengurangi 2 himpunan angka, jika getSum untuk menjumlahkan angka!

def Bagi2Himpunan(a,b):
  sum = 0
  for i in a:
    sum += i
  sum2 = 0
  for i in b:
    sum2 += i
  result = sum/sum2
  return result
Bagi2Himpunan (a = [10, 20, 30], b = [2, 4, 6])