import numpy as np
from fractions import Fraction

def random_array(m, n, x, y):
    return np.random.randint(x, y, size=(m, n))

m = 4
n = 4
x = 0
y = 10

matrices = [random_array(m, n, x, y) for _ in range(26)]

for idx, matrix in enumerate(matrices):
    matrix_name = chr(ord('A') + idx)

    print(f"\n{matrix_name}: ")
    print(matrix)

    inverse_matrix = np.linalg.inv(matrix)
    np.set_printoptions(precision=2, suppress=True)
    print(f"inverse_{matrix_name}: ")
    print(inverse_matrix, "\n")

    print(f"Inverse Matrix {matrix_name} (as fractions):")
    for row in inverse_matrix:
        for element in row:
            fraction_element = Fraction(element).limit_denominator()
            print(f"{fraction_element}", end="\t")
        print()