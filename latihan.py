import numpy as np

#m = input(int("jumlah baris: "))
#n = input(int("jumlah kolom: "))

A = np.array(
    [
        [3,2,1],
        [4,1,3],
        [2,2,2]
    ]
)
B = np.array(
    [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
)
b = np.array(
    [
        [90,54,93]
    ]
)
c = np.array(
    [
        [30,40,35,0,0,0]
    ]
)
cb = np.array(
    [
        [0,0,0]
    ]
)

#gabungan matriks

#print (p1.shape)
print(A)
pAt = np.transpose(A)
print(pAt)
#print (p1t.shape)
print(B)
pBt = np.transpose(B)
print(pBt)
print(b)
pbt = np.transpose(b)
print(pbt)
print(c)
Binv = np.linalg.inv(B)
print(Binv)
print(cb)

#pengali simplex

#iterasi

a = np.array([[30, 40, 35]])
b = np.transpose(np.array([[90, 54, 93]]))

print(np.divide(b, a))

c = np.array([[40, 40, 40]])
print("\n",np.max(c))