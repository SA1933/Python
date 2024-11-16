import numpy as np
from fractions import Fraction

def multiply_matrices(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# Contoh matriks
matrix_a = np.array([[ 0.11688312, 0.01298701, 0.1038961 ],
                     [-0.54545455, 0.27272727, 0.18181818],
                     [-0.61038961, 0.37662338, 0.01298701]])

matrix_b = np.array([[3],
                     [7],
                     [15]])

# Memanggil fungsi untuk mengalikan matriks
result_matrix = multiply_matrices(matrix_a, matrix_b)

# Menampilkan hasil
print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("\nResult Matrix:")
print(result_matrix)

print("\nInverse Matrix (as fractions):")
for row in result_matrix:
    for a in row:
        fraction_matrix = Fraction(a).limit_denominator()
        print(fraction_matrix, end="\t")
    print()