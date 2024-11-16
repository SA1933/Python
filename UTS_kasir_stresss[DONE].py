total_harga = 0
daftar_barang = []

while True:
    try:
        nama_barang = input(f"Masukkan nama barang ke-{len(daftar_barang) + 1} (atau 'selesai' untuk mengakhiri): ")
        
        if nama_barang.lower() == 'selesai':
            break

        harga = float(input(f"Masukkan harga {nama_barang}: "))

        if harga < 0:
            print("Harga tidak valid. Harap masukkan harga yang benar.")
            continue

        total_harga += harga
        daftar_barang.append((nama_barang, harga))

    except ValueError:
        print("Harga tidak valid. Harap masukkan harga yang benar.")

print(f"Total harga sebelum diskon: {total_harga:.2f} Rupiah")

if total_harga > 200000:
    diskon = min(total_harga * 0.10, 100000)
elif total_harga > 40000:
    diskon = min(total_harga * 0.05, 100000)
else:
    diskon = 0

total_harga_diskon = total_harga - diskon

print(f"Total harga setelah mendapatkan diskon: {total_harga_diskon:.2f} Rupiah")

print("Daftar Barang:")
for nama, harga in daftar_barang:
    print(f"{nama}: {harga:.2f} Rupiah")

print(f"Diskon: {diskon:.2f} Rupiah")