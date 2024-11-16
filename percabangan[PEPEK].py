Rp = float(input("Masukan harga barang: "))

if Rp > 50000:
    hasil = Rp * 0.2
    if hasil > 5000:
         hasil = "mendapatkan diskon"
    else:
        hasil < 5000
        hasil = "mendapatkan diskon"
        hasil = Rp - hasil
else:
     Rp < 50000
     hasil = "tidak mendapatkan diskon"

print ("total harga: ", hasil)