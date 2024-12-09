n = []
x = []
y = []
z = []

jenis_counter = 0 + 1
nomor_counter = 000 + 1

while True:
    nama = input(f"Masukkan nama barang ke-{len(n) + 1} (atau ketik '-' untuk mengakhiri): ")
    
    if nama.lower() == '-':
        break

    tahun = 2023
    jenis = f"{jenis_counter:04d}"
    nomor = f"{jenis_counter:010d}"
    n.append(nama)
    x.append(tahun)
    y.append(jenis)
    z.append(nomor)

    jenis_counter += 1
    nomor_counter += 1

for i in range(len(n)):
    print(f"{n[i]}:",x[i],"-",y[i],"-",z[i])