a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
tinggi_target = float(input("Masukkan tinggi target tanaman jagung: "))

hari = 0

while True:
    tinggi_tanaman = a * hari**2 + b * hari + c
    if tinggi_tanaman >= tinggi_target:
        break
    hari += 1

print("Dibutuhkan", hari, "hari untuk mencapai tinggi target", tinggi_target)