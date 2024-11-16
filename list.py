a="mahasiswa 1"
b="mahasiswa 2"
#tipe list masukan ke indeks, contoh:
nama_mahasiswa= ['mahasiswa 1', "mahasiswa 2"]
#diketahui indeksnya
#print(nama_mahasiswa[0])

#memasukan insert kedalam list
nama_mahasiswa.insert(2,"mahasiswa")
#print(nama_mahasiswa)

#menambahkan data dibelakang list
nama_mahasiswa.append('mahasiswa tambahan 2')
print(nama_mahasiswa)

#untuk mengetahui jumlah data dilist
jumlah_data = len(nama_mahasiswa)
print("jumlah data pada list adalah", jumlah_data)

#[] digunakan untuk mengisi data kosong

#contoh:
nama_mahasiswa = []
for i in range (10):
    jumlah_data.append (input("nama mahasiswa "))