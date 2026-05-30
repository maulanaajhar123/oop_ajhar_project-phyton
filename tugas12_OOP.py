total_nilai = 0

# Melakukan perulangan sebanyak 10 kali
for i in range(1, 11):
    nilai = float(input(f"Masukkan nilai siswa ke-{i}: "))
    total_nilai += nilai

print(f"\nTotal nilai dari 10 siswa adalah: {total_nilai}")
