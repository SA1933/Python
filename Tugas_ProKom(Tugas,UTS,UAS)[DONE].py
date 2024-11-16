while True:
    try:
        tugas = float(input("Masukkan nilai Tugas: "))
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
 
        nilai = ( 0.4 * tugas ) + ( 0.3 * uts ) + ( 0.3 * uas )
 
        if nilai > 85:
            grade = "A"
        elif nilai > 80:
            grade = "AB"
        elif nilai > 75:
            grade = "B"
        elif nilai > 70:
            grade = "BC"
        elif nilai > 65:
            grade = "C"
        elif nilai > 60:
            grade = "CD"
        elif nilai > 55:
            grade = "D"
        else:
            grade = "E"
 
        if nilai > 60:
            status = "Lulus"
        else:
            status = "Tidak Lulus"

        print("Nilai Akhir: %0.2f"%nilai)
        print("Grade: {}".format(grade))
        print("Status: {}".format(status))

    except ValueError:
        print("masukan tidak valid. Harap masukan lagi nilai tugas, uts, dan uas")
    
    lanjutkan = input("Apakah anda ingin ingin memasukan angka lagi? (ya/tidak): ")
    if lanjutkan.lower() != "ya":
        break