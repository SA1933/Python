panjang_urutan = int(input("Masukkan panjang urutan Fibonacci: "))

a, b = 0, 1

urutan_fibonacci = []

while len(urutan_fibonacci) < panjang_urutan:
    urutan_fibonacci.append(a)
    a, b = b, a + b

print("Urutan Fibonacci dengan panjang", panjang_urutan, "adalah:")
print(urutan_fibonacci)