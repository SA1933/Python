import numpy as np

p1 = np.transpose(np.array([[3,2,1]]))
p2 = np.transpose(np.array([[4,1,3]]))
p3 = np.transpose(np.array([[2,2,2]]))
p4 = np.transpose(np.array([[1,0,0]]))
p5 = np.transpose(np.array([[0,1,0]]))
p6 = np.transpose(np.array([[0,0,1]]))
cb = np.array([[0,0,0]])
cd = np.array([[30,40,35]])
b  = np.transpose(np.array([[90,54,93]]))
c  = np.array([[30,40,35,0,0,0]])
n  = 3  

# Concatenate matrices
x = np.hstack((p1, p2, p3))
print (x.shape)
y = np.hstack((p4, p5, p6))
print (y.shape)

# Run revised simplex method
#revised_simplex_method(x, y, c, cb, b, n)

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

print("\ninput komponen matrix b, matriks c_d & c basis: ")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))
print("\ninput komponen matrix b: ")
b  = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\ninput komponen matrix c basis: ")
cb = np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)])
print("\ninput komponen matrix cd: ")
cd = np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)])

n = int(input("\ninput jumlah iterasi program: "))

################################################################
print("input konstrain matrix A dan B")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))
print("\ninput komponen matrix A")
x = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\ninput komponen matrix B")
y = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))

print("\ninput konstrain matrix b tujuan")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))
print("\ninput komponen matrix b tujuan")
b = np.transpose(np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))

print("\ninput konstrain matrix C")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))
print("\ninput komponen matrix C")
c = np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)])