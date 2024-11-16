import numpy as np
from fractions import Fraction

def revised_simplex(c, A, b):
    m, n = len(b), len(c)
    c = np.array(c).flatten()  # Ensure c is a flat array
    A = np.array(A)
    b = np.array(b)

    # Tambahkan variabel surplus
    A = np.hstack((A, np.eye(m)))
    c = np.hstack((c, np.zeros(m)))

    # Solusi awal yang memenuhi batasan
    basis = np.arange(n, n + m)

    while True:
        # Hitung tableau
        B = A[:, basis]
        B_inv = np.linalg.inv(B)
        c_B = c[basis]
        tableau = np.vstack((np.hstack((B_inv @ A, B_inv @ b.reshape(-1, 1))),
                             np.hstack((c_B @ B_inv @ A - c, c_B @ B_inv @ b.reshape(-1, 1)))))

        # Periksa optimalitas
        if all(tableau[-1, :-1] >= 0):
            break

        # Pilih variabel masuk
        entering_var = np.argmax(tableau[-1, :-1] < 0)

        # Periksa keterbatasan tak terbatas
        if all(tableau[:-1, entering_var] <= 0):
            raise Exception("Program linier tak terbatas")

        # Pilih variabel keluar
        leaving_var = np.argmin(tableau[:-1, entering_var] > 0)

        # Pivot
        basis[leaving_var] = entering_var

    # Ekstrak solusi optimal
    optimal_solution = np.zeros(n + m)
    optimal_solution[basis] = tableau[:-1, -1]

    return optimal_solution[:n]

def print_fraction_matrix(matrix):
    for row in matrix:
        print(" ".join(str(Fraction(elem).limit_denominator()) for elem in row))

print("--= MEMBUAT PROGRAM INVERSE MATRIX MENGGUNAKAN METODE REVISED SIMPLEX =--\n")

# Input komponen matriks P1, P2, dan P3
m, n = int(input("Masukkan jumlah baris: ")), int(input("Masukkan jumlah kolom: "))
print("\nInput komponen matriks P1: ")
p1 = np.transpose(np.array([[int(input(f"Masukkan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\nInput komponen matriks P2: ")
p2 = np.transpose(np.array([[int(input(f"Masukkan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\nInput komponen matriks P3: ")
p3 = np.transpose(np.array([[int(input(f"Masukkan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))

# Input komponen matriks c
print("\nInput komponen matriks c: ")
m, n = int(input("Masukkan jumlah baris: ")), int(input("Masukkan jumlah kolom: "))
c  = np.array([[int(input(f"Masukkan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)])

# Input komponen matriks b dan c basis
print("\nInput komponen matriks b & c basis: ")
m, n = int(input("Masukkan jumlah baris: ")), int(input("Masukkan jumlah kolom: "))
print("\nInput komponen matriks b: ")
b  = np.transpose(np.array([[int(input(f"Masukkan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))
print("\nInput komponen matriks c basis: ")
cb = np.transpose(np.array([[int(input(f"Masukkan elemen ke- ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))

# Matriks P4, P5, dan P6
p4 = np.transpose(np.array([[1, 0, 0]]))
p5 = np.transpose(np.array([[0, 1, 0]]))
p6 = np.transpose(np.array([[0, 0, 1]]))

print("\nMatrix P1:")
print_fraction_matrix(p1)
print("\nMatrix P2:")
print_fraction_matrix(p2)
print("\nMatrix P3:")
print_fraction_matrix(p3)
print("\nP4:")
print_fraction_matrix(p4)
print("\nP5:")
print_fraction_matrix(p5)
print("\nP6:")
print_fraction_matrix(p6)

# Menggabungkan matriks di atas
A = np.hstack((p1, p2, p3))
B = np.hstack((p4, p5, p6))

print("\nMatrix A:")
print_fraction_matrix(A)
print("\nMatrix B:")
print_fraction_matrix(B)

# Invers matriks B menggunakan metode Revised Simplex
B_inv = revised_simplex(c, A, b)

print("\nInverse matriks B:")
print_fraction_matrix(B_inv)
