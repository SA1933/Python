angka = int(input("Masukkan sebuah angka: "))

print("Faktor-faktor dari angka", angka, "adalah:")
for i in range(1, angka + 1):
    if angka % i == 0:
        print(i)