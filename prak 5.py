# a. Input 3 pasangan titik
print("=== LIST TITIK ===")

titik = []

for i in range(3):
    x = int(input(f"Masukkan x titik ke-{i+1}: "))
    y = int(input(f"Masukkan y titik ke-{i+1}: "))
    titik.append((x, y))

print("\nDaftar titik:")
for t in titik:
    print(t)


# b. Input titik pusat
print("\n=== TUPLE TITIK PUSAT ===")

x_pusat = int(input("Masukkan x titik pusat: "))
y_pusat = int(input("Masukkan y titik pusat: "))

pusat = (x_pusat, y_pusat)

print("Titik pusat:", pusat)


# c. Input dictionary
print("\n=== DICTIONARY ===")

x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
warna = input("Masukkan warna: ")

data_titik = {
    "x": x,
    "y": y,
    "warna": warna
}

print(f"Titik ({data_titik['x']},{data_titik['y']}) berwarna {data_titik['warna']}.")