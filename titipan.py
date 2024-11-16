import numpy as np

# Inisialisasi matriks
# Matriks non basic
p1 = np.transpose(np.array([[3, 2, 1]]))
p2 = np.transpose(np.array([[4, 1, 3]]))
p3 = np.transpose(np.array([[2, 2, 2]]))
# Matrik basis
p4 = np.transpose(np.array([[1, 0, 0]]))
p5 = np.transpose(np.array([[0, 1, 0]]))
p6 = np.transpose(np.array([[0, 0, 1]]))
# Gabungkan matriks basis
A = np.hstack((p1, p2, p3))
# Matriks non basis
B = np.hstack((p4, p5, p6))
# c adalah bentuk selain p1-p6
C = np.array([30, 40, 35, 0, 0, 0])
Cb = np.array([[0, 0, 0]])
b = [90, 54, 53]

# Iterasi 0
# Menghitung pengali matriks basis (phi)
binv = np.linalg.inv(B)
pi = np.dot(Cb, binv)

# Yang dicari matriks non basis
# Menghitung koefisien fungsi tujuan relatif dari var non basis matrik
# Mencari tahu jumlah baris kolom
[baris, ] = A[:, 0].shape
c1aksen = C[0] - np.dot(pi, A[:, 0].reshape(baris, 1))
nilaic1 = c1aksen[0, 0]
print(nilaic1)

c2aksen = C[1] - np.dot(pi, A[:, 1].reshape(baris, 1))
nilaic2 = c2aksen[0, 0]
print(nilaic2)

c3aksen = C[2] - np.dot(pi, A[:, 2].reshape(baris, 1))
nilaic3 = c3aksen[0, 0]
print(nilaic3)

# Membuat matriks entri
matent = np.array([[nilaic1, nilaic2, nilaic3]])
# Mencari nilai max matriks
[barisent, koloment] = np.unravel_index(np.argmax(matent), matent.shape)

# Melanjutkan langkah pada reverse simplex hingga iterasi satu selesai