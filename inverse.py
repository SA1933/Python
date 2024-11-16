import numpy as np
from fractions import Fraction

a = np.array([[2, 1, 3], [4, 0, 1], [3, 2, 5]])

inverse_a = np.linalg.inv(a)

print("Matrix A:")
print(a)

print("\nInverse Matrix (as fractions):")
for row in inverse_a:
    for element in row:
        fraction_element = Fraction(element).limit_denominator()
        print(fraction_element, end="\t")
    print()