import numpy as np

print("input komponen matrix P1 P2 & P3")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))

print("\ninput komponen matrix P1: ")
p1 = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\ninput komponen matrix P2: ")
p2 = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\ninput komponen matrix P3: ")
p3 = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))

p4 = np.transpose(np.array([[1, 0, 0]]))
p5 = np.transpose(np.array([[0, 1, 0]]))
p6 = np.transpose(np.array([[0, 0, 1]]))

print("\ninput komponen matrix c: ")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))
c  = np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)])

print("\ninput komponen matrix b & c basis: ")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))
print("\ninput komponen matrix b: ")
b  = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\ninput komponen matrix c basis: ")
cb = np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)])

n = int(input("\ninput jumlah iterasi program: "))

print("\nMatrix P1:")
print(" ".join(" ".join(map(str, row)) for row in p1))
print("\nMatrix P2:")
print(" ".join(" ".join(map(str, row)) for row in p2))
print("\nMatrix P3:")
print(" ".join(" ".join(map(str, row)) for row in p3))

print("\nmenggabungkan matriks diatas: ")
x = np.hstack((p1, p2, p3))
print("\nA")
print(x)
y = np.hstack((p4, p5, p6))
print("\nB")
print(y)
print("\nmatriks C")
print(c)
print("\nmatriks C basis")
print(cb)
print("\nmatriks B")
print(b)

for i in range(n):
    for iteration in range(1, n + 1):
        print(f"\nIteration {iteration}:")

        print("\ninverse matriks b:")
        Y = np.linalg.inv(y)
        print(Y)

        pi = np.dot(cb, Y)
        print("\nnilai pengali simplex x phi:")
        print(pi)

        [baris, ] = x[:, 0].shape
        c1aksen = c[0,0] - np.dot(pi, x[:, 0].reshape(baris, 1))
        nilai_c1 = c1aksen[0, 0]
        print("\nnilai c1 aksen")
        print(nilai_c1)

        c2aksen = c[0,1] - np.dot(pi, x[:, 1].reshape(baris, 1))
        nilai_c2 = c2aksen[0, 0]
        print("nilai c2 aksen")
        print(nilai_c2)

        c3aksen = c[0,2] - np.dot(pi, x[:, 2].reshape(baris, 1))
        nilai_c3 = c3aksen[0, 0]
        print("nilai c3 aksen")
        print(nilai_c3)

        print("\nentering variabel")
        ent = np.array([[nilai_c1, nilai_c2, nilai_c3]])
        print(ent)

        print("\n---mencari nilai c aksen maksimal---")

        [baris_ent, kolom_ent] = np.where(ent==np.max(ent))
        entering = np.dot(Y, x[:, kolom_ent])
        b_aksen = np.dot(Y, b)
        print("\nnilai b aksen")
        print(b_aksen)
        rasio = np.divide(b_aksen, entering)
        print("\nrasio")
        print(rasio)

        [baris_rasio,kolom_rasio] = np.where(rasio== np.min(rasio))
        atemp  = np.copy(x)
        btemp  = np.copy(y)
        Cbtemp = np.copy(cb)
        x[:, kolom_ent] = btemp[:, baris_rasio]
        y[:, baris_rasio] = atemp[:, kolom_ent]
        cb[:, baris_rasio] = c[:, kolom_ent]

        print("\nmatriks A baru:")
        print(x)
        print("\nmatriks B baru:")
        print(y)
        print("\nC basis baru:")
        print(cb)
