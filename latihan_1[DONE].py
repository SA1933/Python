x = int(input("angka pertama: "))
if x < -1:
    print ("palak kau")
    x = int(input("masukan meneh x = "))
y = int (input("angka kedua: "))
if y < x:
    print ("palak kau")
    y = int(input("masukan meneh, y = "))
z = int (input("angka ketiga: "))
if z < y:
    print ("palak kau")
    z = int(input("masukan meneh, z = "))

hasil_1 = x * y * z
hasil_2 = x % y % z
hasil_3 = x - y - z
hasil_4 = x + y * z

print ("hasil_1= ",hasil_1, "\nhasil_2= ",hasil_2, "\nhasil_3= ",hasil_3, "\nhasil_4= ",hasil_4,)