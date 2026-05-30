t = 0
h = int(input("masukkan harga barang (0 untuk selesai): "))

while h != 0:
    t += h
    h = int(input("masukkan harga barang (0 untuk selesai): "))

if t >= 50000:
    t -= 5000

print("total yang harus dibayar: Rp.", t)