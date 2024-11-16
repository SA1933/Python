import numpy as np

print("input constraint mattiks A!")
m, n = int(input("masukan jumlah baris: ")), int(input("masukan jumlah kolom: "))
print("\ninput komponen matrix P1: ")
A = np.array([[int(input(f"masukan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]) # A = [[3,2,1],[4,1,3],[2,2,2]] 

print(A)

new_A = np.hsplit(A,3)

print(np.transpose([A[0,:]]))
print(np.transpose([A[1,:]]))
print(np.transpose([A[2,:]]))