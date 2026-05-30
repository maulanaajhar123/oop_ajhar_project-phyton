nama = input("Nama barang : ")
harga = int(input("Harga barang : "))
jumlah = int(input("Jumlah beli : "))

total = harga * jumlah

if total >= 50000:
 diskon = total * 0.1

else:
 diskon = 0

bayar = total - diskon
print("Total =", total)
print("Diskon =", diskon)
print("Bayar =", bayar)