x = int(input("Masukkan nilai x: "))

# Menentukan posisi titik
if x > 0:
    print("Titik di kanan layar")
elif x < 0:
    print("Titik di kiri layar")
else:
    print("Titik di tengah")

# Perulangan angka 1 sampai 5
print("menampilkan 5 titik:")
for i in range(1, 6):
    print(f" Titik Ke-{i}")