def pengambilan_keputusan(pilihan):
    if pilihan == 1:
        print("Anda memilih opsi 1. Keputusan Anda: A")
    elif pilihan == 2:
        print("Anda memilih opsi 2. Keputusan Anda: B")
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 atau 2.")

# Input dari pengguna
try:
    pilihan = int(input("Masukkan pilihan Anda (1 atau 2): "))
    pengambilan_keputusan(pilihan)
except ValueError:
    print("Masukkan harus berupa angka.")
