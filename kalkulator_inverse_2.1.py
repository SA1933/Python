import numpy as np
from fractions import Fraction

p1 = np.transpose(np.array([[3,2,1]]))
p2 = np.transpose(np.array([[4,1,3]]))
p3 = np.transpose(np.array([[2,2,2]]))
p4 = np.transpose(np.array([[1,0,0]]))
p5 = np.transpose(np.array([[0,1,0]]))
p6 = np.transpose(np.array([[0,0,1]]))
cb = np.array([[0,0,0]])
cd = np.array([[30,40,35]])
b  = np.transpose(np.array([[90,54,93]]))
#n  = 3
iteration = 0

#print("\nMatrix P1:")
#print(" ".join(" ".join(map(str, row)) for row in p1))
#print("\nMatrix P2:")
#print(" ".join(" ".join(map(str, row)) for row in p2))
#print("\nMatrix P3:")
#print(" ".join(" ".join(map(str, row)) for row in p3))

#print("\nmenggabungkan matriks diatas: ")
x = np.hstack((p1, p2, p3))
#print("\nA")
#print(x)
y = np.hstack((p4, p5, p6))
#print("\nB")
#print(y)
full = np.hstack((p1, p2, p3, p4, p5, p6, b))
print("\nfull inisialisasi: ")
print(full)
print("\nmatrix c: ")
c = np.hstack((cd, cb))
print(c)
#print("\nmatriks b")
#print(b)

print("\nbismillah memulai perhitungan matriks")

while True:
    iteration += 1
    print(f"\n\t\t\t---------- Iterasi {iteration}:")

    print("\ninverse matriks B:")
    Y = np.linalg.inv(y)
    for row in Y:
        for a in row:
            fraction_matrix = Fraction(a).limit_denominator()
            print(fraction_matrix, end="\t")
        print()
    #print(Y)

    pi = np.dot(cb, Y)
    print("\nnilai pengali simplex atau phi:")
    print(pi)

    [baris, ] = x[:, 0].shape
    c1aksen = cd[0,0] - np.dot(pi, x[:, 0].reshape(baris, 1))
    #print(x[:, 0])
    nilai_c1 = c1aksen[0, 0]
    #print("\nnilai c1 aksen")
    #print(nilai_c1)

    c2aksen = cd[0,1] - np.dot(pi, x[:, 1].reshape(baris, 1))
    #print(x[:, 1])   
    nilai_c2 = c2aksen[0, 0]
    #print("nilai c2 aksen")
    #print(nilai_c2)

    c3aksen = cd[0,2] - np.dot(pi, x[:, 2].reshape(baris, 1))
    #print(x[:, 2])
    nilai_c3 = c3aksen[0, 0]
    #print("nilai c3 aksen")
    #print(nilai_c3)

    print("\nmatriks entering variabel:")
    ent = np.array([[nilai_c1, nilai_c2, nilai_c3]])
    print(ent)

    #print("\n---mencari nilai c aksen maksimal---")
    [baris_ent, kolom_ent] = np.where(ent==np.max(ent))
    entering = np.transpose(np.dot(Y, x[:, kolom_ent]))
    print("\ntentukan nilai positif (+) terbesar:")
    print(f"{np.max(ent):.1f}")
    #print("entering\n", entering)
    
    #print(entering.shape)
    b_aksen = np.transpose(np.dot(Y, b))
    print("\nnilai b aksen:")
    print(b_aksen)
    
    x1 = b_aksen[0,0]
    x2 = b_aksen[0,1]
    x3 = b_aksen[0,2]

    if np.max(ent) > 0:
        rasio = np.divide(b_aksen, entering)
        print("\nrasio")
        print(rasio)
        [baris_rasio, kolom_rasio] = np.where(rasio== np.min(rasio))
        print("\ntentukan nilai negatif (-) terkecil:")
        print(np.min(rasio))

        atemp  = np.copy(x)
        btemp  = np.copy(y)
        Cbtemp = np.copy(cb)

        x[:, kolom_ent] = btemp[:, kolom_rasio]
        y[:,  kolom_rasio] = atemp[:, kolom_ent]
        cb[:, kolom_rasio] = c[:, kolom_ent]
        cd[:, kolom_ent] = Cbtemp[:, kolom_rasio]

    elif np.max(ent) < 0:
        print("\nkarena semua nilai entering = negatif, \nmaka:\n----sudah optimal---- ")
        break

        #print("\nmatriks A baru:")
        #print(x)
        #print("\nmatriks B baru:")
        #print(y)
        #print("\nC basis baru:")
        #print(cb)
        #print(cd)
        #print(baris_rasio)
        #print(kolom_rasio)
        #print(np.min(rasio))
        #print(rasio.shape)
        #print(Y.shape)
        #print(b.shape)

print("\nmencari nilai akhir z")
z = c[0,0]*x1 + c[0,1]*x2 + c[0,2]*x3
print("nilai akhir yaitu:\n z =" ,c[0,0],"* x1 +",c[0,1],"* x2 +",c[0,2],"* x3 =", z) 
print("\n")
