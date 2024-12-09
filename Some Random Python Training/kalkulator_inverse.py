import numpy as np
from fractions import Fraction

print("membuat program inverse matrix\n")

m, n = int(input("Enter the number of rows: ")), int(input("Enter the number of columns: "))
matrix = np.transpose(np.array([[int(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]))

print("\nMatrix:")
print("\n".join(" ".join(map(str, row)) for row in matrix))

inverse_a = np.linalg.inv(matrix)

print("\nMatrix A:\n")
print(matrix, "\n")
print("inverse_a")
print(inverse_a)

print("\nInverse Matrix (as fractions):")
for row in inverse_a:
    for a in row:
        fraction_matrix = Fraction(a).limit_denominator()
        print(fraction_matrix, end="\t")
    print()