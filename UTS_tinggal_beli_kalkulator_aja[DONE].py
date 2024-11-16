hasil = None

while True:
    try:
        if hasil is None:
            angka1 = float(input("Masukkan angka pertama: "))
        else:
            angka1 = hasil

        operasi = input("Masukkan operasi (+, -, *, /) atau '=' untuk mengakhiri: ")

        if operasi == '=':
            print("Hasil akhir: ", hasil)
            break

        angka2 = float(input("Masukkan angka kedua: "))

        if operasi == '+':
            hasil = angka1 + angka2
        elif operasi == '-':
            hasil = angka1 - angka2
        elif operasi == '*':
            hasil = angka1 * angka2
        elif operasi == '/':
            if angka2 == 0:
                print("Tidak dapat membagi dengan nol")
                hasil = None
            else:
                hasil = angka1 / angka2
        else:
            print("Operasi tidak valid. Silakan coba lagi.")
            hasil = None

        if hasil is not None:
            print("Hasil:", hasil)
    except ValueError:
        print("Masukan tidak valid. Silakan coba lagi.")
        hasil = None