# Nama file: Latihan11.py
# Pembuat: Rekha Inaya Putri (2022071044)
# Tanggal: 13 September 2023
# Deskripsi: Bagaimana menyusun red sehingga mendapatkan hasil berikut?
#>>> yellow|red
#{'dandelions', 'fire hydrant', 'blood', 'rose', 'leaves'}
#>>> yellow&red
#{‘leaves’,'fire hydrant'}

yellow = {'dandelions', 'leaves', 'fire hydrant'}
red = {'fire hydrant', 'blood', 'rose', 'leaves'}
print("yellow = ", yellow)
print("red = ", red)
print(yellow | red)
print(red & yellow)