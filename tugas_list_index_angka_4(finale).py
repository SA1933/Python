#karena saya ada 2 program jadi begini: run program pertama dulu dan masukan output ke program kedua "random_numbers = [output program pertama]"

#program pertama = random integer untuk menampilkan angka acak untuk program dibawah

import numpy as np

random_numbers = np.random.randint(1, 5, size=50)

print("angka acak:", end=" ")
for number in random_numbers:
    print(number, end=", ")

#program kedua = menampilkan angka == 4 jumlah munculnya dan urutan keberapa

random_numbers = []
print(random_numbers)

count_4 = random_numbers.count(4)

if count_4 > 0:
    print(f"Jumlah kemunculan angka 4: {count_4}")
    print("Urutan kemunculan angka 4:")
    
    for i, num in enumerate(random_numbers, start=1):
        if num == 4:
            print("ke-", i)
else:
    print("Angka 4 tidak muncul dalam list.")

#nahhhhhh kenapa tidak digabung saja? karena masih butuh tutorial pak :>