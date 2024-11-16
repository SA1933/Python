import numpy as np 
#inisialisasi matrik

#matriks non basic
p1 = np.transpose (np.array ([[3 , 2 , 1]]))
p2 = np.transpose (np.array ([[4 , 1 , 3]]))
p3 = np.transpose (np.array ([[2 , 2 , 2]]))
#matrik basis
p4 = np.transpose (np.array ([[1 , 0 , 0]]))
p5 = np.transpose (np.array ([[0 , 1 , 0]]))
p6 = np.transpose (np.array ([[0 , 0 , 1]]))
#gabungkan matrik basis
A = np.hstack((p1,p2,p3))
#matriks non basis
B = np.hstack((p4,p5,p6))
#c adalah bentuk selain p1-p6
c = np.array ([[30, 40, 35, 0, 0, 0]])
Cs = np.array ([[30, 40, 35]]) #matriks fungsi tujuan
Cb = np.array ([[0,0,0]])
b = np.transpose (np.array([[90,54,53]]))
#print ('c', C.shape)
#print (Cb.shape)
#iterasi 0
    #menghitung pengali matrik basis (phi)
for i in range(1):
    binv = np.linalg.inv (B)
    print("BINV ") 
    print(binv)
    pi = np.dot (Cb,binv)
    print ('pi= ', pi)

    [baris, ] = A[:, 0].shape
    c1aksen = Cs [0,0] - np.dot(pi, A[:, 0].reshape(baris, 1))
    nilai_c1 = c1aksen[0, 0]
    print("\nnilai c1 aksen")
    print(nilai_c1)

    c2aksen = Cs[0,1] - np.dot(pi, A[:, 1].reshape(baris, 1))
    nilai_c2 = c2aksen[0, 0]
    print("\nnilai c2 aksen")
    print(nilai_c2)

    c3aksen = Cs[0,2] - np.dot(pi, A[:, 2].reshape(baris, 1))
    nilai_c3 = c3aksen[0, 0]
    print("\nnilai c3 aksen")
    print(nilai_c3)

    print("\nmencari entering variabel")
    matent = np.array([[nilai_c1, nilai_c2, nilai_c3]])
    print(matent)
    #print("\nmencari nilai c aksen maksimal")

    #mencari nilai max matriks
    [barisent, koloment] = np.where (matent == np.max (matent))
    print (np.max (matent))
    #mencari entering variabel
    entering = np.dot(binv,A[:,koloment])
    b_aksen = np.dot(binv,b)
    rasio = np.divide (b_aksen,entering)
    [baris_rasio,kolom_rasio] = np.where(rasio== np.min(rasio))
    print(rasio)
    atemp = np.copy (A)
    btemp = np.copy (B)
    Cbtemp = np.copy (Cb)

    A[:, koloment] = btemp[:, baris_rasio]
    B[:, baris_rasio] = atemp[:, koloment]
    Cb[:, baris_rasio] = c [:, koloment]
    print (A)
    print (B)
    print (Cb)
#var_e = np.where ((koloment == barisent), True, False)
#mencari leaving variable
#var_l = np.logical_not (var_e)
#print (var_e)
#print (var_l)
#print ('variabel masuk')
#print (np.where (var_e==True))
#print ('variabel keluar')
#print (np.where (var_l==True))
#print ('nilai max')
#print (barisent)
#===============================ITERASI 1=====================================
#membuat matrix a dan b yang sudah diperbesar dengan ukuran baris dan kolomnya
#Aek = np.zeros ((baris+len(var_e),baris+len(var_l)))
#Bek = np.zeros ((baris+len(var_e),1))
#for i in range (len(var_e)):
 #   Bek [i + len(var_e)] = B[var_e [i],0]