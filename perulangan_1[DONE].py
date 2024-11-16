while True:
    try:
        angka = float(input("Masukkan angka: "))
        if angka.is_integer():
            print("Ini adalah bilangan positif.")
        else:
            print("Ini adalah bilangan negatif.")          
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka.")
    
    lanjutkan = input("Apakah Anda ingin memasukkan angka lagi? (ya/tidak): ")
    if lanjutkan.lower() != "ya":
        break