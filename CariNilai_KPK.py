# Nama file: CariNilai_KPK.py
# Pembuat: Rekha Inaya Putri
# Tanggal: 3 September 2023
# Deskripsi : Mencari KPK dari 3 dan 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

angka1 = 3
angka2 = 4

kpk = lcm(angka1, angka2)
print(f"KPK dari {angka1} dan {angka2} adalah {kpk}")
