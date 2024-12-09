random_numbers = [2,5,6,4,4]
print(random_numbers)

count_4 = random_numbers.count(4)

if count_4 > 0:
    print("Jumlah kemunculan angka 4:", count_4)
    print("Urutan kemunculan angka 4:")
    for i, num in enumerate(random_numbers, start=1):
        if num == 4:
            print("ke-", i)
else:
    print("Angka 4 tidak muncul dalam list.")