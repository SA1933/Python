import numpy as np
C = []
m, n = map(int, input("Enter dimensions m, n (please enter space): ").split())
if m <= 0 or n <= 0:
                raise ValueError("Dimensions must be positive integers.")
for i in range(m):
                row = input(f"Enter row {i+1}: ").split()
                if len(row) != n:
                    raise ValueError("Invalid number of elements in row.")
                C.append([int(x) for x in row])
p4 = np.transpose (np.array ([[1 , 0 , 0]]))
p5 = np.transpose (np.array ([[0 , 1 , 0]]))
p6 = np.transpose (np.array ([[0 , 0 , 1]]))
A = np.hstack([p4,p5,p6])
B = np.array (C)
x = [0 for i in range(n)]
z = 0
for i in range(n-1, -1, -1):
    max = -1
    index = -1
    for j in range(n):
      if A[i][j] > 0 and B[i][j] > max:
        max = B[i][j]
        index = j
    if max != -1:
      x[index] = max
      z = z + (max * B[i][index])
    for j in range(n):
        if A[i][j] > 0:
          A[i][j] = A[i][j] - max * B[j][index]
        print("Nilai optimal fungsi tujuan: ", z)
        print("Nilai optimal masing-masing variabel: ", (x[i]))
        print("\nSolusi idealis dari sistem linear : \n", x)