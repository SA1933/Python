#Menginput Tahun
tahun = int(input("Tulis Sebuah Tahun: "))
 
#Perulangan Ke-1
if (tahun % 4) == 0:
 
   #Perulangan Ke-2
   if (tahun % 100) == 0:
 
       #Perulangan Ke-3
       if (tahun % 400) == 0:
 
           #Tergolong Tahun Kabisat
           print("{0} adalah Tahun Kabisat".format(tahun))
 
       #Bukan Tergolong Tahun Kabisat
       else:
           print("{0} bukan Tahun Kabisat".format(tahun))
 
   #Tergolong Tahun Kabisat
   else:
       print("{0} adalah Tahun Kabisat".format(tahun))
 
#Bukan Tergolong Tahun Kabisat
else:
   print("{0} bukan Tahun Kabisat".format(tahun))