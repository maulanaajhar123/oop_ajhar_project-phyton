#contoh struktur percabangan if
#inpur data dari pengguna
nilai_ujian = float(input("masukkan nilai ujian siswa :"))

if nilai_ujian >= 90:
   predikat ="sangat baik (A)"
elif nilai_ujian >= 75:
   predikat = "baik (B)"
elif nilai_ujian >= 60:
   predikat = "cukup (C)"
else:
   predikat ="kurang baik(D) - memerlukan remedial"
   
  #menampilkan hasil keputusan
print("hasil evaluasi :",predikat)