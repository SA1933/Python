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

    ################################################################

list_data=[2,1,3,4,5,5,4,4,3,7,8]
#mengganti nilai didalam list
list_data[1]=5
print (list_data)
#sortir nilai dari kecil atau dari a to z
list_data.sort()

#list sort dari besar 
list_data.sort(reverse=True)
print (list_data)

#menghitung jumlah data yang muncul pada list
print(list_data.count(4))

#mencari indeks data angka misal 4 (hanya angka depan yang muncul)

indext_data_angka4= list_data.index(4)

#Tugas memunculkan semua index dari data list yang bernilai 4 menggunakan loop


print(indext_data_angka4)

#gabungkan data
list2=[5,8,1]
list_data.extend(list2)
print(list_data)
#menghapus data didalam list
list_data.remove(6)
print(list_data)