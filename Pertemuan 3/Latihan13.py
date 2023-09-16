# Nama file: Latihan13.py
# Pembuat: Rekha Inaya Putri (2022071044)
# Tanggal: 13 September 2023
# Deskripsi: Buatlah Matrix dengan nilai berikut
#    [[ 100  200  300]
#[700  600  500]
#[900  1000  800 ]]
#Lakukan transpose matrix!

import numpy
matrixL = numpy.array([[100, 200, 300], [700, 600, 500], [900, 1000, 800]])
print("Matrix Latihan = ")
print(matrixL, "\n")
print("# Setelah ditranspose")
transpose_matrixL = numpy.transpose(matrixL)
print("Transpose Matrix Latihan = ")
print(transpose_matrixL)