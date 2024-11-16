import numpy as np

def random_array(m, n, x, y):
    return np.random.randint(x, y, size=(m, n))

m = 4
n = 4
x = 0
y = 10

a = random_array(m, n, x, y)
b = random_array(m, n, x, y)
c = random_array(m, n, x, y)
d = random_array(m, n, x, y)
e = random_array(m, n, x, y)
f = random_array(m, n, x, y)
g = random_array(m, n, x, y)
h = random_array(m, n, x, y)
i = random_array(m, n, x, y)
j = random_array(m, n, x, y)
k = random_array(m, n, x, y)
l = random_array(m, n, x, y)
m_arr = random_array(m, n, x, y)
n_arr = random_array(m, n, x, y)
o = random_array(m, n, x, y)
p = random_array(m, n, x, y)
q = random_array(m, n, x, y)
r = random_array(m, n, x, y)
s = random_array(m, n, x, y)
t = random_array(m, n, x, y)
u = random_array(m, n, x, y)
v = random_array(m, n, x, y)
w = random_array(m, n, x, y)
x_arr = random_array(m, n, x, y)
y_arr = random_array(m, n, x, y)
z = random_array(m, n, x, y)

arrays = [a, b, c, d, e, f, g, h, i, j, k, l, m_arr, n_arr, o, p, q, r, s, t, u, v, w, x_arr, y_arr, z]
inverses = []

for arr in arrays:
    inverse = np.linalg.inv(arr)
    inverses.append(inverse)

np.set_printoptions(precision=2, suppress=True)

for idx, (arr, inv) in enumerate(zip(arrays, inverses)):
    print(f"{chr(ord('A') + idx)}:")
    print(arr)
    print(f"Inverse of {chr(ord('A') + idx)}:")
    print(inv)
    print("\n")
